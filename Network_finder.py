import requests
#url = "http://www.naver.com"
i = 0
addr = "http://192.168.0."
while 1:
    addrl = str(i)
    i =+ 1
    url = addr + addrl
    response = requests.get(url = url)
    status = response.status_code
    if(status == 200):
        print(url)
        break
    print(status)
