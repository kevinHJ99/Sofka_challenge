# Sofka_Challenge
 
 Este programa llamado el juego del conocimiento, realizado en el lenguaje python, con la libreria de interfaz grafica tkinter, solicitado por la empresa Sokfa para el reto tecnico, es entregado por parte de Kevin Fernando Hoyos.
 
 El programa con de 5 carpetas, cada una con el nombre "challenge", y numerada segun la dificultad de cada nivel.
 cada una cuenta con 6 archivos de texto, en uno se hayan las preguntas y en el otro las respuestas.
 
 el programa se compone de 5 archivos:
 
 el primero es el de ModQA: este tiene una clasa que tiene por atributo un numero random y un path, esto para que tanto el metodo "question" y "answer" obtenegan de forma pertinenete tanto las preguntas aleatorias de cada ronda, como las respuestas.
 
 el segudo es el de mensajes: en este archivo seguardan algunos metodos con mensajes en caso de que se gane, se pierda o se retire del juego.
 
 el tercero es el de manager: este archivo es la pieza clave del funcionamiento del programa a traves de la interfaz grafica, pues es el que almecena y nos ayuda y cambiar de frames, sin la necesidad de abrir ventanas, es el programa desde el cual se ejecuta toda la estructura.
 
 el cuarto es el de appgame1: en este esta el funcionamiento de todo el programa, los cambios de frames para las siguientesrondas, el manejo de botones y mas.
 
 el quinto y ultimo, es el archivo Main(): este archivo solo se encarga de importar a manager y finalmente ejecutar el juego.
