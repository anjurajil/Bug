from flask import *
import pymysql as pymysql

bug = Flask(__name__)
bug.secret_key = "abc"
con = pymysql.connect(host="localhost", user="root", password="root", port=3306, db="bug_tracking", charset="utf8")
cmd = con.cursor()
import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect("/")
        return func()
    return secure_function



@bug.route('/')
def login():
    return render_template("BUGLOGIN.html")


@bug.route('/logincheck', methods=['post'])
def logincheck():
    user = request.form['textfield']
    psd = request.form['textfield2']
    cmd.execute("select * from `buglogin` where username='" + user + "' and password='" + psd + "'")
    result = cmd.fetchone()
    if result is None:
        return '''<script>alert("INVALID USERNAME AND PASSWORD");window.location='/'</script>'''
    elif result[3] == "admin":
        session['lid'] = result[0]
        return render_template('ADMINHOME.html')
    elif result[3] == "Developer":
        session['lid'] = result[0]
        return render_template('DEVELOPER HOMEPAGE.html')
    elif result[3] == "Tester":
        session['lid'] = result[0]
        return render_template('TESTER HOMEPAGE.html')
    elif result[3]=="pending":
        return '''<script>alert("REQUEST PENDING");window.location='/'</script>'''
    elif result[3]=="rejected":
        return '''<script>alert("SORRY YOU ARE REJECTED");window.location='/'</script>'''


@bug.route('/setproject')
def setproject():
    return render_template("PROJECTTYPE.html")


@bug.route('/project_setting', methods=['post'])
def project_setting():
    project = request.form['select']
    cmd.execute("insert into `project_type` values(null,'" + project + "')")
    con.commit()
    return '''<script>alert("SUBMITTED SUCCESSFULLY");window.location='/setproject'</script>'''


@bug.route('/signup')
def signup():
    return render_template("HOMEPAGE.html")


@bug.route('/register_dev')
def register_dev():
    return render_template("DEVELOPER REGISTRATION.html")


@bug.route('/developer_registration', methods=['post'])
def developer_registration():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    company = request.form['textarea']
    location = request.form['textfield4']
    qualification = request.form['textfield5']
    skills = request.form['textarea2']
    email = request.form['textfield7']
    contact = request.form['textfield8']
    user = request.form['textfield9']
    psw = request.form['textfield10']
    cmd.execute("insert into `buglogin` values(null,'" + user + "','" + psw + "','pending')")
    id = cmd.lastrowid
    cmd.execute(
        "insert into `developer_registration` values(null,'" + fname + "','" + lname + "','" + company + "','" + location + "','" + qualification + "','" + skills + "','" + email + "','" + contact + "','" + str(
            id) + "')")

    con.commit()
    return '''<script>alert("REGISTERED SUCCESSFULLY");window.location='/signup'</script>'''


@bug.route('/tester_reg')
def tester_reg():
    return render_template("TESTER REGISTRATION.html")


@bug.route('/viewprofile')
def viewprofile():
    id = session['lid']
    cmd.execute("select * from `developer_registration` where loginid='" + str(id) + "'")
    result = cmd.fetchall()
    return render_template("DEVELOPER VIEW.html", value=result)


@bug.route('/update')
def update():
    id = session['lid']
    cmd.execute("select * from `developer_registration` where loginid='" + str(id) + "'")
    result = cmd.fetchone()
    return render_template("DEVELOPER UPDATION.html", value=result)


@bug.route('/developer_updation', methods=['post'])
def developer_updation():
    id = session['lid']
    fname = request.form['textfield']
    lname = request.form['textfield2']
    company = request.form['textarea']
    location = request.form['textfield4']
    qualification = request.form['textfield5']
    skills = request.form['textarea2']
    email = request.form['textfield7']
    contact = request.form['textfield8']
    cmd.execute(
        "update developer_registration set `first_name`='" + fname + "',`last_name`='" + lname + "',`company_name`='" + company + "',`location`='" + location + "',`qualification`='" + qualification + "',`skills`='" + skills + "',`email`='" + email + "',`contact_number`='" + contact + "' where loginid='" + str(
            id) + "'")
    con.commit()
    return '''<script>alert("UPDATED  SUCCESSFULLY");window.location='/viewprofile'</script>'''


@bug.route('/testerhome')
def testerhome():
    return render_template("TESTER HOMEPAGE.html")


@bug.route('/tester_registration', methods=['post'])
def tester_registration():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    experience = request.form['select']
    skill = request.form['textarea']
    location = request.form['textfield5']
    email = request.form['textfield6']
    contact = request.form['textfield7']
    user = request.form['textfield8']
    psw = request.form['textfield9']
    cmd.execute("insert into buglogin values(null,'" + user + "','" + psw + "','pending')")
    id = cmd.lastrowid
    cmd.execute(
        "insert into `tester_registration` values(null,'" + fname + "','" + lname + "','" + experience + "','" + skill + "','" + location + "','" + email + "','" + contact + "','" + str(
            id) + "')")
    con.commit()
    return '''<script>alert("REGISTERED SUCCESSFULLY");window.location='/signup'</script>'''


@bug.route('/viewtester')
def viewtester():
    id = session['lid']
    cmd.execute("select * from `tester_registration` where loginid='" + str(id) + "'")
    result = cmd.fetchall()
    return render_template("TESTER VIEW.html", value=result)


@bug.route('/testerupdate')
def testerupdate():
    id = session['lid']
    cmd.execute("select * from `tester_registration` where loginid='" + str(id) + "'")
    result = cmd.fetchone()
    return render_template("TESTER UPDATION.html", value=result)


@bug.route('/testerupdation', methods=['post'])
def testerupdation():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    experience = request.form['textfield3']
    skill = request.form['textarea']
    location = request.form['textfield5']
    email = request.form['textfield6']
    contact = request.form['textfield7']
    cmd.execute(
        "update tester_registration set `first_name`='" + fname + "',`last_name`='" + lname + "',`experience_level`='" + experience + "',`skill`='" + skill + "',`location`='" + location + "',`email`='" + email + "',contact='" + contact + "'")
    con.commit()
    return '''<script>alert("UPDATED SUCCESSFULLY");window.location='/viewtester'</script>'''


@bug.route('/tester_payment')
def tester_payment():
    id = session['lid']
    cmd.execute("select * from `tester_registration` where loginid='" + str(id) + "'")
    result = cmd.fetchone()
    print(result)
    cmd.execute("select * from `project_type`")
    result1 = cmd.fetchall()
    return render_template("TESTER PAYMENT.html", value=result, value1=result1)


@bug.route('/tester_paymentinsert', methods=['post'])
def tester_paymentinsert():
    testerid=session['lid']
    project_type = request.form['select']
    amount = request.form['textfield3']
    cmd.execute("insert into `tester_payment` values(null,'"+str(testerid)+"','" + project_type + "','" + amount + "')")
    con.commit()
    return '''<script>alert("SUCCESSFULLY ADDED");window.location='/tester_payment'</script>'''


@bug.route('/developerconfirm')
def developerconfirm():
    cmd.execute("SELECT `developer_registration`.*,`buglogin`.`usertype`FROM`developer_registration`JOIN`buglogin`ON`buglogin`.`loginid`=`developer_registration`.`loginid ")
    result = cmd.fetchall()
    return render_template("DEVELOPER CONFIRMATION.html", value=result)


@bug.route('/devaccept')
def devaccept():
    id = request.args.get("id")
    cmd.execute("update `buglogin` set `usertype`='Developer' where `loginid`='" + str(id) + "'")
    con.commit()
    return '''<script>alert("SUCCESSFULLY ACCEPTED");window.location='/developerconfirm'</script>'''


@bug.route('/devreject')
def devreject():
    id = request.args.get("id")
    cmd.execute("update `buglogin` set `usertype`='rejected' where `loginid`='" + str(id) + "'")
    con.commit()
    return '''<script>alert("SUCCESSFULLY REJECTED");window.location='/developerconfirm'</script>'''


@bug.route('/testerconfirm')
def testerconfirm():
    cmd.execute("select `tester_registration`.*,`buglogin`.`usertype`from `tester_registration`join `buglogin`on`buglogin`.`loginid`=`tester_registration`.`loginid`")
    result = cmd.fetchall()
    return render_template("TESTER CONFIRMATION.html", value=result)


@bug.route('/testaccept')
def testaccept():
    id = request.args.get("id")
    cmd.execute("update `buglogin` set usertype='Tester' where `loginid`='" + str(id) + "'")
    con.commit()
    return '''<script>alert("SUCCESSFULLY ACCEPTED");window.location='/testerconfirm'</script>'''


@bug.route('/testreject')
def testreject():
    id = request.args.get("id")
    cmd.execute("update `buglogin` set usertype='rejected' where `loginid`='" + str(id) + "'")
    con.commit()
    return '''<script>alert("SUCCESSFULLY REJECTED");window.location='/testerconfirm'</script>'''


@bug.route('/developertesterview')
def developertesterview():
    cmd.execute("select `tester_registration`.*from`tester_registration`join`buglogin`on`buglogin`.`loginid`=`tester_registration`.`loginid`where`buglogin`.`usertype`='Tester' ")
    result = cmd.fetchall()
    return render_template("DEVELOPER TESTER VIEW.html", value=result)


@bug.route('/sendrequest')
def sendrequest():
    tester_id = request.args.get("id")
    session['tid'] = tester_id
    cmd.execute("select * from `tester_registration`  where loginid='" + tester_id + "'")
    result = cmd.fetchone()
    cmd.execute("select * from `project_type`")
    result1 = cmd.fetchall()
    return render_template("PROJECTTEST REQUEST.html", value=result, value1=result1)


@bug.route('/projecttestrequest', methods=['post'])
def projecttestrequest():
    devid = session['lid']
    testerid = session['tid']
    projecttype = request.form['select']
    projectname = request.form['textfield2']
    description = request.form['textarea']
    date = request.form['textfield3']
    cmd.execute("insert into `project_test_request` values(null,'" + str(devid) + "','" + str(
        testerid) + "','" + projecttype + "','" + projectname + "','" + description + "','" + date + "','pending',null)")
    con.commit()
    return '''<script>alert("REQUEST SEND SUCCESSFULLY");window.location='/developertesterview'</script>'''


@bug.route('/project_testrequest_confirmation')
def project_testrequest_confirmation():
    logid = session['lid']
    cmd.execute("SELECT `project_test_request`.*,`developer_registration`.`first_name`,`developer_registration`.`last_name`,`project_type`.`project_type` FROM `project_test_request` JOIN `developer_registration` ON `developer_registration`.`loginid`=`project_test_request`.`developer_id` JOIN `project_type` ON `project_type`.`projecttypeid`=`project_test_request`.`projecttype_id` WHERE `project_test_request`.`tester_id`='"+str(logid)+"'")
    result = cmd.fetchall()
    print(result)
    return render_template("PROJECT TEST REQUEST CONFIRMATION.html", value=result)
@bug.route('/acceptrequest')
def acceptrequest():
    id=request.args.get("project_test_request_id")
    cmd.execute("update `project_test_request` set request_status='accepted' where project_test_request_id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("REQUEST ACCEPTED SUCCESSFULLY");window.location='/project_testrequest_confirmation'</script> '''
@bug.route('/rejectrequest')
def rejectrequest():
    id=request.args.get("project_test_request_id")
    cmd.execute("update `project_test_request` set request_status='rejected' where `project_test_request_id`='"+id+"'")
    con.commit()
    return '''<script>alert("REQUEST REJECTED SUCCESSFULLY");window.location='/project_testrequest_confirmation'</script> '''


@bug.route('/project_test_details')
def project_test_details():
    cmd.execute("select * from `project_test_request`")
    result = cmd.fetchall()
    print(result)
    return render_template("PROJECT TEST DETAILS.html",value=result)
@bug.route('/senddetails',methods=['post'])
def senddetails():
    name = request.form['select']
    desp=request.form['textarea']
    cmd.execute("insert into `project_test_details`values(null,'"+name+"','"+desp+"')")
    con.commit()
    return '''<script>alert("successfully submitted");window.location='/testerhome'</script>'''
@bug.route('/viewdetails')
def viewdetails():
    lid=session['lid']
    cmd.execute("SELECT `tester_registration`.`first_name`,`tester_registration`.`last_name`,`project_test_request`.`project_name`,`project_test_details`.`test_details`FROM`tester_registration`JOIN`project_test_request`ON`project_test_request`.`tester_id`=`tester_registration`.`loginid`JOIN`project_test_details`ON`project_test_details`.`project_test_request_id`=`project_test_request`.`project_test_request_id`where`project_test_request`.`developer_id`='"+str(lid)+"'")
    result=cmd.fetchall()
    return render_template("VIEWTESTDETAILS.html",value=result)
@bug.route('/teststatus')
def teststatus():
    cmd.execute("select * from `project_test_request`")
    result=cmd.fetchall()
    print(result)
    return render_template("PROJECT TEST STATUS.html",value=result)
@bug.route('/teststatusupload',methods=['post'])
def teststatusupload():
    id=request.form['select']
    print(id)
    status=request.form['select2']
    print(status)
    session['pid']=id
    print( session['pid'])
    cmd.execute("update `project_test_request` set `project_test_status`='"+status+"' where project_test_request_id='"+id+"'")
    con.commit()
    return '''<script>alert("successfully submitted");window.location='/teststatus'</script>'''
@bug.route('/viewstatus')
def viewstatus():
    lid=session['lid']
    cmd.execute("select `tester_registration`.`first_name`,`tester_registration`.`last_name`,`project_test_request`.`project_name`,`project_test_request`.`project_test_status`from`tester_registration`join`project_test_request`on`project_test_request`.`tester_id`=`tester_registration`.`loginid`where`project_test_request`.`developer_id`='"+str(lid)+"' and `request_status`='accepted'")
    result=cmd.fetchall()
    return render_template("PROJECTSTATUSVIEW.html",value=result)
@bug.route('/viewtester_payment')
def viewtester_payment():

    cmd.execute("select `tester_registration`.`first_name`,`tester_registration`.`last_name`,`project_type`.`project_type`,`tester_payment`.`payment`from`tester_registration`join`tester_payment`on`tester_payment`.`testerid`=`tester_registration`.`loginid`join`project_type`on`project_type`.`projecttypeid`=`tester_payment`.`projecttypeid`")
    result=cmd.fetchall()
    return render_template("TESTER PAYMENT VIEW.html",value=result)


@bug.route('/logout')
def logout():
    session.clear()
    return redirect('/')












bug.run(debug=True)
