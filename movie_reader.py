# module pour lancer des app externe
import os
import json
import glob


# recuperer instance d'app
def get_movie(directory):
    appli_ext = []
    for fichier in glob.glob(directory, recursive=True ):
        if fichier.endswith("mkv"):
            appli_ext.append(Other_app(fichier))
        elif fichier.endswith(".mp4"):
            appli_ext.append(Other_app(fichier))
        elif fichier.endswith(".flv"):
            appli_ext.append(Other_app(fichier))
        elif fichier.endswith(".avi"):
            appli_ext.append(Other_app(fichier))
        elif fichier.endswith(".mpg"):
            appli_ext.append(Other_app(fichier))

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
    def read_movie(self):
        os.startfile(self.directory)

