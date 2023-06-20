from flask import  Flask,render_template 
from mypgtable import fetch_data

app=Flask(__name__)

@app.route("/")
def Home():
  return render_template("index.html")



@app.route("/products")
def Customers():
    prods=fetch_data("products")
    return render_template('products.html', products=prods)

@app.route("/sales")
def sales():
    prods=fetch_data("sales")
    return render_template('sales.html', sales=prods)

app.run()




