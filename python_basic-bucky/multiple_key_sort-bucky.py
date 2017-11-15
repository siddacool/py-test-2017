from operator import itemgetter

users = [
    {'fname': 'Brood', 'lname': 'Banger'},
    {'fname': 'Sid', 'lname': 'Man'},
    {'fname': 'Sushant', 'lname': 'Kam'},
    {'fname': 'John', 'lname': 'Smith'},
    {'fname': 'Geb', 'lname': 'Jolt'},
    {'fname': 'Tom', 'lname': 'Anderson'},
    {'fname': 'Sushant', 'lname': 'Aam'}
]

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)
