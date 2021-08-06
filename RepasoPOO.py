#POO Repaso Polimentes 04/08/2021
#NOTA1: Las variables de una instancia son unicas y particulares de cada instancia,
#       en cambio las variables de la clase son compartidas por todas las instancias de esa clase 
#NOTA2: Existen distintos tipos de metodos en una clase: regulares, de la clase y estáticos
#       METODOS REGULARES: Toman automaticamente la instancia (palabra 'self') como primer argumento (véase línea 21)
#       METODOS DE LA CLASE: Toman como primer argumento a la clase en si (palabra 'cls') con ayuda de la palabra
#                            reservada "@classmethod" antes de su definicion (véase línea 27).
#                            También es posible utilizar métodos de la clase como constructores y así particularizar como 
#                            se crean las instancias/objetos(véase línea 34)
#       METODOS ESTÁTICOS: NO pasan nada como argumento, ni la instancias ('self') ni la clase (´cls') por lo que funcionan
#                          como funciones "regulares" pero que decidimos incluir en nuestra clase porque mantienen una relación
#                          lógica con la clase. Solo reciben como argumentos los parametros que estarán específicamente utilizando 
#                          y ya con la palabra reservada @staticmethod antes de su definicion(Véase línea 42)
#NOTA3: Al hablar de herencia entre clases en python nos referimos a la habilidad de heredar atributos y métodos de una 
#       clase "madre" creando subclases obteniendo así todas sus funcionalidades así como sobreescribir y/o agregar dentro 
#       código dentro de esa subclase sin afectar a la clase madre en ninguna forma
import datetime

class Empleado:#asi se declara una clase

    num_de_empleados = 0 #variable de la CLASE 
    sobresueldo = 1.04 #variable de la CLASE

    def __init__(self, nombre, apellido, sueldo): #constructor, la palabra self ayuda a hacer referencia a ESA instancia u objeto de la clase
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.email = nombre + '.' + apellido + '@polimentes.com'

        Empleado.num_de_empleados += 1 # NO tiene sentido cambiar para ninguna intancia el valor, solo cada vez que creo un nuevo empleado ese valor se incrmenta en uno y es por eso que uso el nombre de la clase 'Empleado' y lo pongo en el constructor para que se ejecute cada vez que instancio

    def nombre_completo(self):#METODO REGULAR que permite crear en automatico el nombre completo, una instancia puede hacer referencia a este metodo en especifico y genera su nombre, por eso hace uso de la palabra que hace referencia a la instancia: 'self'
        return '{} {}'.format(self.nombre, self.apellido)

    def aplicar_sobresueldo(self):
        self.sueldo = int(self.sueldo * self.sobresueldo)#Al hacer uso de una variable DE LA CLASE podemos usar la palabra 'self' o el nombre de la clase 'Empleado' antes de hacer uso de ella, sin embargo al elegir self es posible cambiar ese valor en un futuro para alguna instacia en particular SIN modificar el valor definido de la variable de la clase, tambien el uso de 'self' permitira a una subclase sobreescribir el valor de esta variable si asi lo desea

    @classmethod #Método que permite modificar la variable de la clase "sobresueldo"
    def set_sobresueldo(cls, cantidad):
        cls.sobresueldo = cantidad

    @classmethod #Método que funciona como constructor para así permitir crear nuevos empleados recibiendo su información con un formato diferente
    def from_string(cls, emp_str):
        nombre, apellido, sueldo = emp_str.split('-')
        return cls(nombre, apellido, sueldo) #aqui ya estamos creando al nuevo empleado que llego con un formato diferente

    @staticmethod
    def dia_de_trabajo(dia): #Método/Función que unicamente me dice si el día que le indico fue día hábil o de descanso haciendo uso de los metodos de python en donde los dias de la semana se representan por numero (Lunes=0...Domingo=6)
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True

#Código para crear una subclase, como parámetro se indica la clase madre. 
#Si no le agregamos ningún código en particular y solo le indicamos la palabra reservada 'pass' es tal cual una "copia" de la clase madre
class DesarrolladorJr(Empleado):
    pass



emp1 = Empleado('Christian', 'Gil', 200)#al instanciar o crear el objeto de la clase se pasa en automático la referencia a ESA instancia, por lo que ya NO es necesaria la palabra 'self' y solo debemos pasarle los demas atributos
emp2 = Empleado('America', 'Monsalvo', 300)#Al crear una instancia el metodo init o constructor es ejecutado automáticamente
emp3 = Empleado('Test', 'User', 100)

#***PRUEBAS BASICAS DE IMPRESION DE INSTANCIAS Y LOS ATRIBUTOS***
print(emp1)#De esta manera me trae el objeto tal cual, es decir la direccion de memoria donde se guardo ya estando fuera de la clase
print(emp2.email)#Aqui especifico que deseo obtener unicamente el email de la instancia
print('{} {}'.format(emp3.nombre, emp3.apellido))#Y si deseara traer ciertos datod del objeto ero con formato tambien lo indico, sin embargo para hacer esto mejor declaro esto como un metodo de la misma clase

#***PRUEBA DE USO DE METODOS REGULARES***
print (emp1.nombre_completo())#De esta manera logro lo que en la linea anterior pero haciendo uso del metodo de la clase

#***PRUEBAS DE USO DE VARIABLES DE LA CLASE (VARIABLES QUE PUEDEN CAMBIAR SI ASI LODESEO DEPENDIENDO LA INSTANCIA)***
print("SIN VALOR PARTICULAR: ", emp1.__dict__) #Antes de que la varible tenga un valor particular
emp1.sobresueldo = 1.05 #modifico el valor de la variable de la clase pero UNICAMENTE para esta instancia
print("CON VALOR PARTICULAR: ",emp1.__dict__) #Ya habiendo aplicado un valor en especial a esta instancia a la variable de la clase
print("Sobresueldo automatico: ",Empleado.sobresueldo) #El valor actual de la variable de la clase tal cual 
print("Sobresueldo para emp1: ", emp1.sobresueldo)
print("Sobresueldo para emp2: ", emp2.sobresueldo)

#***PRUEBAS DE USO DE VARIABLES DE LA CLASE (VARIABLES QUE NO TIENE CASO, SERÁ LA MISMA PARA TODAS LAS INSTANCIAS)***
print("Numero de empleados: ", Empleado.num_de_empleados)

#***PRUEBAS DE USO DE MÉTODOS DE LA CLASE @classmethod***
Empleado.set_sobresueldo(1.06)
print("Sobresueldo actual de la empresa: ", Empleado.sobresueldo)
print(emp1.sobresueldo)#Vemos que debido a que en la linea 47 le definimos un valor particular asi se sigue manteniendo 
print(emp2.sobresueldo)
print(emp3.sobresueldo)

#***PRUEBAS DE USO DE MÉTODOS DE LA CLASE @classmethod COMO CONSTRUCTORES***
emp4 = 'Damian-Vazquez-1000'
nuevo_emp4 = Empleado.from_string(emp4)
print(nuevo_emp4.email)#Probamos que efectivamemnte los datos a pesar de ser recibidos diferente ya están dados de alta correctamente 

#***PRUEBA DE USO DE METODOS ESTÁTICOS***
fecha = datetime.date(2021, 12, 4)
print("¿Toca trabajar?  ", Empleado.dia_de_trabajo(fecha))
