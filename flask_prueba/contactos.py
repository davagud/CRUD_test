import pyodbc
from flask import Flask, render_template, request, url_for, redirect, flash

cx = pyodbc.connect(
'Driver={SQL Server};'+
'Server=SURFACE\SQLEXPRESS;'+
'Database=FLASK_test;'+
'UID=sa;'+
'PWD=ratona;'
)


app = Flask(__name__)

app.secret_key='los ardillos felices'

@app.route('/')
def Index():
    cur = cx.cursor()
    cur.execute('select * from table_contactos order by id')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', contacts=data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname,phone,email)
        cur = cx.cursor()
        cur.execute('insert into table_contactos (nombre,phone,email) values (?,?,?)',fullname,phone,email )
        cur.commit()
        flash('contacto agregado con éxito')
        return redirect(url_for('Index'))


@app.route('/edit/<string:id>')
def get_contact(id):
    cur=cx.cursor()
    cur.execute('select * from table_contactos where id=?', id)
    data = cur.fetchall()
    print(data)
    #return 'recibido'
    return render_template('edit-contact.html', contact = data[0])


@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur=cx.cursor()
        print(fullname,phone,email,id)
        cur.execute('update table_contactos set nombre=?, phone=?,email=? where id=?',fullname,phone,email,id)
        
        cur.commit()
        flash('actualizado parcero')
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete(id):
    cur=cx.cursor()
    cur.execute('delete table_contactos where id = ?',id)
    cur.commit()
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)

