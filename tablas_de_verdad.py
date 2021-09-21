//primero
# (x or y) or r

//segundo
# (x or y) and r

//tercero
# (x and y) or r

//cuarto
# (x and y) and r
"""
#// FUNCIONES
# (x or y) or z
def primero(x, y, z):
    return ((x or y) or z)

# (x or y) and z
def segundo(x, y, z):
    return ((x or y) and z)

# (x and y) or z
def tercero(x, y, z):
    return ((x and y) or z)

# (x and y) and z
def cuarto(x, y, z):
    return ((x and y) and z)

def tabla_verdad(punto):
    valores_booleanos = [1, 0]
    i=0
    for valor_x in valores_booleanos:
        for valor_y in valores_booleanos:
            for valor_z in valores_booleanos:
                i+=1
                print(f"caso #{i}")
                print(f"x = {valor_x}, y= {valor_y}, r = {valor_z}")
                if (punto == 1):
                    print(f"({valor_x} or {valor_y}) or {valor_z}")
                    print(primero(valor_x, valor_y, valor_z))
                elif (punto == 2):
                    print(f"({valor_x} or {valor_y}) and {valor_z}")
                    print(segundo(valor_x, valor_y, valor_z))
                elif (punto == 3):
                    print(f"({valor_x} and {valor_y}) or {valor_z}")
                    print(tercero(valor_x, valor_y, valor_z))
                elif (punto == 4):
                    print(f"({valor_x} and {valor_y}) and {valor_z}")
                    print(cuarto(valor_x, valor_y, valor_z))

print("Punto 1".center(50, "-"))
print(tabla_verdad(1))

print("Punto 2".center(50, "-"))
print(tabla_verdad(2))

print("Punto 3".center(50, "-"))
print(tabla_verdad(3))

print("Punto 4".center(50, "-"))
print(tabla_verdad(4))



"""
---------------------Punto 1----------------------
caso #1
x = 1, y= 1, r = 1
(1 or 1) or 1
1
caso #2
x = 1, y= 1, r = 0
(1 or 1) or 0
1
caso #3
x = 1, y= 0, r = 1
(1 or 0) or 1
1
caso #4
x = 1, y= 0, r = 0
(1 or 0) or 0
1
caso #5
x = 0, y= 1, r = 1
(0 or 1) or 1
1
caso #6
x = 0, y= 1, r = 0
(0 or 1) or 0
1
caso #7
x = 0, y= 0, r = 1
(0 or 0) or 1
1
caso #8
x = 0, y= 0, r = 0
(0 or 0) or 0
0
"""
"""
---------------------Punto 2----------------------
caso #1
x = 1, y= 1, r = 1
(1 or 1) and 1
1
caso #2
x = 1, y= 1, r = 0
(1 or 1) and 0
0
caso #3
x = 1, y= 0, r = 1
(1 or 0) and 1
1
caso #4
x = 1, y= 0, r = 0
(1 or 0) and 0
0
caso #5
x = 0, y= 1, r = 1
(0 or 1) and 1
1
caso #6
x = 0, y= 1, r = 0
(0 or 1) and 0
0
caso #7
x = 0, y= 0, r = 1
(0 or 0) and 1
0
caso #8
x = 0, y= 0, r = 0
(0 or 0) and 0
0
"""
"""
---------------------Punto 3----------------------
caso #1
x = 1, y= 1, r = 1
(1 and 1) or 1
1
caso #2
x = 1, y= 1, r = 0
(1 and 1) or 0
1
caso #3
x = 1, y= 0, r = 1
(1 and 0) or 1
1
caso #4
x = 1, y= 0, r = 0
(1 and 0) or 0
0
caso #5
x = 0, y= 1, r = 1
(0 and 1) or 1
1
caso #6
x = 0, y= 1, r = 0
(0 and 1) or 0
0
caso #7
x = 0, y= 0, r = 1
(0 and 0) or 1
1
caso #8
x = 0, y= 0, r = 0
(0 and 0) or 0
0
"""
"""
---------------------Punto 4----------------------
caso #1
x = 1, y= 1, r = 1
(1 and 1) and 1
1
caso #2
x = 1, y= 1, r = 0
(1 and 1) and 0
0
caso #3
x = 1, y= 0, r = 1
(1 and 0) and 1
0
caso #4
x = 1, y= 0, r = 0
(1 and 0) and 0
0
caso #5
x = 0, y= 1, r = 1
(0 and 1) and 1
0
caso #6
x = 0, y= 1, r = 0
(0 and 1) and 0
0
caso #7
x = 0, y= 0, r = 1
(0 and 0) and 1
0
caso #8
x = 0, y= 0, r = 0
(0 and 0) and 0
0
"""
