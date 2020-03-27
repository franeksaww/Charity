from django.contrib.auth.models import User
from django.db import models


TYPES = (
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna')
)


class CategoryModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class InstitutionModel(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.name


class DonationModel(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(CategoryModel)
    institution = models.ForeignKey(InstitutionModel,on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=128)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)