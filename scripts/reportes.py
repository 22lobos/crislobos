import csv
import os

def generar_reporte(clientes):
    ruta_reporte = os.path.abspath(os.path.join(os.path.dirname(__file__), '../informes/reporte_saldos.csv'))

    try:
        with open(ruta_reporte, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Cliente', 'Saldo Original', 'Deducciones', 'Saldo Neto'])
            for cliente, saldo in clientes.items():
                deducciones = round(saldo * 0.1, 2)  # Ejemplo de deducción del 10%
                saldo_neto = saldo - deducciones
                writer.writerow([cliente, saldo, deducciones, saldo_neto])
        
        print(f"Reporte generado y exportado a '{ruta_reporte}'")
    except IOError as e:
        print(f"Error al escribir en el archivo CSV: {e}")

