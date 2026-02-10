from django.contrib import admin
from django.urls import path
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view()),

]