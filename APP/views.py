#coding=utf-8  

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = {
    "type": "service_account",
    "project_id": "ringed-arcana-338821",
    "private_key_id": "c1b2438db2651b90b92e06974a08cd40da42c696",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQCdzjDytlclQ+g1\n3jsbmHwXrGtLhVhAV3aPzeuWzIvOfer1qYxgAeIiClWxsV/uF8sz/DHCEtY35ZBX\nW73brqSt34dfwLl2fBbvDUVVLyZZsrDw3MxrDhagbn3VUBJtn04WNCkk6E1HKP1E\no9ugvdj+sCLuT9NOQvMqhWQPP/KGs1NhmUJfmNF2dput6u6N26MHT09y28waxhEr\n73gFZOjD3qhIYHQEUOnXb/U4QmDBmwPks2R1IwBAVJq9tjyOgRaC9Kz7fKHUhMZH\n1OG1KWlb+3LUImqju7/kPV2N9wQO5z5xlMWq+S4kTE0C2wy8OPXycv3Ckz3K1OFL\nbNwjmsKLAgMBAAECggEAK8IqZpNTdPzwnkdigpN1Dad9FTMDtsvKD7RdOLK9rePS\nzI5YY6MCDsho3N4/qKkmauLq9VL93gAlV2QUMJ+sAJ70TgQGKandPiqi6C0r6EGZ\nuSCw+pqsgY5CDG2ovocnQxbxtc9I5ouiN29sjpU2X+F9vjGaeaAtB8R3a5ci7GDL\n6T9YEupA6QkowtpTj0xtUMBRuiMi5a1Oc1ofETMg7mTSsgLbuIUUtfTbDNOpT6ri\nWn1ziTzCOB8wkty8anVUF8je+GfcBKzPLvCpjDkqPW2nUjVXRhCuL4PavsrZrXvd\nxD9evOmUvYRgclhZVo1qU09V87USdAZUlHnXEAEAuQKBgQDXVBl6ePhuW3ZeUBmf\nevstAw5U3TwliNXRuudTsRAoACbqEoHXKUuX+FuyrQIEJQjpPCAbJfsT8Dwn43ze\nsFeyZnEB4CnEZEvQSfj8behWrbe83EMzt4YJP5ZjVqNB2NUx4KAzJVEXIsHc5sxc\nndUwyfyvdllTFmlEgBKBYsWBdQKBgQC7nKVcKUCraLspJtXhnDk93S6d8WpU3nvD\nEt4LZ8EJX/G1hWyZASgY0beDG75+SeDVy/pxoU5jRyFpgxtUYngEGAyfv7SQtsWT\n4WCoOkUqbDoX0TyMDssr1Cqksy8uvtwtcXvDjevLy4e72CXLegrJDMWudDCzpu2g\nG4PjlLKz/wKBgBlbuBxqPqeQceItgLb9XrMwVvG7lCe/c57dafy7L3Hmgq6yO0RB\ngruE7heetEwUqHX/NLC9ylHQyuTPr5byIYHK+qgD5CdSwHLpIz9nGiOLFcZSEj/2\n7vwL1wQf4d4RURosn/EmBeS5nScMryiBFehHAVEQmPhl/UOp6YP/Q885An9oEHuo\nozk72tv195Srj/wwVH+HHGHesYn0qoJ/0Q1CJfXsuhWCySF0ot8n2jvP0SrlbD9+\nx/qzFsFxxUdjhzsLCkv2UF/X5YmyfVEf/zJeVanjjCwJhCsuJIGC2eFSDIwUqN39\nmrswT7T6fOp58zgITQ1ZtxlMjUtBhAGkOtblAoGAXtQvXK1kZ1kXXPdJObHyejml\nv3LXDFd4r6J4es6bIQsjY3ggLDWyiyZ9SzLRIyrejgcU4hVZPyOAiq01gJLXU+/p\nbQsTj9sux6kmJOVhGuFLLNl13JeC8GuMfNteme3M+R1FIAZPXOQ6Z0BkB4SU+ijK\nnsJQT+FQEDXWjZk1FXo=\n-----END PRIVATE KEY-----\n",
    "client_email": "returnrecord@ringed-arcana-338821.iam.gserviceaccount.com",
    "client_id": "110831427047173795415",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/returnrecord%40ringed-arcana-338821.iam.gserviceaccount.com"
}
client = gspread.service_account_from_dict(creds)


def CreateSheet(Return_record):
    sheet = client.open(Return_record).sheet1
    return sheet

from sheet2api import Sheet2APIClient


sheet = client.open('Return Record 2022')
sheet_instance = sheet.get_worksheet(0)
records_data = sheet_instance.get_all_records()
records_data


package2022=list(filter(lambda records_data: records_data["处理情况\n Processing Method"] == "缺包装(Lack of Package)", records_data))
for d in package2022:
    d['Receipt'] = d.pop('收货日期\nReceipt Date')
    d['PN'] = d.pop('产品型号\nP/N')
    d['Num'] = d.pop('数量\nNumber')
    d['Receiver'] = d.pop('签收人\nReceiver')
package2022

def table2022(request):
    return render(request,'table2022.html',{'package2022':package2022})





sheet2021 = client.open('Return Record 2020-2021')
sheet_instance2021 = sheet2021.get_worksheet(0)
records_data2021 = sheet_instance2021.get_all_records()
records_data2021

package20211=list(filter(lambda records_data2021: records_data2021["处理情况"] == "缺包装", records_data2021))
package20212=list(filter(lambda records_data2021: records_data2021["处理情况"] == "缺包装(lack of packaging)", records_data2021))
package2021=package20211+package20212

for d in package2021:
    d['Receipt'] = d.pop('收货日期')
    d['PN'] = d.pop('产品型号')
    d['Num'] = d.pop('数量')
    d['Receiver'] = d.pop('签收人（receiver）')
    d['Ma'] = d.pop('包装物料')
package2021

def table2021(request):
    return render(request,'table2021.html',{'package2021':package2021})




sheetfs2022 = client.open('Return Record 2022')
sheet_instancefs2022 = sheet.get_worksheet(0)
records_datafs2022 = sheet_instancefs2022.get_all_records()
records_datafs2022

fs2022=list(filter(lambda records_datafs2022: records_datafs2022["RMA"].startswith("FS"), records_datafs2022))
for d in fs2022:
    d['Receipt'] = d.pop('收货日期\nReceipt Date')
    d['PN'] = d.pop('产品型号\nP/N')
    d['Num'] = d.pop('数量\nNumber')
    d['Receiver'] = d.pop('签收人\nReceiver')
fs2022
    
def fs2022(request):
    return render(request,'fs2022.html',{'fs2022':fs2022})



def index(request):
    return render(request,'index.html')



def chart(request):
    return render(request,'charts.html')

def base(request):
    return render(request,'base.html')

