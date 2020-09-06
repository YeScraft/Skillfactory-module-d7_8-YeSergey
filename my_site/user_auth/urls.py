from django.urls import reverse_lazy
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from user_auth.views import index, RegisterView, CreateUserProfile
from allauth.account.views import login, logout

app_name = 'user_auth'
urlpatterns = [
    path('', index, name='index'),
    # path('login/', login, name='login'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', logout, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(template_name='register.html',
                                           success_url=reverse_lazy('user_auth:profile-create')), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
    path('accounts/', include('allauth.urls')),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
