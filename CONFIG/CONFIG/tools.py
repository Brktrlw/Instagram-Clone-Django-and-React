from django.utils.timesince import timesince

import socket
hostname    = socket.gethostname()
LOCAL_IP    = socket.gethostbyname(hostname)
PORT_NUMBER ="8000"


def get_last_minute(obj):
    obj=timesince(obj)
    obj=obj.replace(",","")+" ago"
    if str(obj)=="0 minutes ago":
        return "few seconds ago"
    return obj


