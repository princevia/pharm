from django.urls import path, include

from order import views


urlpatterns = [
    path('orders/', views.OrdersList.as_view()),
]
