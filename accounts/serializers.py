from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ('id', 'email', 'password',
                  'first_name', 'last_name', 'address', 'dob', 'mobile')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create_user(**validated_data)
        return user