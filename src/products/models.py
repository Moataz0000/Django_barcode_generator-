from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


class Product(models.Model):
    name = models.CharField(max_length=250)
    bar_code = models.ImageField(upload_to='images/', blank=True)
    country_id = models.CharField(max_length=1,null=True)
    manfacturer = models.CharField(max_length=6, null=True)
    number_id = models.CharField(max_length=5, null=True)
    # other fileds here...
    
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.country_id}{self.manfacturer}{self.number_id}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.bar_code.save('barcode.png', File(buffer), save=False) 
        return super().save(*args, **kwargs)