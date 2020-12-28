import classprac
import shelve
#db=dict(abd=classprac.p,zub=classprac.q)   dictionary mapping to class objects
#print(db)
db=shelve.open('people-shelve')
db['Abd']=classprac.p
db['zub']=classprac.q
for key in db:
    print(key, '=>',db[key])
db.close()
