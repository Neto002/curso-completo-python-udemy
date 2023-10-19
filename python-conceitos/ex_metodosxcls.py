class Connection:
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.set_user(user)
        connection.set_password(password)
        return connection

    @staticmethod
    def log(msg):
        print("Log: ", msg)


c1 = Connection.create_with_auth('neto', '123')

print(c1.user)
print(c1.password)
