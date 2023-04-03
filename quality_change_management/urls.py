from django.contrib import admin
from django.urls import include, path
from .views import main, test

app_name = 'quality_change_management'
urlpatterns = [
    path('', main.top_page, name='top_page'),
    path('test/', test.test, name='test')

]