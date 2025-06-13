from flask import Flask, request, jsonify
from db import init_db, insert_user, get_user_by_id

app = Flask(__name__)
init_db()

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    user_id = insert_user(first_name, last_name)
    return jsonify({'id': user_id, 'first_name': first_name, 'last_name': last_name}), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify({'id': user[0], 'first_name': user[1], 'last_name': user[2]}), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
