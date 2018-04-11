from flask import Flask, request
from flask_restful import Resource ,Api, reqparse


app= Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('A')
parser.add_argument('B')

def add(A,B):
	BB=[[B[0][0]*2,B[0][1]*2,B[0][2]*2],
		[B[1][0]*2,B[1][1]*2,B[1][2]*2],
		[B[2][0]*2,B[2][1]*2,B[2][2]*2]]

	result=[[A[0][0]+BB[0][0],A[0][1]+BB[0][1],A[0][2]+BB[0][2]],
		[A[1][0]+BB[1][0],A[1][1]+BB[1][1],A[1][2]+BB[1][2]],
		[A[2][0]+BB[2][0],A[2][1]+BB[2][1],A[2][2]+BB[2][2]]]
	return result


def mul(A,B):
	result=[[(A[0][0]*B[0][0])+(A[0][1]*B[1][0])+(A[0][2]*B[2][0]),
		(A[0][0]*B[0][1])+(A[0][1]*B[1][1])+(A[0][2]*B[2][1]),
		(A[0][0]*B[0][2])+(A[0][1]*B[1][2])+(A[0][2]*B[2][2])],

		[(A[1][0]*B[0][0])+(A[1][1]*B[1][0])+(A[1][2]*B[2][0]),
		(A[1][0]*B[0][1])+(A[1][1]*B[1][1])+(A[1][2]*B[2][1]),
		(A[1][0]*B[0][2])+(A[1][1]*B[1][2])+(A[1][2]*B[2][2])],

		[(A[2][0]*B[0][0])+(A[2][1]*B[1][0])+(A[2][2]*B[2][0]),
		(A[2][0]*B[0][1])+(A[2][1]*B[1][1])+(A[2][2]*B[2][1]),
		(A[2][0]*B[0][2])+(A[2][1]*B[1][2])+(A[2][2]*B[2][2])]]
	return result

def inverse(A):
	det=((A[0][0]*A[1][1]*A[2][2])+(A[0][1]*A[1][2]*A[2][0])+(A[0][2]*A[1][0]*A[2][1])
		-(A[0][2]*A[1][1]*A[2][0])-(A[0][0]*A[1][2]*A[2][1])-(A[0][1]*A[1][0]*A[2][2]))

	cof=[[0,0,0],[0,0,0],[0,0,0]]
	cof[0][0]=(A[1][1]*A[2][2])-(A[1][2]*A[2][1])
	cof[0][1]=(-1)*((A[1][0]*A[2][2])-(A[1][2]*A[2][0]))
	cof[0][2]=(A[1][0]*A[2][1])-(A[1][1]*A[2][0])
	cof[1][0]=(-1)*((A[0][1]*A[2][2])-(A[0][2]*A[2][1]))
	cof[1][1]=(A[0][0]*A[2][2])-(A[0][2]*A[2][0])
	cof[1][2]=(-1)*((A[0][0]*A[2][1])-(A[0][1]*A[2][0]))
	cof[2][0]=(A[0][1]*A[1][2])-(A[0][2]*A[1][1])
	cof[2][1]=(-1)*((A[0][0]*A[1][2])-(A[0][2]*A[1][0]))
	cof[2][2]=(A[0][0]*A[1][1])-(A[0][1]*A[1][0])
	
	adj=[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(3):
		for j in range(3):
		 	adj[i][j]=cof[j][i]
	
	inver=[[0,0,0],[0,0,0],[0,0,0]]
	for k in range(3):
		for l in range(3):
			inver[k][l]=float(adj[k][l])/det

			
	return inver

def sumMat(A,B):


	result=[[A[0][0]+B[0][0],A[0][1]+B[0][1],A[0][2]+B[0][2]],
		[A[1][0]+B[1][0],A[1][1]+B[1][1],A[1][2]+B[1][2]],
		[A[2][0]+B[2][0],A[2][1]+B[2][1],A[2][2]+B[2][2]]]
	return result




class Addsub(Resource):
        def post(self):
                args = parser.parse_args()
                dataA=args['A']
		dataB=args['B']
		A=[[int(dataA[2]),int(dataA[4]),int(dataA[6])],
			[int(dataA[10]),int(dataA[12]),int(dataA[14])],
			[int(dataA[18]),int(dataA[20]),int(dataA[22])]]
		B=[[int(dataB[2]),int(dataB[4]),int(dataB[6])],
			[int(dataB[10]),int(dataB[12]),int(dataB[14])],
			[int(dataB[18]),int(dataB[20]),int(dataB[22])]]

		Z=add(A,B)
                return {"Z":Z}
class Multiply(Resource):
        def post(self):
                args = parser.parse_args()
                dataA=args['A']
		dataB=args['B']
		A=[[int(dataA[2]),int(dataA[4]),int(dataA[6])],
			[int(dataA[10]),int(dataA[12]),int(dataA[14])],
			[int(dataA[18]),int(dataA[20]),int(dataA[22])]]
		B=[[int(dataB[2]),int(dataB[4]),int(dataB[6])],
			[int(dataB[10]),int(dataB[12]),int(dataB[14])],
			[int(dataB[18]),int(dataB[20]),int(dataB[22])]]

		Z=mul(A,B)
                return {"Z":Z}

class Hardcore(Resource):
        def post(self):
                args = parser.parse_args()
                dataA=args['A']
		dataB=args['B']
		A=[[int(dataA[2]),int(dataA[4]),int(dataA[6])],
			[int(dataA[10]),int(dataA[12]),int(dataA[14])],
			[int(dataA[18]),int(dataA[20]),int(dataA[22])]]
		B=[[int(dataB[2]),int(dataB[4]),int(dataB[6])],
			[int(dataB[10]),int(dataB[12]),int(dataB[14])],
			[int(dataB[18]),int(dataB[20]),int(dataB[22])]]
		a1=mul(A,A)
		a2=inverse(B)
		a12=mul(a1,a2)
		b1=inverse(A)
		b2=B
		b12=mul(b1,b2)
		c1=mul(A,B)
		sum12=sumMat(a12,b12)
		z=sumMat(sum12,c1)
		return {"Z":z}


api.add_resource(Addsub,'/Addsub')
api.add_resource(Multiply,'/Multiply')
api.add_resource(Hardcore,'/Hardcore')


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555)
