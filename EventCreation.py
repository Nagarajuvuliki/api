from flask import Flask,request,session
from flask import render_template
from flask import url_for
from werkzeug.utils import redirect
from dowell import dowellconnection
from datetime import datetime
dd=datetime.now()
time=dd.strftime("%d:%m:%Y,%H:%M:%S")
import re
lav=Flask(__name__)
#get data from api
@lav.route('/events',methods =["GET", "POST"])
def api_data():
    if (request.method=="POST"):
        #define variables
        pfm_id=""
        city_id=""
        day_id=""
        db_id="01"
        process_id=""
        object_id=""
        #get data from api
        request_data=request.get_json()
        #platformcode define
        pfm_code = request_data['platformcode']
        pfm={"platformcode":pfm_code}
        pfm_response=dowellconnection("mstr","bangalore","mysql","platform_master","pfm_master","97654321","ABCDE","fetch",pfm,"nil")
        if not pfm_code in pfm_response or pfm_response=="false":
            return "Platform code not matching"
        else:
            #city_ID=re.findall('\d+',response)[0]
            pfm_id=pfm_code
        city_code = request_data['citycode']
        city={"citycode":city_code}
        city_response=dowellconnection("mstr","bangalore","mysql","city_master","city_master","67654321","ABCDE","fetch",city,"nil")
        if not city_code in city_response or city_response=="false":
            return "City code not matching"
        else:
            city_id=city_code
        day_code = request_data['daycode']
        day={"daycode":day_code}
        day_response=dowellconnection("mstr","bangalore","mysql","day_master","day_master","77654321","ABCDE","fetch",day,"nil")
        if not day_code in day_response or day_response=="false":
            return "day code not matching"
        else:
            day_id=day_code
        db_code = request_data['dbcode']
        db={"dbcode":db_code}
        db_response=dowellconnection("mstr","bangalore","mysql","db_master","db_master","37654321","ABCDE","fetch",db,"nil")
        if not db_code in db_response or db_response=="false":
           return "database code not matching"
        else:
            db_id=db_code
        process_code = request_data['processcode']
        process={"processcode":process_code}
        process_response=dowellconnection("mstr","bangalore","mysql","process_master","process_master","57654321","ABCDE","fetch",process,"nil")
        if not process_code in process_response or process_response=="false":
            return "process code not matching"
        else:
            process_id=process_code
        object_code = request_data['objectcode']
        object={"objectcode":object_code}
        object_response=dowellconnection("mstr","bangalore","mysql","object_master","object_master","47654321","ABCDE","fetch",object,"nil")
        if not object_code in object_response or object_response=="false":
            return "object code not matching"
        else:
            object_id=object_code
        instance=request_data["instancecode"]
        if not instance:
            return "Instance is blank fill again"
        else:
            instance_id=instance
        Context=list(request_data["context"])
        if not Context:
            return "Context is blank"
        else:
            context_is=list(request_data["context"])
        document=request_data["document_id"]
        if not document:
            return "Document is blank"
        else:
            if len(request_data["document_id"])>24:
                return "Invalid document id"
            elif len(request_data["document_id"])<24:
                document=document.zfill(24) # To fill prefix with zero to make length to 24
                document_id=document
        event_id=pfm_id+city_id+day_id+document_id
        if len(event_id) !=30:
            return "Error while creating Event ID"
        else:
            #ls=[pfm_id,city_code,day_id,db_id,request_data["IP_Address"],request_data["login"],request_data["session"],process_id,
            #request_data["regional_time"],request_data["dowell_time"],request_data["location"],object_id,instance_id,context,document_id]
            field = {"eventId":event_id ,
            "DatabaseId":db_id ,"IP":request_data["ip_address"],
            "login":request_data["login_id"],"session":request_data["session_id"],
            "process":process_id,"regional_time":request_data["regional_time"],
            "dowell_time":request_data["dowell_time"],"location":request_data["location"],
            "object":object_id,"instane_id":instance_id,"context": context_is}
            NewObjectID=dowellconnection("FB","bangalore","mongodb","events","events","87654321","ABCDE","insert",field,"nil")
            return f"NewObjectID : {NewObjectID} \n event_id :{event_id}"
    return "its work"
def timefun():
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    return time
@lav.route('/timefun',methods =["GET", "POST"])
def timefunc():
    if (request.method=="POST"):
        request_data=request.get_json()
        value = request_data['value']
        objects = request_data['object']
        rule = request_data['rules']
        login = request_data['login']
        if value and objects and rule and login:
            timer=timefun()
            field = {"somevalue":value,"modified date":timer,"objects":objects,"rule":rule,"login":login}
            #create=dowellconnection("FB","bangalore","mongodb","events","events","87654321","ABCDE","insert",field,"nil")
            return "data successfully sent"
        else:
            return "could not insert data into the database"
    return "it works"
if __name__=='__main__':
    lav.run(debug=True)
