import shelve

field_names = ('name', 'age', 'job', 'pay')
max_field = max(len(f) for f in field_names)
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key: break
    try:
        record = db[key]
    except:
        print('No such key "%s"!' % key)
    else:
        for field in field_names:
            print(field.ljust(max_field), '=>', getattr(record, field))