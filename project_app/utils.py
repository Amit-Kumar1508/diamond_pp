import pickle
import json
import numpy as np

class diamond_price():
    def __init__(self,carat,cut,color,clarity,depth,table,x,y,z):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z

    def load_model(self):
        with open(r'F:\Velocity DataScience\Flask Practice\Diamond price pridiction 2\project_app\Linear_model.pkl','rb') as f:
            self.model = pickle.load(f)

        with open(r'F:\Velocity DataScience\Flask Practice\Diamond price pridiction 2\project_app\diamond_price_pridiction.json','r') as f:
            self.json_data = json.load(f)

    def pridicted_price(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))
        print(test_array)
        print(self.json_data)
        test_array[0] = self.carat
        test_array[1] = self.json_data["cut"][self.cut]
        test_array[2] = self.json_data['color'][self.color]
        test_array[3] = self.json_data['clarity'][self.clarity]
        test_array[4] = self.depth
        test_array[5] = self.table
        test_array[6] = self.x
        test_array[7] = self.y
        test_array[8] = self.z
        for i in range(0,9):
            print(f'{i} :',test_array[i])
        print(f'Test array {test_array}')
        diamond_pri_price = np.around(self.model.predict([test_array])[0],2)
        print(diamond_pri_price)
        return diamond_pri_price

if __name__ == '__main__':
    carat = 0.75
    cut = 'Fair'
    color = 'D'
    clarity = "FL"
    depth = 62.2
    table = 55.0
    x = 1.25
    y = 4.12
    z = 3.44

    di_pr = diamond_price(carat,cut,color,clarity,depth,table,x,y,z)
    di_pr.pridicted_price()