# import des modules necessaire: 
import os
from PySide2 import QtWidgets , QtCore, QtGui
import pyautogui
import launch_other_app
import network_searching
import movie_reader
import music_reader
import glob
from math import *



#fenetre principal: 
class Bureau (QtWidgets.QWidget):
# initialisation: 
    def __init__(self):
        super().__init__()
        self.width, self.height = pyautogui.size()
        self.fenetre_bureau()
        self.connect_ui()
        self.position_des_fenetre = 0
                
# layout principal avec ses boutons: 
    def fenetre_bureau(self):
        """ création du fond et des differents boutons present sur l'interface principal"""

        couleur = "black"
        self.setStyleSheet(f'''
        background-color : {couleur};
        
        ''')

        """self.fond = QtWidgets.QPushButton(self)
        self.fond.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/python.jpg'))
        self.fond.move(0,0)
        self.fond.resize(self.width , self.height)
        self.fond.setIconSize(QtCore.QSize(self.width,self.height))
        self.fond.setStyleSheet('border-style: none;')"""

        self.btn_shortcut_list_work = QtWidgets.QPushButton(self)
        self.btn_shortcut_list_work.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/work.jpg'))
        self.btn_shortcut_list_work.move(0,0)
        self.btn_shortcut_list_work.resize(self.width/40 , self.width/40)
        self.btn_shortcut_list_work.setIconSize(QtCore.QSize(self.width/40,self.width/40))
        self.btn_shortcut_list_work.setFlat(True)

        self.btn_shortcut_list_game = QtWidgets.QPushButton(self)
        self.btn_shortcut_list_game.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/game.jpg'))
        self.btn_shortcut_list_game.move(self.width/40*1 , 0)
        self.btn_shortcut_list_game.resize(self.width/40 ,self.width/40)
        self.btn_shortcut_list_game.setIconSize(QtCore.QSize(self.width/40,self.width/40))
        self.btn_shortcut_list_game.setFlat(True)

        self.btn_shortcut_list_contact = QtWidgets.QPushButton(self)
        self.btn_shortcut_list_contact.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/contact.jpg'))
        self.btn_shortcut_list_contact.move((self.width/40)*2, 0)
        self.btn_shortcut_list_contact.resize(self.width/40 ,self.width/40)
        self.btn_shortcut_list_contact.setIconSize(QtCore.QSize(self.width/40,self.width/40))
        self.btn_shortcut_list_contact.setFlat(True)

        self.btn_music_read = QtWidgets.QPushButton(self)
        self.btn_music_read.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/music.jpg'))
        self.btn_music_read.move((self.width/40)*3, 0)
        self.btn_music_read.resize(self.width/40 ,self.width/40)
        self.btn_music_read.setIconSize(QtCore.QSize(self.width/40,self.width/40))
        self.btn_music_read.setFlat(True)

        self.btn_movie_read = QtWidgets.QPushButton(self)
        self.btn_movie_read.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/movie.jpg'))
        self.btn_movie_read.move((self.width/40)*4, 0)
        self.btn_movie_read.resize(self.width/40 ,self.width/40)
        self.btn_movie_read.setIconSize(QtCore.QSize(self.width/40,self.width/40))
        self.btn_movie_read.setFlat(True)

        self.fond_search = QtWidgets.QPushButton(self)
        self.fond_search.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/google.jpg'))
        self.fond_search.move((self.width/40)*5 , 0)
        self.fond_search.resize((self.width/40) , self.width/40)
        self.fond_search.setIconSize(QtCore.QSize((self.width/40) , self.width/40))
        self.fond_search.setStyleSheet('border-style: none;background-color : rgb(0,0,0,0%)')
        self.le_searching_network = QtWidgets.QLineEdit(self)
        self.le_searching_network.move((self.width/40)*6, 0)
        self.le_searching_network.resize((self.width/40)*6,self.width/40)
        self.le_searching_network.setStyleSheet('background-color : white ;border : none ;color : black;font-size: 27px;')
        self.pb_searching_network = QtWidgets.QPushButton(self)
        self.pb_searching_network.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/search.jpg'))
        self.pb_searching_network.move((self.width/40)*12, 0)
        self.pb_searching_network.resize(self.width/40,self.width/40)
        self.pb_searching_network.setIconSize(QtCore.QSize(self.width/40,self.width/40))
        self.pb_searching_network.setStyleSheet('background-color : rgb(0,0,0,0%);border : none;')

        self.btn_fermer= QtWidgets.QPushButton(self)
        self.btn_fermer.move((self.width/40)*13, 0)
        self.btn_fermer.resize(self.width/40,self.width/40)
        self.btn_fermer.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/fermer.jpg'))
        self.btn_fermer.setIconSize(QtCore.QSize(self.width/40,self.width/40))
   
# connection: 
    def connect_ui(self):
        self.btn_fermer.clicked.connect(self.quitter)
        self.btn_shortcut_list_game.clicked.connect(self.game_app_list)
        self.btn_shortcut_list_work.clicked.connect(self.work_app_list)
        self.pb_searching_network.clicked.connect(self.researching_network)
        self.btn_movie_read.clicked.connect(self.movie_list_open)
        self.btn_music_read.clicked.connect(self.music)
        self.btn_shortcut_list_contact.clicked.connect(self.contact_app_list)
        self.le_searching_network.returnPressed.connect(self.researching_network)   # activation par la touche entrer si le line edit est actif

# recherche google
    def researching_network(self):
        research = self.le_searching_network.text()
        self.le_searching_network.setText("")
        network_searching.network_research(research)

# ouvre les icone game
    def game_app_list(self):
        directory = os.path.dirname(__file__)+"/game_shortcut/**"
        module_a_lancer = launch_other_app
        if self.position_des_fenetre == 0:
            self.bouton_listing = []
            self.external_apps = []
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 1
        elif self.position_des_fenetre == 1:
            self.shoot_external_app_icon()
        elif self.position_des_fenetre == 4:
            self.destroy_movie_btn()
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 1
        else:
            self.shoot_external_app_icon()
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 1

# ouvrir la liste d'icone de logiciel de travail 
    def work_app_list(self):
        directory = os.path.dirname(__file__)+"/work_shortcut/**"
        module_a_lancer = launch_other_app
        if self.position_des_fenetre == 0:
            self.bouton_listing = []
            self.external_apps = []
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 2
        elif self.position_des_fenetre == 2:
            self.shoot_external_app_icon()
        elif self.position_des_fenetre == 4:
            self.destroy_movie_btn()
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 2
        else:
            self.shoot_external_app_icon()
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 2

#contact
    def contact_app_list(self):
        directory = os.path.dirname(__file__)+"/contact/**"
        module_a_lancer = launch_other_app
        if self.position_des_fenetre == 0:
            self.bouton_listing = []
            self.external_apps = []
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 3
        elif self.position_des_fenetre == 3:
            self.shoot_external_app_icon()
        elif self.position_des_fenetre == 4:
            self.destroy_movie_btn()
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 3
        else:
            self.shoot_external_app_icon()
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 3

# music
    def music(self):
        directory = os.path.dirname(__file__)+"/music/*"
        module_a_lancer = music_reader 
        if self.position_des_fenetre == 0:
            self.bouton_listing = []
            self.external_apps = []
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 6
        elif self.position_des_fenetre == 6:
            self.shoot_external_app_icon()
        elif self.position_des_fenetre == 4:
            self.destroy_movie_btn()
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 6
        else:
            self.shoot_external_app_icon()
            self.app_icon_show(module_a_lancer, directory)
            self.position_des_fenetre = 6

# creation des icones ( travail, game, music)
    def app_icon_show(self,module_a_lancer, directory):
        taille_du_fond=0
        ordonnée =1
        abscisse =0 
        for external_app in module_a_lancer.get_extern_app(directory ):
            taille_du_fond +=1
        taille_main_window =(self.width/40) + self.width/20*(1+(floor(taille_du_fond/7)))
        
        
        self.fond = QtWidgets.QPushButton(self)
        self.fond.resize(self.width/20*7, self.width/20*(1+(floor(taille_du_fond/7))))
        self.fond.move(0,self.width/40)
        self.fond.show()
        self.fond.setStyleSheet('background-color: rgb(20,20,20,95%);')
        
        for external_app in module_a_lancer.get_extern_app(directory ):
            self.external_apps.append(external_app)
            if f'image_{external_app.app_name()}.jpg' in os.listdir(os.path.dirname(__file__)+'/image'): 
                self.btn_external_app = QtWidgets.QPushButton(self)
                self.btn_external_app.setIcon(QtGui.QIcon(os.path.dirname(__file__)+'/image/image_'+ external_app.app_name()+'.jpg'))
                self.btn_external_app.setIconSize(QtCore.QSize(self.width/20-5,self.width/20-5))
                self.btn_external_app.setFlat(True)
            else:
                self.btn_external_app = QtWidgets.QPushButton(external_app.app_name(),self)
                self.btn_external_app.setStyleSheet("color : white;background-color:rgb(38,38,38);")
            
            self.btn_external_app.move(self.width/20*abscisse,self.width/20*(ordonnée-0.5))
            abscisse += 1
            if abscisse == 7:
                abscisse = 0
                ordonnée +=1
            self.btn_external_app.resize(self.width/20 ,self.width/20)
            
            self.btn_external_app.clicked.connect(external_app.launch)
            self.btn_external_app.clicked.connect(self.shoot_external_app_icon)            
            self.btn_external_app.show()
            self.bouton_listing.append(self.btn_external_app)
            resize(taille_main_window)
            
# destruction des icones (travail , game,music)
    def shoot_external_app_icon(self):
        for self.btn_external_app in self.bouton_listing:
            self.btn_external_app.deleteLater()
        self.fond.deleteLater()
        self.external_apps = []
        self.bouton_listing = []
        self.position_des_fenetre = 0
        
        resize(self.width/40)

# ouverture du lecteur de film
    def movie_list_open(self):
        if self.position_des_fenetre == 0:
            self.movie_list_ui()
            self.position_des_fenetre = 4
        elif self.position_des_fenetre == 4:
            self.destroy_movie_btn()
        else:
            self.shoot_external_app_icon()
            self.movie_list_ui()
            self.position_des_fenetre = 4

# creation de la liste de film
    def movie_list_ui(self):
        directory = os.path.dirname(__file__)+"/movie/**"
        movies = movie_reader.get_movie(directory)
        self.fond = QtWidgets.QPushButton(self)
        self.fond.resize(self.width/20*7,self.width/20)
        self.fond.move(0,self.width/40 )
        self.fond.setStyleSheet('background-color: rgb(20,20,20,95%);')
        self.fond.show()
        
        self.movie_list = QtWidgets.QListWidget(self)
        self.movie_list.setStyleSheet('''
        background-color: rgb(10,10,10,35%);
        color: rgb(80,80,80,95%);
        border:none;
        ''')
        self.btn_play_movie = QtWidgets.QPushButton("Play",self)
        self.btn_play_movie.move(self.width/40*9,self.width/40)
        self.btn_play_movie.resize(self.width/20,self.width/20)
        self.btn_play_movie.setStyleSheet("color : white;font-size: 27px;")
        self.btn_play_movie.show()

        for movie in movies:
            lw_movie = QtWidgets.QListWidgetItem(movie.app_name())
            lw_movie.setData(QtCore.Qt.UserRole , movie)
            self.movie_list.addItem(lw_movie)

        self.movie_list.move(self.width/40*4,self.width/40)
        self.movie_list.resize(self.width/40*4,self.width/20)
        self.movie_list.show()
        self.position_des_fenetre = 4
        self.btn_play_movie.clicked.connect(self.play_movie)
        resize(self.width/40 + self.width/20)

# lancer le film selectionner
    def play_movie(self):
        for selected_item in self.movie_list.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.read_movie()
        self.destroy_movie_btn()

# detruire les boutons pour selectioner un film 
    def destroy_movie_btn (self):

        self.fond.deleteLater()
        self.movie_list.deleteLater()
        self.btn_play_movie.deleteLater()
        self.bouton_listing = []
        self.external_apps = []
        self.position_des_fenetre = 0
        resize(self.width/40)

# quitter: 
    def quitter(self):
        exit()
        





def main_window():
    # lancer l'application
    
    
    a, b = pyautogui.size()
    ui.resize( a/40*14, a/40)
    ui.move(a/40*13, 0) 
    #ui.showMaximized()
    #ui.move(0, 0)
    ui.show()
    
    
def resize(taille_main_window, ): 
    width , height = pyautogui.size()
    ui.resize(width/40*14,taille_main_window)

app = QtWidgets.QApplication([])  
ui = Bureau()
ui.setWindowFlags(QtCore.Qt.FramelessWindowHint)       
main_window()
app.exec_()

