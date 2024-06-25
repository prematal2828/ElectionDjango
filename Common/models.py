from django.db import models

from Account.models import UserAccount


# Create your models here.
class Country(models.Model):
    countryName = models.TextField(max_length=100)
    countryNameBan = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.countryName


class Division(models.Model):
    divisionName = models.TextField(max_length=100)
    divisionNameBan = models.TextField(max_length=100, null=True)
    countryId = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.divisionName


class District(models.Model):
    districtName = models.TextField(max_length=100)
    districtNameBan = models.TextField(max_length=100, null=True)
    divisionID = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.districtName


class Upazila(models.Model):
    upazilaName = models.TextField(max_length=100)
    upazilaNameBan = models.TextField(max_length=100, null=True)
    districtId = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.upazilaName


class Union(models.Model):
    unionName = models.TextField(max_length=100)
    unionNameBan = models.TextField(max_length=100, null=True)
    upazilaId = models.ForeignKey(Upazila, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.unionName


class Ward(models.Model):
    wardName = models.TextField(max_length=100)
    wardNameBan = models.TextField(max_length=100, null=True)
    unionId = models.ForeignKey(Union, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.wardName


class CityCorporation(models.Model):
    cityCorpName = models.TextField(max_length=100)
    cityCorpNameBan = models.TextField(max_length=100, null=True)
    divisionId = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.cityCorpName


class Municipality(models.Model):
    municipalityName = models.TextField(max_length=100)
    municipalityNameBan = models.TextField(max_length=100, null=True)
    districtId = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.municipalityName


class Address(models.Model):
    line1 = models.TextField(max_length=500)
    divisionId = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True)
    districtId = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    upazilaId = models.ForeignKey(Upazila, on_delete=models.SET_NULL, null=True, blank=True)
    unionId = models.ForeignKey(Union, on_delete=models.SET_NULL, null=True, blank=True)
    wardId = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, blank=True)
    cityCorporationId = models.ForeignKey(CityCorporation, on_delete=models.SET_NULL, null=True, blank=True)
    municipalityId = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.line1


class Designation(models.Model):
    designationName = models.TextField(max_length=100)
    designationNameBan = models.TextField(max_length=100, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='created_designations')
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='updated_designations')
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(auto_now_add=True, null=True)
    deletedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='deleted_designations')

    def __str__(self):
        return self.designationName


class Company(models.Model):
    companyName = models.TextField(max_length=100)
    companyNameBan = models.TextField(max_length=100, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='created_companies')
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='updated_companies')
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(auto_now_add=True, null=True)
    deletedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='deleted_companies')

    def __str__(self):
        return self.companyName


class UserInfo(models.Model):
    userAccountId = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    designationId = models.ForeignKey(Designation, null=True, blank=True, on_delete=models.SET_NULL)
    companyId = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
