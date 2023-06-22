from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Customer, Whishlist
from .forms import CustomerCreationForm, CustomerForm
from order.models import Order

class OrderHistoryInline(admin.TabularInline): # ReadOnlyTabularInline
    model = Order
    extra = 0
    # mostrar solo 3 campos
    # fields = ('status', 'total')

    # readonly_fields = ('__all__',)
    
class WhishlistInline(admin.TabularInline):
    model = Whishlist
    extra = 0


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    # form = CustomerForm
    add_form = CustomerCreationForm

    inlines = [
        OrderHistoryInline,
        WhishlistInline,
    ]

    readonly_fields = ('date_joined', 'last_login',)

    fieldsets = (
        # (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("username", "email", "password", "first_name", "last_name","phone", "address", "city", "country")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}),
        )