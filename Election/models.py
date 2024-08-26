from django.db import models
from Account.models import UserAccount
from Common.models import Address


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

    def __str__(self):
        return self.center_name


class ElectionInfo(models.Model):
    election_info_name = models.TextField(max_length=100)
    election_info_name_ban = models.TextField(max_length=100, null=True)
    election_type = models.ForeignKey(ElectionType, on_delete=models.SET_NULL, null=True, blank=True)
    candidate_ids = models.ManyToManyField(UserAccount, related_name='candidates_election_info')
    worker_ids = models.ManyToManyField(UserAccount, related_name='workers_election_info')
    total_voter = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_election_info')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='updated_election_info')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_election_info')

    def __str__(self):
        return self.election_info_name


class ElectionData(models.Model):
    election_id = models.ForeignKey(ElectionInfo, on_delete=models.SET_NULL, null=True, blank=True)
    worker_id = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True)
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

    def __str__(self):
        return str(self.election_id)
