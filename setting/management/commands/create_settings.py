from customer.models import Customer
from django.core.files import File
from django.core.management.base import BaseCommand
from setting.models import Setting, SiteMeta, Tax, ShippingCharge
import os

class Command(BaseCommand):
    help = 'Create initial settings for the ecommerce project'

    def handle(self, *args, **options):
        # Create superuser
        # Customer.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

        if Setting.objects.exists():
            self.stdout.write(self.style.WARNING('Settings already created.'))
            return
        
        # sitte configuration initial
        setting = Setting()
        setting.site_name = 'Nainah Collection'
        setting.site_description = 'A family-owned business that wants to offer you not just a place to shop, but a wonderful experience.'
        setting.site_address = '54 Allen St, Springfield, MA 01108 USA'
        setting.site_phone = '+1 413-273- 9878'
        setting.site_email = 'infonainah@nainahcollection.com'
        setting.site_facebook = 'https://www.facebook.com/nainahcollection'
        setting.site_instagram = 'https://www.instagram.com/nainahcollectioncompany/'
        setting.site_tiktok = 'https://www.tiktok.com/@nainahcollection22'

        img_path = os.path.join(os.getcwd(), 'setting/management/commands/logo.png')
        
        with open(img_path, 'rb') as f:
            setting.site_logo.save('logo.png', File(f), save=True)
            setting.site_favicon.save('logo.png', File(f), save=True)
            setting.site_icon.save('logo.png', File(f), save=True)

        


        setting.save()

        # # site meta initial

        site_meta = SiteMeta()
        site_meta.setting = setting
        site_meta.meta_title = 'Nainah Collection'
        site_meta.meta_description = 'A family-owned business that wants to offer you not just a place to shop, but a wonderful experience.'
        site_meta.meta_keywords = 'Nainah Collection, Nainah, Collection, Nainah Collection Company, Nainah Co'
        site_meta.meta_author = 'Nainah Collection'
        site_meta.meta_robots = 'index, follow'
        site_meta.meta_image = 'images/site/site_logo.jpg'
        site_meta.save()

        # # tax initial
        tax = Tax()
        tax.setting = setting
        tax.tax_percentage = 0.0625
        tax.save()
        
        # # shipping charge initial
        shipping_charge = ShippingCharge()
        shipping_charge.setting = setting
        shipping_charge.shipping_charge = 5.00
        shipping_charge.save()
        
        self.stdout.write(self.style.SUCCESS('Initial settings created successfully.'))
        
# exectute the command in the terminal
# python manage.py create_settings