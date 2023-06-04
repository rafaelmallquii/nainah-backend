from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, OrderHistory, Whishlist

from .forms import CustomerCreationForm, CustomerForm

# Register your models here.

class ReadOnlyTabularInline(admin.TabularInline):
    def has_add_permission(self, request, obj=None):
        return False

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.can_delete = False  # Opcionalmente, puedes deshabilitar también la eliminación
        return formset

class OrderHistoryInline(admin.StackedInline): # ReadOnlyTabularInline
    model = OrderHistory
    extra = 0

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

    readonly_fields = ('date_joined', 'last_login', 'orderhistory',)

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