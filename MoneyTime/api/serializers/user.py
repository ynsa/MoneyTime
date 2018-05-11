# 3rd party
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # merchant = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'last_login',
        )

    # def get_merchant(self, obj):
    #     return MerchantForUserSerializer(obj.merchant).data
