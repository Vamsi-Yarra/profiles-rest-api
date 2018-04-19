from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """
    Serializes a name string for testing our APIView
    """
    name = serializers.CharField(max_length=10)

    #DRF serializer provides in-built validations
class UserProfileSerializer(serializers.ModelSerializer):
    """A Serializer for our user profile objects"""

    class Meta:
        model = models.UserProfile
    #this tells django serializer that this model UserProfile is used
        fields = ('id','email','name','password')
        extra_kwargs = {'password': {'write_only':True}}
    #user the UserProfile model make sure password is Write write_only

    def create(self,validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
        email = validated_data['email'],
        name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
