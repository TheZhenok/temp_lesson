class User:

    def __init__(self,name: str,
                 login: str) -> None:
        self.name = name
        self.login = login

    def __call__(self, *args: tuple, **kwds: dict) -> None:
        print("I'm here!")


a = User(name='Bob',
         login='lll')
a()
