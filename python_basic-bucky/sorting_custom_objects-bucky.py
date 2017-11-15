from operator  import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return r'{name} : {id}'.format(name=self.name,
                                       id=str(self.user_id))

users = [
    User('Sid', 25),
    User('Sushant', 26),
    User('Mic', 49),
    User('Stan', 85),
    User('Joe', 9),
    User('Jim', 2)
]

for user in users:
    print(user)

print('----')

for user in sorted(users, key=attrgetter('name')):
    print(user)

print('----')

for user in sorted(users, key=attrgetter('user_id')):
    print(user)