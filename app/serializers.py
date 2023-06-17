from rest_framework import serializers
from app.models import *
from django.contrib.auth.hashers import make_password
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer


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

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(choices=FACULTY_TYPE_CHOICES)
    department = serializers.ChoiceField(choices=DEPT_CHOICES)
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['role'] = self.validated_data.get('role', '')
        data_dict['department'] = self.validated_data.get('department', '')
        return data_dict

class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('role','department',)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'