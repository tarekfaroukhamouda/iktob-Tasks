from flask import Flask,request
app = Flask(__name__)

@app.route('/total',methods=['POST'])
def getTotal():
   data = request.json
   numbers=data.get('objects',[])
   total = 0
   if not isinstance(numbers, list):
      return "Please send it as List "

   if len(numbers) > 0:

      for i in numbers:
          if not  i.isnumeric():
             return 'Please Insert numeric values'
          total+=float(i)

   return "Total is "+str(total)
@app.route('/con',methods=['POST'])
def concatened():
   data = request.json

   first=data.get('first',"")
   secand=data.get('secand',"")
   if first.isnumeric() or secand.isnumeric():
      return 'Please insert String values'
   return first+" "+secand


if __name__ == '__main__':
   app.run()