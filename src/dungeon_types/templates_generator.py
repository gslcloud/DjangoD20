import os

DUNGEON_TYPES = {
    "cave": "cave_template",
    "castle": "castle_template",
    "dungeon": "dungeon_template",
}

TEMPLATES_DIR = "templates"
GENERATED_TEMPLATES_DIR = "generated_templates"

def detect_dungeon_type(dungeon_type):
    normalized_dungeon_type = dungeon_type.lower().strip()
    if normalized_dungeon_type not in DUNGEON_TYPES:
        raise ValueError("Unsupported dungeon type")
    return normalized_dungeon_type

def generate_template(dungeon_type):
    normalized_dungeon_type = detect_dungeon_type(dungeon_type)

    template_name = DUNGEON_TYPES[normalized_dungeon_type]

    template_path = os.path.join(TEMPLATES_DIR, template_name)
    if not os.path.exists(template_path):
        raise FileNotFoundError("Template file not found")

    # TODO: Implement logic to generate the template content
    template_content = f"Template for {normalized_dungeon_type}"

    generated_template_dir = os.path.join(GENERATED_TEMPLATES_DIR, normalized_dungeon_type)
    os.makedirs(generated_template_dir, exist_ok=True)

    generated_template_path = os.path.join(generated_template_dir, template_name)

    # TODO: Implement logic to write the generated template content to the file
    with open(generated_template_path, "w") as f:
        f.write(template_content)

    return generated_template_path