from django.db import models

class Shoes(models.Model):
    class Meta:
        verbose_name_plural = 'Shoes'
    SIZES = [
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
    ]
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unisex', 'Unisex')
    ]
    brand = models.CharField(max_length= 20)
    model = models.CharField(max_length= 40)
    price = models.DecimalField(decimal_places=2, max_digits=6, default=800)
    description = models.TextField()
    premier_date = models.CharField(blank= True, null= True, max_length=4)
    size = models.CharField(max_length= 2, choices= SIZES)
    gender = models.CharField(max_length= 10, choices= GENDER, default='Unisex')
    quantity = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField(upload_to='static/images' ,null= True, blank= True)
    def __str__(self):
        return self.size



