### **Step-by-Step Lecture: Building a REST API using FastAPI (with Dummy Database)**

---

### **Step 1: Introduction to FastAPI**
Before starting with code, explain why FastAPI is a good choice:
- **High Performance**: FastAPI is asynchronous, making it faster for handling requests.
- **Automatic Documentation**: It automatically generates documentation using Swagger and ReDoc.
- **Type Hints**: It’s based on Python type hints, making the code clean and easier to understand.

---

### **Step 2: Setting Up the Environment**
1. **Install FastAPI and Uvicorn**:
   - FastAPI is the web framework, and Uvicorn is the ASGI server used to serve the FastAPI app.

   Install both with pip:

   ```bash
   pip install fastapi uvicorn
   ```

2. **Create the Project File**:
   Create a file named `main.py` for your FastAPI app.

---

### **Step 3: Setting Up FastAPI App and Dummy Database**
1. **Basic FastAPI Setup**:
   In `main.py`, create a basic FastAPI app:

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"message": "Welcome to the FastAPI REST API!"}
   ```

   - **Explanation**: This creates a basic FastAPI app with a single endpoint (`/`) that returns a welcome message.

2. **Define a Dummy Database**:
   Next, let’s create a dummy database, similar to how we did with Flask:

   ```python
   users = [
       {"id": 1, "name": "Alice", "email": "alice@example.com"},
       {"id": 2, "name": "Bob", "email": "bob@example.com"},
       {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
   ]
   ```

---

### **Step 4: Creating API Endpoints in FastAPI**

#### **1. GET all users**
```python
@app.get("/users")
def get_users():
    return {"users": users}
```

- **Explanation**: This endpoint responds with a JSON list of all users from the dummy database.

#### **2. GET a single user by ID**
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return {"user": user}
    return {"error": "User not found"}, 404
```

- **Explanation**: This allows you to fetch a single user by their `user_id`. If the user is not found, it returns a 404 error.

#### **3. POST a new user**
```python
from fastapi import Body

@app.post("/users")
def add_user(user: dict = Body(...)):
    user["id"] = len(users) + 1
    users.append(user)
    return {"user": user}, 201
```

- **Explanation**: This accepts a JSON payload to add a new user to the dummy database. FastAPI uses **Body** to extract the incoming JSON data. The new user is assigned a unique `id`.

#### **4. PUT (update) an existing user**
```python
@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict = Body(...)):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(user_data)
        return {"user": user}
    return {"error": "User not found"}, 404
```

- **Explanation**: This updates an existing user’s data based on the provided `user_id`. If the user doesn’t exist, a 404 error is returned.

#### **5. DELETE a user**
```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted"}, 200
```

- **Explanation**: This removes a user from the dummy database by filtering out the user with the specified `user_id`.

---

### **Step 5: Running and Testing the FastAPI App**
1. **Run the FastAPI App**:
   FastAPI apps are run using Uvicorn. Use this command to start the server:

   ```bash
   uvicorn main:app --reload
   ```

   - **Explanation**: `main` is the filename, `app` is the FastAPI instance, and `--reload` allows for automatic reloading on file changes.

2. **Test API Endpoints**:
   You can test the API using tools like **Postman**, **cURL**, or by visiting the auto-generated documentation at:

   - **Swagger UI**: `http://127.0.0.1:8000/docs`
   - **ReDoc**: `http://127.0.0.1:8000/redoc`

   Example test cases:
   - **GET all users**: 
     - URL: `http://127.0.0.1:8000/users`
   - **GET a single user**: 
     - URL: `http://127.0.0.1:8000/users/1`
   - **POST a new user**:
     - URL: `http://127.0.0.1:8000/users`
     - Body:
     ```json
     {
       "name": "David",
       "email": "david@example.com"
     }
     ```
   - **PUT to update a user**:
     - URL: `http://127.0.0.1:8000/users/2`
     - Body:
     ```json
     {
       "name": "Bob Jr.",
       "email": "bobjr@example.com"
     }
     ```
   - **DELETE a user**:
     - URL: `http://127.0.0.1:8000/users/3`

---

### **Step 6: Conclusion and Next Steps**
- **Key Concepts Learned**:
  - Basics of creating RESTful API endpoints using FastAPI.
  - How to handle various HTTP methods (GET, POST, PUT, DELETE).
  - Using a dummy database (a list of dictionaries) to simulate data storage.
  - FastAPI’s built-in features like automatic docs generation.

- **Next Steps**:
  - Connect to a real database (SQLite, PostgreSQL, etc.).
  - Add validation using **Pydantic** models.
  - Implement authentication (JWT, OAuth2, etc.).
  - Handle more advanced scenarios like pagination and filtering.

---

### **Complete `main.py` File Example**
Here’s the complete file for the FastAPI project:

```python
from fastapi import FastAPI, Body

app = FastAPI()

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API!"}

@app.get("/users")
def get_users():
    return {"users": users}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return {"user": user}
    return {"error": "User not found"}, 404

@app.post("/users")
def add_user(user: dict = Body(...)):
    user["id"] = len(users) + 1
    users.append(user)
    return {"user": user}, 201

@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict = Body(...)):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(user_data)
        return {"user": user}
    return {"error": "User not found"}, 404

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted"}, 200
```

