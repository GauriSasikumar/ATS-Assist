from rest_framework import serializers
from .models import Applicant, Skill, Job

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"



class GetApplicantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id','username','skills', 'name', 'experience', 'education', 'email', 'about', 'location']



class GetApplicantSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['username', 'skills']



class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"