from api.models import Student, CustomUser
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    class Meta:
        model = Student
        fields = ['password', 'index_number', 'full_name', 'name_with_initials', 'date_of_birth', 'gender', 'enrolled_date', 'address', 'special_notes']
    
    def create(self, validated_data):
        user_data = {
            'username': validated_data['index_number'],
            'password': validated_data.pop('password')
        }
        user = CustomUser.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student
    
class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
    def update(self, instance, validated_data):
        
        user_data = {
            'password': validated_data.pop('password')
        }
        
        CustomUser.objects.get(username=instance.index_number).update(**user_data)
        
        instance.index_number = validated_data.get('index_number', instance.index_number)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.name_with_initials = validated_data.get('name_with_initials', instance.name_with_initials)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.enrolled_date = validated_data.get('enrolled_date', instance.enrolled_date)
        instance.address = validated_data.get('address', instance.address)
        instance.special_notes = validated_data.get('special_notes', instance.special_notes)
        instance.save()
        return instance