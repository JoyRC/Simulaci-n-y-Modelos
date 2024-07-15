import random

def lanzamiento_de_dados():
    saldo_inicial = 0 
    while saldo_inicial < 100 or saldo_inicial > 250:
        saldo_inicial = int(input("Ingresa tu saldo inicial (entre 100 y 250): "))
        if saldo_inicial < 100 or saldo_inicial > 250:
            print("Saldo inicial inválido. Debe ingresar un monto entre 100 y 250.")
            continue
    
    saldo_actual = saldo_inicial
    apuesta_minima = 5
    apuesta_maxima = 250
    ganancia_acumulada = 0
    perdida_acumulada = 0

    while saldo_actual > 0:
        apuesta = int(input(f"Ingresa tu apuesta (entre {apuesta_minima} y {apuesta_maxima}): "))
        if apuesta < apuesta_minima or apuesta > apuesta_maxima:
            print("Apuesta inválida. Debes apostar entre 5 y 250.")
            continue

        if apuesta > saldo_actual:
            print("No posee los fondos para realizar esta apuesta, por favor escoga otro monto.")
            continue

        dado = random.randint(1, 6)
        if dado % 2 == 0:
            ganancia = apuesta * 2
            saldo_actual += ganancia - apuesta
            ganancia_acumulada += ganancia
            print(f"¡Número par! Ganaste {ganancia}. Saldo actual: {saldo_actual}")
        else:
            saldo_actual -= apuesta
            perdida_acumulada -= apuesta
            print(f"Número impar. Perdiste {apuesta}. Saldo actual: {saldo_actual}")

        if saldo_actual >= 500:
            print("¡Felicidades! Has alcanzado una ganancia acumulada de 500.")
            break
        elif saldo_actual <= -100:
            print("Has llegado a una pérdida acumulada de -100. El juego termina.")
            break

        #decision = input("¿Quieres seguir jugando? (s/n): ")
        #if decision.lower() != 's':
            #print(f"Decidiste retirarte. Tu saldo final es: {saldo_actual}")
            #break

lanzamiento_de_dados()