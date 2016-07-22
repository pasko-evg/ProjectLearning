from PP4E.preview.initdata import sue, tom, bob
import pickle

for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    rec_file = open(key + '.pkl', 'wb')
    pickle.dump(record, rec_file)
    rec_file.close()

