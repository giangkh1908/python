from fastapi import FastAPI

# creat app

app = FastAPI()

# tạo 1 api
# @app.get("/users/{user_id}") # user_id using in function get_user
# def get_user(user_id: int):
#     return {"user_id": user_id, "message": "User found!"}

@app.get("/search") #   search using in function search
def search_users(name: str, age: int = None):
    return {"name": name, "age": age}
    
    