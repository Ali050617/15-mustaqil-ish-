from django.urls import path
from . import views


app_name = 'courses'


urlpatterns = [
    path('list', views.course_list, name='courses_list'),
    path('create/', views.courses_create, name='courses_create'),
    path('update/<int:pk>/', views.course_update, name='update'),
    path('detail/<int:pk>/', views.course_detail,  name='detail'),
    path('delete/<int:pk>/', views.course_delete, name='delete')
]