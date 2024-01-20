from django.db import models

class CharacterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    scaffold_template = models.TextField()

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    abilities = models.ManyToManyField(Ability)

    def __str__(self):
        return self.name