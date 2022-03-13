from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, home_phone=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_phone = home_phone
        self.email = email
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.firstname}:{self.lastname}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize
