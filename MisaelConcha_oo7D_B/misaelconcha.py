import os 
os.system("cls")

def cls():
    os.system("cls")

def menu():
    print('''
          

          *** MENU PRINCIPAL *** 
            1. Stock marca. 
            2. Búsqueda por precio. 
            3. Eliminar producto. 
            4. Salir
          
          ''')
    op=num_valido("Ingrese un vbalor entre 1 y 4: ",1,4) 
    return op
    
def num_valido(pregunta,li,ls):
    while True:
        try:
            n=int(input(pregunta))
            if n>=li and n<=ls:
                return n
            else:
                print("Debe seleccionar una opción válida!! ")
        except:
            print("Error, debe ingresar solo numeros")

def stock_marca(marca):
    print("Consultar marca")
    print("----------\n")
    marca=input("Ingrese marca a consultar: ")
    sw=0
    for datos in range (len(productos)):
        if productos["hp"]==marca:
            print(f"{productos[datos]["hp"]}")
            sw=1
            break



#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],]
#stock = {modelo: [precio, stock], ...]



def busqueda_precio(pregunta,p_min,p_max):
    lista_resultados=[]
    for datos  in productos.items():
        modelo,precio,stock=datos





def eliminar_producto():
    print("Eliminar un producto")
    print("----------\n")
    modelo=input("Ingrese modelo a actualizar: ")
    sw=0
    for i in range (len(stock)):
        if stock[i]["8475HD"]=="8475HD":
            print(f"{stock[i]["8475HD"]}")
        








productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'], 
 '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
 'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
 'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'], 
 '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
 '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
 }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1], 
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7], 
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
 } 

while True:
    cls()
    opcion=menu()
    cls()
    match opcion:
        case 1:
            stock_marca("marca")
        case 2:
            busqueda_precio("Los notebooks entre los precios consultas son: ",0,99999999999) 
        case 3:
            eliminar_producto()
        case 4:
            break
        case _:
            print("Error, debe ingresar solo numeros")
    os.system("pause")
print("Programa finalizado")