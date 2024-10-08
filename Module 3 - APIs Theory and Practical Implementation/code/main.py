from fastapi import FastAPI
from dummy_database import users

app = FastAPI()

# Root Route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API!"}  

# GET REQUEST
@app.get("/users")
def get_users():
    return {"users": users}

# GET REQUEST by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"error": "User not found"}, 404

# POST REQUEST
@app.post("/users")
def add_user(user: dict):
    user["id"] = len(users) + 1
    users.append(user)
    return {"user": user}, 201

# PUT/UPDATE REQUEST
@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    for user in users:
        if user["id"] == user_id:
            user.update(user_data)
            return {"user": user}
    return {"error": "User not found"}, 404

# DELETE REQUEST
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    for user in users:
        if user["id"] == user_id:
            users = [user for user in users if user["id"] != user_id]
            return {"message": "User deleted"}, 200
    return {"error": "User not found"}, 404