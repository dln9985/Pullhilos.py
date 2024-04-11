import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

print("")
print("----------------------------------------")
print("2 hilos")

globalarrayNum = []
def EnumeradorDos( inicio, fin ):
    logging.info(f'Función con rango: {inicio} - {fin}')
    for i in range ( inicio, fin+1 , 1):
        globalarrayNum.append(i)
        time.sleep(0.01)
    return 0

t0 = time.time()
listaHilos= []
t= threading.Thread(target=EnumeradorDos, args=(1,50))
listaHilos.append(t)
t.start()
t= threading.Thread(target=EnumeradorDos, args=(51,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join()
    
tf = time.time() - t0

globalarrayNum.sort()
print(f"Tiempo de ejecución: {tf}")
print (globalarrayNum)

print("----------------------------------------")
print("Pool de hilos")

def printHW():
    logging.info(f'Función HW')
    print("Hola Mundo :)")
    
Num_Veces= 4  

t0 = time.time()
globalarrayNum = []
with ThreadPoolExecutor( max_workers= 2 ) as executor:
    Valinicio = 1
    rango = 200
    subrango = int(rango//Num_Veces)
    for i in range(Valinicio,  rango , subrango):
        executor.submit(EnumeradorDos, Valinicio, subrango )
        Valinicio = 1 + subrango
        subrango = (rango//Num_Veces) + subrango

tf = time.time() - t0

globalarrayNum.sort()   
print(f"Tiempo de ejecución: {tf}") 
print(globalarrayNum)