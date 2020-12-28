import pickle
a=10101
b='Hello'
f1=open('pickle_trial','ab+')
pickle.dump(a,f1)
pickle.dump(b,f1)
f1.seek(0)
while True:
    try:
        b=pickle.load(f1)
        print(b)
    except:
        break