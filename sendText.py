 
import urllib.request
import urllib.parse

def sendSMS(apikey, numbers, message):
    apikey = 'r73gUxOx+fg-G51KIvTy4HdrNZXRgR3C8rz581SFSY' 
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message': message,})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

sendSMS('apikey','917470400587', 'This is your message')
