from init import db
import shelve
import pprint
#print (db)
bob,sue=db['bob'],db['sue']
file=shelve.open("people-shelve")
""" 
for inserting element first time, shelves work just like dictionary of dictionary
"""
#file['bob'],file['sue']=bob,sue
#update
#bob=file['bob']
#bob['pay']=20
#file['bob']=bob
for key in file:
    print(key,'=>',file[key])

file.close()