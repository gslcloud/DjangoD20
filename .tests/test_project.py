import pytest
from django.test import TestCase
from ..models import Dungeon


@pytest.fixture
def dungeon_data():
    return {
        'name': 'Test Dungeon',
        'dungeon_type': 'maze',
        'size': 10,
    }


@pytest.mark.django_db
class DungeonTestCase(TestCase):
    def test_create_dungeon(self, dungeon_data):
        # Create a new dungeon
        dungeon = Dungeon.objects.create(**dungeon_data)
        
        # Verify that the dungeon is saved to the database
        self.assertEqual(Dungeon.objects.count(), 1)
        
        # Verify the dungeon attributes
        self.assertEqual(dungeon.name, dungeon_data['name'])
        self.assertEqual(dungeon.dungeon_type, dungeon_data['dungeon_type'])
        self.assertEqual(dungeon.size, dungeon_data['size'])
        
    def test_set_invalid_dungeon_type(self):
        dungeon = Dungeon()
        
        # Set an invalid dungeon type
        with self.assertRaises(ValueError):
            dungeon.dungeon_type = 'invalid_type'
    
    def test_generate_map(self, dungeon_data):
        dungeon = Dungeon.objects.create(**dungeon_data)
        
        # Generate the dungeon map
        dungeon.generate_map()
        
        # Verify that the map is generated
        self.assertIsNotNone(dungeon.map)
        
        # Verify the dimensions of the generated map
        self.assertEqual(len(dungeon.map), dungeon.size)
        self.assertEqual(len(dungeon.map[0]), dungeon.size)

    # Add more test cases for edge cases and additional functionality

