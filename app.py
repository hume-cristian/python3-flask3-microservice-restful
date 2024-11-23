from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados para la lista de usuarios
users_list = [
    {"id": 1, "first_name": "James", "last_name": "Gosling", "nationality": "Canadian", "occupation" : "Computer Scientist", "known_for" : "Java (Programming Language)"},
    {"id": 2, "first_name": "Anders", "last_name": "Hejlsberg", "nationality": "Danish", "occupation" : "Lead Systems Architect", "known_for" : "CSharp (Programming Language)"},
    {"id": 3, "first_name": "Yukihiro", "last_name": "Matsumoto", "nationality": "Japanese", "occupation": "Computer Scientist", "known_for": "Ruby (Programming Language)"},
    {"id": 4, "first_name": "Guido", "last_name": "Van Rossum", "nationality": "Netherlands", "occupation" : "Benevolent Dictator for Life", "known_for" : "Python (Programming Language)"},
    {"id": 5, "first_name": "Bjarne", "last_name": "Stroustrup", "nationality": "Danish", "occupation": "Computer Scientist", "known_for": "C++ (Programming Language)"},
]

# Ruta para obtener todas los usuarios
@app.route("/python/api/v1/users", methods=["GET"])
def get_users():
    return jsonify({"users": users_list})

# Ruta para obtener un usuario por su ID
@app.route("/python/api/v1/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = next((user for user in users_list if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(user)

# Ruta para crear un nuevo usuario
@app.route("/python/api/v1/users", methods=["POST"])
def create_user():
    if not request.json or "title" not in request.json:
        return jsonify({"error": "El título de la tarea es obligatorio"}), 400
    new_user = {
        "id": len(users_list) + 1,
        "title": request.json["title"],
        "done": request.json.get("done", False),
    }
    users_list.append(new_user)
    return jsonify(new_user), 201

# Ruta para actualizar un usuario
@app.route("/python/api/v1/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((user for user in users_list if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    if not request.json:
        return jsonify({"error": "Datos no válidos"}), 400
    user["title"] = request.json.get("title", user["title"])
    user["done"] = request.json.get("done", user["done"])
    return jsonify(user)

# Ruta para eliminar un usuario
@app.route("/python/api/v1/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users_list
    users_list = [user for user in users_list if user["id"] != user_id]
    return jsonify({"result": True})

if __name__ == "__main__":
    app.run(debug=True)
