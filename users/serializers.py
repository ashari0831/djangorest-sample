from rest_framework import serializers
from users.models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

    def create(self, validated_data):

        return User.objects.create_user(
                name=validated_data['name'], 
                email=validated_data['email'],
                password=validated_data['password']
            )

