bob=['Bob Smith',42,30000,'software']
sue=['Sue Jones',45,40000,'hardware']
people=[bob,sue]
for person in people:
    print(person)
print(people[1][0].split()[-1])

pays=map(lambda x: x[2],people)
print(list(pays))
