import sqlite3
con=sqlite3.connect("database.db")
cur=con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users
            ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,
             mail TEXT, phone TEXT, city TEXT, address TEXT)
                """)
con.commit()
users={"Alice":["3091238","alice@mail.com","Bucaramanga","Calle 10"],"Wanda":["23409234","wanda@mail.com","Pidecuesta","Carrera 0W-15"],"Lola":["309448023","lola@mail.com","Giron","Calle 11 #4"],"Pepito":["31023912","pepito@mail.com","Lebrija","Vereda 4"],"Juan":["1203213","juan@mail.com","Bucaramanga","Calle 11 # 5-5"],"Pepe":["312302","pepe@mail.com","Mesa Santos","Avenida 6 Casa 4"]}

def crear_usuario(name,phone,mail,city,address):
    cur.execute("INSERT INTO users (name,mail,phone,city,address) VALUES (?, ?,?,?,?)",(name,phone,mail,city,address))
    con.commit()
def mostrar_usuarios():
    cur.execute("SELECT * FROM users")
    return cur.fetchall()
def update(id,phone,mail,city,address):
    cur.execute("UPDATE users SET phone = ?, mail = ?, city = ?, address = ?, WHERE id = ?", (phone,mail,city,address,id))
    con.commit()
def update_phone(id,phone):
    cur.execute("UPDATE users SET phone = ? WHERE id = ?", (phone,id))
    con.commit()
def update_mail(id,mail):
    cur.execute("UPDATE users SET mail = ? WHERE id = ?", (mail, id))
    con.commit()
def delete_user(id):
    cur.execute("DELETE FROM users WHERE id = ?", (id,))
    con.commit()
for i,cant in users.items():
    crear_usuario(i,cant[0],cant[1],cant[2],cant[3])
while True:
    seleccion=int(input("1/Crear Usuario, 2/Mostrar usuario, 3/Actualizar excepto nombre, 4/Actualizar telefono, 5/Actualizar mail, 6/Eliminar usuario, 0/Salir\n"))
    if seleccion == 0:
        break
        con.close()
    elif seleccion== 1:
        nombre=input("Ingrese nombre:")
        tel=input("Ingrese telefono:")
        email=input("Ingrese correo electronico:")
        ciudad=input("Ingrese Ciudad:")
        direccion=input("Ingrese direccion:")
        crear_usuario(nombre,tel,email,ciudad,direccion)
    elif seleccion== 2:
        print(mostrar_usuarios())
    elif  seleccion==3:
        ide=int(input("ingrese su id:"))
        tel=input("Ingrese telefono:")
        email=input("Ingrese correo electronico:")
        ciudad=input("Ingrese Ciudad:")
        direccion=input("Ingrese direccion:")
        update(ide,tel,email,ciudad,direccion)
    elif seleccion==4:
        ide=int(input("Ingrese su id:"))
        tel=input("Ingrese telefono:")
        update_phone(ide,tel)
    elif seleccion==5:
        ide=int(input("ingrese su id:"))
        email=input("Ingrese correo electronico:")
        update_mail(ide,email)
    elif seleccion==6:
        ide=int(input("ingrese su id:"))
        delete_user(ide)
    else:
        print("Seleccione una opcion correcta")