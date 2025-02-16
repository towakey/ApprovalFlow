#!python
# -*- coding: utf-8 -*-

import os
import io
import sys
import datetime
import configparser
import cgi
import cgitb
import uuid
import shutil
import re


app_name = "ApprovalFlow"

str_code = "utf-8"

permission = 0o764



if 'REQUEST_URI' in os.environ:
    REQUEST_URL = os.environ['REQUEST_URI']
else:
    # IIS用
    REQUEST_URL = os.environ['PATH_INFO']

cgitb.enable(display=1, logdir=None, context=5, format='html')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
form = cgi.FieldStorage()
mode = form.getfirst("mode", '')

def header():
    print(f"""
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="./css/bootstrap.css">
        <script src="./js/bootstrap.bundle.js"></script>
        <title>{app_name}</title>
    </head>
    <body>
""")

def footer():
    print("""
        </div>
    </body>
</html>
""")

def nav():
    print(f"""
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="./index.py">{app_name}</a>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="./index.py?mode=create">新規作成</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
""")

if __name__ == "__main__":
    print("Content-Type: text/html; charset=UTF-8\r\n")
    if mode == '':
        header()
        nav()
        print(f"""
        <div class="container">
            <h1 class="my-4">承認システム</h1>
            <div class="card">
                <div class="card-body">
                    <div class="card-text">
                        
                    </div>
                </div>
            </div>
""")
        footer()

    elif mode == 'create':
        header()
        nav()
        print(f"""
        <div class="container">
            <form action="./index.py" method="POST">
                <input type="hidden" name="mode" value="create"/>
                <h1 class="my-4">新規作成</h1>
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">
                            <input type="text" name="create_task_name"/>
                        </h5>
                        <div class="card-text">
                            
                        </div>
                    </div>
                </div>
            </form>
        </div>
""")
        footer()
        footer()

