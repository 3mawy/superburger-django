from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

# router.register(r'current-user', views.CurrentUserView)
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'sizes', views.SizeViewSet)
router.register(r'menu-item-sizes', views.MenuItemSizeViewSet)
router.register(r'menu-items', views.MenuItemViewSet)
router.register(r'offers', views.OfferViewSet)
router.register(r'order-items', views.OrderItemViewSet)
router.register(r'placed-orders', views.PlacedOrderViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'customers', views.CustomerViewSet),
router.register(r'cart', views.CartViewSet)
router.register(r'cart-items', views.CartItemViewSet)
router.register(r'areas', views.AreaViewSet)
router.register(r'addresses', views.AddressViewSet)
router.register(r'carousel-images', views.CarouselImageViewSet)
router.register(r'extras', views.ExtraViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('order-create', views.post_order, name='order-create'),
    path('current-customer', views.current_customer, name='current-customer'),
    path('current-customer-orders', views.current_customer_orders, name='current-customer-orders'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]
