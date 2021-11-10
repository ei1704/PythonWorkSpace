import pickle

big_num = 2**100

with open('files/bignum.pkl', 'wb') as f:
    pickle.dump(big_num, f)
