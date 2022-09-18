from rest_framework import serializers
from account.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'full_name', 'username' )