import random

def asignar_saldos_aleatorios():
    clientes = {}
    for i in range(10):
        saldo = round(random.uniform(1000, 10000), 2)  # Genera un saldo aleatorio entre 1000 y 10000
        clientes[f"Cliente {i+1}"] = saldo
    return clientes
