import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)

db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key: break
    mes = input('Do you want to update or watch data? Input\nupdate for update,\nwatch for watch:\n')
    if mes.strip() == 'update':
        if key in db:
            record = db[key]
        else:
            record = Person(name='?', age='?')
        for field in fieldnames:
            currval = getattr(record, field)
            newtext = input('\t[%s]=%s\n\t\tnew? =>' % (field, currval))
            if newtext:
                setattr(record, field, eval(newtext))
        db[key] = record
    elif mes.strip() == 'watch':
        try:
            record = db[key]
        except:
            print('No such key "%s"!' % key)
        else:
            for field in fieldnames:
                print(field.ljust(maxfield), '=> ', getattr(record, field))
    else:
        print('Sorry, incorrect option! Try again, please')
db.close()
