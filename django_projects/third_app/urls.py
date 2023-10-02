from django.urls import  path
from .views import *

urlpatterns = [
    path('', appfirst, name='appfirst'),
    path('class/', appclass, name='appclass'),
    path('info/', appinfo, name='appinfo'),
    path('contacts/', appcontact, name='appcontact'),
    path('table/', apptable, name='apptable'),
    path('signup/', appsign, name="appsign"),
    path('restapi/', customerCreateView.as_view(), name='rest'),
    path('restapi/<int:pk>/', customerCreateSpecific.as_view(), name='rests'),
    path('secondrest/<int:pk>/', practiceCreateView.as_view(), name='secondApi'),
    path('thirdrest/<int:pk>/', apiCreateSpecific.as_view(), name="thirdrest")
]