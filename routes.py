from application import app
from flask import render_template,request
from flask_mysqldb import MySQL

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'practice_initiative_management'

@app.route("/")
@app.route('/project')
def project():
    if request.method == "GET":
        details = request.args.get
        #proj_id = details('proj_id')
        #proj_name = details('proj_name')
        #client_name = details('client_name')
        #proj_start = details('proj_start')
        #proj_end = details('proj_end')
        #proj_status = details('proj_status')
        #proj_skills = details('proj_skills')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM project")
        projdata = cur.fetchall()
        count = len(projdata)
        for x in projdata:
            print(x)
        mysql.connection.commit()
        cur.close()
        return render_template('project.html',projdata = projdata, count = count)