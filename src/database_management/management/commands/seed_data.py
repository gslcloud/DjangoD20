"""
This module provides seed data for the Dungeon Master application.
"""

from typing import Dict, List, Type

from django.db.models import Model

def seed_data(model: Type[Model], data: List[Dict[str, str]]) -> None:
    """
    Seed data into the given model.

    Args:
        model (Type[Model]): The model to seed data into.
        data (List[Dict[str, str]]): A list of dictionaries containing the data to seed.

    Raises:
        ValueError: If the data list is empty or if the required fields are missing.
    """
    if not data:
        raise ValueError("Data list cannot be empty")

    required_fields = model._meta.required_fields
    for entry in data:
        missing_fields = [field for field in required_fields if field not in entry]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    for entry in data:
        model.objects.create(**entry)


# Example usage
if __name__ == "__main__":
    from myapp.models import MyModel
    
    example_data = [
        {"field1": "value1", "field2": "value2", "field3": "value3"},
        {"field1": "value4", "field2": "value5", "field3": "value6"},
    ]
    
    seed_data(MyModel, example_data)