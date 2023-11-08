def Requests(header_info,url):
    import requests
    Session=requests.Session()
    Session.headers.update(header_info)
    result=Session.get(url)
    if result.status_code!=200:
        return [result.status_code,result.reason]
    else:
        return result
    