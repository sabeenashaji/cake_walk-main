
from django.urls import path
from . import views
app_name="cake"

urlpatterns = [
   path("",views.home,name="home"),
   path("product/",views.product,name="product"),
   path("single_product/<int:pk>/",views.single_product,name="single_product"),
   path("profile/",views.profile,name="profile"),
   path("contact/",views.contact,name="contact"),
   path("signup/",views.signup,name="signup"),
   path("login/",views.login,name="login"),
]
