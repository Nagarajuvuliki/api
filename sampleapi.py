import json
import pprint
def senddata(url,data):
    import requests
    url=url
    data=data
    r=requests.post(url,json=data)
    return r
# IP="" #request.META.get("REMOTE_ADDR")
def sendapi():
    from datetime import datetime
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    url1="https://100003.pythonanywhere.com/eventcreation"
    data={"platformcode":"FB" ,"citycode":"101","daycode":"0",
                "dbcode":"pfm" ,"ip_address":"127.0.0.1",
                "login_id":"lav1","session_id":"new1",
                "processcode":"1","regional_time":time,
                "dowell_time":time,"location":"2244651",
                "objectcode":"1","instancecode":"10001","context":"rad",
                "document_id":"3003","rules":"some rules"
                }
    try :
        l=senddata(url1,data)
        print(l.text)
    except:
        print("server not found")
p="FB1010000000000000000000003003"
print(len(p))