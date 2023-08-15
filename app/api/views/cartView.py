from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from api import serializers

from api.models import Extra, CartItem, MenuItemSize, MenuItem, Size, Offer
from django.db.models import Q

# TODO::REVIEW
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def current_customer_cart(request):
    user = request.user
    cart = user.customer.cart
    serialized_cart = serializers.CartSerializer(cart)

    return Response({
        "cart": serialized_cart.data
    })


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_cart(request):
    user = request.user
    cart = user.customer.cart
    size = None

    item_id = request.data.get('item_id')
    quantity = request.data.get('quantity')
    size_id = request.data.get('size_id')
    extras = request.data.get('extras', [])
    offer_id = request.data.get('offer_id')

    if item_id:
        # Get the selected item and size
        item = MenuItem.objects.get(id=item_id)
        size = Size.objects.get(id=size_id)
        item_size = MenuItemSize.objects.get(menu_item=item, size=size_id)
        price = item_size.price
        offer = None  # Initialize offer as None
    elif offer_id:
        # Get the selected offer
        offer = Offer.objects.get(id=offer_id)
        price = offer.price
        item = None  # Initialize item as None
    else:
        return Response({"error": "No item or offer provided."}, status=status.HTTP_400_BAD_REQUEST)

    # Calculate the extras price
    extras_price = 0
    for extra_id in extras:
        extra = Extra.objects.get(id=extra_id)
        extras_price += extra.price

    # Calculate the total price
    total_price = (price + extras_price) * quantity

    # Check if the item or offer already exists in the cart
    cart_item = None
    existing_cart_items = cart.cart_items.filter(Q(item=item) | Q(offer=offer))

    # Check if the cart item has the same size and extras
    for existing_item in existing_cart_items:
        existing_extras = set(existing_item.extras.all().values_list('id', flat=True))
        if existing_item.size == size and existing_extras == set(extras):
            cart_item = existing_item
            break

    if cart_item:
        # Increment quantity and update total price
        cart_item.quantity += quantity
        cart_item.total_price += total_price
        cart_item.save()
    else:
        # Create a new cart item
        cart_item = CartItem.objects.create(
            quantity=quantity,
            item_price=price,
            total_price=total_price,
            size=size,
            cart=cart,
            item=item,
            offer=offer,
            extras_price=extras_price
        )
        # Add extras to the cart item
        for extra_id in extras:
            extra = Extra.objects.get(id=extra_id)
            cart_item.extras.add(extra)

    # Update the cart's total price
    cart.total_price += total_price
    cart.save()

    serialized_cart = serializers.CartSerializer(cart)

    return Response({
        "message": "Item or offer added to cart",
        "cart": serialized_cart.data
    })


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_from_cart(request, cart_item_id):
    user = request.user
    cart = user.customer.cart

    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
    except CartItem.DoesNotExist:
        return Response({"message": "Item not found in the cart"}, status=status.HTTP_404_NOT_FOUND)

    total_price_to_deduct = cart_item.total_price
    cart_item.delete()
    cart.total_price -= total_price_to_deduct
    cart.save()

    serialized_cart = serializers.CartSerializer(cart)

    return Response({
        "message": "Item removed from cart",
        "cart": serialized_cart.data
    })

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def clear_cart(request):
    user = request.user
    cart = user.customer.cart

    cart.cart_items.all().delete()

    cart.total_price = 0
    cart.save()

    # Serialize the cleared cart
    serialized_cart = serializers.CartSerializer(cart)

    return Response({
        "message": "Cart cleared",
        "cart": serialized_cart.data
    })
