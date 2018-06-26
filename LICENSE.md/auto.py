import requests
import csv
from lxml import etree
import time


def getreferer(s, url, headers):
    res = s.get(url=url, headers=headers)
    if res.status_code == 200:
        s.headers['Referer'] = response.url
    return res


main_url = 'https://website/'
login_url = 'https://website/takelogin.php'

s = requests.Session()
s.headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

login_headers = {}
# login_headers[':authority'] = 'website'
# login_headers[':method'] = 'POST'
# login_headers[':path'] = '/takelogin.php'
# login_headers[':scheme'] = 'https'
login_headers['upgrade-insecure-requests'] = '1'

login_data = {
    'username': '',  ## 账号
    'password': '',  ## 密码
}

conp = s.post(url=login_url, data=login_data, headers=login_headers)
# print(conp.text)

startid = 2250;
endid = 3250;
base_url = 'https://website/details.php?id='
end_url = '&hit=1&cmtpage=1'

idheaders = {}
# idheaders[':authority'] = 'website'
# idheaders[':method'] = 'POST'
# idheaders[':path'] = '/comment.php?action=add&type=torrent'
# idheaders[':scheme'] = 'https'
idheaders['content-type'] = 'application/x-www-form-urlencoded'
idheaders['origin'] = 'https://website'
idheaders['upgrade-insecure-requests'] = '1'
# idheaders[''] = ''

iddata = {
    'pid': '',
    'body': '非常感谢发布',
}

for tmpid in range(startid, endid):
    id_url = base_url + str(tmpid) + end_url
    idres = s.get(url=id_url)
    blidcont = etree.HTML(idres.text).xpath('//input[@id="qr"]')
    print(id_url)
    if len(blidcont):
        idheaders['referer'] = id_url
        iddata['pid'] = tmpid
        eleidres = s.post(url='https://website/comment.php?action=add&type=torrent', headers=idheaders, data=iddata)
        if eleidres.status_code == 200:
            print(str(tmpid) + ' : ' + id_url + " success")
            time.sleep(17)
        else:
            print(str(tmpid) + ' : ' + id_url + " fail")





