from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Root@123',
    'database': 'demo_flask'
}

@app.route('/', methods=['GET'])
def get_books():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM book")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

@app.route('/create', methods=['POST'])
def create_books():
    new_book = request.get_json()
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book (publisher,name,date) VALUES (%s, %s, %s)", (new_book['publisher'], new_book['name'], new_book['date']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(new_book), 201

@app.route('/update/<int:id>', methods=['PUT'])
def update_book(id):
    updated_book = request.get_json()
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET publisher=%s, name=%s, date=%s WHERE id=%s", (updated_book['publisher'], updated_book['name'], updated_book['date'], id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(updated_book)

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'result': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)



































# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import mysql.connector
# from mysql.connector import Error

# app = Flask(__name__)
# CORS(app) 

# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'Root@123',
#     'database': 'demo_flask'
# }

# @app.route('/', methods=['GET'])
# def get_all_users():
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM book")
#         results = cursor.fetchall()
#         return jsonify(results)
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# @app.route('/create', methods=['POST'])
# def create_user():
#     new_user = request.get_json()
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         cursor.execute("INSERT INTO book (publisher, name, date) VALUES (%s, %s, %s)", (new_user['publisher'], new_user['name'], new_user['date']))
#         connection.commit()
#         return jsonify(new_user), 201
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# @app.route('/update/<int:id>', methods=['PUT'])
# def update_user(id):
#     new_book = request.get_json()
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         cursor.execute("UPDATE book SET publisher=%s, name=%s, date=%s WHERE id=%s", (new_book['publisher'], new_book['name'],new_book['date'], id))
#         connection.commit()
#         return jsonify(new_book)
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# @app.route('/delete/<int:id>', methods=['DELETE'])
# def delete_user(id):
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         cursor.execute("DELETE FROM book WHERE id=%s", (id,))
#         connection.commit()
#         return jsonify({'result': 'User deleted'})
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# if __name__ == '__main__':
#     app.run(debug=True)
