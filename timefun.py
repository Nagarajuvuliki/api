def senddata(url,data):
    import requests
    url=url
    data=data
    r=requests.post(url,json=data)
    return r
def sendapi():
    url="https://100003.pythonanywhere.com/timefun"
    data={"value":1003,"object":"obj_id","rules":"rule_id","login":"Nagaraju"}
    try :
        l=senddata(url,data)
        print(l.text)
    except:
        print("server not found")
sendapi()
