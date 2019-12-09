
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from django_registration.backends.one_step.views import RegistrationView
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('houses.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
