import sqlite3
from flask.templating import render_template_string
import pandas as pd
from sqlalchemy import create_engine, engine
from flask import Flask,render_template,request,redirect
import os
from werkzeug.utils import secure_filename
app=Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_4#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=["GET","POST"])
def func():
    if request.method=="POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        df = pd.read_excel(file,None)
        # print(df)
        a = df.values()
        # print(a)
        # print(df.values())
        def foo(df):
            list1 = []
            for j in df.keys():
                list1.append(j)
                return list1
        engine = create_engine("sqlite:///data.db", echo=False)
        for i in a:
            print(i)
            df = pd.read_excel(file,None)
            i.to_sql(foo(df),con=engine, if_exists="append", index=False)
        return redirect('/')
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)