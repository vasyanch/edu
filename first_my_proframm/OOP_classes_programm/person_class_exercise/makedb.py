from person import Person, Manager
bob = Person('Bob Smith')
sue = Person('Sue Jones', 'dev', 10000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for objec in (bob, sue, tom):
    db[objec.name] = objec
db.close()
