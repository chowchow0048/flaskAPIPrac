from flask import Flask, request, jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

users = {
    '1': {'name': 'Al', 'age': 26},
    '2': {'name': 'Bobby', 'age': 32},
    '3': {'name': 'Arthur', 'age': 41},
}

# @app.route('/users', methods=['POST'])
# def create_user():
#     user_id = str(int(max(users.keys())) + 1)
#     name = request.json['name']
#     age = request.json['age']

#     user = {'name': name, 'age': age}

#     users[user_id] = user

#     return jsonify({'id': user_id, 'name': name, 'age': age})

@api.route('/user')
class CreateUser(Resource):
    def post(self):
        user_id = str(int(max(users.keys())) + 1)
        name = request.json['name']
        age = request.json['age']

        user = {
            'name': name,
            'age': age
        }

        users[user_id] = user

        return jsonify({'id': user_id, 'name': name, 'age': age})
    
@api.route('/user/<user_id>')
class ReadUser(Resource):
    def get(self, user_id):
        if user_id in users:
            return jsonify({'id': user_id, 'name': users[user_id]['name'], 'age': users[user_id]['age']})
        else:
            return "ERR: NO SUCH USER"

@api.route('/user/all')
class ReadAllUsers(Resource):
    def get(self):
        return jsonify(users)
    
@api.route('/user/<user_id>')
class UpdateUser(Resource):
    def put(self, user_id):
        if user_id in users:
            name = request.json['name']
            age = request.json['age']
            
            users[user_id]['name'] = name
            users[user_id]['age'] = age

            return jsonify({'id': user_id, 'name': users[user_id]['name'], 'age': users[user_id]['age']})
        else:
            return "ERR: NO SUCH USER"
        
@api.route('/user/<user_id>')        
class DeleteUser(Resource):
    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return "USER SUCCESSFULY DELETED"
        else:
            return "ERR: NO SUCH USER"
        
if __name__ == '__main__':
    app.run(debug=True)