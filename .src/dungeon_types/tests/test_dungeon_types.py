import unittest
import re
from dungeon_generator import DungeonGenerator

class TestDungeonTypes(unittest.TestCase):

    def test_generate_dungeon_type_forest(self):
        generator = DungeonGenerator()
        dungeon_type = generator.generate_dungeon_type("forest")
        self.assertEqual(dungeon_type, "Forest")

    def test_generate_dungeon_type_cave(self):
        generator = DungeonGenerator()
        dungeon_type = generator.generate_dungeon_type("cave")
        self.assertEqual(dungeon_type, "Cave")

    def test_generate_dungeon_type_castle(self):
        generator = DungeonGenerator()
        dungeon_type = generator.generate_dungeon_type("castle")
        self.assertEqual(dungeon_type, "Castle")

    def test_generate_dungeon_type_tower(self):
        generator = DungeonGenerator()
        dungeon_type = generator.generate_dungeon_type("tower")
        self.assertEqual(dungeon_type, "Tower")

    def test_generate_dungeon_type_village(self):
        generator = DungeonGenerator()
        dungeon_type = generator.generate_dungeon_type("village")
        self.assertEqual(dungeon_type, "Village")

    def test_generate_dungeon_type_invalid(self):
        generator = DungeonGenerator()
        dungeon_type = generator.generate_dungeon_type("invalid")
        self.assertIsNone(dungeon_type)

    def test_generate_dungeon_type_format(self):
        generator = DungeonGenerator()
        dungeon_type = generator.generate_dungeon_type("forest")
        self.assertIsNotNone(dungeon_type)
        self.assertTrue(re.match(r"^[A-Z]", dungeon_type))

if __name__ == '__main__':
    unittest.main()