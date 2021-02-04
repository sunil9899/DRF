from django.contrib import admin
from django.urls import path
from api import views, views1

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentdetails/', views.StudentList.as_view()),
    # path('studentdetails/', views.StudentCreate.as_view()),
    # path('studentdetails/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('studentdetails/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentdetails/<int:pk>/', views.StudentDestroy.as_view()),
    path('studentdetails/', views.StudentListCreate.as_view()),
    # path('studentdetails/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    # path('studentdetails/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
    path('studentdetails/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
    path('studentdetails1/', views1.StudentListCreate.as_view()),
    path('studentdetails1/<int:pk>/',
         views1.StudentRetrieveUpdateDestroy.as_view()),
]
