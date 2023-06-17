from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
FACULTY_TYPE_CHOICES = (
        ("Doctor", 'Doctor'),
        ("Nurse", 'Nurse'),
        ("Receptionist", 'Receptionist'),
    )

DEPT_CHOICES = (
        ('Anesthesia & ICU Department', 'Anesthesia & ICU Department'),
        ('Behavioral Medicine', 'Behavioral Medicine'),
        ('Child Health', 'Child Health'),
        ('Clinical Physiology', 'Clinical Physiology'),
        ('Dental & Maxillofacial Surgery', 'Dental & Maxillofacial Surgery'),
        ('Emergency Medicine', 'Emergency Medicine'),
        ('Family Medicine & Public Health', 'Family Medicine & Public Health'),
        ('Genetics Department', 'Genetics Department'),
)

class CustomUser(AbstractUser):
    role = models.CharField(choices=FACULTY_TYPE_CHOICES, max_length=15)
    department = models.CharField(choices=DEPT_CHOICES, max_length=35)

    def __str__(self) -> str:
        return self.email

    def natural_key(self):
        return (self.email,)

class Doctor(models.Model):
    FACULTY_TYPE_CHOICES = [
        ("doctor", 'Doctor'),
        ("nurse", 'Nurse'),
        ("receptionist", 'Receptionist'),
    ]

    DEPT_CHOICES = [
        ('Anesthesia & ICU Department', 'Anesthesia & ICU Department'),
        ('Behavioral Medicine', 'Behavioral Medicine'),
        ('Child Health', 'Child Health'),
        ('Clinical Physiology', 'Clinical Physiology'),
        ('Dental & Maxillofacial Surgery', 'Dental & Maxillofacial Surgery'),
        ('Emergency Medicine', 'Emergency Medicine'),
        ('Family Medicine & Public Health', 'Family Medicine & Public Health'),
        ('Genetics Department', 'Genetics Department')
    ]

    department = models.CharField(max_length=100, choices=DEPT_CHOICES, default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



class Receptionist(models.Model):
    DEPT_CHOICES = [
        ('Anesthesia & ICU Department', 'Anesthesia & ICU Department'),
        ('Behavioral Medicine', 'Behavioral Medicine'),
        ('Child Health', 'Child Health'),
        ('Clinical Physiology', 'Clinical Physiology'),
        ('Dental & Maxillofacial Surgery', 'Dental & Maxillofacial Surgery'),
        ('Emergency Medicine', 'Emergency Medicine'),
        ('Family Medicine & Public Health', 'Family Medicine & Public Health'),
        ('Genetics Department', 'Genetics Department')
    ]

    department = models.CharField(max_length=100, choices=DEPT_CHOICES, default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Nurse(models.Model):
    DEPT_CHOICES = [
        ('Anesthesia & ICU Department', 'Anesthesia & ICU Department'),
        ('Behavioral Medicine', 'Behavioral Medicine'),
        ('Child Health', 'Child Health'),
        ('Clinical Physiology', 'Clinical Physiology'),
        ('Dental & Maxillofacial Surgery', 'Dental & Maxillofacial Surgery'),
        ('Emergency Medicine', 'Emergency Medicine'),
        ('Family Medicine & Public Health', 'Family Medicine & Public Health'),
        ('Genetics Department', 'Genetics Department')
    ]

    department = models.CharField(max_length=100, choices=DEPT_CHOICES, default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)