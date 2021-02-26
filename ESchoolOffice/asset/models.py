from django.db import models
# Create your models here.


class Merchant(models.Model):
    mer_name = models.CharField(max_length=100)
    mer_address = models.CharField(max_length=300)
    mer_contactno = models.CharField(max_length=13)
    mer_email = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s %s" % (
            self.mer_name, self.mer_address, self.mer_contactno, self.mer_email)


class Asset(models.Model):
    asset_name = models.CharField(max_length=1000)
    asset_description = models.CharField(max_length=1000)

    def __str__(self):
        return "%s %s" % (
            self.asset_name, self.asset_description)


class AssetManagementIn(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.RESTRICT)
    assetmgmtin_date = models.DateField()
    assetmgmtin_billno = models.CharField(max_length=20)
    assetmgmtin_billamount = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s" % (
            self.merchant, self.assetmgmtin_date, self.assetmgmtin_billno, self.assetmgmtin_billamount)


class AssetManagementDetails(models.Model):
    assetmanagementin = models.ForeignKey(AssetManagementIn, on_delete=models.RESTRICT)
    assetdet_qty = models.IntegerField()
    assetdet_unitrate = models.IntegerField()

    def __str__(self):
        return "%s %s %s" % (
            self.assetmanagementin, self.assetdet_qty, self.assetdet_unitrate)


class AssetManagementOut(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.RESTRICT)
    assetmgmtout_qty = models.IntegerField()
    assetmgmtout_particulars = models.CharField(max_length=1000)

    def __str__(self):
        return "%s %s %s" % (
            self.asset, self.assetmgmtout_qty, self.assetmgmtout_particulars)


class Stock(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.RESTRICT)
    stock_qty = models.IntegerField()

    def __str__(self):
        return "%s %s" % (
            self.asset, self.stock_qty)
