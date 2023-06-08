from django.urls import path
from .views import landing_page
from django.conf.urls.static import static

urlpatterns = [
    path('', landing_page, name='landing_page'),
]

