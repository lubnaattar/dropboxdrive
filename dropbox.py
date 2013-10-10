from flask import render_template
from flask import request
import urllib2
import json
import dropbox

from flask import Flask
app = Flask(__name__)


@app.route('/login')
def input_page():
	return render_template('login.html') 

@app.route('/callback')
def callback():
	return render_template('callback_dropbox.html')


def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB','TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
	
@app.route('/access_token')
def db_accessToken():
	token = request.args.get('token','')	
	print token
	raw_data = urllib2.urlopen("https://api.dropbox.com/1/account/info?access_token=%s" % token).read()
	data = json.loads(raw_data)
	print data		
	quota=data["quota_info"]["quota"]
	print quota	
	
	
	#print "display Files **"
	#raw_data1 = urllib2.urlopen("https://api-content.dropbox.com/1/files/dropbox/access_token=%s" % token).read()
	#data1 = json.loads(raw_data1)
	#print "display Files"
	#print data1
	
	#raw_data1 = urllib2.urlopen("https://api.dropbox.com/1/metadata/sandbox/home?access_token=%s" % token).read()
	#data1 = json.loads(raw_data1)
	#print "this is metadata"
	#print data1	
	
	return render_template('view.html',user=data["display_name"], emailId=data["email"], quotaDisplay = sizeof_fmt(int(quota)))
	
	
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
