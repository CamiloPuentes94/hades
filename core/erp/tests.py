'''
Ejemplos de ORM
'''
from config.wsgi import *
from core.erp.models import Category

# listar

# query =Type.objects.all()
# print(query)

#insercion
"""tipo = Type()
tipo.name = 'Presidente'
tipo.save()"""

#edicion

# tipo = Type.objects.get(id=1)
# print(tipo)

#sub consultas con tablas relacionadas
# obj = Employee.objects.filter(typeid=1)

data = ['Leche y derivados', 'carnes, pescados y huevos', 'Patatas, legumbres, frutps secos', 'Verduras y Hortalizas',
        'Frutas', 'Cereales y derivados', 'azucar y dulces', 'Grasas, aceite y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))