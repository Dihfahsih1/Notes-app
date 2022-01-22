from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes" ),
    path('notes/', views.getNotes, name="notes" ),
    path('notes/create/', views.createNote, name="create-Note" ),
    path('notes/<str:pk>/update/', views.updateNote, name="update-Note" ),
    path('notes/<str:pk>/delete/', views.deleteNote, name="delete-Note" ),
    path('notes/<str:pk>/', views.getNote, name="note" ),
]
