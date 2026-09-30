estudiantes = ["Anette", "Heidi", "Juan", "Irma"]
maestros = ["Zurita", "Valencia", "Torres"]
materias = ["programacion", "Matematicas", "redes"]

estudian = [
    ("Anette", "programacion"),
    ("Heidi", "Matematicas"),
    ("Juan", "redes")
]

imparten = [
    ("Zurita", "programacion"),
    ("Valencia", "redes"),
    ("Torres", "Matematicas")
]

inscritos = [
    ("Anette", "programacion"),
    ("Heidi", "Matematicas"),
    ("Juan", "redes")
]


def estudiante(x):
    return x in estudiantes


def maestro(x):
    return x in maestros


def estudia(x, y):
    return (x, y) in estudian


def imparte(x, y):
    return (x, y) in imparten


def inscrito(x, y):
    return (x, y) in inscritos


print("CONSULTAS")

print("estudiante('Anette'):", estudiante("Anette"))
print("estudiante('Juan'):", estudiante("Juan"))

print("maestro('Zurita'):", maestro("Zurita"))
print("maestro('Valencia'):", maestro("Valencia"))

print("estudia('Anette', 'programacion'):", estudia("Anette", "programacion"))
print("estudia('Heidi', 'Matematicas'):", estudia("Heidi", "Matematicas"))

print("inscrito('Anette', 'programacion'):", inscrito("Anette", "programacion"))
print("inscrito('Heidi', 'Matematicas'):", inscrito("Heidi", "Matematicas"))