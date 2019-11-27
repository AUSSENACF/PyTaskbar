# module pour lancer des app externe
import os
import json
import glob


# recuperer instance d'app
def get_extern_app(directory):
    appli_ext = []
    appli_ext = [Other_app(fichier) for fichier in glob.glob(directory, recursive=True ) if fichier.endswith(".lnk") or fichier.endswith(".url")]
    return appli_ext

# les differente utilisation des app externe
class Other_app:
    def __init__(self , directory):
        self.directory = directory
        
# .app_name(): nom de l app
    def app_name(self):
        self.name = (self.directory.split('\\')[-1])
        self.name = self.name.split(".")[0]
        return self.name
# .launch(): lancement de l app
    def launch(self):
        os.startfile (self.directory)