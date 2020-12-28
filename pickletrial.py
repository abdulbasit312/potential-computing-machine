import pickle
import pprint
dbfile=open('people-pickle','ab')#opening in write mode delted all existing data
from init import db 
#pprint.pprint(db)
pickle.dump(db,dbfile)
dbfile.close()
dbfile=open('people-pickle','ab')
rec={'ccc':{'name':'Abdul Basit','age':23,'pay':40000,'job':'swe'}}
pickle.dump(rec,dbfile)
dbfile.close()
with open ('people-pickle','rb') as dbfile:
    dbfile.seek(0)
    while True:
        try:
            ab=pickle.load(dbfile)
            print(ab)
        except:
            break
pprint.pprint(ab)