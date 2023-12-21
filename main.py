x = open("Expected.txt").readlines()
f = open("Output.txt" , "w")

from datetime import datetime

now = datetime.now() # current date and time


print(x)

lists = []
loclen = 8

for i in range(3):
    j = []

    for i in range(loclen):
        k = []
        j.append(k)

    lists.append(j)


def old():

    for line in x:
        outputline = "|"
        elements = line.split("\t")
        for i in range(len(elements)):
            elements[i] = elements[i].strip()
            if elements[i].isalnum():
                locations[i].append(elements[i])
                outputline += elements[i]
            outputline += "|"
        f.write(outputline + "\n")

    for l in lists:
        print(l)


# Location[locationID][List]
# 0 - Poznan, 1 - Rzeszow, 2 - Gdansk, 3 - Krakow, 4 - Wroclaw, 5 - Prague, 6 - Ostrava, 7 - Bratislava
# 0 - Accepted, 1 - Pending, 2 - Waiting
for line in x:
    person = line.split("\t")
    locationid = 0
    statusid = 0
    match person[1].lower():
         case "poznan":
             locationid = 0
         case "rzeszow":
             locationid = 1
         case "gdansk":
             locationid = 2
         case "krakow":
             locationid = 3
         case "wroclaw":
             locationid = 4
         case "prague":
             locationid = 5
         case "ostrava":
             locationid = 6
         case "bratislava":
             locationid = 7
         case _ : continue
    match person[2].lower():
        case "waiting":
            statusid = 2
        case "pending":
            statusid = 1
        case "accepted":
            statusid = 0
        case _ : continue
    lists[statusid][locationid].append(person[0])

p1 = ""
for line in open("p1.txt").readlines():
    p1 += line
f.write(p1 + "\n")

longestlen = 0
for i in range(loclen):
    if len(lists[0][i]) > longestlen:
        longestlen = len(lists[0][i])


# list[location][competitorid]
for i in range(longestlen): # linie
    f.write("|")
    for j in range(loclen): # elementy w liniach
        if i < len(lists[0][j]):
            f.write(lists[0][j][i] + "|")
        else:
            f.write("|")
    f.write("\n")


#pending list
p2 = ""
for line in open("p2.txt").readlines():
    p2 += line
f.write("\n" + p2 + "\n")

penlist = lists[1]
print(penlist)
penlist.pop()
penlist.pop()
penlist.pop(3)
penlist.pop(0)

longestlen = 0
for i in range(4):
    if len(penlist[i]) > longestlen:
        longestlen = len(penlist[i])


# list[location][competitorid]
for i in range(longestlen): # linie
    f.write("|")
    for j in range(4): # elementy w liniach
        if i < len(penlist[j]):
            f.write(penlist[j][i] + "|")
        else:
            f.write("|")
    f.write("\n")








p3 = ""
for line in open("p3.txt").readlines():
    p3 += line
f.write("\n" + p3 + "\n")

longestlen = 0
for i in range(loclen):
    if len(lists[2][i]) > longestlen:
        longestlen = len(lists[2][i])


# list[location][competitorid]
for i in range(longestlen): # linie
    f.write("|")
    for j in range(loclen): # elementy w liniach
        if i < len(lists[2][j]):
            f.write(lists[2][j][i] + "|")
        else:
            f.write("|")
    f.write("\n")


f.write("\nLast update: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")