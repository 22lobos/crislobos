import os

def calcular_estadisticas(clientes):
    # Realizar cálculos de estadísticas (ejemplo)
    total_clientes = len(clientes)
    suma_saldos = sum(clientes.values())
    saldo_promedio = suma_saldos / total_clientes
    
    # Definir la ruta absoluta al archivo de estadísticas
    ruta_archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../informes/estadisticas.txt'))
    
    # Escribir las estadísticas en el archivo
    with open(ruta_archivo, 'w') as file:
        file.write("Estadísticas calculadas:\n")
        file.write(f"Número total de clientes: {total_clientes}\n")
        file.write(f"Suma de todos los saldos: {suma_saldos}\n")
        file.write(f"Saldo promedio de los clientes: {saldo_promedio}\n")

    print(f"Estadísticas calculadas y guardadas en '{ruta_archivo}'")
