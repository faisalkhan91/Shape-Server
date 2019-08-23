#!/usr/local/bin/python3


#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 8/23/2019                                              #
#############################################################################################

# Importing system module

import sqlite3
import random

random.seed()
db = sqlite3.connect("canvasdb.db")
cdb = db.cursor()

# cdb.execute("create table shapes (type text, outlinecolor text, fillcolor text, outlinetype text, numpoints integer, location text)")

objectlist = []
types = ["oval", "rectangle", "polygon"]
colors = ["black", "brown", "orange", "yellow", "red", "blue", "green", "purple", "pink"]
outtypes = ["solid", "dashed", "dotted"]

for index in range(0, 100):
	objtype = random.choice(types)
	outcolor = random.choice(colors)
	fillcolor = random.choice(colors)
	outtype = random.choice(outtypes)
	if objtype == "oval" or objtype == "rectangle":
		num = 2
		x1 = random.randint(0, 500)
		y1 = random.randint(0, 500)
		x2 = x1 + random.randint(1, 100)
		y2 = y1 + random.randint(1, 100)
		pointlist = str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2)
	else:
		num = random.randint(3, 10)
		pointlist = ""

		for n in range(0, num):
			pointlist += str(random.randint(0, 500)) + " " + str(random.randint(0, 500)) + " "

	objectlist.append([objtype, outcolor, fillcolor, outtype, num, pointlist])

# cdb.executemany("insert into shapes (type, outlinecolor, fillcolor, outlinetype, numpoints, location) values (?, ?, ?, ?, ?, ?)", objectlist)

# cdb.execute("delete from shapes where type == 'polygon' and numpoints > 7")

objectlist = cdb.execute("select * from shapes where type == 'polygon' and numpoints > 5 AND numpoints < 7 order by outlinecolor desc, numpoints asc")

for obj in objectlist:
	print(obj[1], obj[0], obj[5])

db.commit()
db.close()

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
