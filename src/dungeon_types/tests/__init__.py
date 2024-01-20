import unittest

from .test_dungeon_types import DungeonTypesFeatureTest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(DungeonTypesFeatureTest))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

```python
import unittest

class DungeonTypesFeatureTest(unittest.TestCase):
    def setUp(self):
        # Add setup logic here
        pass

    def tearDown(self):
        # Add teardown logic here
        pass

    def test_create_dungeon_types(self):
        # Add test case logic here
        pass
    
    def test_switch_configurations(self):
        # Add test case logic here
        pass
    
    def test_verify_dungeon_templates(self):
        # Add test case logic here
        pass

if __name__ == "__main__":
    unittest.main()