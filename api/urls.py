from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', obtain_auth_token),

    path('get-user/<str:pk>/', getRole),
    path('add-profile-info/', profileInfo),
    path('get-profile-info/<str:pk>/', getProfileInfo),
    path('update-profile-info/<str:pk>/', updateProfileInfo),

    path('get-shop-name/', getShopName),
    path('get-shop-name/<str:pk>/', getSingleShopName),

    path('add-coffee/', addCoffee),
    path('get-coffee/', getCoffee),
    path('get-single-item/<str:pk>/', getSingleItem),
    path('update-coffee/<str:pk>/', updateCoffee),

    path('add-recommended-coffee/', addRecommendedCoffee),
    path('get-recommended-coffee/', getRecommendedCoffee),
    path('delete-recommended-coffee/<str:pk>/', deleteRecommendedCoffee),

    path('add-is-favourite/', addIsFavourite),
    path('get-is-favourite/', getIsFavourite),
    path('is-favourite/<str:pk>/', isFavourite),

    path('get-order/', getOrder),
    path('make-order/', makeOrder),
    path('delete-order/<str:pk>/', orderDelete),
]