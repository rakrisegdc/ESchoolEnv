from django.db import models
from staff.models import Staff


# Create your models here.
class Pettycash(Models.model):
    staff = models.ForeignKey(Staff, on_delete=models.RESTRICT)
    pettycash_date = models.DateField()
    pettycash_particulars = models.CharField(max_length=1000)
    pettycash_amount = models.IntegerField(max_length=20)

    def __str__(self):
        return "%s %s %s %s" % (
        self.staff, self.pettycash_date, self.pettycash.pettycash_particulars, self.pettycash_amount)


class Pettycashapproval(Models.model):
    pettycash = models.ForeignKey(Pettycash, on_delete=models.RESTRICT)
    pettycashappr_date = models.DateField()
    pettycashappr_voucherno = models.CharField(max_length=1000)
    pettycashappr_voucherfile = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s %s %s" % (
        self.pettycash, self.pettycashappr_date, self.pettycashappr_voucherno, self.pettycashappr_voucherfile)
