from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_projects/', views.add_projects, name='add_projects'),
    path("project_index/", ProjectIndexView.as_view(), name="project_index"),
    path("project_index/<int:pk>/", views.project_detail, name="project_detail"),
    path('project/<int:pk>/update/',
         ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/',
         ProjectDeleteView.as_view(), name='project_delete'),
]
