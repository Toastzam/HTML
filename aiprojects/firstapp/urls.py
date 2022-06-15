from django.urls import path
from.import views

urlpatterns = [
    path('',views.hi),
    path('carami',views.carami),
    path('young',views.young)
]
