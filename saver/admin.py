# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Algorithm, Distribution, Saver
from .models import Account, Liability, Asset

admin.site.register(Algorithm)
admin.site.register(Distribution)
admin.site.register(Saver)
admin.site.register(Account)
admin.site.register(Liability)
admin.site.register(Asset)
