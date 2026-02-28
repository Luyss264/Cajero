def cajero():

    saldoInicial=1000
    
    print("BIENVENIDO AL CAJERO AUTOMATICO\n")

    try:
        vecesOP = int(input("¿Cuántas operaciones deseas realizar?: "))
    except ValueError:
        print("VALOR NO VALIDO")
        cajero()

    for i in range(vecesOP):

        print(f"OPERACION {i+1} DE {vecesOP}")
        print("SELECCIONA UNA OPCIÓN POR NÚMERO:")
        print("1-Consultar Saldo")
        print("2-Retirar dinero")
        print("3-Depositar dinero")
        print("4-Cuantas operaciones hechas")
        print("5-Salir")
        
        try:
            consultaUser = int(input())
        except ValueError:
            print("OPCIÓN NO VALIDA")
            continue
            
        if consultaUser == 1:
            print(f"el saldo es de: {saldoInicial}")
        
        elif consultaUser == 5:
            print("Adiós")
            break
        
        

        elif consultaUser == 2:

            while True:

                try:
                    retiro = int(input("ingresa cantidad a retirar: "))
                except ValueError:
                    print("VALOR NO VALIDO")
                    continue

                if retiro < 0:
                    print("No se puede retirar una cantidad negativa")
                    continue

                elif saldoInicial >= retiro:
                    saldoInicial = saldoInicial - retiro
                    print(f"el nuevo saldo es de: {saldoInicial}")
                    break
                
                elif saldoInicial < retiro:
                    print("Monto insuficiente")
                    break

                else:
                    print("VALOR INVALIDO")
                    break

        elif consultaUser == 3:

            while True:
                
                try:
                    deposito = int(input("ingresa cantidad a depositar: "))
                except ValueError:
                    print("VALOR NO VALIDO")
                    continue

                if deposito < 0:
                    print("No se puede depositar una cantidad negativa")
                    continue
                
                elif deposito > 0:
                    saldoInicial = saldoInicial + deposito
                    print(f"el nuevo saldo es de: {saldoInicial}")
                    break
                else:
                    print("VALOR INVALIDO")
                    break
        
        elif consultaUser == 4:
            
            print(f"haz realizado {i} operaciónes")
            
        else:
            print("OPCIÓN NO VALIDA")

    print("Gracias por usar el cajero")
        
cajero()