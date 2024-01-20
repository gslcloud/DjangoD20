from django.db import models

class DungeonType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    # Add validations for fields
    def clean(self):
        # Validate name length
        if len(self.name) > 255:
            raise ValidationError("Name is too long.")

    # Add foreign key relationship to Project or Campaign model
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='dungeon_types')

    # Add additional fields
    difficulty_level = models.IntegerField(choices=DIFFICULTY_LEVEL_CHOICES)
    length = models.IntegerField()
    recommended_party_size = models.IntegerField()

    # Add methods for performing common operations
    def calculate_average_rating(self):
        # Code to calculate average rating based on user reviews
        pass