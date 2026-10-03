import validators
class User:
    def __init__(self, email=None):
        self._email = None
        if email is not None:
            self.email = email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, other):
        if validators.email(other):
            self._email = other
        else:
           raise ValueError("Invalid email")

usr = User()
print(usr.email)
usr.email = "myemail@email.com"
print(usr.email)