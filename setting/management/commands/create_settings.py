from customer.models import Customer
from django.core.files import File
from django.core.management.base import BaseCommand
from setting.models import Setting, SiteMeta, Tax, ShippingCharge, Currency
import os


CITY_TAXES = (
    ('Alabama', '4.00'),
    ('Alaska', '0.00'),
    ('Arizona', '5.60'),
    ('Arkansas', '6.50'),
    ('California (b)', '7.25'),
    ('Colorado', '2.90'),
    ('Connecticut', '6.35'),
    ('Delaware', '0.00'),
    ('D.C.', '6.00'),
    ('Florida', '6.00'),
    ('Georgia', '4.00'),
    ('Hawaii (c)', '4.00'),
    ('Idaho', '6.00'),
    ('Illinois', '6.25'),
    ('Indiana', '7.00'),
    ('Iowa', '6.00'),
    ('Kansas', '6.50'),
    ('Kentucky', '6.00'),
    ('Louisiana', '4.45'),
    ('Maine', '5.50'),
    ('Maryland', '6.00'),
    ('Massachusetts', '6.25'),
    ('Michigan', '6.00'),
    ('Minnesota', '6.875'),
    ('Mississippi', '7.00'),
    ('Missouri', '4.225'),
    ('Montana (d)', '0.00'),
    ('Nebraska', '5.50'),
    ('Nevada', '6.85'),
    ('New Hampshire', '0.00'),
    ('New Jersey (e)', '6.625'),
    ('New Mexico (c)', '5.125'),
    ('New York', '4.00'),
    ('North Carolina', '4.75'),
    ('North Dakota', '5.00'),
    ('Ohio', '5.75'),
    ('Oklahoma', '4.50'),
    ('Oregon', '0.00'),
    ('Pennsylvania', '6.00'),
    ('Puerto Rico', '10.50'),
    ('Rhode Island', '7.00'),
    ('South Carolina', '6.00'),
    ('South Dakota (c)', '4.50'),
    ('Tennessee', '7.00'),
    ('Texas', '6.25'),
    ('Utah (b)', '6.10'),
    ('Vermont', '6.00'),
    ('Virginia (b)', '5.30'),
    ('Washington', '6.50'),
    ('West Virginia', '6.00'),
    ('Wisconsin', '5.00'),
    ('Wyoming', '4.00'),
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
        
        for city, tax_rate in CITY_TAXES:
            Tax.objects.create(
                setting=setting,
                city=city,
                tax_rate=tax_rate
            )
            
        
        self.stdout.write(self.style.SUCCESS('Initial settings created successfully.'))
        
# exectute the command in the terminal
# python manage.py create_settings