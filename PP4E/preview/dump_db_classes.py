import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay, db[key].__class__)

bob = db['bob']
print(bob.last_name())
print(db['tom'].last_name())
