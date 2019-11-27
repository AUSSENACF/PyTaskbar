# module pour lancer des app externe
import os
import json
import glob


# recuperer instance d'app
def get_extern_app(directory):
    appli_ext = []
    appli_ext = [Other_app(fichier) for fichier in glob.glob(directory, recursive=True ) ]
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
    def directory_path(self):
        return self.directory
# .launch(): lancement de l app
    def launch(self):
        if self.directory.endswith(".mp3") or self.directory.endswith(".url"):
            os.startfile(self.directory)
        else:
            try:
                playlist = os.path.join(os.path.dirname(__file__), 'playlist.m3u')
                with open(playlist, 'w') as f:
                        f.write("#EXTM3U")
                musics = []
                musics =  [Other_app(fichier) for fichier in glob.glob(self.directory+"/**", recursive=True ) if fichier.endswith(".mp3") ]
                for music in musics:
                    with open(playlist, 'a') as f:
                        f.write(f"\n#EXTINF:0,{music.app_name()}.mp3\n{music.directory_path()}")
                os.startfile(playlist)
            except:
                print("erreur")                       
                        
                        
                        
                        
                        
                        
                        
"""for file in mp3_list:
f.write(file + "\n")
directory_list.append(music.directory_path())
os.startfile(directory_list)

mp3_list =[i for i in os.listdir(os.path.dirname(__file__)+"/music")  if i.endswith(".mp3")]
print(mp3_list)


os.startfile(playlist)








directory = os.path.dirname(__file__)+"/music" 
extensions = [
        ".mp3",
        ".m4a",
        ".ogg",
        ".flac",
    ]              
files = []

for file in os.listdir(directory):
    file = os.path.join(directory, file)
    if os.path.isdir(file):
            files.extend(_get_all_files(file, extensions))
    elif os.path.splitext(file)[1].lower() in extensions:
            files.append(file)



playlist = os.path.join(os.path.dirname(__file__), 'playlist.m3u')


music_files = []
musics =[fichier for fichier in glob.glob(os.path.dirname(__file__)+"/music", recursive=True ) if fichier.endswith(".mp3")]
for music in musics:
    music_files.append(music)

playlist = os.path.join(BASE_DIRECTORY, 'playlist.m3u')

    

music_files = files

with open(playlist, 'w') as f:
    for file in music_files:
        f.write(file + "\n")

os.startfile(playlist)"""
           
            
