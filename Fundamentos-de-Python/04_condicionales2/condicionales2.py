print("Escribe tu nombre:")
nombre = input()
print("Escribe tu edad")
edad = int(input())

if nombre == "Julio" and edad > 20:
      print("Saludos Julio, Eres un adulto")
elif nombre == "Julio" and edad <= 20:
    print("Saludos Julio, Eres un joven")
else:
     print("saludos")
