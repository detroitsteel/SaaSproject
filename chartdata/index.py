from flask import Flask, jsonify, request, json
import chartdata.dbconnect as db
import chartdata.getsumdata as gq
import chartdata.getsumpandata as gp
import chartdata.getchartdataparmcsv as gc

app = Flask(__name__)

database = r"./randomized_chart_data.sqlite"
#database = r"/home/kxa/ChlBuild/data/randomized_chart_data.sqlite"

@app.route('/smdataqu')
def get_smdataqu():
  with app.app_context():
    conn = db.create_connection(database)
    qrpdta = gq.getsumquery(conn)
  return qrpdta

@app.route('/smdatapd')
def get_smdatapd():
  conn = db.create_connection(database)
  pdpdta = gp.getsumquery(conn)
  return pdpdta

@app.route('/chartdatacsvpost/<path:csvpath>')
def chartdatacsvpost(csvpath):
  conn = db.create_connection(database)
  cl1 = '/'
  cl1 = cl1 + csvpath #Path('home/kxa/PycharmProjects/Chl1Build/idlist.csv')
  rptdta = gc.getdataquery(conn, cl1)
  return rptdta
