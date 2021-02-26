from django.db import models
from parent.models import Parent
from django.utils import timezone
from user_settings.models import Mothertongue, State, Relation
from academic_Settings.models import Acyear, Standard, ExamMarks


class Student(models.Model):
    stud_admno = models.CharField(max_length=15)
    standard = models.ForeignKey(Standard, on_delete=models.RESTRICT)
    stud_regdate = models.DateField(default=timezone.now)
    stud_name = models.CharField(max_length=100)
    stud_address = models.CharField(max_length=300)
    state = models.ForeignKey(State, on_delete=models.RESTRICT)
    stud_email = models.EmailField(max_length=30)
    stud_adharno = models.CharField(max_length=12)
    stud_religion = models.CharField(max_length=50)
    stud_caste = models.CharField(max_length=50)
    stud_nationality = models.CharField(max_length=30)
    mothertongue = models.ForeignKey(Mothertongue, on_delete=models.RESTRICT)
    stud_dob = models.DateField()
    parent = models.ForeignKey(Parent, on_delete=models.RESTRICT)
    stud_bloodgroup = models.IntegerField()
    stud_gender = models.CharField(max_length=1)

    def __str__(self):
        return self.stud_admno


class StudentAcademic(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    classdivision = models.ForeignKey(ClassDivision, on_delete=models.RESTRICT)
    acyear = models.ForeignKey(AcYear, on_delete=models.RESTRICT())

    def __str__(self):
        return self.student


class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    exammarks = models.ForeignKey(ExamMarks, on_delete= models.RESTRICT)
    studmark_obtained = models.IntegerField()

    def __str__(self):
        return self.student


class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    relation = models.ForeignKey(Relation, on_delete=models.RESTRICT)
    parent_name = models.CharField(max_length=100)
    parent_permaddress = models.CharField(max_length=300)
    parent_commaddress = models.CharField(max_length=300)
    parent_contactno = models.CharField(max_length=13)
    parent_email = models.CharField(max_length=30)
    parent_adharno = models.CharField(max_length=12)
    parent_occupation = models.CharField(max_length=300)
    parent_bloodgroup = models.IntegerField()

    def __str__(self):
        return self.student








