from django.contrib import admin

from .models import Food, Method, Nutrition

admin.site.register(Food)
admin.site.register(Method)
admin.site.register(Nutrition)
