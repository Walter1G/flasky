from flask import Flask, request, make_response, redirect, abort, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)

bootstrap = Bootstrap(app) 


# @app.route('/')
# def index():
#     user_agent =request.headers.get('user-Agent')
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     # print(user_agent)
#     # return '<p>Your browser is {}</p>'.format(user_agent)
#     # response.set_cookie('answer','42')
#     # return response
#     return redirect('http://www.example.com')

# @app.route('/user/<name>')
# def user(name):
#  return '<h1>Hello, {}!</h1>'.format(name)

# @app.route('/user/<id>')
# def get_user(id):
#  user = load_user(id)
#  if not user:
#     abort(404)
#  return '<h1>Hello, {}</h1>'.format(user.name)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
