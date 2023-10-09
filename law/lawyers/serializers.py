from rest_framework import serializers
from lawyers.models import Lawyers
from django.contrib.auth import get_user_model

User = get_user_model()

class LawyerSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = Lawyers
        fields = ('id', 'username', 'password', 'password_confirmation', 'email', 'phone_number', 'rank')

    def check_fields(self, data):
        # Check if the fields are empty
        required_fields = ['username', 'password', 'password_confirmation', 'email', 'phone_number', 'rank']

        for field_name in required_fields:
            if not data.get(field_name):
                raise serializers.ValidationError(f'{field_name} cannot be empty!!!')

    def validate_username(self, value):
        # Check if username exists
        if Lawyers.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username already exists")
        return value
    
    def validate_email(self, value):
        # Check if email exists
        if Lawyers.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists")
        return value
    
    def validate(self, data):
        # Check if passwords match
        password = data.get('password')
        password_confirmation = self.context.get('request').data.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match')
        
        return data
    
    def create(self, validated_data):
        password_confirmation = validated_data.pop('password_confirmation', None)

        if validated_data['password'] != password_confirmation:
            raise serializers.ValidationError('Passwords do not match')
        
        user = User.objects.create_user(**validated_data)

        return user
        
