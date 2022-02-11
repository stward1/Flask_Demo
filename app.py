#importing flask to stand up as REST API and CORS for accessing it from a client
from flask import Flask
from flask_cors import CORS

#importing CSV file reading stuff to work with sample data
import csv

#setting the name of the app; __name__ returns the name of the current Python module
app = Flask(__name__)

#this just enables CORS for all domains on all routes, consider security issues around this
CORS(app)

#decorator that says the next function, home(), is a Flask view function. This converts the return into an HTTP response
#replace "/" with whatever path you want; this is a good default but consider what endpoints you want to reference in the widget/client
@app.route("/")
def home():
    #grabbing and formatting the CSV data as a JSON object; this would probably just use a MySql reader once we stand that up
    myJsonObj = getData()
    # print(myJsonObj)
    return myJsonObj










#loads and returns the CSV data, which is in the dataTest folder (swap out for connection string data)
def getData():
    #opens the file
    file = open(".\\dataTest\\sampleData.csv")
    #opens the file with a CSV reader, I guess?
    csvreader = csv.reader(file)

    #loading the first row into an array; this array is just the name of each field
    header = []
    #next(csv.reader) will populate an array with all the values of the next row of a CSV; not super important once we swap to SQL
    header = next(csvreader)
    
    #loading each row into an array; the first row is skipped since we already read it once with next
    rows = []
    for row in csvreader:
        rows.append(row)

    #closing the file
    file.close()

    #some logic I wrote to combine the two arrays into a manageable JSON object
    records = []
    for row in rows:
        records.append({
            header[0]: row[0],
            header[1]: row[1]
        })

    return { "data": records }
