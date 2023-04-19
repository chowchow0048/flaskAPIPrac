from flask import Flask, request, jsonify
app = Flask(__name__)

users = {
    '1': {'name': 'Al', 'age': 26},
    '2': {'name': 'Bobby', 'age': 32},
    '3': {'name': 'Arthur', 'age': 41},
}

@app.route('/users', methods=['POST'])
def create_user():
    user_id = str(int(max(users.keys())) + 1)
    name = request.json['name']
    age = request.json['age']

    user = {'name': name, 'age': age}

    users[user_id] = user

    return jsonify({'id': user_id, 'name': name, 'age': age})

@app.route('/users/<user_id>', methods=['GET'])
def read_user(user_id):
    if user_id in users:
        return jsonify({'id': user_id, 'name': users[user_id]['name'], 'age': users[user_id]['age']})
    else:
        return jsonify({'error': 'User not found'}), 404
    
@app.route('/users/all', methods=['GET'])
def read_all_users():
    return jsonify(users)

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        name = request.json['name']
        age = request.json['age']

        users[user_id]['name'] = name
        users[user_id]['age'] = age

        return jsonify({'id': user_id, 'name': name, 'age': age})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)