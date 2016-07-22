import pickle

db_file = open('people-pickle', 'rb')
db = pickle.load(db_file)
db_file.close()

db['sue']['pay'] *= 1.1
db['tom']['name'] = 'Big Tommy'

db_file = open('people-pickle', 'wb')
pickle.dump(db, db_file)
db_file.close()
