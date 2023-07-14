from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Customer
from .forms import CustomerCreationForm, CustomerForm
from order.models import Order

class OrderHistoryInline(admin.TabularInline): # ReadOnlyTabularInline
    model = Order
    extra = 0

@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    # form = CustomerForm
    add_form = CustomerCreationForm

    inlines = [
        OrderHistoryInline,
    ]

    readonly_fields = ('date_joined', 'last_login',)
    list_display = ('email', 'username', 'is_staff','_orders', 'is_active', 'date_joined', 'last_login',)
    fieldsets = (
        # (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ('username', 'email', 'password', 'phone', 'address_line_1', 'address_line_2', 'city', 'state', 'postcode', 'country')}),
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
    
    def _orders(self, obj: Customer) -> int:
        return obj.order_set.all().count()