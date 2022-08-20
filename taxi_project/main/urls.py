from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index_page', views.index_page, name='index_page'),
    path('drivers', views.drivers_page, name='drivers_page'),
    path('drivers_application', views.drivers_application_page, name='drivers_application_page'),
    path('passengers', views.passengers_page, name='passengers_page'),
    path('helpdesk', views.helpdesk_page, name='helpdesk_page'),
    path('register', views.register_page, name='register_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_view, name='logout_view'),
    path('profile', views.profile_page, name='profile_page'),
    path('profile/delete', views.profile_delete_view, name='delete_profile'),

]