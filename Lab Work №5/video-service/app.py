from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

VIDEOS = [
  {
    "id": 1,
    "title": "123",
    "description": "123",
    "ownerId": 1,
    "status": "ready",
    "ownerCheck": "User not verified yet"
  },
  {
    "id": 2,
    "title": "312",
    "description": "312",
    "ownerId": 2,
    "status": "analyzing",
    "ownerCheck": "User not verified yet"
  }
]


# URL user-сервиса из переменных окружения (если не указано, берем localhost)
USER_SERVICE_URL = os.environ.get('USER_SERVICE_URL', 'http://localhost:8000')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Video service is running"}), 200

@app.route('/api/v1/videos', methods=['GET'])
def get_videos():
    return jsonify(VIDEOS), 200

@app.route('/api/v1/videos', methods=['POST'])
def create_video():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400
    
    new_id = len(VIDEOS) + 1
    video = {
        "id": new_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "ownerId": data.get("ownerId"),
        "status": "analyzing"
    }
    VIDEOS.append(video)

    # Проверка, существует ли указанный владелец в User Service
    if video["ownerId"]:
        check_url = f"{USER_SERVICE_URL}/api/v1/users/{video['ownerId']}"
        r = requests.get(check_url)
        if r.status_code == 200:
            video["ownerCheck"] = "User exists"
        else:
            video["ownerCheck"] = "User not found"

    return jsonify(video), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
