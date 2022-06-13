'''
este modulo contiene el procedimiento para
obtener las preguntas y las respuestas
mediante archivo de texto

'''
import linecache

#         ===//las preguntas se obtienen de forma aleatoria con el uso del modulo random//===
#         ===//este sera instanciado mediante el metodo contructor//===
class QuestionAndAnswer():
     def __init__(self, random=None, path=''):
          self.random = random
          self.path = path

     #    ===//este metodo contiene las preguntas//===
     def question(self):
          with open(self.path+'\preguntas.txt') as f:
               if self.random == 1:
                    self.query1 = f.readlines()[0]
                    print(self.query1)
                    return self.query1
               elif self.random == 2:
                    self.query2 = f.readlines()[1]
                    print(self.query2)
                    return self.query2
               elif self.random == 3:
                    self.query3 = f.readlines()[2]
                    print(self.query3)
                    return self.query3
               elif self.random == 4:
                    self.query4 = f.readlines()[3]
                    print(self.query4)
                    return self.query4
               elif self.random == 5:
                    self.query5 = f.readlines()[4]
                    print(self.query5)
                    return self.query5

     #    ===//este metodo contiene las respuestas//===
     def answer(self):
          if self.random == 1:
               self.answer1 = linecache.getline(self.path+'\Answers1.txt', 1).strip()
               self.answer2 = linecache.getline(self.path+'\Answers1.txt', 2).strip()
               self.answer3 = linecache.getline(self.path+'\Answers1.txt', 3).strip()
               self.answer4 = linecache.getline(self.path+'\Answers1.txt', 4).strip()
               print(self.answer1)
               print(self.answer2)
               print(self.answer3)
               print(self.answer4)
               return [self.answer1, self.answer2, self.answer3, self.answer4]
          elif self.random == 2:
               self.answer1 = linecache.getline(self.path+'\Answers2.txt', 1).strip()
               self.answer2 = linecache.getline(self.path+'\Answers2.txt', 2).strip()
               self.answer3 = linecache.getline(self.path+'\Answers2.txt', 3).strip()
               self.answer4 = linecache.getline(self.path+'\Answers2.txt', 4).strip()
               print(self.answer1)
               print(self.answer2)
               print(self.answer3)
               print(self.answer4)
               return [self.answer1, self.answer2, self.answer3, self.answer4]
          elif self.random == 3:
               self.answer1 = linecache.getline(self.path+'\Answers3.txt', 1).strip()
               self.answer2 = linecache.getline(self.path+'\Answers3.txt', 2).strip()
               self.answer3 = linecache.getline(self.path+'\Answers3.txt', 3).strip()
               self.answer4 = linecache.getline(self.path+'\Answers3.txt', 4).strip()
               print(self.answer1)
               print(self.answer2)
               print(self.answer3)
               print(self.answer4)
               return [self.answer1, self.answer2, self.answer3, self.answer4]
          elif self.random == 4:
               self.answer1 = linecache.getline(self.path+'\Answers4.txt', 1).strip()
               self.answer2 = linecache.getline(self.path+'\Answers4.txt', 2).strip()
               self.answer3 = linecache.getline(self.path+'\Answers4.txt', 3).strip()
               self.answer4 = linecache.getline(self.path+'\Answers4.txt', 4).strip()
               print(self.answer1)
               print(self.answer2)
               print(self.answer3)
               print(self.answer4)
               return [self.answer1, self.answer2, self.answer3, self.answer4]
          elif self.random == 5:
               self.answer1 = linecache.getline(self.path+'\Answers5.txt', 1).strip()
               self.answer2 = linecache.getline(self.path+'\Answers5.txt', 2).strip()
               self.answer3 = linecache.getline(self.path+'\Answers5.txt', 3).strip()
               self.answer4 = linecache.getline(self.path+'\Answers5.txt', 4).strip()
               print(self.answer1)
               print(self.answer2)
               print(self.answer3)
               print(self.answer4)
               return [self.answer1, self.answer2, self.answer3, self.answer4]