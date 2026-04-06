from django.urls import path
from .views import UserView, RoleView

urlpatterns = [
    path('users', UserView.as_view()),            # GET, POST
    path('users/<int:id>', UserView.as_view()),   # GET one, PUT, DELETE
    path('roles', RoleView.as_view()),
]

