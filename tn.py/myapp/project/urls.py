from django.urls import path
from . import views

urlpatterns = [
    path('addpoll',views.add_poll),
    path('getpoll',views.get_poll),
    path('question/<int:id>/', views.set_active),
    path('active', views.active_polls),
    path('qount/<int:id>/', views.poll_qount),
]
