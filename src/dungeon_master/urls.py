from django.urls import path
from . import views

app_name = 'dungeon_master'

urlpatterns = [
    path('characters/', views.character_list, name='dungeon_master:character_list'),  # Permission: Authenticated user
    path('characters/create/', views.create_character, name='dungeon_master:create_character'),  # Permission: Authenticated user
    path('characters/<int:pk>/', views.character_detail, name='dungeon_master:character_detail'),  # Permission: Authenticated user
    path('characters/<int:pk>/update/', views.update_character, name='dungeon_master:update_character'),  # Permission: Admin only
    path('characters/<int:pk>/delete/', views.delete_character, name='dungeon_master:delete_character'),  # Permission: Admin only

    # Add URL patterns for dungeons and other components as needed
]