from flask import Flask, request, jsonify
from datacl import get_azure_data,len_of_excel,write_to_excel,getdata


app = Flask("__name__")

@app.route('/fdata')
def fdata_func():                       # full data refresh
    row = get_azure_data()              # get data from azure in a row
    len_excel = len_of_excel()          # get number of last row in excel
    if (row!=[]):                       # check if data was avaialabe from azure
        write_to_excel(len_excel,row)   # updating excel
    upd_time=getdata("time")            # getting last upadte time from excel
    d={}
    d["val"] = upd_time                 # saving it in dict
    return jsonify(d)                   # returning the value

@app.route('/odata',methods=['GET'])
def odata_func():                                  #only data fetch
    upd_time=getdata(str(request.args["sensor"]))  # getting last upadte value of that sensor from excel
    d={}
    d["val"] = upd_time
    return jsonify(d)


if __name__=="__main__":
    app.run(port=32)
