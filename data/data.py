class User:
    def __init__(self, email: str, password: str, name: str):
        self.access_token = None
        self.email = email
        self.password = password
        self.name = name

    def set_access_token(self, access_token: str):
        self.access_token = access_token

    def get_login_json(self):
        return { "email": self.email, "password": self.password }

    def get_register_json(self):
        return {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }

class Ingredient:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name