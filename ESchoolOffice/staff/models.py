from django.db import models


class Designation(models.Model):
    desig_name = models.CharField(max_length=100)

    def __str__(self):
        return self.desig_name


class LeaveType(models.Model):
    leave_type = models.CharField(max_length=100)

    def __str__(self):
        return self.leave_type


