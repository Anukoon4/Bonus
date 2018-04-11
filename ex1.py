from flask import Flask, request
from flask_restful import Resource ,Api, reqparse
from flask_cors import CORS
import json,cmath

app= Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('data1')
parser.add_argument('data2')



class Add(Resource):
        def post(self):
                args = parser.parse_args()
                data1=args['data1']
		data2=args['data2']
		datacom1=complex(data1)
		datacom2=complex(data2)
		addition=str(datacom1+datacom2)[1:-1]
                return {"data":addition}

class SubCom(Resource):
        def post(self):
                args = parser.parse_args()
                data1=args['data1']
		data2=args['data2']
		datacom1=complex(data1)
		datacom2=complex(data2)
		sub=str(datacom1-datacom2)[1:-1]
                return {"data":sub}

class mulCom(Resource):
        def post(self):
                args = parser.parse_args()
                data1=args['data1']
		data2=args['data2']
		datacom1=complex(data1)
		datacom2=complex(data2)
		multiply=str(datacom1*datacom2)[1:-1]
                return {"data":multiply}



api.add_resource(Add,'/Add')
api.add_resource(SubCom,'/Sub')
api.add_resource(mulCom,'/Multiply')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555)
