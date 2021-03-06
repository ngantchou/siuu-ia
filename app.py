import flask
import csv
from werkzeug.utils import secure_filename
from flask import  abort,request,send_file,jsonify, make_response
from Untitled import Model
model=Model()

from flask_cors import CORS, cross_origin
app = flask.Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/recommend', methods = ['GET', 'POST'])
def append_file():
    
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      print("coming",request.form["id"])
      if request.form["id"]!="":
          id=str(request.form["id"])
          print(id,type(id))
          response=model.recommendation(id)
          return _corsify_actual_response(jsonify(response))
      else:
          return "error"
   else:
      return "error"
  
@app.route('/adduser', methods = ['GET', 'POST'])
def add_user():
    
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      
      row=[]
      row.append(request.form["id"])
      row.append(request.form["name"])
      row.append(request.form["city"])
      row.append(request.form["Followers"])
      row.append(request.form["Follow"])
      row.append(request.form["visited_places"])
      row.append(request.form["contact_list"])
      row.append(request.form["contact"])
      row.append(request.form["Interest"])
      print("data a rha",row)
      if request.form["id"]!="":
          
          with open("./Data.csv",encoding='utf8', mode='a+', newline='') as Data:
                employee_writer = csv.writer(Data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow(row)
                return _corsify_actual_response(jsonify("success"))
       #   id=str(request.form["id"])
        #  print(id,type(id))
         # response=model.recommendation(id)
          
      else:
          return "error"
   else:
      return "error"
  
@app.route('/deleteuser', methods = ['GET', 'POST'])
def delete_user():
    
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      
      ids=request.form["id"]
    
      print("data a rha",ids)
      if request.form["id"]!="":
          
            lines=[]
            with open('./Data.csv',encoding='utf8') as readFile:
            
                reader = csv.reader(readFile)
            
                for row in reader:
                    lines.append(row)
                    print(row)
                    if ids in row[3]:
                        row[3]=row[3].replace((ids+","),"")
                        row[3]=row[3].replace((","+ids),"")
                        row[3]=row[3].replace(ids,"")
                    if ids in row[4]:
                        row[4]=row[4].replace((ids+","),"")
                        row[4]=row[4].replace((","+ids),"")
                        row[4]=row[4].replace(ids,"")
                    if row[0] == ids:
                           lines.remove(row)
            
            with open('Data.csv', 'w',encoding='utf8', newline='') as writeFile:
            
                writer = csv.writer(writeFile)
            
                writer.writerows(lines)
                return _corsify_actual_response(jsonify("success"))
       #   id=str(request.form["id"])
        #  print(id,type(id))
         # response=model.recommendation(id)
          
      else:
          return "error"
   else:
      return "error"

@app.route('/update', methods = ['GET', 'POST'])
def update():
    
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      cols=["name","city","Followers","Follow","visited_places","contact_list","contact","Interest"]
      cols2=["Followers","Follow","visited_places","contact_list","Interest"]
      ids=request.form["id"]
      column=request.form["column"]
      value=request.form["value"]
      print("data a rha",ids)
      if request.form["id"]!="":
          
            lines=[]
            with open('./Data.csv',encoding='utf8') as readFile:
            
                reader = csv.reader(readFile)
            
                for row in reader:
                    
                    if row[0] == ids and column not in cols2:
                           print("index",cols.index(column))
                           row[(cols.index(column)+1)]=value
                           print("row",row)
                    elif row[0] == ids and column in cols2:
                        if row[(cols.index(column)+1)]=="":
                            row[(cols.index(column)+1)]="["+value+"]"
                        elif value not in row[(cols.index(column)+1)]:
                            row[(cols.index(column)+1)]=row[(cols.index(column)+1)].replace("]","")
                            row[(cols.index(column)+1)]=(row[(cols.index(column)+1)]+","+value+"]")
                        print("row",row)
                    lines.append(row)
            with open('./Data.csv', 'w',encoding='utf8', newline='') as writeFile:
            
                writer = csv.writer(writeFile)
            
                writer.writerows(lines)
                return _corsify_actual_response(jsonify("success"))
       #   id=str(request.form["id"])
        #  print(id,type(id))
         # response=model.recommendation(id)
          
      else:
          return "error"
   else:
      return "error"
  
@app.route('/remove', methods = ['GET', 'POST'])
def remove():
    
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      cols=["name","city","Followers","Follow","visited_places","contact_list","contact","Interest"]
      cols2=["Followers","Follow","visited_places","contact_list","Interest"]
      ids=request.form["id"]
      column=request.form["column"]
      value=request.form["value"]
      print("data a rha",ids)
      if request.form["id"]!="":
            if column in cols2:
                lines=[]
                with open('./Data.csv',encoding='utf8') as readFile:
                
                    reader = csv.reader(readFile)
                
                    for row in reader:
                        
                
                        if row[0] == ids and column in cols2:
                            if row[(cols.index(column)+1)]=="":
                                pass
                            elif value in row[(cols.index(column)+1)]:
                                row[(cols.index(column)+1)]=row[(cols.index(column)+1)].replace((","+value),"")
                                row[(cols.index(column)+1)]=row[(cols.index(column)+1)].replace((value+","),"")
                                row[(cols.index(column)+1)]=row[(cols.index(column)+1)].replace(value,"")
                                row[(cols.index(column)+1)]=row[(cols.index(column)+1)].replace("[]","")
                            print("row",row)
                        lines.append(row)
                with open('./Data.csv', 'w',encoding='utf8', newline='') as writeFile:
                
                    writer = csv.writer(writeFile)
                
                    writer.writerows(lines)
                    return _corsify_actual_response(jsonify("success"))
            else:
                return _corsify_actual_response(jsonify("error"))
       #   id=str(request.form["id"])
        #  print(id,type(id))
         # response=model.recommendation(id)
          
      else:
          return "error"
   else:
      return "error"
  
@app.route('/getnewsfeed', methods = ['GET', 'POST'])
def replace_file():
    
   #print("coming",request)
   if request.method == "OPTIONS": # CORS preflight
        print("optionho")
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      data = request.form["typ"]
      print("coming",data)
      #typ="News"
      response=model.newsfeed(data)
      return _corsify_actual_response(jsonify(response))
   else:
      return "error"
@app.route('/addnewsfeed', methods = ['GET', 'POST'])
def add_news():
    
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      
      row=[]
      row.append(request.form["id"])
      row.append(request.form["NewsFeed"])
      row.append(request.form["Type"])
      print("data a rha",row)
      if request.form["id"]!="":
          
          with open("./NewsFeed.csv",encoding='utf8', mode='a+', newline='') as Data:
                employee_writer = csv.writer(Data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow(row)
                return _corsify_actual_response(jsonify("success"))
       #   id=str(request.form["id"])
        #  print(id,type(id))
         # response=model.recommendation(id)
          
      else:
          return "error"
   else:
      return "error"
  
@app.route('/deletenewsfeed', methods = ['GET', 'POST'])
def delete_news():
    
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      
      ids=request.form["id"]
    
      print("data a rha",ids)
      if request.form["id"]!="":
          
            lines=[]
            with open('./NewsFeed.csv',encoding='utf8') as readFile:
            
                reader = csv.reader(readFile)
            
                for row in reader:
                    lines.append(row)
                    print(row)
                  
                    if row[0] == ids:
                           lines.remove(row)
            
            with open('./NewsFeed.csv', 'w',encoding='utf8', newline='') as writeFile:
            
                writer = csv.writer(writeFile)
            
                writer.writerows(lines)
                return _corsify_actual_response(jsonify("success"))
       #   id=str(request.form["id"])
        #  print(id,type(id))
         # response=model.recommendation(id)
          
      else:
          return "error"
   else:
      return "error"
def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    #response.headers.add('Access-Control-Allow-Headers', "*")
    #response.headers.add('Access-Control-Allow-Methods', "*")
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port = 3000, threaded=True,debug=True, use_reloader=True)