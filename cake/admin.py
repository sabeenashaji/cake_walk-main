from django.contrib import admin
from . models import Category,Cake,Profile,SignUp


# Register your models here.
admin.site.register(Category)
admin.site.register(Cake)
admin.site.register(Profile)
admin.site.register(SignUp)