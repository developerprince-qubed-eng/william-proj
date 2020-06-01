import random

class Polygon():
    def __init__(self):
        self.data = []

    def polygon_checker(self,desc):
        prodsum = []
        total = 0
        ele = 0
        try:
            if(len(desc) % 2 == 0):
                for _, x in desc.items():
                    prod = x * (x+1)
                    prodsum.append(prod)
                while(ele < len(prodsum)):
                    total = total + prodsum[ele]
                    ele += 1
                print("Description is Complete the area is", total)
            else:
                print("Description is incomplete")  
        except:
            print("An Exception occured")


poly = Polygon()

desc = {'N':17.5, 'E':20.4, 'S':25, 'E':7.6, 'S':10, 'W':56, 'N':17.5, 'E':28}
poly.polygon_checker(desc)