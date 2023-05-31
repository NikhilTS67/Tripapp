from . import views
from django.urls import path

urlpatterns = [
        path('',views.fstfn, name='fstfn'),
        # path('second/', views.sndfn, name='sndfn'),
        # path('second/third/', views.thdfn, name='thdfn'),
        # path('fourth/', views.forfn, name='forfn')

]