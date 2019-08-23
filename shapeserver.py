#!/usr/local/bin/python3


#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 8/23/2019                                              #
#############################################################################################

# Importing system module

import wsgiref.simple_server
import urllib.parse
import sqlite3


def webapp(environ, start_response):

	if environ['REQUEST_METHOD'] == "GET":

		response = """
			<html>
			<head>
			<title>Shape DB Server</title>
			</head>
			<body>
			Welcome to the Shape DB Server. Please specify the types of shapes you are interested in below.<br>
			<form method="POST">
			Enter shape type: <input type="text" name="shapetype"><br>
			Number of points in shape: 
			<input type="range" name="numpoints" min="2" max="10" value="2" id="numbar" oninput="numbar.value=numpoints.value">
			<output name="numbarout" id="numbar">2</output><br>
			Outline color: <select name="outcolor">
			<option value="black">Black</option>
			<option value="orange">Orange</option>
			<option value="red">Red</option>
			<option value="blue">Blue</option>
			</select><br>
			<input type="radio" name="outstyle" value="solid">Solid
			<input type="radio" name="outstyle" value="dashed">Dashed
			<input type="radio" name="outstyle" value="dotted">Dotted<br>
			<input type="submit" name="submitbutton" value="Display circles">
			</form>
			</body>
			</html>"""

	elif environ['REQUEST_METHOD'] == "POST":

		numbytes = int(environ['CONTENT_LENGTH'])
		data = environ['wsgi.input'].read(numbytes).decode("utf-8")
		datadict = urllib.parse.parse_qs(data)
		conn = sqlite3.connect('canvasdb.db')
		curs = conn.cursor()

		query = "select * from shapes where "
		query += "numpoints == "+datadict['numpoints'][0]
		if "shapetype" in datadict :
			query += " and type == '"+datadict['shapetype'][0]+"'"
		query += " and outlinecolor == '"+datadict['outcolor'][0]+"'"
		if "outstyle" in datadict :
			query += " and outlinetype == '"+datadict['outstyle'][0]+"'"
		query += " order by type"
		answer = curs.execute(query)
		response = """
			<html>
			<head>
			<title>Shape DB Server</title>
			</head>
			<body>
			The selected circles are:<br>
			Type   Outline color  Fill color  Outline Style  Num points  Location<br>"""

		for obj in answer:
			response += str(obj[0])+"  "+str(obj[1])+"  "+str(obj[2])+"  "+str(obj[3])+"  "+str(obj[4])+"  "+str(obj[5])+"<br>"
		response += "</body></html>"

	response = response.encode("utf-8")
	numbytes = len(response)
	status = "200 ok"
	headers = [('Content-type', 'text/html, charset=utf08'), ('Content-length', str(numbytes))]
	start_response(status, headers)
	return [response]


servobj = wsgiref.simple_server.make_server("", 8050, webapp)
servobj.serve_forever()

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
