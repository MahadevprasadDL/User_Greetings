from django.shortcuts import render
from datetime import datetime

def greet(request):
    date = datetime.now()
    msg = "Hlo Guys !!! Very Good "

    h = int(date.strftime("%H"))
    
    if 5 <= h < 12:
        msg += "Morning !!!"
    elif 12 <= h < 18:
        msg += "Afternoon !!!"
    elif 18 <= h < 22:
        msg += "Evening !!!"
    else:
        msg += "Night !!!"

    return render(request, "greet.html", {"data": msg, "date": date})
