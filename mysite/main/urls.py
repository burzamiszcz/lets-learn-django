from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_new_offer", views.add_new_offer, name="add_new_offer"),
    path('ad/<adId>', views.show_offer, name="show_offer"),
    path('conversation/<str:receiver_username>/', views.conversation, name='conversation'),
    path('conversations/', views.conversations, name='conversations'),

]