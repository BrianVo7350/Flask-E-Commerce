from app import app
from app.models import Products
from flask import url_for
from flask import flash, redirect, render_template, request, url_for
# from flask_login import current_user, login_required


@app.route('/')
def homePage():
    all_products = Products.query.all()
    return render_template('index.html',all_products=all_products)

# Temporary fake product 
@app.route('/product')
def fakeProductPage():
    return render_template('product.html')

@app.route('/product/<int:product_id>')
def productPage(product_id):
    product = Products.query.get(product_id)
    return render_template('product.html',product=product)

@app.route('/runcode')
def runcode():
    
    # all_products = Products.query.all()
    values = [1,2,3,6,9]
    for val in values:
        print("hello")
    
    # for product in all_products:
    #     print(product)

    # CODE TO ADD PRODUCT TO DATABASE
    # title = '85" Class QN90C Samsung Neo QLED 4K Smart TV (2023)'
    # image_url = "https://image-us.samsung.com/SamsungUS/home/television-home-theater/tvs/03242023/QN90C_85_75_65_55.jpg?$product-details-jpg$"
    # price = 4799.99
    # description = "Some TVs just have it. They make everything look good—even hard stuff like 4K upscaling, weird viewing angles and daytime sports. But when it's Samsung Neo QLED 4K we're talking about, there's no need to be jealous. Because—thanks to its brilliant picture, dynamic audio and stellar design—it'll make you look good, too."
    # product1 = Products(title,price,description,image_url)
    # product1.saveToDB()
    
    
    return redirect(url_for("homePage"))