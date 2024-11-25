from tkinter import Tk, Canvas
from visualizer_tabs import *
from binary_search_tree import *

class BinarySearchTreeVisualizer:
    def __init__(self):
        # Init de Tkinter.
        self.window = Tk()
        self.window.title("Binary Search Tree Visualizer")
        self.window.geometry("800x600")
        self.window.config(bg = "white")
        self.window.resizable(0, 0)

        self.canvas = Canvas(self.window, width = 800, height = 400, bg = "white", highlightthickness = 0)
        self.canvas.place(x=0, y=120)

        # Init des différents onglets.
        self.edit_tab = VisualizerEditTab(self, 20, 5)
        self.info_tab = VisualizerInfoTab(self, 580, 5)
        self.command_tab = VisualizerCommandTab(self, 18, 510)

        # Init de l'arbre.
        self.tree = BinarySearchTree()

        self.update()

        self.window.mainloop()

    def draw(self, tree, x, y, depth=1):
        if tree.root is not None:
            radius = 11
            center_x = x
            center_y = y

            self.canvas.create_oval(center_x - radius, center_y - radius,
                                    center_x + radius, center_y + radius, outline = "black",
                                    fill = "lightgrey")

            self.canvas.create_text(center_x, center_y, text=str(tree.root))

            x2 = 6 * (2 ** (6 - depth))
            y2 = 70

            if tree.left is not None and tree.left.root is not None:
                left_x = x - x2
                left_y = y + y2
                self.canvas.create_line(center_x, center_y, left_x, left_y, fill="black")
                self.draw(tree.left, left_x, left_y, depth + 1)

            if tree.right is not None and tree.right.root is not None:
                right_x = x + x2
                right_y = y + y2
                self.canvas.create_line(center_x, center_y, right_x, right_y, fill="black")
                self.draw(tree.right, right_x, right_y, depth + 1)


    def update(self):
        self.canvas.delete("all")
        self.draw(self.tree, 400, 15)
        self.info_tab.update()

a = BinarySearchTreeVisualizer()
