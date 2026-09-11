import os
import importlib

COMMANDS = []

def load_commands():
    """Charge automatiquement toutes les commandes du dossier commands/"""
    commands_dir = os.path.dirname(__file__)
    for filename in os.listdir(commands_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"commands.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "register"):
                module.register(COMMANDS)
    return COMMANDS
