nombre = input("Inserta tu nombre ")
ApellidoParterno = input("Inserta tu Apellido paterno ") 
ApellidoMaterno = input("Inserta tu Apellido materno ")
FechaNacimiento = input("Inserta tu fecha de nacimiento (aaaa/mm/dd) ")
sexo = input("Inserta tu sexo (H/M) ")
entidadFederativa = input("Inserta tu entidad federativa (2 letras) ")


curp = ApellidoParterno[0:2] + ApellidoMaterno[0:1] + nombre[0:1]
curp = curp + FechaNacimiento[2:4] + FechaNacimiento[5:7] + FechaNacimiento[8:10]
curp = curp + sexo + entidadFederativa
print(curp.upper())