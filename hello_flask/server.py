from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)    
app.secret_key= "i love pickles"

@app.route('/')          
def hello_world():
    # my_list= [ 10, 23, {"name":"john", "age": 34}]

    all_users= ["john", "cara", "jamie"]

    logged_in_user= "Martha"

    return  render_template('index.html', all_users=all_users, current_user=logged_in_user)

@app.route('/register')
def register_form():
    return render_template('user_form.html')

@app.route('/process_user', methods=['POST'])
def process_user():
    # print(f'the request.form is {request.form}')
    session['first_name']= request.form['f_name']
    session['last_name']= request.form['l_name']
    session['email']= request.form['email']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/success')

if __name__=="__main__":   
    app.run(debug=True)   
