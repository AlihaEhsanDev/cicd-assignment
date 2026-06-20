from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def setup_function():
    main.tasks.clear()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task():
    payload = {"title": "Write tests", "done": False}
    response = client.post("/tasks", json=payload)

    assert response.status_code == 201
    assert response.json() == payload


def test_get_tasks_grows():
    before = client.get("/tasks")
    assert before.status_code == 200
    assert isinstance(before.json(), list)
    assert len(before.json()) == 0

    client.post("/tasks", json={"title": "First task"})
    after = client.get("/tasks")

    assert after.status_code == 200
    assert len(after.json()) == 1
    assert after.json()[0]["title"] == "First task"
    assert after.json()[0]["done"] is False


def test_create_task_empty_title_fails():
    response = client.post("/tasks", json={"title": "   "})

    assert response.status_code == 400
    assert response.json()["detail"] == "Title cannot be empty"
