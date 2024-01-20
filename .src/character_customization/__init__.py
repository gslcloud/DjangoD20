from typing import List, Optional
from .character_classes import CharacterClass
from .scaffolding_templates import ScaffoldTemplate


class CharacterCustomization:
    def __init__(self) -> None:
        self.character_classes: List[CharacterClass] = [
            CharacterClass(name="Warrior", strength=10, agility=5, intelligence=3),
            CharacterClass(name="Mage", strength=3, agility=5, intelligence=10),
            CharacterClass(name="Rogue", strength=5, agility=10, intelligence=3),
        ]

        self.scaffold_templates: List[ScaffoldTemplate] = [
            ScaffoldTemplate(name="Basic", base_template="base.html"),
            ScaffoldTemplate(name="Advanced", base_template="advanced_base.html"),
            ScaffoldTemplate(name="Custom", base_template="custom_base.html"),
        ]

    def get_character_classes(self) -> List[CharacterClass]:
        return self.character_classes

    def add_character_class(self, character_class: CharacterClass) -> None:
        self.character_classes.append(character_class)

    def get_scaffold_templates(self) -> List[ScaffoldTemplate]:
        return self.scaffold_templates

    def add_scaffold_template(self, scaffold_template: ScaffoldTemplate) -> None:
        self.scaffold_templates.append(scaffold_template)

    def generate_character(self, class_name: str) -> Optional[dict]:
        character_class = None
        for cls in self.character_classes:
            if cls.name == class_name:
                character_class = cls
                break

        if character_class is not None:
            character = {
                "class_name": character_class.name,
                "strength": character_class.strength,
                "agility": character_class.agility,
                "intelligence": character_class.intelligence,
            }
            return character
        else:
            raise CharacterClassNotFoundError(f"Invalid character class name: {class_name}")


class CharacterClassNotFoundError(ValueError):
    pass