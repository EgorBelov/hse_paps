from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------------------
# Пример хранилища в памяти
# ---------------------------
USERS = [
    {"id": 1, "username": "1", "email": "1@example.com"},
    {"id": 2, "username": "2", "email": "2@example.com"}
]
VIDEOS = [
    {"id": 101, "title": "123", "description": "123", "status": "ready"}
]
ANALYSIS = {
    101: {
        "videoId": 101,
        "objects": [{"name": "person", "timestamp": "00:00:02"}],
        "analysisStatus": "completed"
    }
}

# ---------------------------
# USERS
# ---------------------------
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify(USERS), 200

@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = next((u for u in USERS if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": {"code": 404, "message": "User not found"}}), 404

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "username" not in data or "email" not in data:
        return jsonify({"error": {"code": 400, "message": "Invalid user data"}}), 400
    new_id = max(u["id"] for u in USERS) + 1 if USERS else 1
    new_user = {
        "id": new_id,
        "username": data["username"],
        "email": data["email"]
    }
    USERS.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in USERS if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": {"code": 404, "message": "User not found"}}), 404
    data = request.get_json()
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200

@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global USERS
    user = next((u for u in USERS if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": {"code": 404, "message": "User not found"}}), 404
    USERS = [u for u in USERS if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

# ---------------------------
# VIDEOS
# ---------------------------
@app.route('/api/v1/videos', methods=['GET'])
def get_videos():
    return jsonify(VIDEOS), 200

@app.route('/api/v1/videos', methods=['POST'])
def create_video():
    data = request.get_json()
    if not data or "title" not in data or "description" not in data:
        return jsonify({"error": {"code": 400, "message": "Invalid video data"}}), 400
    new_id = max(v["id"] for v in VIDEOS) + 1 if VIDEOS else 1
    new_video = {
        "id": new_id,
        "title": data["title"],
        "description": data["description"],
        "status": "analyzing"
    }
    VIDEOS.append(new_video)
    return jsonify(new_video), 201

@app.route('/api/v1/videos/<int:video_id>/analysis', methods=['GET'])
def get_video_analysis(video_id):
    result = ANALYSIS.get(video_id)
    if not result:
        return jsonify({"error": {"code": 404, "message": "Analysis not found"}}), 404
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
