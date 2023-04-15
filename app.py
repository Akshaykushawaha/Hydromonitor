from flask import Flask, request, jsonify
from datacl import get_azure_data,len_of_excel,write_to_excel,getdata


app = Flask("__name__")

@app.route('/fdata')
def fdata_func():
    row = get_azure_data()
    len_excel = len_of_excel()
    
    write_to_excel(len_excel,row)
    upd_time=getdata("time")
    d={}
    d["val"] = upd_time
    return jsonify(d)

@app.route('/odata',methods=['GET'])
def odata_func():
    upd_time=getdata(str(request.args["sensor"]))
    d={}
    d["val"] = upd_time
    return jsonify(d)


if __name__=="__main__":
    app.run(port=32)
    