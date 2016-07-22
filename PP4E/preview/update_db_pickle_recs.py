import pickle

sue_file = open('sue.pkl', 'rb')
sue = pickle.load(sue_file)
sue_file.close()
sue['pay'] *= 1.1
sue_file = open('sue.pkl', 'wb')
pickle.dump(sue, sue_file)
sue_file.close()
