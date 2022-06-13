from ModQA import *

class WinGame():

     def message(self):

          felicitacion ='                         ¡FELICIDADES!'
          winner = f'''                 
Has demostrado ser toda una enciclopedia, te mente este llena de conocimiento.
Has alcanzado el premio mayor gracias a tus destrezas! 
     '''

          return [felicitacion, winner]

class StartGame():

     def message(self):
          welcome = '!BIENVENIDO JUGADOR!'
          introduction = '''                 
                              Hola , bienvenido a este divertido juego llamado JUEGO DE CONOCIMIENTO, ¿estás preparado para poner a prueba tus conocimientos?
                         El juego es sencillo, debes pasar 5 rondas, en cada ronda se te hará una pregunta, 
                              obviamente en cada ronda la pregunta será más complicada que la anterior, 
                                   si eliges la opción correcta recibirás una bonificación, si fallas se acabará el juego. 
                              También tienes la opción de abandonar si no estás preparado para pasar al siguiente nivel.

                              Entonces, ¿estás listo para empezar? 

                              ¡EMPECEMOS!     
          '''
          return [welcome, introduction]


class EndGame():

     def message(self):
          sorry = f'''         QUE PENA!
          
               Al parecer no lograste completar este nivel
          
          Fortalece tus conocimientos y te esperamos en tu proximo intento!'''
          
          retire = f'''
                         TE HAS RETIRADO!
          Pero no te sientas mal por ello, tampoco esta mal dar un paso a costado al tiempo.
               Fortalece tus conocimientos y te esperamos en tu proximo intento!
     
     '''

          return [sorry, retire]