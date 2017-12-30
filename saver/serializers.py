from rest_framework import serializers
from .models import Algorithm, Distribution, Saver
from .models import Account, Liability, Asset
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = ('id', 'account_number', 'percentage')


class AlgorithmSerializer(serializers.ModelSerializer):
    distributions = DistributionSerializer(many=True)

    class Meta:
        model = Algorithm
        fields = ('id', 'name', 'distributions')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'balance')


class SaverSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    algorithm = AlgorithmSerializer()
    accounts = AccountSerializer(many=True)

    class Meta:
        model = Saver
        fields = ('id', 'algorithm', 'user', 'accounts')


class LiabilitySerializer(serializers.ModelSerializer):
    saver = SaverSerializer()

    class Meta:
        model = Liability
        fields = ('id', 'name', 'saver', 'cost')


class AssetSerializer(serializers.ModelSerializer):
    saver = SaverSerializer()

    class Meta:
        model = Asset
        fields = ('id', 'name', 'saver', 'income')
