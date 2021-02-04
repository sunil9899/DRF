from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentdetails/', views.ListCreateStudentAPI.as_view()),
    path('studentdetails/<int:pk>/',
         views.RetrieveUpdateDestroyStudentAPI.as_view()),
]
