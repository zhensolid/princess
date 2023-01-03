from flask import Flask,render_template
from get_data import get_excel_date

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = get_excel_date()
    # print(result)
    # return render_template("index.html",result=result)
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)