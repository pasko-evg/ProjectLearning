dbFileName = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def store_dbase(ydb, dbfilename=dbFileName):
    """сохраняет базу данных в файл"""
    db_file = open(dbfilename, 'w')
    for key in ydb:
        print(key, file=db_file)
        for (name, value) in ydb[key].items():
            print(name + RECSEP + repr(value), file=db_file)
        print(ENDREC, file=db_file)
    print(ENDDB, file=db_file)
    db_file.close()


def load_dbase(dbfilename=dbFileName):
    """восстанавливает данные, реконструируя базу данных"""
    db_file = open(dbfilename)
    import sys
    sys.stdin = db_file
    ydb = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        ydb[key] = rec
        key = input()
    return ydb

if __name__ == '__main__':
    from PP4E.preview.initdata import db
    store_dbase(db)
