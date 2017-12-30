# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from django.conf import settings


class Algorithm(models.Model):
    name = models.CharField(_('Nombre'), max_length=150)

    class Meta:
        verbose_name = "Algorithm"
        verbose_name_plural = "Algorithms"

    def __str__(self):
        return self.name


class Distribution(models.Model):
    account_number = models.IntegerField(_('Número de cuenta'))
    percentage = models.IntegerField(_('Porcentaje de distribución'))
    algorithm = models.ForeignKey(
        Algorithm,
        verbose_name=_('Algoritmo de ahorro'),
        related_name='distributions'
    )

    class Meta:
        verbose_name = "Distribution"
        verbose_name_plural = "Distributions"

    def __str__(self):
        return str(self.account_number) + ' :' + str(self.percentage)


class Saver(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Usuario'),
        related_name='savers'
    )

    algorithm = models.ForeignKey(
        Algorithm,
        verbose_name=_('Algoritmo de ahorro'),
        related_name='savers'
    )

    class Meta:
        verbose_name = "Saver"
        verbose_name_plural = "Savers"

    def __str__(self):
        return self.user.username + " " + self.algorithm.name


class Account(models.Model):
    name = models.CharField(_('Nombre de la cuenta'), max_length=50)
    balance = models.FloatField(_('Balance'))
    saver = models.ForeignKey(
        Saver,
        verbose_name=_('Ahorrador'),
        related_name='accounts'
    )

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.name + ' :' + str(self.balance)


class Liability(models.Model):
    name = models.CharField(_('Nombre'), max_length=150)
    cost = models.FloatField(_('Costo'))
    saver = models.ForeignKey(
        Saver,
        verbose_name=_('Ahorrador'),
        related_name='liabilities'
    )

    class Meta:
        verbose_name = "Liability"
        verbose_name_plural = "Liabilities"

    def __str__(self):
        return self.name + ' :' + str(self.cost)


class Asset(models.Model):
    name = models.CharField(_('Nombre'), max_length=150)
    income = models.FloatField(_('Ganancia'))
    saver = models.ForeignKey(
        Saver,
        verbose_name=_('Ahorrador'),
        related_name='assets'
    )

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"

    def __str__(self):
        return self.name + ' :' + str(self.income)
