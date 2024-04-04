from django.urls import path
from rental import views

urlpatterns = [
    path('offers/', views.OfferList.as_view(), name='offer-list'),
    path('offers/<int:pk>/', views.OfferDetails.as_view(), name='offer-details'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetails.as_view(), name='user-details'),
]
