from tkinter import Frame, Label, Entry, Button, END
from binary_search_tree import *

class VisualizerEditTab:
    """ Gère l’onglet en haut à gauche permettant d’ajouter/retirer des valeurs. """

    def __init__(self, visualizer, x, y):
        self.visualizer = visualizer

        self.frame = Frame(self.visualizer.window, width=200, height=100, bg="lightgrey", highlightbackground = "black", highlightthickness = 1)
        self.frame.place(x = x, y = y)

        self.add_label = Label(self.frame, text="Ajouter Valeur :", bg = "lightgrey")
        self.add_label.place(x = 10, y = 15)

        self.add_entry = Entry(self.frame, width=6)
        self.add_entry.place(x = 110, y = 15)

        self.add_button = Button(self.frame, text="OK", command=self.on_add, bg = "white")
        self.add_button.place(x = 160, y = 15)

        self.del_label = Label(self.frame, text="Enlever Valeur :", bg = "lightgrey")
        self.del_label.place(x = 10, y = 60)

        self.del_entry = Entry(self.frame, width=6)
        self.del_entry.place(x = 110, y = 60)

        self.del_button = Button(self.frame, text="OK", command=self.on_del, bg = "white")
        self.del_button.place(x = 160, y = 60)

    def on_add(self):
        """ Gère l'ajout des valeurs dans l'arbre. """

        value = int(self.add_entry.get()) # Récupère la valeur.
        self.visualizer.tree.insert(value) # Insère la valeur.
        self.visualizer.update() 
        self.add_entry.delete(0, END) # Efface la saisie.

    def on_del(self):
        """ Gère le retirement des valeurs dans l'arbre. """

        value = int(self.del_entry.get()) # Récupère la valeur.
        self.visualizer.tree.remove(value) # Insère la valeur.
        self.visualizer.update()
        self.del_entry.delete(0, END) # Efface la saisie.


class VisualizerInfoTab:
    """ Gère l’onglet en haut à droite affichant les informations sur l’arbre. """

    def __init__(self, visualizer, x, y):
        self.visualizer = visualizer

        self.frame = Frame(self.visualizer.window, width=200, height=100, bg="lightgrey", highlightbackground = "black", highlightthickness = 1)
        self.frame.place(x = x, y = y)

        self.size_label = Label(self.frame, text="Taille de l'arbre : ", bg = "lightgrey")
        self.size_label.place(x = 10, y = 5)

        self.depth_label = Label(self.frame, text="Profondeur de l'arbre : ", bg = "lightgrey")
        self.depth_label.place(x = 10, y = 35)

        self.leaf_label = Label(self.frame, text="Nombre de feuilles : ", bg = "lightgrey")
        self.leaf_label.place(x = 10, y = 65)

    def update(self):
        """ Met à jour les différent labels. """

        # Récupération des données. 
        size = self.visualizer.tree.size()
        depth = self.visualizer.tree.depth()
        leaves = self.visualizer.tree.leaves()

        # Mise à jour du texte.
        self.size_label.config(text="Taille de l'arbre : " + str(size))
        self.depth_label.config(text="Profondeur de l'arbre : " + str(depth))
        self.leaf_label.config(text="Nombre de feuilles : " + str(leaves))


class VisualizerCommandTab:
    """  Gère l’onglet en bas proposant diverses fonctionnalités. """

    def __init__(self, visualizer, x, y):
        self.visualizer = visualizer

        self.frame = Frame(self.visualizer.window, width=764, height=80, bg="lightgrey", highlightbackground = "black", highlightthickness = 1)
        self.frame.place(x = x, y = y)

        self.nouveau_button = Button(self.frame, text = "Nouveau", width = 10, command = self.nouveau)
        self.nouveau_button.place(x = 10, y = 10)

        self.largeur_button = Button(self.frame, text = "Largeur", width = 10, command = self.largeur)
        self.largeur_button.place(x = 120, y = 10)

        self.prefixe_button = Button(self.frame, text = "Préfixe", width = 10, command = self.prefixe)
        self.prefixe_button.place(x = 230, y = 10)

        self.infixe_button = Button(self.frame, text = "Infixe", width = 10, command = self.infixe)
        self.infixe_button.place(x = 340, y = 10)

        self.postfixe_button = Button(self.frame, text = "Postfixe", width = 10, command = self.postfixe)
        self.postfixe_button.place(x = 450, y = 10)

        self.export_button = Button(self.frame, text = "Exporter", width = 10, command = self.exporter)
        self.export_button.place(x = 560, y = 10)

        self.reduire_button = Button(self.frame, text = "Réduire", width = 10, command = self.reduire)
        self.reduire_button.place(x = 670, y = 10)

        self.output_entry = Entry(self.frame, width = 123)
        self.output_entry.place(x = 10, y = 50)

    def nouveau(self):
        """ Réinitialise l'arbre. """

        self.visualizer.tree = BinarySearchTree()
        self.visualizer.update()

    def infixe(self):
        """ Affiche les valeurs de l'arbre parcouru en infixe. """

        valeur = self.visualizer.tree.infixe()
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, valeur)

    def prefixe(self):
        """ Affiche les valeurs de l'arbre parcouru en préfixe. """

        valeur = self.visualizer.tree.prefixe()
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, valeur)

    def postfixe(self):
        """ Affiche les valeurs de l'arbre parcouru en postfixe. """

        valeur = self.visualizer.tree.postfixe()
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, valeur)

    def largeur(self):
        """ Affiche les valeurs de l'arbre parcouru en largeur. """

        valeur = self.visualizer.tree.largeur()
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, valeur)

    def exporter(self):
        """ Affiche l'arbre écrit sous forme de triplets imbriqués. """

        tree = self.visualizer.tree.exporter()
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, tree)
    
    def reduire(self):
        """
        Modifie la structure de l'arbre pour minimiser sa hauteur.
        Appelée lors du clic sur le bouton "Réduire".
        """

        valeur = self.visualizer.tree.reduire()
        self.nouveau()
        for c in valeur:
            self.visualizer.tree.insert(c) # Insère les nouvelles valeurs de l'arbre.
        self.visualizer.update()  # Mise à jour de l'affichage