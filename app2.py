from flask import Flask, request, jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

users = {
    '1': {'name': 'Al', 'age': 26},
    '2': {'name': 'Bobby', 'age': 32},
    '3': {'name': 'Arthur', 'age': 41},
}

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
    
class ReadUser(Resource):
    def get(self, user_id):
        if user_id in users:
            return jsonify({'id': user_id, 'name': users[user_id]['name'], 'age': users[user_id]['age']})
        else:
            return "ERR: NO SUCH USER"

class ReadAllUsers(Resource):
    def get(self):
        return jsonify(users)

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
        
class DeleteUser(Resource):
    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return "USER SUCCESSFULY DELETED"
        else:
            return "ERR: NO SUCH USER"
        
api.add_resource(CreateUser, "/user")
api.add_resource(ReadUser, "/user/<user_id>")
api.add_resource(ReadAllUsers, "/user/all")
api.add_resource(UpdateUser, "/user/<user_id>")
api.add_resource(DeleteUser, "/user/<user_id>")
        
if __name__ == '__main__':
    app.run(debug=True)