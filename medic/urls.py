
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from patient.views import search, RecordListView, RecordDetailView, RecordCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_signup/', user_views.signup, name='user_signup'),
    path('record/', RecordListView.as_view(), name='record'),
    path('record/search/', search, name='search'),
    path('record/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('record/new/', RecordCreateView.as_view(), name='new_record'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('patient.urls')),
    path('register/', include('practitioner.urls')),   
]
