from django.db import models
from django.utils import timezone


# Create your models here.

class Subject(models.Model):
    sub_name = models.CharField(max_length=60)

    def __str__(self):
        return self.sub_name

class Standard(models.Model):
    standard_name = models.IntegerField()

    def __str__(self):
        return str(self.standard_name)

class Division(models.Model):
    div_name = models.CharField(max_length=1)

    def __str__(self):
        return self.div_name

class ClassDivision(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.RESTRICT)
    division = models.ForeignKey(Division, on_delete=models.RESTRICT)

class AcademicYear(models.Model):
    acyear_year = models.CharField(max_length=9)
    acyear_startdate = models.DateField(default=timezone.now)
    acyear_enddate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.acyear_year

class ExamDetail(models.Model):
    exam_name = models.CharField(max_length=100)
    academicyear = models.ForeignKey(AcademicYear, on_delete=models.RESTRICT)

    def __str__(self):
        return self.exam_name

class Grade(models.Model):
    grade_per = models.IntegerField()
    grade_grade = models.CharField(max_length=2)

    def __str__(self):
        return self.grade_grade

class ClassSubject(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.RESTRICT)
    subject = models.ForeignKey(Subject, on_delete=models.RESTRICT)

class ExamMark(models.Model):
    examdetail = models.ForeignKey(ExamDetail, on_delete=models.RESTRICT)
    classsubject = models.ForeignKey(ClassSubject, on_delete=models.RESTRICT)
    exammark_max = models.IntegerField()
    exammark_pass = models.IntegerField()

class AcademicCalander(models.Model):
    academicyear = models.ForeignKey(AcademicYear, on_delete=models.RESTRICT)
    accal_datefrom = models.DateField(default=timezone.now)
    accal_dateto = models.DateField(default=timezone.now)
    accal_particulars = models.CharField(max_length=1000)