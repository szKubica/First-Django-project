from django.db import models


class MoreInfo(models.Model):

    class Meta:
        verbose_name_plural = 'More Info'
    CONDITION = {
        (1, 'Descent'),
        (2, 'Good'),
        (3, 'Excellent'),
        (4, 'New')
    }
    TYPE = {
        (1, 'Sport'),
        (2, 'Lifestyle'),
        (3, 'Elegant'),
        (4, 'Other')
    }
    condition = models.PositiveSmallIntegerField(choices=CONDITION, blank=False)
    type = models.PositiveSmallIntegerField(choices=TYPE, default=4)


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
    size = models.CharField(max_length=2, choices= SIZES)
    gender = models.CharField(max_length=10, choices= GENDER, default='Unisex')
    quantity = models.PositiveSmallIntegerField(default=1)
    photo = models.ImageField(upload_to='shoes_images', null=True, blank=True)
    more_info = models.OneToOneField(MoreInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.brand_with_model()

    def brand_with_model(self):
        return "{} {}".format(self.brand, self.model)


class Opinion(models.Model):
    STARS = {
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    }
    comment = models.TextField(blank=True, null=True)
    stars = models.SmallIntegerField(choices=STARS, blank=False, default=5)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)


class WearedBy(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    shoes = models.ManyToManyField(Shoes)