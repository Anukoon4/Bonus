from flask import Flask, request
from flask_restful import Resource ,Api, reqparse
from flask_cors import CORS
import json

app= Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('data1')
parser.add_argument('data2')
parser.add_argument('data3')
parser.add_argument('data4')
parser.add_argument('data5')
parser.add_argument('data6')
parser.add_argument('data7')
parser.add_argument('data8')
parser.add_argument('data9')
parser.add_argument('data10')

def merge(Arraydata):
	if len(Arraydata)>1:
		mid=len(Arraydata)//2
		left=Arraydata[:mid]
		right=Arraydata[mid:]
		merge(left)
		merge(right)
		i=0;j=0;k=0;	
		while i <len(left) and j <len(right):
			if left[i] < right[j]:
				Arraydata[k]=left[i]
				i=i+1
			else:
				Arraydata[k]=right[j]
				j=j+1
			k=k+1
		while i<len(left):
			Arraydata[k]=left[i]
			i=i+1
			k=k+1

		while j<len(right):
			Arraydata[k]=right[j]
			j=j+1
			k=k+1

def bubble(Arraydata):
	for i in range(len(Arraydata)-1,0,-1):
		for j in range(i):
			if Arraydata[j]>Arraydata[j+1]:
				temp=Arraydata[j]
				Arraydata[j]=Arraydata[j+1]
				Arraydata[j+1]=temp


def quick(Arraydata):

    if not Arraydata:
        return []

    pivots = [x for x in Arraydata if x == Arraydata[0]]
    lesser = quick([x for x in Arraydata if x < Arraydata[0]])
    greater = quick([x for x in Arraydata if x > Arraydata[0]])

    return lesser + pivots + greater




class bubbleSort(Resource):
        def post(self):
                args = parser.parse_args()
                data1=int(args['data1'])
                data2=int(args['data2'])
                data3=int(args['data3'])
                data4=int(args['data4'])
                data5=int(args['data5'])
                data6=int(args['data6'])
                data7=int(args['data7'])
                data8=int(args['data8'])
                data9=int(args['data9'])
                data10=int(args['data10'])
		Arraydata=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,]
		bubble(Arraydata)

                return {"data":str(Arraydata)}

class mergeSort(Resource):
        def post(self):
                args = parser.parse_args()
                data1=int(args['data1'])
                data2=int(args['data2'])
                data3=int(args['data3'])
                data4=int(args['data4'])
                data5=int(args['data5'])
                data6=int(args['data6'])
                data7=int(args['data7'])
                data8=int(args['data8'])
                data9=int(args['data9'])
                data10=int(args['data10'])
		Arraydata=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
		merge(Arraydata)

		return {"data":str(Arraydata)}

class quickSort(Resource):
        def post(self):
                args = parser.parse_args()
                data1=int(args['data1'])
                data2=int(args['data2'])
                data3=int(args['data3'])
                data4=int(args['data4'])
                data5=int(args['data5'])
                data6=int(args['data6'])
                data7=int(args['data7'])
                data8=int(args['data8'])
                data9=int(args['data9'])
                data10=int(args['data10'])
		Arraydata=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
		Arraydata=quick(Arraydata)

		return {"data":str(Arraydata)}
		

api.add_resource(bubbleSort,'/Bubble')
api.add_resource(quickSort,'/Quick')
api.add_resource(mergeSort,'/Merge')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555)
