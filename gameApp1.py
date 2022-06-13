import tkinter as tk
from Messages import *
from ModQA import *
from random import randint

RAM = randint(1, 5)
S = StartGame()
E = EndGame()
W = WinGame()

#    ===//esta clase contiene el primer frame, que es el de bienvenida//===
class StartPage(tk.Frame):

     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller
          self.text = tk.StringVar(self, value='')

          self.init_widgets()


     def move_pages(self):
          self.controller.show_frame(PageOne)
          #Player(self.controller.txt)

     def init_widgets(self):
          tk.Label(
               self,
               text=S.message()[0],
               font=('Helvetica', 20, 'bold', 'italic'
               )).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=100,
               padx=40
          )
          tk.Label(
               self,
               text='Introduce Tu Nombre Jugador!',
               bg='RoyalBlue1',
               fg='gainsboro',
               font=('Helvetica', 10, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               expand=True
          )
          tk.Entry(
               self,
               justify=tk.CENTER,
               textvariable=self.text
          ).pack(
               side=tk.TOP,
               expand=True
          )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command= self.move_pages
          ).pack(
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )
          tk.Label(
               self,
               text=S.message()[1],
               font=('Helvetica', 11, 'bold', 'italic'
                     )).pack(
               expand=True,
               pady=30,
               padx=50
          )


#	===//se encarga de ejecutar el 1er frame y la 1ra ronda//===
class PageOne(tk.Frame):

     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller
          self.answerOpts = tk.IntVar(self, value=1)

          self.init_widgets()

     def retire_option(self):
          self.controller.show_frame(RetirePage)

     def move_pages(self):
          self.controller.answer = self.answerOpts.get()
          if RAM == 1:
               if self.controller.answer == 1:
                    self.controller.show_frame(PageTwo)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 2:
               if self.controller.answer == 3:
                    self.controller.show_frame(PageTwo)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 3:
               if self.controller.answer == 4:
                    self.controller.show_frame(PageTwo)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 4:
               if self.controller.answer == 4:
                    self.controller.show_frame(PageTwo)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 5:
               if self.controller.answer == 4:
                    self.controller.show_frame(PageTwo)
               else:
                    self.controller.show_frame(FinalPageB)

     def init_widgets(self):
          PATH = '\challenge1'
          QA = QuestionAndAnswer(RAM, PATH)
          tk.Label(
               self,
               text=f'NIVEL 1',
               font=('Helvetica', 8, 'bold', 'italic'),
          ).pack(
               anchor='ne',
               expand=True,
               pady=20,
               padx=20
          )
          tk.Label(
               self,
               text='RONDA 1',
               font=('Helvetica', 13, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=40
          )
          tk.Label(
               self,
               text=QA.question(),
               font=('Helvetica', 15, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=35
          )
          optionsFrame = tk.Frame(self)
          optionsFrame.configure()
          optionsFrame.pack(
               side=tk.TOP,
               fill=tk.BOTH,
               padx=30,
               pady=30
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[0],
               variable = self.answerOpts,
               activebackground='deep sky blue',
               value=1
               ).grid(
               column=0,
               row=2,
               sticky='w'
               )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[1],
               variable = self.answerOpts,
               activebackground='deep sky blue',
               value=2
               ).grid(
               column=3,
               row=2,
               sticky='w'
               )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[2],
               variable = self.answerOpts,
               activebackground='deep sky blue',
               value=3
               ).grid(
               column=5,
               row=2,
               sticky='w'
               )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[3],
               variable = self.answerOpts,
               activebackground='deep sky blue',
               value=4
               ).grid(
               column=7,
               row=2,
               sticky='w'
               )
          tk.Button(
               self,
               text='Retirarse',
               bg='gainsboro',
               command=self.retire_option,
               anchor='w'
               ).pack(
                    fill='x',
                    pady=30,
                    padx=550,
                    expand=True
               )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command=self.move_pages,
               anchor='e'
          ).pack(
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )
          
#	===//se encarga de ejecutar la ronda 2//===
class PageTwo(tk.Frame):
     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller
          self.answerOpts = tk.IntVar(self, value=1)

          self.init_widgets()

     def retire_option(self):
          self.controller.show_frame(RetirePage)

     def move_pages(self):
          self.controller.answer = self.answerOpts.get()
          if RAM == 1:
               if self.controller.answer == 2:
                    self.controller.show_frame(PageThree)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 2:
               if self.controller.answer == 3:
                    self.controller.show_frame(PageThree)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 3:
               if self.controller.answer == 3:
                    self.controller.show_frame(PageThree)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 4:
               if self.controller.answer == 4:
                    self.controller.show_frame(PageThree)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 5:
               if self.controller.answer == 1:
                    self.controller.show_frame(PageThree)
               else:
                    self.controller.show_frame(FinalPageB)

     def init_widgets(self):
          PATH = '\challenge2'
          QA = QuestionAndAnswer(RAM, PATH)
          tk.Label(
               self,
               text=f'NIVEL 3',
               font=('Helvetica', 8, 'bold', 'italic'),
          ).pack(
               anchor='ne',
               expand=True,
               pady=20,
               padx=20
          )
          tk.Label(
               self,
               text='RONDA 2',
               font=('Helvetica', 13, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=40
          )
          tk.Label(
               self,
               text=QA.question(),
               font=('Helvetica', 13, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=35
          )
          optionsFrame = tk.Frame(self)
          optionsFrame.configure()
          optionsFrame.pack(
               side=tk.TOP,
               fill=tk.BOTH,
               padx=30,
               pady=30
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[0],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=1
                         ).grid(
               column=0,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[1],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=2
                         ).grid(
               column=3,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[2],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=3
                         ).grid(
               column=5,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[3],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=4
                         ).grid(
               column=7,
               row=2,
               sticky='w'
          )
          tk.Button(
               self,
               text='Retirarse',
               bg='gainsboro',
               command=self.retire_option
          ).pack(
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command=self.move_pages
          ).pack(
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )
          
#	===//ronda 3 del juego//===
class PageThree(tk.Frame):
     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller
          self.answerOpts = tk.IntVar(self, value=1)

          self.init_widgets()

     #    ===//esta opcion permite mostrar el frame para retirarse del juego//===
     def retire_option(self):
          self.controller.show_frame(RetirePage)

     #    ===//esta opcion nos movera al frame del siguiente nivel, sino te muestra el frame con el mensaje de consuelo//===
     def move_pages(self):
          self.controller.answer = self.answerOpts.get()
          if RAM == 1:
               if self.controller.answer == 3:
                    self.controller.show_frame(PageFour)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 2:
               if self.controller.answer == 4:
                    self.controller.show_frame(PageFour)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 3:
               if self.controller.answer == 1:
                    self.controller.show_frame(PageFour)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 4:
               if self.controller.answer == 2:
                    self.controller.show_frame(PageFour)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 5:
               if self.controller.answer == 2:
                    self.controller.show_frame(PageFour)
               else:
                    self.controller.show_frame(FinalPageB)

     #    ===//estos son los widgets que controlan la app//===
     def init_widgets(self):
          PATH = '\challenge3'
          QA = QuestionAndAnswer(RAM, PATH)

          tk.Label(
               self,
               text=f'NIVEL 3',
               font=('Helvetica', 8, 'bold', 'italic'),
          ).pack(
               anchor='ne',
               expand=True,
               pady=20,
               padx=20
          )
          tk.Label(
               self,
               text='RONDA 2',
               font=('Helvetica', 13, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=40
          )
          tk.Label(
               self,
               text=QA.question(),
               font=('Helvetica', 15, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=35
          )
          optionsFrame = tk.Frame(self)
          optionsFrame.configure()
          optionsFrame.pack(
               side=tk.TOP,
               fill=tk.BOTH,
               padx=30,
               pady=30
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[0],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=1
                         ).grid(
               column=0,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[1],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=2
                         ).grid(
               column=3,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[2],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=3
                         ).grid(
               column=5,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[3],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=4
                         ).grid(
               column=7,
               row=2,
               sticky='w'
          )
          tk.Button(
               self,
               text='Retirarse',
               bg='gainsboro',
               command=self.retire_option
          ).pack(
               anchor=tk.W,
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command=self.move_pages
          ).pack(
               anchor=tk.E,
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )
          
#	===//se encarga de ejecutar la ronda 4//===
class PageFour(tk.Frame):
     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller
          self.answerOpts = tk.IntVar(self, value=1)

          self.init_widgets()

     def retire_option(self):
          self.controller.show_frame(RetirePage)

     def move_pages(self):
          self.controller.answer = self.answerOpts.get()
          if RAM == 1:
               if self.controller.answer == 4:
                    self.controller.show_frame(PageFive)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 2:
               if self.controller.answer == 1:
                    self.controller.show_frame(PageFive)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 3:
               if self.controller.answer == 3:
                    self.controller.show_frame(PageFive)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 4:
               if self.controller.answer == 2:
                    self.controller.show_frame(PageFive)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 5:
               if self.controller.answer == 2:
                    self.controller.show_frame(PageFive)
               else:
                    self.controller.show_frame(FinalPageB)

     #    ===//estos son los widgets que controlan la app//===
     def init_widgets(self):
          PATH = '\challenge4'
          QA = QuestionAndAnswer(RAM, PATH)

          tk.Label(
               self,
               text=f'NIVEL 4',
               font=('Helvetica', 8, 'bold', 'italic'),
          ).pack(
               anchor='ne',
               expand=True,
               pady=20,
               padx=20
          )
          tk.Label(
               self,
               text='RONDA 4',
               font=('Helvetica', 13, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=40
          )
          tk.Label(
               self,
               text=QA.question(),
               font=('Helvetica', 15, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=35
          )
          optionsFrame = tk.Frame(self)
          optionsFrame.configure()
          optionsFrame.pack(
               side=tk.TOP,
               fill=tk.BOTH,
               padx=30,
               pady=30
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[0],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=1
                         ).grid(
               column=0,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[1],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=2
                         ).grid(
               column=3,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[2],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=3
                         ).grid(
               column=5,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[3],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=4
                         ).grid(
               column=7,
               row=2,
               sticky='w'
          )
          tk.Button(
               self,
               text='Retirarse',
               bg='gainsboro',
               command=self.retire_option,
               anchor='w'
          ).pack(
               anchor=tk.W,
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command=self.move_pages,
               anchor='w'
          ).pack(
               anchor=tk.E,
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )

#	===//se encarga de ejecutar la ronda 5//===
class PageFive(tk.Frame):
     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller
          self.answerOpts = tk.IntVar(self, value=1)

          self.init_widgets()

     def retire_option(self):
          self.controller.show_frame(RetirePage)

     def move_pages(self):
          self.controller.answer = self.answerOpts.get()
          if RAM == 1:
               if self.controller.answer == 4:
                    self.controller.show_frame(FinalPageW)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 2:
               if self.controller.answer == 3:
                    self.controller.show_frame(FinalPageW)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 3:
               if self.controller.answer == 1:
                    self.controller.show_frame(FinalPageW)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 4:
               if self.controller.answer == 2:
                    self.controller.show_frame(FinalPageW)
               else:
                    self.controller.show_frame(FinalPageB)
          if RAM == 5:
               if self.controller.answer == 4:
                    self.controller.show_frame(FinalPageW)
               else:
                    self.controller.show_frame(FinalPageB)

     #    ===//estos son los widgets que controlan la app//===
     def init_widgets(self):
          PATH = '\challenge5'
          QA = QuestionAndAnswer(RAM, PATH)

          tk.Label(
               self,
               text=f'NIVEL 5',
               font=('Helvetica', 8, 'bold', 'italic'),
          ).pack(
               anchor='ne',
               expand=True,
               pady=20,
               padx=20
          )
          tk.Label(
               self,
               text='RONDA 2',
               font=('Helvetica', 13, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=40
          )
          tk.Label(
               self,
               text=QA.question(),
               font=('Helvetica', 15, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               fill='x',
               expand=True,
               pady=60,
               padx=35
          )
          optionsFrame = tk.Frame(self)
          optionsFrame.configure()
          optionsFrame.pack(
               side=tk.TOP,
               fill=tk.BOTH,
               padx=30,
               pady=30
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[0],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=1
                         ).grid(
               column=0,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[1],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=2
                         ).grid(
               column=3,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[2],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=3
                         ).grid(
               column=5,
               row=2,
               sticky='w'
          )
          tk.Radiobutton(optionsFrame,
               text=QA.answer()[3],
               variable=self.answerOpts,
               activebackground='deep sky blue',
               value=4
                         ).grid(
               column=7,
               row=2,
               sticky='w'
          )
          tk.Button(
               self,
               text='Retirarse',
               bg='gainsboro',
               command=self.retire_option
          ).pack(
               anchor=tk.E,
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command=self.move_pages
          ).pack(
               anchor=tk.E,
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )

 #   ===//frame que envia el mensaje al ganar el juego//===
class FinalPageW(tk.Frame):
     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller

          self.init_widgets()

     def move_pages(self):
          self.controller.show_frame(StartPage)

     def init_widgets(self):
          tk.Label(
               self,
               text=W.message()[0],
               font=('Helvetica', 16, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               expand=True,
               pady=30,
               padx=50
          )
          tk.Label(
               self,
               text=W.message()[1],
               font=('Helvetica', 13, 'bold', 'italic')
          ).pack(
               side=tk.TOP,
               expand=True,
               pady=30,
               padx=50
          )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command=self.move_pages
          ).pack(
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )


# 	===//frame si el jugador se retira//===
class RetirePage(tk.Frame):
     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller

          self.init_widgets()

     def move_pages(self):
          self.controller.show_frame(StartPage)

     def init_widgets(self):
          tk.Label(
               self,
               text=E.message()[1],
               font=('Helvetica', 12, 'bold', 'italic'
                     )).pack(
               expand=True,
               pady=30,
               padx=50
               )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command=self.move_pages
          ).pack(
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )


#	===//frame si el jugador pierde//===
class FinalPageB(tk.Frame):
     def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(background='RoyalBlue1')
          self.controller = controller

          self.init_widgets()

     def move_pages(self):
          self.controller.show_frame(StartPage)

     def init_widgets(self):
          tk.Label(
               self,
               text=E.message()[0],
               font=('Helvetica', 12, 'bold', 'italic'
                     )).pack(
               expand=True,
               pady=30,
               padx=50
               )
          tk.Button(
               self,
               text='Continuar',
               bg='gainsboro',
               command=self.move_pages
          ).pack(
               fill='x',
               pady=30,
               padx=550,
               expand=True
          )