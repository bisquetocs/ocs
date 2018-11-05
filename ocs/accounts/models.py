"""
Description: Account models file
Modified by:
Modify date:
"""


from django.db import models
from django.contrib.auth.models import User, Group
from provider.models import Provider
from franchise.models import Franchise

# OCSUSer model, model used to represent the user of the system
class OCSUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    id_franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=10)
    rfc = models.CharField(max_length=12)
    num_ss = models.CharField(max_length=12)
    direccion = models.CharField(max_length=200)
    active = models.BooleanField(null = False, default = True)

# Model used to represent the relationship between a group(LOS ROLES) and a provider or franchise
class IsProviderOrFranchise(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_provider = models.BooleanField(null=False, default=False)
    is_franchise = models.BooleanField(null=False, default=False)
    id_admin = models.BooleanField(null=False, default=False)
