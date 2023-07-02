from customer.models import Customer
from django.core.files import File
from django.core.management.base import BaseCommand
from setting.models import Setting, SiteMeta, TaxAndShipment, Currency
import os


CITY_TAXES = (
    ('Alabama', '4.00', '0.00'),
    ('Alaska', '0.00', '0.00'),
    ('Arizona', '5.60', '0.00'),
    ('Arkansas', '6.50', '0.00'),
    ('California (b)', '7.25', '0.00'),
    ('Colorado', '2.90', '0.00'),
    ('Connecticut', '6.35', '0.00'),
    ('Delaware', '0.00', '0.00'),
    ('D.C.', '6.00', '0.00'),
    ('Florida', '6.00', '0.00'),
    ('Georgia', '4.00', '0.00'),
    ('Hawaii (c)', '4.00', '0.00'),
    ('Idaho', '6.00', '0.00'),
    ('Illinois', '6.25', '0.00'),
    ('Indiana', '7.00', '0.00'),
    ('Iowa', '6.00', '0.00'),
    ('Kansas', '6.50', '0.00'),
    ('Kentucky', '6.00', '0.00'),
    ('Louisiana', '4.45', '0.00'),
    ('Maine', '5.50', '0.00'),
    ('Maryland', '6.00', '0.00'),
    ('Massachusetts', '6.25', '0.00'),
    ('Michigan', '6.00', '0.00'),
    ('Minnesota', '6.875', '0.00'),
    ('Mississippi', '7.00', '0.00'),
    ('Missouri', '4.225', '0.00'),
    ('Montana (d)', '0.00', '0.00'),
    ('Nebraska', '5.50', '0.00'),
    ('Nevada', '6.85', '0.00'),
    ('New Hampshire', '0.00', '0.00'),
    ('New Jersey (e)', '6.625', '0.00'),
    ('New Mexico (c)', '5.125', '0.00'),
    ('New York', '4.00', '0.00'),
    ('North Carolina', '4.75', '0.00'),
    ('North Dakota', '5.00', '0.00'),
    ('Ohio', '5.75', '0.00'),
    ('Oklahoma', '4.50', '0.00'),
    ('Oregon', '0.00', '0.00'),
    ('Pennsylvania', '6.00', '0.00'),
    ('Puerto Rico', '10.50', '0.00'),
    ('Rhode Island', '7.00', '0.00'),
    ('South Carolina', '6.00', '0.00'),
    ('South Dakota (c)', '4.50', '0.00'),
    ('Tennessee', '7.00', '0.00'),
    ('Texas', '6.25', '0.00'),
    ('Utah (b)', '6.10', '0.00'),
    ('Vermont', '6.00', '0.00'),
    ('Virginia (b)', '5.30', '0.00'),
    ('Washington', '6.50', '0.00'),
    ('West Virginia', '6.00', '0.00'),
    ('Wisconsin', '5.00', '0.00'),
    ('Wyoming', '4.00', '0.00'),
)

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
        setting.site_reg_no = '00-000-000'
        setting.site_website = 'https://nainahcollection.com'
        setting.site_email = 'infonainah@nainahcollection.com'
        setting.site_facebook = 'https://www.facebook.com/nainahcollection'
        setting.site_instagram = 'https://www.instagram.com/nainahcollectioncompany/'
        setting.site_tiktok = 'https://www.tiktok.com/@nainahcollection22'

        img_path = os.path.join(os.getcwd(), 'setting/management/commands/logo.png')
        
        with open(img_path, 'rb') as f:
            setting.site_banner_small.save('logo.png', File(f), save=True)
            setting.site_banner_large.save('logo.png', File(f), save=True)
            setting.site_banner_collections.save('logo.png', File(f), save=True)
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

        # # Taxes initial
        
        Currency.objects.create(
            setting=setting,
            # currency='USD',
            currency_symbol='$',
            currency_code='USD',
            # currency_rate=1.00,
            # is_active=True
        )
        
        for city, tax_rate, shipment_amount in CITY_TAXES:
            TaxAndShipment.objects.create(
                setting=setting,
                city=city,
                tax_rate=tax_rate,
                shipment_amount=shipment_amount,
            )
            
        self.stdout.write(self.style.SUCCESS('Initial settings created successfully.'))
        
# exectute the command in the terminal
# python manage.py create_settings