from django.urls import path
from levelfourapp import views

#Template tagging
app_name = 'levelfourapp'

urlpatterns = [
    path('relative/',views.relative, name='relative'),
    path('other/',views.other, name='other')
]
