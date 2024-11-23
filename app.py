from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados para la lista de tareas
users_list = [
    {"id": 1, "title": "Comprar comida", "done": False},
    {"id": 2, "title": "Leer un libro", "done": True},
]

# Ruta para obtener todas las tareas
@app.route("/python/api/v1/users", methods=["GET"])
def get_users():
    return jsonify({"users": users_list})

# Ruta para obtener una tarea por su ID
@app.route("/python/api/v1/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = next((user for user in users_list if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(user)

# Ruta para crear una nueva tarea
@app.route("/python/api/v1/users", methods=["POST"])
def create_task():
    if not request.json or "title" not in request.json:
        return jsonify({"error": "El título de la tarea es obligatorio"}), 400
    new_user = {
        "id": len(users_list) + 1,
        "title": request.json["title"],
        "done": request.json.get("done", False),
    }
    users_list.append(new_user)
    return jsonify(new_user), 201

# Ruta para actualizar una tarea
@app.route("/python/api/v1/users/<int:user_id>", methods=["PUT"])
def update_task(user_id):
    user = next((user for user in users_list if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    if not request.json:
        return jsonify({"error": "Datos no válidos"}), 400
    user["title"] = request.json.get("title", user["title"])
    user["done"] = request.json.get("done", user["done"])
    return jsonify(user)

# Ruta para eliminar una tarea
@app.route("/python/api/v1/users/<int:user_id>", methods=["DELETE"])
def delete_task(user_id):
    global users_list
    users_list = [user for user in users_list if user["id"] != user_id]
    return jsonify({"result": True})

if __name__ == "__main__":
    app.run(debug=True)
