from django.db import models
from student.models import Student
from staff.models import Staff


class DocumentType(models.Model):
    doctype_name = models.CharField(max_length=50)


class DocumentUpload(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    documenttype = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    file_path = models.CharField(max_length=100)


class OldDocumentsclass (models.Model):
    admno_from = models.CharField(max_length=50)
    admno_to = models.CharField(max_length=15)
    olddocu_file = models.CharField(max_length=100)
