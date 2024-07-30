from django.urls import path
from mon_api.views import get_personnes
from mon_api.views import PersonneRegisterView, PlayerRegisterView, ManagerRegisterView, PersonneLoginView, PersonneLogoutView

urlpatterns = [
    path('register/', PersonneRegisterView.as_view(), name='register'),
    path('register/player/', PlayerRegisterView.as_view(), name='register-player'),
    path('register/manager/', ManagerRegisterView.as_view(), name='register-manager'),
    path('login/', PersonneLoginView.as_view(), name='login'),
    path('logout/', PersonneLogoutView.as_view(), name='logout'),
    path('personnes/', get_personnes, name='get_personnes'),
]
