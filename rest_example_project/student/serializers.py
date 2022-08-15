from rest_framework.serializers import ModelSerializer
from .models import Student

class StudientSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ["name","age","class_student", "height", "weight"]