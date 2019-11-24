from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'upload'
urlpatterns =[
        path('upload_file/', views.upload_file, name='upload_file'),
        
        path('handle_uploaded_file/', views.handle_uploaded_file, name='handle_uploaded_file'),
        #url(r'upload_file/$', views.upload_file),
        ]
