#Este programa determina el promedio
#Leer las calificaciones
c1=int(input("c1="))
c2=int(input("c2="))
c3=int(input("c3="))
c4=int(input("c4="))
promedio=(c1+c2+c3+c4)/4
if (promedio>=6):
    print("El alumno esta aprobado, p="+str(promedio))
else:
    print("El alumno esta reprobado, p="+str(promedio))