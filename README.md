# CAJERO AUTOMATICO
---
En este documento se explicará la logica del código realizado para un cajero automatico.

---
## Usabilidad

El programa simula un cajero automatico, por ende, tiene diversas características propias de uno.

### Utilidades

* Poder definir cantidad de operaciones
* Pedir opciones de operación
* Realizar cada operación sugerida
* Si un dato es incorrecto reiniciar la petición

---
## Sustentación

Basándonos en las utilidades, la explicación del código irá por partes, partiendo de la primera linea a la última.

---
### Definir función ejecutora

Una manera de iniciar automaticamente un programa es definiendo el código en una función y posteriormente ponerle un nombre, siguiendo esta lógica se procede a definir.

```py
def cajero():
```
---
### Registro e inicio de sesión

Para iniciar sesión se necesita una base de datos, en este ejemplo, al no contar con una se debe tener en cuenta el registro y usarlo como base una vez registrado un usuario

#### Registro

Para registrar, se usa un objeto donde se contendrá el registro.

```py
usuarios = {}
```
Una vez hecho esto se agrega el siguiente codigo para definir _**nombre**_ y _**contraseña**_, Luego de esto hay que definir que _**nombre**_ será un atributo de _**usuarios,**_ y _**contraseña**_ su valor.

```py
    print("Registro de usuario")

    nombre = input("Crea tu nombre de usuario: \n")
    contraseña = input("Crea tu contraseña: \n")

    usuarios[nombre]= contraseña

    print("El usuario ha sido registrado correctamente.")
```
Aquí _**nombre**_ ya está definido como atributo de _**usuarios**_.

#### Inicio de Sesión

Una vez registrado el usuario, se puede simular la base de datos y se procede a iniciar su sesión.

Se hace una comparación si el valor del atributo en _**usuarios**_ coincide con los "input" _**nombre_inicio**_ y _**contraseña_inicio**_.

```py
    print("Inicio de sesión")

    nombre_inicio = input("Introduce tu nombre: \n")
    contraseña_inicio = input("Introduce tu contraseña: \n")
    
    if nombre_inicio in usuarios:
        if usuarios[nombre_inicio] == contraseña_inicio:
            print("Acceso concedido.")
        else: 
            print("La contraseña o el usuario son incorrectos.")
    else: 
        print("El usuario no existe")
```
---
### Definir saldo inicial

Como no contamos con base de datos real y el monto sí o sí debe ser definido como en la realidad, se define una variable cuyo valor sería 1000

```py
saldoInicial = 1000
```
---
### Pedir cantidad de operaciónes

Para que el usuario pueda definir cuantas veces desea que se ejecute el programa se le pregunta cuantas veces se ejecuta y usamos ese valor ya en una variable, y metemos esa variable en _**range()**_ de un ciclo de iteración _**for**_

```py
    try:
        vecesOP = int(input("¿Cuántas operaciones deseas realizar?: "))
    except ValueError:
        print("VALOR NO VALIDO")
        cajero()

    for i in range(vecesOP):
```
---
### Selección de operación

Cuando el usuario define cuantas operaciones desea realizar, pasa a elegir que operación desea que se realice, en este caso tenemos 5 opciones.

* Consultar saldo
* Retirar dinero
* Depositar dinero
* Cuantas operaciones hechas
* Salir

Para que el usuario sea capaz de seleccionar una opción, creamos una variable "input" similar a la variable _**vecesOP**_, pero usaremos ese dato para condiciones.

```py
        try:
            consultaUser = int(input())
        except ValueError:
            print("OPCIÓN NO VALIDA")
            continue
```

Al estar en un ciclo _**for**_, si se escribe un dato incorrecto definimos _**continue**_ para que reintente.

#### Consultar saldo

Si el usuario define en _**consultaUser**_ el número _**"1"**_
se ejecutará el siguiente código:

```py
        if consultaUser == 1:
            print(f"el saldo es de: {saldoInicial}")
            break
```

#### Retirar dinero

Si es igual a _**"2"**_ se ejecutará el siguiente:

```py
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
```
Se encapsula en la condición un ciclo **While**, ya que si el usuario inserta un valor incorrecto un _**continue**_ lo devolverá al inicio del ciclo, en este caso la petición del **input**

#### Depositar dinero

Si la opción del usuario es == _**3**_ se ejecutará un código con similares condiciones al retiro en cuanto a la definición del valor

```py
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
```
#### Consultar cuantas operaciones hechas

Aveces el usuario puede no estar seguro de la cantidad de operaciones que definió. En el codigo se definió print de cada iteracion del _**for**_ en el que se encuentra, sin embargo hay una opcíon para mostrarlo.

```py
        elif consultaUser == 4:
            
            print(f"haz realizado {i} operaciónes")
```
en la opción _**4**_ usamos _**i**_ ya que en _**for i in range(vecesOP)**_, _**i**_ referencia como valor a cada iteracion creada por el _**range()**_, si esta en la tercera iteracion, el _**print()**_ mostrará _"haz realizado 3 operaciones"_

#### Salir

Para que el usuario pueda abortar. ya que puede decidir no proceder en la iteración o en general, entonces existe la opción que si define _**5**_ procede a detener el programa, no realiza mas ciclo y termina.

```py
        elif consultaUser == 5:

            print("Adiós")
            break    
``` 
### Final del codigo

una vez terminado el programa, muestra el siguiente mensaje.

```py
    print("Gracias por usar el cajero")
```

Y por ultimo, llamamos la función para que automaticamente al abrir el programa se ejecute.

```py
cajero()
```

