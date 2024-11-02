from django.core.management.base import BaseCommand
from products.models import Product





class Command(BaseCommand):
    help = 'Check barcode prodcuts..'
    
    
    
    def handle(self, *args, **kwargs):
        product_count = Product.objects.all().count()
        print(f'You have {product_count} objects. \n')
        
        qs = Product.objects.all()
        counter = 0
        for _ in qs:
            if not _.bar_code:
                counter =+ 1
                print(f'{counter} object not have barcodes.')
   