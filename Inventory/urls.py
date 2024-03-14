from django.urls import path
from .views import *

urlpatterns=[
         path('home/',Homepage),
         path('contact/',Contactpage),
          path('about/',Aboutpage),
          path('services/',Servicespage),
          path('peacock/',Peacock),
]