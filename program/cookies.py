from flask import Flask,make_response,request#To build a web application make_response for setting resopnse,request to get cookies
app=Flask(__name__)#constructor of flask class 
@app.route('/set')#To give the route for web browser
def setcookie():#To set cookies
	resp=make_response("setting cookies")#for setting cookies
	resp.set_cookie('framework','flask33') #setting flask as cookies
	return resp
@app.route('/get')
def getcookie():#To get Cookies
	framework=request.cookies.get('framework')#request for geeting cookies
	return 'The framework is'+framework#gives cookies as flask33

if __name__ == '__main__':#is name is exactly main?
		app.run()# To run the application