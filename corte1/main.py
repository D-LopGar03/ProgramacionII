import Asignatura, Estudiante, ProgramaAcademico

estudiante1 = Estudiante.Estudiante("Juan", "M", 20, 3)
asignatura1 = Asignatura.Asignatura("Matematicas", 3, 100)



estudiante1.inscribir_asignatura(asignatura1)
print(estudiante1.asignaturas)