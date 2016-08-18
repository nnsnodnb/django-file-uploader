from django.conf.urls import url
from upload_form import views

urlpatterns = [
    url(r'^$', views.form, name = 'form'),
    url(r'^complete/', views.complete, name = 'complete'),
]
