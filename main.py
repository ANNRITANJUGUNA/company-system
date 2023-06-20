from flask import  Flask,render_template 
from mypgtable import fetch_data

app=Flask(__name__)

@app.route("/")
def Home():
  return render_template("index.html")



@app.route("/customers")
def sales():
    prods=fetch_data("customers")
    
    
    return render_template('products.html', customers=prods)

app.run()




