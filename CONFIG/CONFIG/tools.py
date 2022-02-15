from django.utils.timesince import timesince

import socket
hostname    = socket.gethostname()
LOCAL_IP    = socket.gethostbyname(hostname)
PORT_NUMBER ="8000"


def get_last_minute(obj):
    obj=timesince(obj)
    obj=obj.replace(",","")+" ago"
    obj=obj.replace("minutes","m")#
    obj=obj.replace("minute","m")
    obj=obj.replace("hours","h")
    obj=obj.replace("hour","h")
    return obj


