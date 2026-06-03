notas = []
suma = 0
for contador in range(5):
    while True:
        try:
            nota = float(input(f"Ingrese nota {contador + 1}:"))

        except ValueError:
            print("La nota debe ser un numero")
        else:
            if nota >=1 and nota <=7:
                suma += nota
                nota.append(nota)
                print("Nota registrada con exito")
                break
            else:
                print("La nota debe estar entre 1 y 7")
promedio = suma/len(notas)
print(f"Promedio : {promedio}")
print ("Hola")