from django.contrib import admin
from .models import Deposits, User, Wallet
# admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Wallet)
admin.site.register(Deposits)
# Register your models here.
