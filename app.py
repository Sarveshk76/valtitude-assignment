from flask import Flask, url_for
from flask import render_template
import pandas as pd
import json
import datetime

app = Flask(__name__)

def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime):
        return obj.isoformat() 
    raise TypeError("Type not serializable") 

@app.route('/')
def excel_data():
    df = pd.read_excel("data_for_assignment.xlsx")
    df = df.dropna(axis = 0, how = 'all')
    df = df.iloc[:,3:]
    json_data = json.dumps(df.to_dict(), default=serialize_datetime)
    json_data = json.loads(json_data)
    return render_template('index.html', json_data=json_data)
