from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=255, unique=True)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    level = models.IntegerField()
    attributes = models.ManyToManyField(Attribute)

    def calculate_total_attribute_points(self):
        total_points = 0
        for attribute in self.attributes.all():
            total_points += attribute.value
        return total_points

    @property
    def class_details(self):
        return self.character_class.details

class CharacterClass(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()

class Attribute(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()