from crud_app import app
from flask import render_template,redirect,request,session
from crud_app.models.user import User


@app.route('/')
def index():
    users = User.show_users()
    print(users)
    return render_template('index.html', users=users)

@app.route('/user/new')
def new():
    return render_template('new.html')

@app.route('/create' ,methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/')

@app.route('/user/show/<int:id>')
def show_user(id):
    form ={
        "id":id
    }
    return render_template('info.html', user = User.show_user(form))

@app.route('/user/edit/<int:id>')
def edit(id):
    form = {
        "id":id
    }
    user = User.show_user(form)
    return render_template('edit.html' , user = user)

@app.route('/user/update', methods=['POST'])
def update():
    User.update_user(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    form = {
        "id":id
    }
    User.delete_user(form)
    return redirect('/')