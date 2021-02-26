from django.db import models
from ESchoolOffice.student.models import Student
from ESchoolOffice.staff.models import Staff


class DocumentType(models.Model):
    doctype_name = models.CharField(50)


class DocumentUpload(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    documenttype = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    file_path = models.CharField(100)


class OldDocumentsclass (models.Model):
    admno_from = models.CharField(50)
    admno_to = models.CharField(15)
    olddocu_file = models.CharField(100)
