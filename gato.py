import random
import time
import os

gato_tablero = {
    "A1":"",
    "A2":"",
    "A3":"",
    "B1":"",
    "B2":"",
    "B3":"",
    "C1":"",   
    "C2":"",   
    "C3":"",   
}
alternativas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
x = " "
def mostrar_tablero():
    print('')
    print(4*x +'1', 3*x +'2', 3*x +'3')
    print('')
    print("A", 3*x+ gato_tablero["A1"], " | ", gato_tablero["A2"], " | ", gato_tablero["A3"])
    print(3*x +'--------------')
    print("B", 3*x+ gato_tablero["B1"], " | ", gato_tablero["B2"], " | ", gato_tablero["B3"],)
    print(3*x +'--------------')
    print("C", 3*x+ gato_tablero["C1"], " | ", gato_tablero["C2"], " | ", gato_tablero["C3"],)
    print('')
    print('')

contador_empate = 0
mostrar_tablero()

ficha_jugador=''
ficha_cpu=''

print("Bienvenido a GATO")
print("Usted se enfrentará a la CPU")
while True:
    ficha = input("Elija su ficha 'X' / 'O'")
    if ficha == 'X':
        ficha_jugador = ficha
        ficha_cpu = 'O'
        break
    elif ficha == 'O':
        ficha_jugador = ficha
        ficha_cpu = 'X'
        break
    else:
        print("Ficha equivocada, Intente Nuevamente")
        time.sleep(1)
        continue

if ficha_jugador == 'X' or ficha_jugador=='O':
    print("Su Ficha elegida es: ", ficha_jugador)
    print("La ficha de la cpu es: ", ficha_cpu)
    mostrar_tablero()
    input("Presione Enter para continuar...")

while True:
    os.system("cls")
    mostrar_tablero()
    while True:
        print("El jugador", ficha_jugador ,"está en su jugada\n")
        jugada1 = input("Ingrese su jugada: ")
        if gato_tablero.get(jugada1) == "":
            gato_tablero[jugada1] = ficha_jugador
            contador_empate += 1
            break
        else:
            print("Posición ocupada")
            print("Vuelva a intentar")
            continue
    #COMPROBAR SI ES GANADOR
    if gato_tablero["A1"] == ficha_jugador and gato_tablero["A2"] == ficha_jugador and gato_tablero["A3"] == ficha_jugador:
        print("Felicitaciones!: GANASTE")
        break
    elif gato_tablero["B1"] == ficha_jugador and gato_tablero["B2"] == ficha_jugador and gato_tablero["B3"] == ficha_jugador:
        print("Felicitaciones!: GANASTE")
        break        
    elif gato_tablero["C1"] == ficha_jugador and gato_tablero["C2"] == ficha_jugador and gato_tablero["C3"] == ficha_jugador:
        print("Felicitaciones!: GANASTE")
        break
    elif gato_tablero["A1"] == ficha_jugador and gato_tablero["B1"] == ficha_jugador and gato_tablero["C1"] == ficha_jugador:
        print("Felicitaciones!: GANASTE")
        break        
    elif gato_tablero["A2"] == ficha_jugador and gato_tablero["B2"] == ficha_jugador and gato_tablero["C2"] == ficha_jugador:
        print("Felicitaciones!: GANASTE")
        break        
    elif gato_tablero["A3"] == ficha_jugador and gato_tablero["B3"] == ficha_jugador and gato_tablero["C3"] == ficha_jugador:
        print("Felicitaciones!: GANASTE")
        break    
    elif gato_tablero["A1"] == ficha_jugador and gato_tablero["B2"] == ficha_jugador and gato_tablero["C3"] == ficha_jugador:
        print("Felicitaciones!: GANASTE")
        break    
    elif gato_tablero["A3"] == ficha_jugador and gato_tablero["B2"] == ficha_jugador and gato_tablero["C1"] == ficha_jugador:
        print("Felicitaciones!: GANASTE")
        break
    if contador_empate == 9:
        print("La partida resultó en empate. Sigue intentandolo!")
        break
    os.system("cls")
    mostrar_tablero()
    while True:
        print("La cpu esta pensando su jugada ... ")
        jugada_cpu_1 = random.choice(alternativas)
        time.sleep(random.randint(1,10))
        if gato_tablero.get(jugada_cpu_1) == "":
            gato_tablero[jugada_cpu_1] = ficha_cpu
            contador_empate += 1
            break
        else:
            print("Posición ocupada")
            continue
    #COMPROBAR SI ES GANADOR
    if gato_tablero["A1"] == ficha_cpu and gato_tablero["A2"] == ficha_cpu and gato_tablero["A3"] == ficha_cpu:
        print("Lo sentimos!: LA CPU HA GANADO")
        break        
    elif gato_tablero["B1"] == ficha_cpu and gato_tablero["B2"] == ficha_cpu and gato_tablero["B3"] == ficha_cpu:
        print("Lo sentimos!: LA CPU HA GANADO")
        break        
    elif gato_tablero["C1"] == ficha_cpu and gato_tablero["C2"] == ficha_cpu and gato_tablero["C3"] == ficha_cpu:
        print("Lo sentimos!: LA CPU HA GANADO")
        break        
    elif gato_tablero["A1"] == ficha_cpu and gato_tablero["B1"] == ficha_cpu and gato_tablero["C1"] == ficha_cpu:
        print("Lo sentimos!: LA CPU HA GANADO")
        break        
    elif gato_tablero["A2"] == ficha_cpu and gato_tablero["B2"] == ficha_cpu and gato_tablero["C2"] == ficha_cpu:
        print("Lo sentimos!: LA CPU HA GANADO")
        break        
    elif gato_tablero["A3"] == ficha_cpu and gato_tablero["B3"] == ficha_cpu and gato_tablero["C3"] == ficha_cpu:
        print("Lo sentimos!: LA CPU HA GANADO")
        break        
    elif gato_tablero["A1"] == ficha_cpu and gato_tablero["B2"] == ficha_cpu and gato_tablero["C3"] == ficha_cpu:
        print("Lo sentimos!: LA CPU HA GANADO")
        break        
    elif gato_tablero["A3"] == ficha_cpu and gato_tablero["B2"] == ficha_cpu and gato_tablero["C1"] == ficha_cpu:
        print("Lo sentimos!: LA CPU HA GANADO")
        break
    if contador_empate == 9:
        print("La partida resultó en empate")
        break
mostrar_tablero()
print("La partida se cerrará en 5")
time.sleep(1)
print("La partida se cerrará en 4")
time.sleep(1)
print("La partida se cerrará en 3")
time.sleep(1)
print("La partida se cerrará en 2")
time.sleep(1)
print("La partida se cerrará en 1")
time.sleep(1)