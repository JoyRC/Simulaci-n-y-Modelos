import random

def lanzamiento_de_dados_automatico():
    
    saldo_inicial = random.randint(10, 100)
    saldo_actual = saldo_inicial
    apuesta = 5
    ganancia_acumulada = 0
    perdida_acumulada = 0
    veces_jugadas = 0
    veces_ganadas = 0
    veces_perdidas = 0

    while saldo_actual > 0:
        dado = random.randint(1, 6)
        
        if dado % 2 == 0:
            ganancia = apuesta * 2
            saldo_actual += ganancia - apuesta
            ganancia_acumulada += ganancia
            veces_ganadas += 1
        
        else:
            saldo_actual -= apuesta
            perdida_acumulada -= apuesta
            veces_perdidas += 1
        
        veces_jugadas+= 1

        if ganancia_acumulada >= 500 or perdida_acumulada <= -100:
            break

    print(f"Saldo inicial: {saldo_inicial}")
    print(f"Saldo final: {saldo_actual}")
    print(f"Ganancia acumulada: {ganancia_acumulada}")
    print(f"Pérdida acumulada: {perdida_acumulada}")
    print(f"Partidas ganadas: {veces_ganadas}")
    print(f"Partidas perdidas: {veces_perdidas}")
    print(f"Porcentaje de victorias: {(veces_ganadas/veces_jugadas)*100}")
    print(f"Porcentaje de derrotas: {(veces_perdidas/veces_jugadas)*100}")
    print(f"Total de partidas jugadas: {veces_jugadas}")


lanzamiento_de_dados_automatico()
