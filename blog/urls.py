from django.urls import path
from django.conf.urls.static import static
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs),
    path('<int:id>/', views.details, name = 'newblog')
]