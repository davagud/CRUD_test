import pyodbc


strcx = 'Driver={SQL Server};Server=saisqlserver.database.windows.net;Database=test;UID=it;PWD=Cof97045;'
cx = pyodbc.connect(strcx)


def crear(cx):
    nombre = input('nombre: ')
    telefono = input('telefono: ')
    cursor = cx.cursor()
    cursor.execute('insert into table_test (nombre,telefono) values (?,?)',nombre, telefono)
    cursor.commit()


def update(cx):
    pass


def listar(cx):
    print('LISTAR:')
    cursor = cx.cursor()
    cursor.execute('select * from table_test')
    for fila in cursor:
        print(fila)


def delete(cx):
    pass

if __name__ =='__main__':
    crear(cx)
    listar(cx)

cx.close()