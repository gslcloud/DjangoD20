from django.db import models


class Dungeon(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    dungeon = models.ForeignKey(Dungeon, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Monster(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='monsters')
    name = models.CharField(max_length=255)
    level = models.IntegerField()

    def __str__(self):
        return self.name


class Item(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name