from django.urls import path
# Импортируем созданные нами представления
from .views import MainPage, DetailPage
urlpatterns = [
   path('', MainPage.as_view(), name='mainpage'),
   path('<int:pk>', DetailPage.as_view(), name='detailpage'),
]
