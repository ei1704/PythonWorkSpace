import pickle
with open('files/bignum.pkl', 'rb') as f:
    big_num = pickle.load(f)
    print(big_num)
