class User:
    name: str
    last_name: str
    password: str

    def __init__(self, name: str, last_name: str, password: str):
        self.name = name
        self.last_name = last_name
        self.password = password

    def __str__(self):
        return "{'name':" + self.name + ", 'last_name':" + self.last_name + ", 'password':" + self.password + "}"
