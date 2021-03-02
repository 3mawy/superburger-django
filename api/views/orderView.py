from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.models import Address, Customer, Status, PlacedOrder, MenuItem, MenuItemSize, Offer, OrderItem

json_test = {
    "placed_order": {
        "order_time": "04:14:49.289732",
        "delivery": True,
        "delivery_notes": "ggg",
        "complete": False,
        "delivery_address": 1,
        "customer": 2,
        "status": 1
    },
    "order_items": [{
        "quantity": 2,
        "size": 3,
        "comments": "aa",
        "placed_order": 1,
        "offer": None,
        "item": 1
    }]
}


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def post_order(request):
    grand_total = 0

    placed_order = json_test.get('placed_order')
    order_time = placed_order.get('order_time')
    delivery = placed_order.get('delivery')
    delivery_notes = placed_order.get('delivery_notes')
    complete = placed_order.get('complete')
    delivery_address = Address.objects.get(pk=placed_order.get('delivery_address'))
    customer = Customer.objects.get(pk=placed_order.get('customer'))
    status = Status.objects.get(pk=placed_order.get('status'))

    order = PlacedOrder.objects.create(order_time=order_time, delivery=delivery, delivery_notes=delivery_notes,
                                       complete=complete, total_price=0, delivery_address=delivery_address,
                                       customer=customer, status=status)

    order_items = json_test.get('order_items')
    for order_item in order_items:
        quantity = order_item.get('quantity')
        size = order_item.get('size')
        comments = order_item.get('comments')
        placed_order = order
        item_flag = order_item.get('item')
        if item_flag:
            item = MenuItem.objects.get(pk=item_flag)
            offer = None
            item_size = MenuItemSize.objects.get(menu_item=item, size=size)
            price = item_size.price
        else:
            offer = Offer.objects.get(pk=order_item.get('offer'))
            item = None
            price = offer.price

        total_price = price * quantity
        OrderItem.objects.create(quantity=quantity, item_price=price, total_price=total_price,
                                 comments=comments, placed_order=placed_order,
                                 item=item, offer=offer)
        grand_total = grand_total + total_price
    order.total_price = grand_total
    order.save()
    return Response({"message": "order and order items added Successfully!",
                     "customer_email": order.customer.user.email, "order_num": order.id})

