import pprint

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hwd'}

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hwd')

sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hwd'

names = ['name', 'age', 'pay', 'job']
value = ['Sue Jones', 45, 40000, 'hwd']

sue = dict(zip(names, value))

# print('bob: ', bob)
# print('sue: ', sue)

fields = ('name', 'age', 'pay', 'job')
record = dict.fromkeys(fields, '?')

# print record

people = [bob, sue]
# for person in people:
# print(person['name'], person['pay'], sep=': ')

G = (rec['age'] for rec in people if rec['age'] >= 45)
# print(G)
# print(G.__next__())

bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)}

# print(bob2)
# print(bob2['name'])
# print(bob2['name']['last'])
# print(bob2['pay'][1])

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hwd')

db = {'bob': bob, 'sue': sue}

print(db)

pprint.pprint(db)

for key in db:
    print(key, '=>', db[key]['pay'])

db['tom'] = dict(name='Tom', age=50, job=None, pay=0)

print([rec['age'] for rec in db.values()])
print([rec['name'] for rec in db.values() if rec['age'] >= 45])
