#1
users = [ "Dabid", "Maia", "Jose", "Juan", "Maria"]
print(users)

post = ("Titulo", "Subtitulo", "Contenido")
print(post)

product_cost = 88.4
comision = 0.08
qty = 450
print (product_cost)
print (comision)
print (qty)

from decimal import Decimal
print(Decimal(product_cost))

players = {
  "Portero" : "Dabid",
  "Defensa" : "Maia",
  "Medio" : "Jose",
  "Delantero" : "Juan",
  "Suplente" : "Maria"
}
print(players)

#2
import math
product_cost = 36.25
print(math.ceil(product_cost))

#3
import math
print(math.sqrt(product_cost))

#4
print(list(players.values())[0])

#5
print(post[1])

#6
users.extend(["Alex"])
print(users)

#7
users[0] = "Ander"
print(users)

#8
users.sort()
print(users)

#9
post += ("Comentario",)
print(post)
