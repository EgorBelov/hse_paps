from flask import Flask, request, jsonify

app = Flask(__name__)

# Храним пользователей в памяти
USERS = [
  { "id": 1, "username": "1", "email": "1@example.com" },
  { "id": 2, "username": "2",   "email": "2@example.com" }
]


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "User service is running"}), 200

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify(USERS), 200

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "username" not in data or "email" not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    new_id = len(USERS) + 1
    user = {
        "id": new_id,
        "username": data["username"],
        "email": data["email"]
    }
    USERS.append(user)
    return jsonify(user), 201

@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = next((u for u in USERS if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    # Слушаем на 0.0.0.0, порт 8000
    app.run(host='0.0.0.0', port=8000)
