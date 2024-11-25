class BinarySearchTree:
    """ Gère la structure abstraite de l’arbre binaire de recherche. """

    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, value, depth = 1):
        """ Insère la valeur rentrée dans l'arbre. """

        if not (0 <= value <= 999) or depth > 6:
            return None

        if self.root is None:
            self.root = value
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        else:
            if value < self.root:
                self.left.insert(value, depth + 1)
            elif value > self.root:
                self.right.insert(value, depth + 1)
            else: 
                print("Insertion impossible.")

    def remove(self, value):
        """ Retire la valeur rentrée de l'arbre. """

        if self.root is None:
            return None

        if value == self.root:
            if self.left.root is None:
                return self.right
            elif self.right.root is None:
                return self.left
            else:
                min_value = self.right.find_min()
                self.root = min_value
                self.right = self.right.remove(min_value)
        elif value < self.root:
            self.left = self.left.remove(value)
        else:
            self.right = self.right.remove(value)

        return self

    def find_min(self):
        if self.left.root is None:
            return self.root
        return self.left.find_min()

    def size(self):
        """ Retourne la taille de l'arbre. """

        if self.root is None:
            return 0
        return 1 + self.left.size() + self.right.size()

    def depth(self):
        """ Retourne la profondeur de l'arbre. """

        if self.root is None:
            return 0
        return 1 + max(self.left.depth(), self.right.depth())

    def leaves(self):
        """ Retourne le nombre de feuilles dans l'arbre. """

        if self.root is None:
            return 0
        if self.left.root is None and self.right.root is None:
            return 1
        return self.left.leaves() + self.right.leaves()

    def infixe(self):
        """ Affiche les valeurs de l'arbre parcouru en infixe. """

        if self.root is None:
            return " "
        return self.left.infixe() + str(self.root) + "," + self.right.infixe()

    def prefixe(self):
        """ Affiche les valeurs de l'arbre parcouru en préfixe. """

        if self.root is None:
            return " "
        return str(self.root) + "," + self.left.prefixe() + self.right.prefixe()

    def postfixe(self):
        """ Affiche les valeurs de l'arbre parcouru en postfixe. """

        if self.root is None:
            return " "
        return self.left.postfixe() + self.right.postfixe() + str(self.root) + ","

    def largeur(self):
        resultat = []
        if self.root is not None:
            queue = [self]
            while queue:
                current = queue.pop(0)
                resultat.append(str(current.root))
                if current.left.root is not None:
                    queue.append(current.left)
                if current.right.root is not None:
                    queue.append(current.right)
        return ', '.join(resultat)

    def exporter(self):
        """ Renvoie une chaîne de caractère décrivant l’arbre à l’aide de triplets imbriqués."""

        if self.root is None:
            return "()"
        return "({}, {}, {})".format(self.root, self.left.exporter(), self.right.exporter())

    def restructurer_liste_recursive(self, liste):
        if not liste:
            return []

        taille = len(liste)
        milieu = taille // 2

        gauche = liste[:milieu]
        droite = liste[milieu:]

        restructuree = [droite] + [gauche]

        return restructuree[0] + self.restructurer_liste_recursive(restructuree[1])
    
    def reduire(self):
        prefixe = self.prefixe()
        prefixe = extraire_nombres(prefixe)
        

        return self.restructurer_liste_recursive(prefixe)

def extraire_nombres(chaine):
    """ Extrait les nombre d'une chaine de caractère"""
    
    nombres = []
    nombre_actuel = ''
    chiffre = "1234567890"
    for caractere in chaine:
        if caractere in chiffre:
            nombre_actuel += caractere
        elif nombre_actuel:
            nombres.append(int(nombre_actuel))
            nombre_actuel = ''
    if nombre_actuel:
        nombres.append(int(nombre_actuel))
    return nombres