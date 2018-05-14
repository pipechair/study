#coding:utf-8
from bottle import run,route,template,redirect,request,post
import sqlite3

@route("/")
def index():
    todo_list = get_todo()
    return template("index",todo_list=todo_list)

@route("/enter",method=["POST"])
def enter():
    todo=request.POST.getunicode("todo_list")
    #データベースにtodo_listを書き込む
    save_todo(todo)
    #return todo
    return redirect("/")

@route("/delete",method=["POST"])
def delete():

    conn=sqlite3.connect("todo.db")
    c=conn.cursor()

    delete="delete from todo_list where todo='{0}'".format(request.POST.getunicode("finished"))
    c.execute(delete)
    conn.commit()
    return redirect("/")

#データベースにtodo_listを保存
def save_todo(todo):
    conn= sqlite3.connect('todo.db')
    c= conn.cursor()
    insert="insert into todo_list(todo) values('{0}')".format(todo)
    c.execute(insert)
    conn.commit()

#データベースのtodo_listを読み込む
def get_todo():
    conn= sqlite3.connect('todo.db')
    c= conn.cursor()
    select="select * from todo_list"
    c.execute(select)
    row = c.fetchall()
    return row
run(host="localhost",port=8080,debug=True,reloader=True)
