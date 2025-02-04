import requests
import pytest
import time

# Предполагаем, что compose запущен, и user-service доступен на localhost:8000, video-service - на localhost:9000
USER_URL = "http://127.0.0.1:8000"
VIDEO_URL = "http://127.0.0.1:9000"

@pytest.mark.integration
def test_create_user_and_video():
    # 1. Создаём пользователя
    user_data = {"username": "bob", "email": "bob@example.com"}
    r_user = requests.post(f"{USER_URL}/api/v1/users", json=user_data)
    assert r_user.status_code == 201
    user = r_user.json()
    user_id = user["id"]
    
    # 2. Создаём видео, привязанное к этому пользователю
    video_data = {"title": "Integration Test Video", "ownerId": user_id}
    r_video = requests.post(f"{VIDEO_URL}/api/v1/videos", json=video_data)
    assert r_video.status_code == 201
    video = r_video.json()
    assert video["ownerId"] == user_id
    assert video["ownerCheck"] == "User exists"  # Поскольку пользователь реально существует
