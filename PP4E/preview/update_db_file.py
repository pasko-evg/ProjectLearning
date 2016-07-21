from PP4E.preview.make_db_file import load_dbase, store_dbase

db = load_dbase()
db['sue']['pay'] *= 1.1
db['tom']['name'] = 'Tom Snow'
store_dbase(db)


