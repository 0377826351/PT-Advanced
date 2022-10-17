from django.shortcuts import render
from datetime import datetime

def show_info(request):
    info = {
        'countries':[
            'VietNam',
            'England',
            'US',
            'Germany',
        ],
        'now':datetime.now()
    }

    return render(request,'list_ct.html',info)
    
def show_info_detail(request, detail):
    if detail == 'VietNam':
        context = {
            'ten': 'Việt Nam',
            'dientich':'331.210 km²',
            'now':datetime.now()
        }
    elif detail == 'England':
        context = {
            'ten': 'Anh',
            'dientich':'243.610 km²',
            'now':datetime.now()
        }
    elif detail == 'US':
        context = {
            'ten': 'Mỹ',
            'dientich':'9.834.000 km²',
            'now':datetime.now()
        }
    elif detail == 'Germany':
        context = {
            'ten': 'Đức',
            'dientich':'357.588 km²',
            'now':datetime.now()
        }
    return render(request,'country_info.html',context)