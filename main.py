from scripts.asignacion import asignar_saldos_aleatorios
from scripts.clasificacion import clasificar_saldos
from scripts.estadisticas import calcular_estadisticas
from scripts.reportes import generar_reporte

def main():
    print("Bienvenido al Sistema de Gestión Financiera del Banco Internacional")
    while True:
        print("\nSeleccione una opción:")
        print("1. Asignar Saldos Aleatorios para 10 Clientes")
        print("2. Clasificar Saldos en Tres Rangos")
        print("3. Ver Estadísticas Avanzadas sobre los Saldos")
        print("4. Generar Reporte Detallado y Exportar a CSV")
        print("5. Salir del Programa")
        
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        
        if opcion == '1':
            clientes = asignar_saldos_aleatorios()
            print("\nSaldos asignados aleatoriamente:")
            for cliente, saldo in clientes.items():
                print(f"{cliente}: {saldo}")
        
        elif opcion == '2':
            if 'clientes' not in locals():
                print("Primero debe asignar saldos aleatorios.")
            else:
                clasificacion = clasificar_saldos(clientes)
                print("\nClasificación de Saldos:")
                for categoria, lista_clientes in clasificacion.items():
                    print(f"{categoria}:")
                    for cliente, saldo in lista_clientes:
                        print(f"  {cliente}: {saldo}")
        
        elif opcion == '3':
            if 'clientes' not in locals():
                print("Primero debe asignar saldos aleatorios.")
            else:
                calcular_estadisticas(clientes)
        
        elif opcion == '4':
            if 'clientes' not in locals():
                print("Primero debe asignar saldos aleatorios.")
            else:
                generar_reporte(clientes)
        
        elif opcion == '5':
            print("¡Hasta luego! Gracias por utilizar el Sistema de Gestión Financiera.")
            break
        
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()
