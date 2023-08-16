# views.py
from django.http import JsonResponse

from api import serializers
from api.models import Category, MenuItem


def get_menu_items_by_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        menu_items = category.menuitem_set.all()
        menu_items_serialized = serializers.MenuItemSerializer(menu_items, many=True)

        return JsonResponse({
            "category": {
                "id": category.id,
                "name": category.name,
                "image": category.image.image.url if category.image else None
            },
            "count": len(menu_items),
            "menu_items": menu_items_serialized.data,
        })
    except Category.DoesNotExist:
        return JsonResponse({"error": "Category not found"}, status=404)
