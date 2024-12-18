from django.db import models
from Account.models import UserAccount
from Common.models import Address, Party


# Create your models here.

class ElectionType(models.Model):
    election_type_name = models.TextField(max_length=100)
    election_type_name_ban = models.TextField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_election_type')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_election_type')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_election_type')

    def __str__(self):
        return self.election_type_name


class ElectionCenter(models.Model):
    center_name = models.TextField(max_length=200)
    center_name_ban = models.TextField(max_length=200)

    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_election_center')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_election_center')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_election_center')

    @property
    def address_details(self):
        return self.address

    def __str__(self):
        return self.center_name


class ElectionSeat(models.Model):
    election_seat_name = models.TextField(max_length=100)
    election_seat_name_ban = models.TextField(max_length=100, null=True)

    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    election_center = models.ManyToManyField(ElectionCenter, related_name='election_center_info', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_election_seat')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_election_seat')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_election_seat')

    def __str__(self):
        return self.election_seat_name


class ElectionInfo(models.Model):
    election_info_name = models.TextField(max_length=100)
    election_info_name_ban = models.TextField(max_length=100, null=True)
    election_type = models.ForeignKey(ElectionType, on_delete=models.SET_NULL, null=True, blank=True)

    candidates = models.ManyToManyField(UserAccount, related_name='candidates_info', blank=True)
    parties = models.ManyToManyField(Party, related_name='party_info', blank=True)

    workers = models.ManyToManyField(UserAccount, related_name='workers_info')
    total_voter = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_election')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_election')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_election')

    @property
    def election_type_details(self):
        return self.election_type

    @property
    def candidates_details(self):
        return self.candidates

    @property
    def workers_details(self):
        return self.workers

    @property
    def party_details(self):
        return self.parties

    def __str__(self):
        return self.election_info_name


class ElectionData(models.Model):
    election = models.ForeignKey(ElectionInfo, on_delete=models.SET_NULL, null=True, blank=True)
    worker = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True)
    vote_count = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_election_data')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_election_data')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_election_data')

    @property
    def election_details(self):
        return self.election

    @property
    def worker_details(self):
        return self.worker

    def __str__(self):
        return str(self.election)
