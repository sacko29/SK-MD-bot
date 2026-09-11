import os
import importlib

def load_commands():
    """Charge automatiquement toutes les commandes du dossier commands/"""
    commands = []
    commands_dir = os.path.dirname(__file__)

    print(f"📂 Dossier commands : {commands_dir}")
    print(f"📄 Fichiers trouvés : {os.listdir(commands_dir)}")

    for filename in os.listdir(commands_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"commands.{filename[:-3]}"
            try:
                print(f"⏳ Chargement de {module_name}...")
                module = importlib.import_module(module_name)
                if hasattr(module, "register"):
                    module.register(commands)
                    print(f"✅ {filename} chargé avec succès")
                else:
                    print(f"⚠️ {filename} n'a pas de fonction register")
            except Exception as e:
                print(f"❌ ERREUR dans {filename} : {e}")

    print(f"📦 Total commandes chargées : {len(commands)}")
    return commands
