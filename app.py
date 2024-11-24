from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data for the user list
users_list = [
    {"id": 1, "first_name": "James", "last_name": "Gosling", "nationality": "Canadian", "occupation" : "Computer Scientist", "known_for" : "Java (Programming Language)"},
    {"id": 2, "first_name": "Anders", "last_name": "Hejlsberg", "nationality": "Danish", "occupation" : "Lead Systems Architect", "known_for" : "CSharp (Programming Language)"},
    {"id": 3, "first_name": "Yukihiro", "last_name": "Matsumoto", "nationality": "Japanese", "occupation": "Computer Scientist", "known_for": "Ruby (Programming Language)"},
    {"id": 4, "first_name": "Guido", "last_name": "Van Rossum", "nationality": "Netherlands", "occupation" : "Benevolent Dictator for Life", "known_for" : "Python (Programming Language)"},
    {"id": 5, "first_name": "Bjarne", "last_name": "Stroustrup", "nationality": "Danish", "occupation": "Computer Scientist", "known_for": "C++ (Programming Language)"},
]

# Route to retrieve all users
@app.route("/python/api/v1/users", methods=["GET"])
def get_users():
    return jsonify({"users": users_list})

# Route to retrieve a user by their ID
@app.route("/python/api/v1/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = next((user for user in users_list if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(user)

# Route to create a new user
@app.route("/python/api/v1/users", methods=["POST"])
def create_user():
    if not request.json or "first_name" not in request.json:
        return jsonify({"error": "Bad Request"}), 400
    new_user = {
        "id": len(users_list) + 1,
        "first_name": request.json["first_name"],
        "last_name": request.json["last_name"],
        "nationality": request.json["nationality"],
        "occupation": request.json["occupation"],
        "known_for": request.json["known_for"],
    }
    users_list.append(new_user)
    return jsonify(new_user), 201

# Route to update a user
@app.route("/python/api/v1/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((user for user in users_list if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "Not Found"}), 404
    if not request.json:
        return jsonify({"error": "Bad Request"}), 400
    user["first_name"] = request.json.get("first_name", user["first_name"])
    user["last_name"] = request.json.get("last_name", user["last_name"])
    user["nationality"] = request.json.get("nationality", user["nationality"])
    user["occupation"] = request.json.get("occupation", user["occupation"])
    user["known_for"] = request.json.get("known_for", user["known_for"])
    return jsonify(user)

# Route to delete a user
@app.route("/python/api/v1/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users_list
    users_list = [user for user in users_list if user["id"] != user_id]
    return jsonify({"result": True})

if __name__ == "__main__":
    app.run(debug=True)
