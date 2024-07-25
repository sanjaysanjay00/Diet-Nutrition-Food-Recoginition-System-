from flask import Flask, render_template, flash, request, session, send_file
from flask import render_template, redirect, url_for, request
import os
import mysql.connector
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/NewFood")
def NewFood():
    base_dir = 'Data/'
    catgo = os.listdir(base_dir)
    return render_template('NewFood.html', data=catgo)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user="root", password='280124', host='localhost', database='db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('AdminHome.html', data=data, flash='Login successfully')

        else:
            flash("uname Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user="root", password='280124', host='localhost', database='db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/FoodInfo")
def FoodInfo():
    conn = mysql.connector.connect(user="root", password='280124', host='localhost', database='db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM foodtb  ")
    data = cur.fetchall()
    return render_template('FoodInfo.html', data=data)


@app.route("/newfood", methods=['GET', 'POST'])
def newfood():
    if request.method == 'POST':
        ftime = request.form['ftime']
        range = request.form['range']
        fname = request.form['fname']
        qty = request.form['qty']
        Info = request.form['info']

        conn = mysql.connector.connect(user="root", password='280124', host='localhost', database='db')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO foodtb (ftime, frange, fname, qty, info) VALUES ('{ftime}','{range}','{fname}','{qty}','{Info}');")
        conn.commit()
        conn.close()

        flash('New Food Info Register successfully')

        base_dir = 'Data/'
        catgo = os.listdir(base_dir)
        return render_template('NewFood.html', data=catgo)


@app.route("/ARemove")
def ARemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='280124', host='localhost', database='db')
    cursor = conn.cursor()
    cursor.execute(
        "delete from foodtb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Food  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='280124', host='localhost', database='db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM foodtb ")
    data = cur.fetchall()

    return render_template('FoodInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='280124', host='localhost', database='db')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO regtb (name, mobile, email, address, uname, password) VALUES ('{name}', '{mobile}', '{email}', '{address}', '{uname}', '{password}');")
        conn.commit()
        conn.close()
        flash('User Register successfully')

    return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        uname = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='280124', host='localhost', database='db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * from regtb where uname='{uname}' and password='{password}';")
        data = cursor.fetchone()
        if data is None:

            flash('uname or Password is wrong')
            return render_template('UserLogin.html')
        else:

            conn = mysql.connector.connect(user="root", password='280124', host='localhost', database='db')
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM regtb WHERE uname='{uname}' AND password='{password}';")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']
    conn = mysql.connector.connect(user="root", password='280124', host='localhost', database='db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  where uname='" + uname + "' ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/BMI")
def BMI():
    return render_template('BMI.html')


@app.route("/bmi", methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
        out = ''
        if bmi <= 18.5:
            out = 'UnderWeight'
        elif 18.5 < bmi <= 24.9:
            out = 'NormalWeight'
        elif 24.9 < bmi <= 29.9:
            out = 'OverWeight'
        elif bmi > 30.0:
            out = 'OBESE'
        session['bmi'] = out
        return render_template('Prediction.html', bmi=out)




def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        
        file = request.files['file']
        file.save('static/upload/Test.jpg')
        fname = 'static/upload/Test.jpg'

        import warnings
        warnings.filterwarnings('ignore')

        base_dir = 'Data/'
        catgo = os.listdir(base_dir)
       # print(catgo)
        classifierLoad = tf.keras.models.load_model('model/model.h5')
        test_image = image.load_img('static/upload/Test.jpg', target_size=(200, 200))
       # print(type(test_image))
        test_image = np.expand_dims(test_image, axis=0)
       # print(type(test_image))
        result = classifierLoad.predict(test_image)
        print(result)

        ind = np.argmax(result)

        print(catgo[ind])

        if catgo[ind] == "burger":
            pre = "Calories: 350 Fat: 14gSodium: 630mg Carbohydrates: 35g Fiber: 1.95g Sugars: 6.01g Protein: 17g"
        elif catgo[ind] == "butter_naan":

            pre = '''Calories: 262.
Fat: 5 grams.
Carbs: 45 grams.
Protein: 9 grams.
Fiber: 2 grams.
Sugar: 3 grams.
Sodium: 18% of the Daily Value (DV)
Iron: 16% of the DV.'''

        elif catgo[ind] == "chai":

            pre = """Total Fat 0 g
Saturated fat 0 g
Cholesterol 0 mg
Sodium 4 mg	
Potassium 18 mg	
Total Carbohydrate 0.2 g	
Dietary fiber 0 g """
        elif catgo[ind] == "chapati":

            pre = """otal Fat 3.7ggrams6%Daily Value
Saturated Fat 1.3ggrams7%Daily Value
Trans Fat 0ggrams
Polyunsaturated Fat 0.3ggrams
Monounsaturated Fat 0.8ggrams
Cholesterol 0 mgmilligrams
Sodium 119 mgmilligrams
Potassium 78mgmilligrams
Total Carbohydrates 18ggrams
Dietary Fiber 3.9ggrams16
Sugars 1.2g"""

        elif catgo[ind] == "chole_bhature":
            pre = """Saturated Fat 4.1ggrams21%Daily Value
Trans Fat 0.2ggrams
Cholesterol 5.7mgmilligrams
Sodium 507mgmilligrams
Potassium 526mgmilligrams
Total Carbohydrates 59ggrams
Dietary Fiber 11ggrams
Sugars 8.6g"""

        elif catgo[ind] == "dal_makhani":

            pre = """Total Fat 19g. 29%
Saturated Fat 9.9g. 50%
Trans Fat 0.6g.
Cholesterol 44mg. 15%
Sodium 372mg. 16%
Potassium 567mg. 16%
Total Carbohydrates 31g. 10%
Dietary Fiber 10g. 40%"""
        elif catgo[ind] == "dhokla":

            pre = """Total Fat 7.4g. 11%
Saturated Fat 2.5g. 13%
Cholesterol 3.3mg. 1%
Sodium 310mg. 13%
Potassium 240mg. 7%
Total Carbohydrates 16g. 5%
Dietary Fiber 2.5g. 10%
Sugars 5.7g."""
        elif catgo[ind] == "fried_rice":

            pre = """Total Fat 2.3 g	3%
Saturated fat 0.5 g	2%
Trans fat regulation 0 g	
Cholesterol 23 mg	7%
Sodium 396 mg	16%
Potassium 88 mg	2%
Total Carbohydrate 31 g	10%
Dietary fiber 1.1 g	4%
Sugar 0.4 g"""

        elif catgo[ind] == "idli":
            pre = """35-39 calories, 2-3 grams of protein, 2-5 grams of dietary fibre and 6-10 grams of carbohydrates; 1-5 milligram of iron, and trace amounts of calcium, folate, potassium, and vitamin A depending on the flavour item used in it"""

        elif catgo[ind] == "jalebi":
            pre = """Total Fat 3.5g. 5%
Saturated Fat 2.1g. 11%
Cholesterol 8.5mg. 3%
Sodium 4.7mg. 0%
Potassium 81mg. 2%
Total Carbohydrates 29g. 10%
Dietary Fiber 0.4g. 2%
Sugars 19g."""


        elif catgo[ind] == "kaathi_rolls":

            pre = """Total Fat 23g. 35%
Saturated Fat 2.5g. 13%
Cholesterol 0mg. 0%
Sodium 760mg. 32%
Total Carbohydrates 56g. 19%
12%
Sugars 0g.
Protein 8g."""
        elif catgo[ind] == "kadai_paneer":

            pre = """Calories per Serving: 458.
Total Fat: 33g.
Saturated Fat: 2g.
Cholesterol: 1mg.
Sodium: 1400mg.
Potassium: 444.
Carbohydrates: 25g.
Dietary Fiber: 5g."""
        elif catgo[ind] == "kulfi":

            pre = """Total Fat 7.6g. 12%
Saturated Fat 5.3g. 27%
Cholesterol 17mg. 6%
Sodium 104mg. 4%
Potassium 195mg. 6%
Total Carbohydrates 25g. 8%
Dietary Fiber 0.2g. 1%
Sugars 22g."""

        elif catgo[ind] == "masala_dosa":
            pre = """Total Fat 3.7g. 6%
Saturated Fat 0.5g. 3%
Cholesterol 0mg. 0%
Sodium 94mg. 4%
Potassium 76mg. 2%
Total Carbohydrates 29g. 10%
Dietary Fiber 0.9g. 3%
Sugars 0.2g."""

        elif catgo[ind] == "momos":

            pre = """Total Fat 2.2ggrams3%Daily Value
Saturated Fat 0.4ggrams
Trans Fat 0ggrams
Cholesterol 11mgmilligrams
Sodium 11mgmilligram
Potassium 102mgmilligrams
Total Carbohydrates 7.2ggrams
Dietary Fiber 0.4g"""
        elif catgo[ind] == "paani_puri":

            pre = """Saturated Fat 0.8ggrams
Trans Fat 0.2ggrams
Cholesterol 0mgmilligrams
Sodium 110mgmilligrams
Potassium 90mgmilligrams
Total Carbohydrates 15ggrams
Dietary Fiber 2.2ggrams
Sugars 1.9g"""
        elif catgo[ind] == "pakode":

            pre = """Total Fat 23g. 35%
Saturated Fat 2.5g. 13%
Cholesterol 0mg. 0%
Sodium 760mg. 32%
Total Carbohydrates 56g. 19%
12%
Sugars 0g.
Protein 8g."""

        elif catgo[ind] == "pav_bhaji":
            pre = """Total Fat 7.6g. 12%
Saturated Fat 5.3g. 27%
Cholesterol 17mg. 6%
Sodium 104mg. 4%
Potassium 195mg. 6%
Total Carbohydrates 25g. 8%
Dietary Fiber 0.2g. 1%
Sugars 22g."""

        elif catgo[ind] == "pizza":
            pre = """Total Fat 2.2ggrams3%Daily Value
Saturated Fat 0.4ggrams
Trans Fat 0ggrams
Cholesterol 11mgmilligrams
Sodium 11mgmilligram
Potassium 102mgmilligrams
Total Carbohydrates 7.2ggrams
Dietary Fiber 0.4g"""

        elif catgo[ind] == "samosa":
            pre = """Saturated Fat 0.8ggrams
Trans Fat 0.2ggrams
Cholesterol 0mgmilligrams
Sodium 110mgmilligrams
Potassium 90mgmilligrams
Total Carbohydrates 15ggrams
Dietary Fiber 2.2ggrams
Sugars 1.9g"""

        out = session['bmi']
            #return render_template('Prediction.html', bmi=out)

        conn = mysql.connector.connect(user="root", password='280124', host='localhost', database='db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM foodtb where frange='{str(out)}' and fname='{str(catgo[ind])}';")
        data = cur.fetchall()

        return render_template('Result.html', fer=pre, result=catgo[ind], org=fname ,bmi=out , data=data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
