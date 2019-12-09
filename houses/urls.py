from django.urls import path
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update'),
    path('house/details/<int:id>/', views.details, name='details'),
    path('houses/', views.houses, name='houses'),
    path('search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)