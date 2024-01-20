# Dungeon Master Initialization File

from django.db import models

class DungeonMaster:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Welcome, {self.name}! Prepare to embark on a new adventure in the world of Dungeon Master.")

    def create_dungeon(self, name):
        dungeon = Dungeon(name)
        dungeon.save()
    
    def delete_dungeon(self, dungeon):
        dungeon.delete()
    
    def get_dungeon(self, name):
        try:
            dungeon = Dungeon.objects.get(name=name)
            return dungeon
        except Dungeon.DoesNotExist:
            print(f"Dungeon {name} does not exist.")
    
    def get_all_dungeons(self):
        dungeons = Dungeon.objects.all()
        return dungeons


class Dungeon(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name