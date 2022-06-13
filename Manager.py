import tkinter as tk
from Messages import *
from gameApp1 import *


#         ===//esta clase es la encargada de inicializar todo//===
#         ===//tambien es la encargada de crear el metodo con el cual se generan nuevos frames//===
class App(tk.Tk):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.title('Juego de Preguntas')

          container = tk.Frame(self)
          container.pack(
               side= tk.TOP,
               fill= tk.BOTH,
               expand=True
          )
          self.answer = 1
          self.txt = ''
          container.configure(background='RoyalBlue1')
          container.grid_columnconfigure(0, weight=1)
          container.grid_rowconfigure(0, weight=1)

          self.frames = {}

          for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, FinalPageB, FinalPageW, RetirePage):
               frame = F(container, self)
               self.frames[F] = frame
               frame.grid(row=0, column=0, sticky="nsew")
          self.show_frame(StartPage)

     def show_frame(self, container):
          frame = self.frames[container]
          frame.tkraise()