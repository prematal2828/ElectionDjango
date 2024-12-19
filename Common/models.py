from django.db import models
from Account.models import UserAccount


class Country(models.Model):
    country_name = models.TextField(max_length=100)
    country_name_ban = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.country_name


class Division(models.Model):
    division_name = models.TextField(max_length=100)
    division_name_ban = models.TextField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def country_details(self):
        return self.country

    def __str__(self):
        return self.division_name


class District(models.Model):
    district_name = models.TextField(max_length=100)
    district_name_ban = models.TextField(max_length=100, null=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def division_details(self):
        return self.division

    def __str__(self):
        return self.district_name


class Upazila(models.Model):
    upazila_name = models.TextField(max_length=100)
    upazila_name_ban = models.TextField(max_length=100, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def district_details(self):
        return self.district

    def __str__(self):
        return self.upazila_name


class Union(models.Model):
    union_name = models.TextField(max_length=100)
    union_name_ban = models.TextField(max_length=100, null=True)
    upazila = models.ForeignKey(Upazila, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def upazila_details(self):
        return self.upazila

    def __str__(self):
        return self.union_name


class Ward(models.Model):
    ward_name = models.TextField(max_length=100)
    ward_name_ban = models.TextField(max_length=100, null=True)
    union = models.ForeignKey(Union, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def union_details(self):
        return self.union

    def __str__(self):
        return self.ward_name


class CityCorporation(models.Model):
    city_corp_name = models.TextField(max_length=100)
    city_corp_name_ban = models.TextField(max_length=100, null=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def division_details(self):
        return self.division

    def __str__(self):
        return self.city_corp_name


class Municipality(models.Model):
    municipality_name = models.TextField(max_length=100)
    municipality_name_ban = models.TextField(max_length=100, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def district_details(self):
        return self.district

    def __str__(self):
        return self.municipality_name


class Address(models.Model):
    line1 = models.TextField(max_length=500)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    upazila = models.ForeignKey(Upazila, on_delete=models.SET_NULL, null=True, blank=True)
    union = models.ForeignKey(Union, on_delete=models.SET_NULL, null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, blank=True)
    city_corporation = models.ForeignKey(CityCorporation, on_delete=models.SET_NULL, null=True, blank=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def division_details(self):
        return self.division

    @property
    def district_details(self):
        return self.district

    @property
    def upazila_details(self):
        return self.upazila

    @property
    def union_details(self):
        return self.union

    @property
    def ward_details(self):
        return self.ward

    @property
    def city_corporation_details(self):
        return self.city_corporation

    @property
    def cmunicipality_details(self):
        return self.municipality

    def __str__(self):
        return self.line1


class Designation(models.Model):
    designation_name = models.TextField(max_length=100)
    designation_name_ban = models.TextField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_designations')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_designations')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_designations')

    def __str__(self):
        return self.designation_name


class Company(models.Model):
    company_name = models.TextField(max_length=100)
    company_name_ban = models.TextField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_companies')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_companies')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_companies')

    def __str__(self):
        return self.company_name


class UserInfo(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    designation = models.ForeignKey(Designation, null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def user_account_details(self):
        return self.user_account

    @property
    def address_details(self):
        return self.address

    @property
    def designation_details(self):
        return self.designation

    @property
    def company_details(self):
        return self.company

    def __str__(self):
        return str(self.user_account.username)


class Party(models.Model):
    party_name = models.TextField(max_length=200)
    party_name_ban = models.TextField(max_length=200, null=True)
    party_symbol = models.TextField(max_length=200, null=True)
    party_symbol_image = models.ImageField(upload_to='Images/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_party')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_party')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_party')

    @property
    def party_member_details(self):
        return self.party_members

    def __str__(self):
        return self.party_name


