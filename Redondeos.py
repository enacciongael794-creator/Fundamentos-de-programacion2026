import math
pi = 3.1416
redondeoAbajo = round(pi, 2)
redondeoArriba = round(pi, 1)
pifloor = math.floor(pi)
piceil = math.ceil(pi)
pi4decimales = round(pi, 4)
print("Redondeo hacia abajo: ", redondeoAbajo)
print("Redondeo hacia arriba: ", redondeoArriba)
print("Redondeo hacia abajo con floor: ", pifloor)
print("Redondeo hacia arriba con ceil: ", piceil)
print("Pi con 4 decimales: ", pi4decimales)