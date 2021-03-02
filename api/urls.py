from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'sizes', views.SizeViewSet)
router.register(r'menu-item-sizes', views.MenuItemSizeViewSet)
router.register(r'menu_items', views.MenuItemViewSet)
router.register(r'offers', views.OfferViewSet)
router.register(r'order-items', views.OrderItemViewSet)
router.register(r'placed-orders', views.PlacedOrderViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'areas', views.AreaViewSet)
router.register(r'addresses', views.AddressViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('order-create', views.post_order, name='order-create')
]
