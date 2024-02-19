# generate_fake_data.py

# Set up Django environment
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Change 'your_project' to your Django project name
django.setup()

# Import Django models
from home.models import Person

people_data = [
    ("James Smith", "Always has more expressions than an emoji keyboard."),
    ("Mary Johnson", "Could turn any conversation into a monologue about coffee beans."),
    ("John Williams", "Once sent a text to a microwave by accident."),
    ("Patricia Brown", "Turns every situation into a groan-worthy pun fest."),
    ("Robert Jones", "Owns more gadgets than Batman's utility belt."),
    ("Linda Davis", "Can make a dance party happen in a library."),
    ("Michael Miller", "Treats snack bags and dip jars like a science experiment."),
    ("Jennifer Garcia", "Conversation is basically a meme showcase."),
    ("William Martinez", "Crafting attempts end up looking like modern art."),
    ("Elizabeth Robinson", "Joint pains predict the weather better than meteorologists.")
]


for p in people_data:
    person = Person(name=p[0], description=p[1])
    person.save()
    print(f"Saved {person}")