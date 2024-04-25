#clases
class Profesor:
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email

    def dame_tu_nombre(self):
        return self.__nombre__
    
class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None
    def falta(self):
        self.__inasistencias__ += 1
    def libre(self):
        if self.__inasistencias__ >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"
    def elegir_dieta(self, la_dieta):
        self.__dieta__ = la_dieta
    def vegano(self):
        self.__dieta__ = "vegano"
    def mentoria(self, profesor):
        self.__mentor__ = profesor
        
class Materia:
    def __init__(self, el_nombre_de_la_materia):
        #asi se definen los atributos (__atributo__)
        self.__nombre__ = el_nombre_de_la_materia



#objetos

profe_elio = Profesor("Elio", "elio@gmail")
profe_gabi = Profesor("Gabriel", "gabi@gmail")

profe_elio.dame_tu_nombre()
profe_gabi.dame_tu_nombre()

alumno_juan = Alumno("Juan")
alumno_maria = Alumno("Maria")
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.vegano()
print(alumno_juan.__dieta__)
alumno_juan.mentoria(profe_elio)
print(alumno_juan.__mentor__)
print(alumno_juan.__mentor__.__nombre__)
print(alumno_maria.__mentor__)
alumno_maria.falta()
alumno_maria.falta()
alumno_maria.falta()
alumno_maria.falta()
alumno_maria.falta()
alumno_maria.elegir_dieta("vegetariana")
print(alumno_maria.__dieta__)

materia_1 = Materia("Computacion")
materia_2 = Materia("Matematica")


#print(alumno_juan.libre())
#print(alumno_maria.libre())
#print(profe_elio.dame_tu_nombre())
#print(profe_gabi.dame_tu_nombre())
#print(alumno_juan.__inasistencias__)
