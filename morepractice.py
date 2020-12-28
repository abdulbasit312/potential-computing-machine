import pickle
import pprint
import pickle
rec=dict(a=dict(name='Abdul Basit',roll=90))
file=open('trial','ab')
pickle.dump(rec,file)
rec2=dict(b=dict(name='Zubaida',roll=89))
pickle.dump(rec2,file)
file.close()
file=open('trial','rb')
while True:
    try:
        fp=pickle.load(file)
        pprint.pprint(fp)
    except:
        break
file.close()