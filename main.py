from ast import pattern
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import request 
# from flask_mysqldb import MySQL
import mysql.connector

application = Flask(__name__)

def getMysqlConnection():          # taro di bawah application = Flask(__name__)
  return mysql.connector.connect(user='root', host='localhost', port='3306', password='', database='hospital') # x ganti pake nama databasenya

#LandingPage
@application.route('/')
@application.route('/Home/')
def Home():
    return render_template('LandingPage.html',judul='LandingPage')

  #login  
# @application.route('/login/')
# def login():
#      return render_template('login.html',judul='login')
   
   #Dashboard
@application.route('/Dashboard2')
def Dashboard():
     return render_template('Dashboard2.html',judul='Dashboard')

@application.route('/cobaDB')    # taro di bawah fungsi index, nama route sesuain aja
def cobaDB():                    # nama fungsi sesuain aja
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from dokter" # x ganti pake nama tabelnya
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('cobaDB.html',kalimat=output_json) # nama file html sesuain aja

    #Dashboard
# @application.route('/cobaDB')
# def cobaDB():
#      return render_template('cobaDB.html',judul='cobaDB')

@application.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'GET':
        return render_template('insert.html')
    elif request.method == 'POST':
        id_dokter = request.form['id_dokter']
        nama_dokter = request.form['nama_dokter']
        spesialis = request.form['spesialis']
        no_telp = request.form['telp']
        alamat = request.form['alamat']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data berhasil ditambahkan."
            sqlstr = "INSERT INTO `dokter` (`id_dokter`,`nama_dokter`,`spesialis`,`no_telp`,`alamat`) VALUES ("+id_dokter+", '"+nama_dokter+"', '"+spesialis+"', '"+no_telp+"','"+alamat+"');"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('cobaDB'))
    else:
        return render_template('insert.html')

@application.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data berhasil ditambahkan."
            sqlstr = "DELETE FROM dokter WHERE id_dokter = '"+str(id)+"';"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('cobaDB'))
    return redirect(url_for('cobaDB'))

@application.route('/login', methods=['GET', 'POST'])
def login():
    db = getMysqlConnection()
    # try:
    #     cur = db.cursor()
    #     sukses = "Data berhasil ditambahkan."
    #     sqlstr = "SELECT * from user"
    #     print(sqlstr)
    #     cur.execute(sqlstr)
    #     output_json = cur.fetchall()
    #     print(output_json)
    #     db.commit()
    #     cur.close()
    # except Exception as e:
    #     print("Error in SQL:\n", e)
    # finally:
    #     db.close()

    if request.method == 'GET':
        return render_template('login.html')	
    elif request.method =='POST':
        user = request.form['user']			
        passwd = request.form['passwd']		
        print(passwd)

        cur = db.cursor()
        sukses = "Data berhasil ditambahkan."
        sqlstr = f"SELECT * from user where Username = '{user}'"
        cur.execute(sqlstr)
        output_json = cur.fetchone()
        print(output_json)
        cur.close()
       

        if user == output_json[0]:
            if passwd == str(output_json[1]):
                return redirect(url_for('cobaDB'))
        
        return render_template('login.html')
        # for kolom in output_json:
        #     for i in range(len(kolom)):
        #         if str(user) == kolom[i]:
        #             print("username sama")
        #             if str(passwd) == kolom[i+1]:
        #                 print(kolom[i+1])
        #                 print("password sama")
        #                 return redirect(url_for('cobaDB'))
        #             else:
        #                 break

    
@application.route('/dokter')    # taro di bawah fungsi index, nama route sesuain aja
def dokter():                    # nama fungsi sesuain aja
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from dokter" # x ganti pake nama tabelnya
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('dokter.html',kalimat=output_json) # nama file html sesuain aja

@application.route('/kamar')    # taro di bawah fungsi index, nama route sesuain aja
def kamar():                    # nama fungsi sesuain aja
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from kamar" # x ganti pake nama tabelnya
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('kamar.html',kalimat=output_json) # nama file html sesuain aja

@application.route('/obat')    # taro di bawah fungsi index, nama route sesuain aja
def obat():                    # nama fungsi sesuain aja
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from obat" # x ganti pake nama tabelnya
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('obat.html',kalimat=output_json) # nama file html sesuain aja

@application.route('/pasien')    # taro di bawah fungsi index, nama route sesuain aja
def pasien():                    # nama fungsi sesuain aja
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from pasien" # x ganti pake nama tabelnya
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('pasien.html',kalimat=output_json) # nama file html sesuain aja

@application.route('/perawat')    # taro di bawah fungsi index, nama route sesuain aja
def perawat():                    # nama fungsi sesuain aja
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from perawat" # x ganti pake nama tabelnya
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('perawat.html',kalimat=output_json) # nama file html sesuain aja

@application.route('/rekammedis')    # taro di bawah fungsi index, nama route sesuain aja
def rekammedis():                    # nama fungsi sesuain aja
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from rekam_medis" # x ganti pake nama tabelnya
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('rekammedis.html',kalimat=output_json) # nama file html sesuain aja

if __name__ == '__main__':
    application.run(debug=True)