import threading 
import time
from threading import Thread
import gui as gui
import ml as ml 
from random import randint
import concurrent.futures

class main():

    def __init__(self):

        my_gui = gui.GUI()
        my_ml = ml.ML()

        t1 = time.perf_counter()

        my_classes = [my_gui, my_ml]
        i = 0 

        for my_classes[i] in range (0,1): 
            print("il processo si sta eseguendo") 


        with concurrent.futures.ThreadPoolExecutor() as executor:

        t2 = time.perf_counter()

        #creo i miei thread

      #  my_gui = gui.GUI()
       # my_ml = ml.ML()

    #li faccio avviare 

      #  my_gui.start()
      #  my_ml.start()

        #per attendere che un thread termini 
       # my_gui.join()
       # my_ml.join()

      #  print("Fine")

        #definisco i lock
      #  threadLock = threading.Lock()

        
