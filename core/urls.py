"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from core import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from core import routing
from order.reports import order_pdf

from product.views import AvailableColorsAPIView, AvailableSizesAPIView
from product.reports import generate_product_report

from newsletter.views import SubscriberCreateAPIView

from customer.views import CustomerActive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routing.router.urls)),
    
    # debug toolbar
    # path("__debug__/", include("debug_toolbar.urls")),
    
    # api schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # # PDF Reports
    path('order-pdf/<int:pk>', order_pdf, name='order-pdf'),
    path('products/pdf/', generate_product_report, name='product-pdf'),
    
    path('summernote/', include('django_summernote.urls')),
    
    # product endpoints
    path('api/colors/', AvailableColorsAPIView.as_view(), name='colors'),
    path('api/sizes/', AvailableSizesAPIView.as_view(), name='sizes'),
    
    # Subscriber endpoints
    path('api/subscriber/', SubscriberCreateAPIView.as_view(), name='subscriber'),
    
    # user activation confirm endpoint
    path('auth/user/confirm-activation/<str:email>', CustomerActive.as_view(), name='confirm-activation'),
    
    # # Djoser Endpoints
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

