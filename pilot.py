import urllib.request
import time
import pywhatkit

def notification():
    number = {"Yomola": "+2349020327517", "Dele":"+2347036836302"}

    url_list = {"Blue processmaker":"https://processmaker.gtbank.com/sysworkflow/en/gtbank_pro/login/login",
       "BVNPM": "https://bvnpms.gtbank.com/sys/en/neoclassic/login/login",
      "CIS PM": "https://cispm.gtbank.com/sysworkflow/en/neoclassic/login/login",
      "Video Banking":"https://vbanking.gtbank.com/videochat",
      "SAP" : "https://sts.gtbank.com/adfs/ls/idpinitiatedsignon.aspx"}
    for name,url in url_list.items():
        
        if (urllib.request.urlopen(url).getcode() == 200):
            print(urllib.request.urlopen(url).getcode())
            for nam_mob,mobile in number.items():
                hour,minute = int(time.strftime("%H")),int(time.strftime("%M")) + 1
                pywhatkit.sendwhatmsg(mobile, 'Hi ' + str(nam_mob)+ ", \n\n" + str(name) + " was down at " + str(hour) + str(minute-1),hour ,minute)
        else:
            pass
        
while True:
    
     notification()