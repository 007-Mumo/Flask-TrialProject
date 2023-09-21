from flask import Flask, redirect, url_for, request,render_template,make_response,session, redirect, url_for
from flask import markupsafe_escape
app = Flask(__name__)
app.secret_key = "mumo"


#@app.route('/hello')
#def zello_world():
# return "hello MUMO"


#@app.route('/')
#def hello_world():
#   return "hello world"


#def hello_world():
 #  return "hello MUMO AVENGED"
#app.add_url_rule("/", "hello", hello_world)



#@app.route('/hello/<name>')
#def hello_name(name):
#   return "Hello %s!" % name

#@app.route('/blog/<int:postID>')
#def show_blog(postID):
#   return 'Blog Number %d' % postID

#@app.route('/rev/<float:revNo>')
#def revision(revNo):
#   return 'Revision Number %f' % revNo

#@app.route('/flask')
#def hello_flask():
#   return 'Hello Flask'

#@app.route('/python/')
#def hello_python():
#   return 'Hello Python'

#@app.route('/admin')
#def hello_admin():
#   return 'Hello Admin'

#@app.route('/guest/<guest>')
#def hello_guest(guest):
#   return 'Hello %s as Guest' % guest

#@app.route('/user/<name>')
#def hello_user(name):
#   if name =='admin':
#     return redirect(url_for('hello_admin'))
   
#  else:
      
#      return redirect(url_for('hello_guest',guest = name))

#@app.route('/success/<name>')
#def success(name):
#   return 'welcome %s' % name

#@app.route('/login',methods = ['POST', 'GET'])
#def login():
#   if request.method == 'POST':
#      user = request.form['nm']
#      return redirect(url_for('success',name = user))
#   else:
#      user = request.args.get('nm')
#      return redirect(url_for('success',name = user))


@app.route('/')
def student():
   return render_template('student.html')



@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template('result.html',result = result)
   #else:
    #  result = request.form
     # return render_template('result.html',result = result)

@app.route('/indexing')
def index():
   return render_template('index1.html')


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    user = request.form['nm']
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

@app.route('/trial')
def index2():
   return render_template ('hello.html')


@app.route("/index")
def index1():
   return render_template("index.html")


@app.route('/LOG')
def index3():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route('/lOG-in', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username/></p>
      <p<<input type = submit value = Login/></p>
   </form>
	
   '''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))





if __name__ == '__main__':
   app.run(debug=True)

#app.debug = True
#app.run()
#pp.run(debug = True)