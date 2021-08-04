from flask import Flask, redirect, url_for, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

#DB config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'YourPassWordHere'
app.config['MYSQL_DB'] = 'proj1'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/insurance", methods=['GET', 'POST'])
def insurance():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Add':
            Details = request.form
            one = Details['INS_Code']
            two = Details['Name']
            three = Details['Address'] 
            four = Details['City'] 
            five = Details['State']
            six = Details['Zip']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO ins(INS_code,Insurance_Name,Address,City,State,Zipcode) VALUES(%s,%s,%s,%s,%s,%s)",(one,two,three,four,five,six))
            mysql.connection.commit()
            return 'Success'
        elif request.form['submit_button'] == 'Delete':
            Details = request.form
            one = Details['INS_Code']
            cur = mysql.connection.cursor()
            cur.execute(f"DELETE FROM ins WHERE INS_Code = '{one}'")
            mysql.connection.commit()
            return 'Success'
        elif request.form['submit_button'] == 'Query':
            Details = request.form
            one = Details['INS_Code']
            cur = mysql.connection.cursor()
            data = cur.execute(f"SELECT * FROM ins WHERE INS_Code = '{one}'")
            if data > 0:
                data2 = cur.fetchall()
                return render_template('insurance_Result.html', data2 = data2)
            else:
                return 'data not exist?'
        elif request.form['submit_button'] == 'Report':
            return render_template("insuranceRP.html")
        elif request.form['submit_button'] == 'Exit':
            return render_template("index.html")
        else: 
            return 'lol we confused, go back to homepage quick'
    else:
        return render_template("insurance.html")
    
  
@app.route("/patient", methods=['GET', 'POST'])
def patient():
        if request.method == 'POST':
            if request.form['submit_button'] == 'Add':
                Details = request.form
                one = Details['P_Code']
                two = Details['P_Name']
                three = Details['INS_Code'] 
                four = Details['P_Address']
                five = Details['P_Address2']  
                six = Details['P_City']
                seven = Details['P_State']
                eight = Details['P_Zip']
                cur = mysql.connection.cursor()
                print(one,two,three,four,five,six,seven,eight)
                cur.execute("INSERT INTO patients(Code,Name,INS_Company_Code,Address_line_1,Address_line_2,City,State,Zip) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(one,two,three,four,five,six,seven,eight))
                mysql.connection.commit()
                return 'Success'
            elif request.form['submit_button'] == 'Delete':
                Details = request.form
                one = Details['P_Code']
                cur = mysql.connection.cursor()
                cur.execute(f"DELETE FROM patients WHERE Code = '{one}'")
                mysql.connection.commit()
                return 'Success'
            elif request.form['submit_button'] == 'Query':
                Details = request.form
                one = Details['P_Code']
                cur = mysql.connection.cursor()
                data = cur.execute(f"SELECT * FROM patients WHERE Code = '{one}'")
                if data > 0:
                    data2 = cur.fetchall()
                    return render_template('patient_Result.html', data2 = data2)
                else:
                    return 'data not exist?'
            elif request.form['submit_button'] == 'Report':
                return render_template('patientRP.html')
            elif request.form['submit_button'] == 'Exit':
                return render_template("index.html")     
            else:
                return 'lol we confused, go back to homepage quick'
                
        else:
            return render_template("patient.html")

@app.route("/doctors", methods=['GET', 'POST'])
def doctors():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Add':
            Details = request.form
            one = Details['MD_Code']
            two = Details['MD_Name']
            three = Details['MD_Address'] 
            four = Details['MD_City'] 
            five = Details['MD_State']
            six = Details['MD_Zip']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO mds(Code,Name,Address,City,State,Zipcode) VALUES(%s,%s,%s,%s,%s,%s)",(one,two,three,four,five,six))
            mysql.connection.commit()
            return 'Success'
        elif request.form['submit_button'] == 'Delete':
            Details = request.form
            one = Details['MD_Code']
            cur = mysql.connection.cursor()
            cur.execute(f"DELETE FROM mds WHERE Code = '{one}'")
            mysql.connection.commit()
            return 'Success'
        elif request.form['submit_button'] == 'Query':
            Details = request.form
            one = Details['MD_Code']
            cur = mysql.connection.cursor()
            data = cur.execute(f"SELECT * FROM mds WHERE Code = '{one}'")
            if data > 0:
                data2 = cur.fetchall()
                return render_template('doctors_Result.html', data2 = data2)
            else:
                return 'data not exist?'
        elif request.form['submit_button'] == 'Report':
            return render_template('doctorRP.html')
        elif request.form['submit_button'] == 'Exit':
            return render_template("index.html")     
        else:
            return 'lol we confused, go back to homepage quick'
    return render_template("doctors.html")

@app.route("/treatments", methods=['GET', 'POST'])
def treatments():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Add':
            Details = request.form
            one = Details['ID']
            two = Details['P_Code']
            three = Details['MD_Code']
            four = Details['MP_Code'] 
            five = Details['DOT'] 
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO treatments(ID,Patient_code,MD_Code,MP_Code,Date_of_treatment) VALUES(%s,%s,%s,%s,%s)",(one,two,three,four,five))
            mysql.connection.commit()
            return 'Success'
        elif request.form['submit_button'] == 'Delete':
            Details = request.form
            one = Details['ID']
            cur = mysql.connection.cursor()
            cur.execute(f"DELETE FROM treatments WHERE ID = {one}")
            mysql.connection.commit()
            return 'Success'
        elif request.form['submit_button'] == 'Query':
            Details = request.form
            one = Details['ID']
            cur = mysql.connection.cursor()
            data = cur.execute(f"SELECT * FROM treatments WHERE ID = '{one}'")
            if data > 0:
                data2 = cur.fetchall()
                return render_template('treatment_Result.html', data2 = data2)
            else:
                return 'data not exist?'
        elif request.form['submit_button'] == 'Report':
            return render_template('treatmentRP.html')
        elif request.form['submit_button'] == 'Exit':
            return render_template("index.html")     
        else:
            return 'lol we confused, go back to homepage quick'
    return render_template("treatments.html")

@app.route("/medicalP", methods=['GET', 'POST'])
def medicalP():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Add':
            Details = request.form
            one = Details['MP_Code']
            two = Details['Description']
            three = Details['Price']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO medical(MP_Code,Description,Price) VALUES(%s,%s,%s)",(one,two,three))
            mysql.connection.commit()
            return 'Success'
        elif request.form['submit_button'] == 'Delete':
            Details = request.form
            one = Details['MP_Code']
            cur = mysql.connection.cursor()
            cur.execute(f"DELETE FROM medical WHERE MP_Code = '{one}'")
            mysql.connection.commit()
            return 'Success'
        elif request.form['submit_button'] == 'Query':
            Details = request.form
            one = Details['MP_Code']
            cur = mysql.connection.cursor()
            data = cur.execute(f"SELECT * FROM medical WHERE MP_Code = '{one}'")
            if data > 0:
                data2 = cur.fetchall()
                return render_template('medicalP_Result.html', data2 = data2)
            else:
                return 'data not exist?'
        elif request.form['submit_button'] == 'Exit':
            return render_template("index.html")                
        else: 
            return 'lol we confused, go back to homepage quick'
    else:
        return render_template("medicalP.html")

@app.route("/InsuranceRPPage2.html")
def insP2():
    return render_template("InsuranceRPPage2.html") 

@app.route("/patientRPPage2.html")
def patientP2():    
    return render_template("patientRPPage2.html")

@app.route("/DoctorRPPage2.html")
def doctorP2():
    return render_template("DoctorRPPage2.html")

@app.route("/treatmentRPPage2.html")
def treatmentP2():
    return render_template("treatmentRPPage2.html")

@app.route("/InsuranceRP.html")
def insP1():
    return render_template("InsuranceRP.html") 

@app.route("/patientRP.html")
def patientP1():    
    return render_template("patientRP.html")

@app.route("/DoctorRP.html")
def doctorP1():
    return render_template("DoctorRP.html")

@app.route("/treatmentRP.html")
def treatmentP1():
    return render_template("treatmentRP.html")

if __name__ == "__main__":
    app.run()

