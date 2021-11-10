import pickle
with open('files/pics.pkl', 'rb') as f:
    x = pickle.load(f)
print(x)
