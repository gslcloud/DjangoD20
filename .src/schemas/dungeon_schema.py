from django.db import models


class DungeonSchema(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dungeon = models.ForeignKey(DungeonSchema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name