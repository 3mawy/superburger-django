from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api.models import MenuItemSize, Offer
from api.serializers import PlacedOrderSerializer, OrderItemSerializer


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def post_order(request):
    grand_total = 0
    user = request.user
    placed_order = request.data['placed_order']

    order_data = {
        "delivery": placed_order.get('delivery'),
        "delivery_notes": placed_order.get('delivery_notes'),
        "delivery_address": placed_order.get('delivery_address'),
        "customer": user.customer.id,
        "total_price": 0,
        "status": 1
    }
    serializer = PlacedOrderSerializer(data=order_data)
    serializer.is_valid(True)
    order = serializer.save()

    order_items = request.data['order_items']
    for order_item in order_items:
        quantity = order_item.get('quantity')
        item = order_item.get('item')
        offer = order_item.get('offer')
        size = order_item.get('size')
        if item:
            item_size = MenuItemSize.objects.get(menu_item=item, size=size)
            price = item_size.price
        elif offer:
            offer_price = Offer.objects.get(pk=order_item.get('offer'))
            price = offer_price.price
        else:
            raise ValidationError("no menu items or offer")
        total_price = price * quantity
        item_data = {
            "quantity": quantity,
            "size": size,
            "comments": order_item.get('comments'),
            "placed_order": order.id,
            "item": item,
            "offer": offer,
            "item_price": price,
            "total_price": total_price,
        }
        item_serializer = OrderItemSerializer(data=item_data)
        item_serializer.is_valid(True)
        item_serializer.save()

        grand_total = grand_total + total_price
    order.total_price = grand_total
    order.save()
    return Response({"message": "order and order items added Successfully!",
                     "customer_email": user.email, "order_num": order.id})
