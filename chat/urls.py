from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.index, name='index'),
    path('asosiy/', views.asosiy, name='asosiy'),
    path('yangiyil/', views.yangiyil, name='yangiyil'),
    path('youtubedownload/', views.youtubedownload, name='youtubedownload'),
    path('tiktokdownload/', views.tiktokdownload, name='tiktokdownload'),
    path('obxavo/', views.obxavo, name='obxavo'),
    path('adminChat/', views.adminChat, name='adminChat'),
    path('friend/', views.friend, name='friend'),
    path('albom/', views.albom, name='albom'),
    path('allfotoalbom/', views.allfotoalbom, name='allfotoalbom'),
    path('status/', views.status, name='status'),
    path('levelbuy/', views.levelbuy, name='levelbuy'),
    path('change_password', views.change_password, name='change_password'),
    path('oyin', views.oyin, name='oyin'),
    path('extra', views.extra, name='extra'),
    path('support', views.support, name='support'),
    path('kurs', views.kurs, name='kurs'),
    path('change_username', views.change_username, name='change_username'),
    path('anketa', views.anketa, name='anketa'),
    path('settings', views.settings, name='settings'),
    path('personalChange', views.personalChange, name='personalChange'),
    path('othersection', views.othersection, name='othersection'),
    path('chat', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('api/users/<int:pk>', views.user_list, name='user-detail'),
    path('api/users', views.user_list, name='user-list'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),

]
