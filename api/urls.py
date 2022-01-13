from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes" ),
    path('Notes/', views.getNotes, name="notes" ),
    path('Note/<str:pk>', views.getNote, name="note" ),
]
