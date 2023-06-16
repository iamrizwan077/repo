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
class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(choices=FACULTY_TYPE_CHOICES)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['role'] = self.validated_data.get('role', '')
        return data_dict

class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('role',)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'