filename="people-file.txt"
ENDDB='enddb.'
ENDREC='endrec.'
RECSEP='=>'
#db is dictionary so key vqlue identifoes elements
def storeDbase(db,dbfilename=filename):
    dbfile=open(dbfilename,'w')
    for key in db:
        for(name,value) in db[key].items():
            print(name+RECSEP+repr(value),file=dbfile) # can also use dbfile.write()
        print(ENDREC,file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()
def loadDbase(dbfilename=filename):
    dbfile=open(dbfilename,'r')
    import sys
    sys.stdin=dbfile
    db={}#empty dictionary
    key=input()
    while key!=ENDDB:
        rec={}
        field=input()
        while field!=ENDREC:
            name,value=field.split(RECSEP)
            rec[name]=eval(value)
            field=input()
        db[key]=rec
        key=input()
    return db
db=dict(bob=dict(name='Bob Smith',age=42,pay=30000,job='dev'),
        sue=dict(name='Sue James',age=45,pay=40000,job='hdw'))
if __name__=='__main__':
    storeDbase(db)
    f=loadDbase()
    import pprint
    pprint.pprint(f)
    #print(db)
    