from django.db import models
from Account.models import UserAccount
from Common.models import Address


# Create your models here.


class ElectionType(models.Model):
    electionTypeName = models.TextField(max_length=100)
    electionTypeNameBan = models.TextField(max_length=100, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='created_electionType')
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='updated_electionType')
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(auto_now_add=True, null=True)
    deletedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='deleted_electionType')

    def __str__(self):
        return self.electionTypeName


class ElectionCenter(models.Model):
    centerName = models.TextField(max_length=200)
    centerNameBan = models.TextField(max_length=200)

    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)

    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='created_electionCenter')
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='updated_electionCenter')
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(auto_now_add=True, null=True)
    deletedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='deleted_electionCenter')

    def __str__(self):
        return self.centerName


class ElectionInfo(models.Model):
    electionInfoName = models.TextField(max_length=100)
    electionInfoNameBan = models.TextField(max_length=100, null=True)
    electionType = models.ForeignKey(ElectionType, on_delete=models.SET_NULL, null=True, blank=True)
    candidateIds = models.ManyToManyField(UserAccount, related_name='candidates_electionInfo')
    workerIds = models.ManyToManyField(UserAccount, related_name='workers_electionInfo')
    totalVoter = models.IntegerField()

    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='created_electionInfo')
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='updated_electionInfo')
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(auto_now_add=True, null=True)
    deletedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='deleted_electionInfo')

    def __str__(self):
        return self.electionInfoName


class ElectionData(models.Model):
    electionId = models.ForeignKey(ElectionInfo, on_delete=models.SET_NULL, null=True, blank=True)
    workerId = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True)
    voteCount = models.IntegerField()

    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='created_electionData')
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='updated_electionData')
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(auto_now_add=True, null=True)
    deletedBy = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='deleted_electionData')
