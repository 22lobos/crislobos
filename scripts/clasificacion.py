def clasificar_saldos(clientes):
    clasificacion = {
        'Bajo': [],
        'Medio': [],
        'Alto': []
    }
    for cliente, saldo in clientes.items():
        if saldo <= 3000:
            clasificacion['Bajo'].append((cliente, saldo))
        elif saldo <= 7000:
            clasificacion['Medio'].append((cliente, saldo))
        else:
            clasificacion['Alto'].append((cliente, saldo))
    return clasificacion
