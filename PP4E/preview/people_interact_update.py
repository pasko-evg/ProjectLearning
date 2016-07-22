import shelve
from PP4E.preview.person import Person

field_names = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in field_names:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\tnew? => ' % (field, currval))
        print(newtext)
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()
