from flask import Flask, jsonify, redirect, url_for, request
from flask.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user 

'''
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# config
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)
'''

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

set_pass='123'
set_user='pepe'

@app.route('/login', methods = ['POST', 'GET'])
def login():
    render_template('login.html')
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']        
        if password == set_pass and username == set_user:
            return redirect(url_for('/'))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


@app.route('/')
@login_required
def calculadora():
    return render_template('calculadora.html')

@app.route('/suma/<op1>/<op2>', methods = ['POST', 'GET'])
@login_required
def suma(op1, op2):
    n_op1 = float(op1)
    n_op2 = float(op2)

    resultat = {'operador': 'suma', 'resultat': str(n_op1 + n_op2)}
    return jsonify(resultat), 200

@app.route('/resta/<op1>/<op2>')
@login_required
def resta(op1, op2):
    n_op1 = float(op1)
    n_op2 = float(op2)

    resultat = {'operador': 'resta', 'resultat': n_op1 - n_op2}
    return jsonify(resultat), 200

@app.route('/multiplicacio/<op1>/<op2>')
@login_required
def multiplicacio(op1, op2):
    n_op1 = float(op1)
    n_op2 = float(op2)

    resultat = {'operador': 'multiplicacio', 'resultat': n_op1 * n_op2}
    return jsonify(resultat), 200

@app.route('/divisio/<op1>/<op2>')
@login_required
def divisio(op1, op2):
    n_op1 = float(op1)
    n_op2 = float(op2)

    resultat = {'operador': 'divisio', 'resultat': n_op1 / n_op2}
    return jsonify(resultat), 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port='5000')
