from django.urls import path
from rest_framework import routers
from setting.views import SettingViewSet
from category.views import CategoryList
from product.views import ProductViewSet, TagViewSet
from order.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'setting', SettingViewSet, basename='setting')
router.register(r'category', CategoryList, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'order', OrderViewSet, basename='order')