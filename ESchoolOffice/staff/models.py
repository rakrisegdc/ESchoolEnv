from django.db import models


class Designation(models.Model):
    desig_name = models.CharField(max_length=100)

    def __str__(self):
        return self.desig_name


class LeaveType(models.Model):
    leave_type = models.CharField(max_length=100)

    def __str__(self):
        return self.leave_type


class Staff(models.Model):

    STAFF_STATUS = (
        ('T', 'T'),
        ('N', 'N'),
    )

    STAFF_ACTIVE = (
        (1, "Active"),
        (0, "In-Active"),
    )

    staff_name = models.CharField(max_field=100)
    staff_address = models.CharField(max_field=300)
    staff_contactno = models.CharFiled(max_field=10)
    staff_email = models.CharFiled(max_length=100)
    staff_dob = models.DateFiield()
    staff_doj = models.DateFiield()
    staff_status = models.CharFiled(max_length=1, choices=STAFF_STATUS)
    desig_id = models.ForeignKey(Designation, on_delete=models.RESTRICT)
    staff_adharno = models.IntegerField(max_length=12)
    staff_active = models.IntegerField(max_length=1, choices=STAFF_ACTIVE)

    def __str__(self):
        return self.staff_name
