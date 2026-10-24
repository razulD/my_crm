from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
def get_db():
	return sqlite3.connect('crm.db')
@app.route('/')
def home():
	search_query = request.args.get('q', '')
	conn = get_db()
	cursor = conn.cursor()
	if search_query:
		cursor.execute("SELECT * FROM clients WHERE name LIKE ?", ('%' + search_query + '%',))
	else:
		cursor.execute("SELECT * FROM clients")
	clients = cursor.fetchall()
	conn.close()
	return render_template('index.html', clients=clients, search_query=search_query)
@app.route('/add', methods=['POST'])
def add_client():
	name = request.form['name']
	phone = request.form['phone']
	status = request.form['status']
	conn = sqlite3.connect('crm.db')
	cursor = conn.cursor()
	cursor.execute("INSERT INTO clients (name, phone, status) VALUES (?, ?, ?)",(name, phone, status))

	conn.commit()
	conn.close()
	return redirect('/')
@app.route('/delete/<int:client_id>')
def delete_client(client_id):
	conn = sqlite3.connect('crm.db')
	cursor = conn.cursor()
	cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
	conn.commit()
	conn.close()
	return redirect('/')
@app.route('/edit/<int:client_id>')
def edit_page(client_id):
	conn = sqlite3.connect('crm.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
	client = cursor.fetchone()
	conn.close()
	return render_template('edit.html', client=client)
@app.route('/update/<int:client_id>', methods=['POST'])
def update_client(client_id):
	name = request.form['name']
	phone = request.form['phone']
	status = request.form['status']
	conn = sqlite3.connect('crm.db')
	cursor = conn.cursor()
	cursor.execute("UPDATE clients SET name = ?, phone = ?, status = ? WHERE id = ?", (name, phone, status, client_id))
	conn.commit()
	conn.close()

	return redirect('/')

if __name__ == '__main__':

	app.run(debug=True, port=5555)
