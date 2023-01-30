from project_app.utils import  diamond_price
from flask import Flask, jsonify, render_template, request
import config

app = Flask(__name__)
#**************************Base API*******************
@app.route('/')
def diamond_model():
    print('Welcome to Diamond Price Prediction Model')
    # return 'Diamond Page' # render_template('index.html')
    return render_template('index.html')
#***************************Model API*****************
@app.route(rule='/price_predict',methods = ['GET','POST'])
def my_diamond_price():
    # print('diamond price prediction page')
    # return 'Diamond Price pridiction'
    if request.method == 'POST':
        print('POST Method')
        # return "POST POST"
        data = request.form
        print('My data',data)
        carat = eval(data['carat'])
        cut = data['cut']
        color = data['color']
        clarity = data['clarity']
        depth = eval(data['depth'])
        table = eval(data['table'])
        x = eval(data['x'])
        y = eval(data['y'])
        z = eval(data['z'])
        print(carat)
        print(cut)
        print(color)
        print(clarity)
        print(depth)
        print(table)
        print(x)
        print(y)
        print(z)
        di_prx = diamond_price(carat,cut,color,clarity,depth,table,x,y,z)
        charges = di_prx.pridicted_price()
        print('charges :',charges)
        # return f'Diamond pridicted ptice :{charges}'
        return jsonify({'Result':f"Predicted diamond Price: RS.{charges}"})
    else:

        print('GET Method')
        data1 = request.args
        print('My data2',data1)
        carat = data1['carat']
        cut = data1['cut']
        color = data1['color']
        clarity = data1['clarity']
        depth = data1['depth']
        table = data1['table']
        x = data1['x']
        y = data1['y']
        z = data1['z']
        print(carat)
        print(cut)
        print(color)
        print(clarity)
        print(depth)
        print(table)
        print(x)
        print(y)
        print(z)
        di_prx = diamond_price(carat,cut,color,clarity,depth,table,x,y,z)
        charges = di_prx.pridicted_price()
        print('charges :',charges)
        return jsonify({'Result':f"Predicted diamond Price: RS.{charges}"})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT_NUMBER,debug=False)