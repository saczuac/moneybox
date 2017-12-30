# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from .models import Algorithm, Distribution, Saver
from .models import Account, Liability, Asset
from rest_framework import viewsets
from serializers import UserSerializer, AlgorithmSerializer
from serializers import SaverSerializer, DistributionSerializer
from serializers import AccountSerializer, LiabilitySerializer
from serializers import AssetSerializer
# from rest_framework import permissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class DistributionViewSet(viewsets.ModelViewSet):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class SaverViewSet(viewsets.ModelViewSet):
    queryset = Saver.objects.all()
    serializer_class = SaverSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class LiabilityViewSet(viewsets.ModelViewSet):
    queryset = Liability.objects.all()
    serializer_class = LiabilitySerializer
    # permission_classes = (permissions.IsAuthenticated,)


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    # permission_classes = (permissions.IsAuthenticated,)
