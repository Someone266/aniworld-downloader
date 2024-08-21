# Aniworld Scraper
# Author: JMcrafter26
# Description: A scraper for aniworld (german anime site)
# Version: see version variable below
# License: MIT License
# DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.
# Please respect the laws of your country and the country of the website you are scraping.

# This code was minified to save space. If you want to read the code, please read the original files.


Bl='Download complete'
Bk='No internet connection'
Bj='Invalid option, try again'
Bi='download'
Bh='archive'
Bg='Choose an option by pressing the number'
Bf='There is a program update available'
Be='Downloading assets...'
Bd='You are up to date'
Bc='success'
Bb='message'
Ba='q. Quit'
BZ='h. Help/Info'
BY='0. Settings'
BX='6. Get anime info'
BW='5. Open anime folder'
BV='4. Clean up'
BU='3. Serve content'
BT='2. Continue Download'
BS='1. Download Assistant'
BR='Checking for updates...'
BQ='Episoden:'
BP='producer'
BO='trailer'
BN='animeSeason'
BM='This type of url is not supported yet. It may be supported in the future'
BL='anime/stream'
BK='Invalid url! Please enter a valid aniworld.to url'
BJ='content'
BI='og:title'
BH='navigate'
BG='document'
BF='de,en-US;q=0.7,en;q=0.3'
BE='Priority'
BD='Sec-Fetch-User'
BC='Sec-Fetch-Site'
BB='Sec-Fetch-Mode'
BA='Sec-Fetch-Dest'
B9='Upgrade-Insecure-Requests'
B8='Accept-Language'
B7='User-Agent'
B6='outtmpl'
B5=KeyError
Ao='Error:'
An='Something went wrong with the update check'
Am='yes'
Al='Invalid url'
Ak='/staffel-'
Aj='/episode-'
Ai='stream.json'
Ah='url'
Ag='fsk'
Af='Or paste your cookie key in the settings'
Ae='DDoS-Guard'
Ad='utf-8'
Ac=enumerate
Ab=Exception
AP='option'
AO='updateHash'
AN='update'
AM='Press enter to exit'
AL='./anime'
AK='./anime/index.json'
AJ='href'
AI='strong'
AH='div'
AB='autoUpdate'
AA='downloads'
A9='update.bat'
A8='/stream.json'
A7='picture'
A6='https://aniworld.to'
A5='aniworld.to'
A4='nt'
A3='anime/'
A2=exit
y='mode'
x='i'
w='pathname'
v='[<>:"/\\\\|?*]'
u='tags'
t='html.parser'
s='1'
r=False
q=range
m='Press enter to continue'
l='totalEpisodes'
k='description'
j='prefHost'
i=' '
f='program'
e='seasons'
d='episodes'
c='status'
b=len
a='settings.json'
Z='anime'
Y='streamtape'
X='assets'
W='enddate'
V='startdate'
U='w'
T=int
R='voe'
O='title'
N='r'
K=''
I=str
H='\n'
G=None
F=input
E=open
A=print
import os as C,shutil as n,time as J,json as D
def AQ(path,season,episode):
	T='../../';V='/downloads';Q='downloads.json';K=path;H=episode;F=season
	if K is not G and F is not G and H is not G:
		if C.path.exists(f"{K}/video/{F}/{H}.mp4"):A(f"{B.WARNING}File {K}/video/{F}/{H}.mp4 already exists. Skipping...{B.ENDC}");return
	if not C.path.exists(C.getcwd()+V):C.makedirs(C.getcwd()+V)
	L=K.split(A3)[1]
	if not C.path.exists(f"downloads/{L}"):C.makedirs(f"downloads/{L}")
	W=A1(j)
	with E(f"{K}/stream.json",N)as M:X=D.load(M)
	C.chdir(f"downloads/")
	if not C.path.exists(Q):
		with E(Q,U)as M:D.dump({},M)
	with E(Q,N)as M:O=D.load(M)
	if L in O and F in O[L]and H in O[L][F]:A()
	else:O.setdefault(L,{}).setdefault(F,{})[H]='downloading'
	with E(Q,U)as M:D.dump(O,M)
	C.chdir(f"{L}")
	if W==R:S=X[R][I(F)][I(H)];P=As(S)
	elif W==Y:S=X[Y][I(F)][I(H)];P=Aq(S)
	else:A('Invalid host');J.sleep(2);return
	if P is G:A(f"{B.FAIL}Download failed{B.ENDC}");C.chdir(T);J.sleep(2);return
	C.chdir(T);C.makedirs(f"{K}/video/{F}",exist_ok=True);P=f"downloads/{L}/{P}";n.move(f"{P}",f"{K}/video/{F}/{H}.mp4");A(f"Moved to {K}/video/{F}/{H}.mp4")
import requests as S,bs4 as z,js2py,re as g
from yt_dlp import YoutubeDL as Ap
def Aq(url,retry=r):
	try:E,C=Bm(url)
	except Ab as D:
		A(D)
		if not retry:A(B.WARNING+'Error getting direct url, retrying...'+B.ENDC);return Aq(url,True)
		else:A(B.FAIL+'Failed to get direct url! Try again later or switch to another hoster.'+B.ENDC);return
	C=C.replace('"',K);C=C.replace(i,'_');C=C.replace(H,K);C=C.replace('\r',K);F={B6:C}
	with Ap(F)as G:
		try:G.download(E)
		except Ab as D:pass;At()
	return C
def Bm(url):
	D='id=';I={B7:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',B8:BF,B9:s,BA:BG,BB:BH,BC:'none',BD:'?1',BE:'u=1'};J=S.get(url,headers=I);C=K;E=z.BeautifulSoup(J.content,t);L=E.find('meta',attrs={'name':BI})[BJ];M=E.find(AH,id='robotlink').find_next('script');B=M.text;B=B.split(H);F=[]
	for G in B:
		if G.startswith("document.getElementById('ide"):F.append(G)
	B=F[-1];B=B.split('document.getElementById')[1];B=B.split('innerHTML = ')[1];B=B.rstrip(';');B=js2py.eval_js(B);B=B.split('?')[1]
	if not B.startswith(D):B=D+g.sub('^.*?=',K,B)
	C='https://streamtape.com/get_video?'+B;A(C);return C,L
import sys as P,os as C,glob,wget as AR
from bs4 import BeautifulSoup as Bn
import base64 as Ar
def As(URL):
	L='var sources';J=URL;J=I(J);R={B7:'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',B8:BF,B9:s,BA:BG,BB:BH,BC:'none',BD:'?1',BE:'u=1'};F=S.get(J,headers=R);M=Bn(F.content,t)
	if F.text.startswith('<script>'):N="window.location.href = '";O=b(N);P=F.text.find(N);T=F.text.find("'",P+O);U=F.text[P+O:T];return As(U)
	V=M.find('meta',attrs={'name':BI});E=V[BJ];E=E.replace(i,'_');A('Name of file: '+E);G=M.find_all(string=g.compile(L));G=I(G);W=G.index(L);B=G[W:];X=B.index(';');B=B[:X];B=B.replace('var sources = ',K);B=B.replace("'",'"');B=B.replace('\\n',K);B=B.replace('\\',K);Y=',';Z=K;B=Z.join(B.rsplit(Y,1));Q=D.loads(B)
	try:C=Q['mp4'];C=Ar.b64decode(C);C=C.decode(Ad);AR.download(C,out=f"{E}_SS.mp4")
	except B5:
		try:
			C=Q['hls'];C=Ar.b64decode(C);C=C.decode(Ad);E=E+'_SS.mp4';a={B6:E}
			with Ap(a)as c:
				try:c.download(C)
				except Ab as d:pass
			At()
		except B5:A('Could not find downloadable URL. Voe might have change their site. Check that you are running the latest version of voe-dl, and if so file an issue on GitHub.');quit()
	A(H);return E
def At():
	A=C.getcwd()
	for B in glob.iglob(C.path.join(A,'*.part')):C.remove(B)
import sys as P,http.server
def C5(title='AniWorld Scraper'):
	B=title
	if C.name==A4:C.system(f"title {B}")
	else:A(f"]0;{B}\a")
def h(url):
	Y='span';P='a';F=url
	if A5 not in F:A(B.WARNING+BK+B.ENDC);J.sleep(2);return
	if not BL in F:A(B.WARNING+BM+B.ENDC);J.sleep(2);return
	h=S.get(F);Z=h.text
	if Ae in Z:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Af);J.sleep(2);return
	D=z.BeautifulSoup(Z,t);E=D.find(AH,class_='series-title').find('h1').string;E=E.strip();E=E.split(H)[0];A('Getting info for:',E);j=D.find('p',class_='seri_des').get('data-full-description');N=D.find(Y,itemprop='startDate').string;Q=D.find(Y,itemprop='endDate').string
	if Q=='heute':R='ONGOING'
	else:R='FINISHED'
	C=D.find(AI,string='Staffeln:').parent.parent.parent.find_all('li');C=[A.text for A in C];C=[A.replace(i,K)for A in C];C=[A for A in C if A];C=[A for A in C if A.isnumeric()];C=b(C);L={}
	for a in q(1,T(C)+1):L[a]=Bo(F,a)
	L=L;f=sum(L.values());U=D.find(AH,class_='seriesCoverBox').find('noscript').find('img').get('src');U=A6+U
	try:g=D.find(P,class_='trailerButton').get(AJ)
	except:g=K
	X=D.find_all(P,itemprop='genre');X=[A.string for A in X];m=D.find(AI,class_='seriesProducer').text;n=D.find(AH,class_=Ag).get('data-fsk');M=D.find(P,class_='imdb-link')
	if M is not G:M=M.get(AJ)
	else:M=K
	A(R+' ('+N+' - '+Q+') - '+I(f)+' episodes - '+I(C)+' seasons');o={O:E,k:j,BN:{'year':T(N[:4]),'season':N[5:]},c:R,d:L,l:f,e:C,V:N,W:Q,A7:U,BO:g,u:X,BP:m,Ag:n,'imdb':M,Ah:F};return o
def AC(info):
	B=info;A('Setting up anime folder...');F=f"{B[O]} ({B[V]}-{B[W]})";F=g.sub(v,K,F);J=f"./{F}";F=f"anime/{F}"
	if not C.path.exists(F):C.makedirs(F)
	with E(f"{F}/info.json",U)as G:D.dump(B,G,indent=4)
	I=B[A7].split('.')[-1]
	if not C.path.exists(f"{F}/image.{I}"):AR.download(B[A7],f"{F}/image.{I}")
	B[A7]=f"image.{I}";B[w]=J
	with E(f"{F}/info.json",U)as G:D.dump(B,G,indent=4)
	if C.path.exists(AK):
		with E(AK,N)as G:H=D.load(G)
	else:H=[]
	L={O:B[O],u:B[u],V:B[V],W:B[W],c:B[c],k:B[k],l:B[l],e:B[e],w:J}
	for(M,P)in Ac(H):
		if P[O]==B[O]:H[M]=L;break
	else:H.append(L)
	with E(AK,U)as G:D.dump(H,G,indent=4)
	A('Anime folder setup complete')
def AS(url,season,episodes=G,info=G):
	T='Season stream urls already exist';Q=url;L=info;J=season;F=episodes
	if F is G:U=S.get(Q);X=U.text;Z=z.BeautifulSoup(X,t);F=Z.find(AI,string=BQ).parent.parent.parent;F=F.find_all('li');F=b(F)-1
	A(f"Getting streams for season {J} with {F} episodes...");M=f"{L[O]} ({L[V]}-{L[W]})";M=g.sub(v,K,M);A('Path:',M)
	if C.path.exists(A3+M+A8):
		with E(A3+M+A8,N)as a:
			B=D.load(a);A('Found stream.json');A('Checking if season already exists...')
			if R in B:
				if I(J)in B[R]:A(T);return B
			if Y in B:
				if I(J)in B[Y]:A(T);return B
	else:B={}
	B={}
	for P in q(1,F+1):
		if L is not G:B[P]=AU(Q,J,P,L)
		else:B[P]=AU(Q,J,P)
		AT(P/F)
	A(H);A('Done with season',J);return B
def AT(percent):A=percent;B=50;C=T(round(B*A));D='='*C+'-'*(B-C);P.stdout.write(f"\rProgress: [{D}] {A*100:.2f}%");P.stdout.flush()
def AU(url,season,episode,info=G):
	b='No stream url found';a=url;Z=info;X=episode;L=season;a=a+f"/staffel-{L}/episode-{X}";e=S.get(a);c=e.text
	if Ae in c:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Af);J.sleep(2);return
	d=z.BeautifulSoup(c,t)
	if Z is not G:H=f"{Z[O]} ({Z[V]}-{Z[W]})";H=g.sub(v,K,H);H=f"anime/{H}/stream.json"
	else:H=f"stream.json"
	M=d.find(x,class_='icon VOE')
	if M is G:A('No voe download found, skipping...');return
	M=M.parent;M=M.get(AJ);M=A6+M;T=Au(M)
	if T is G:A(b);return
	if C.path.exists(H):
		with E(H,N)as Q:F=D.load(Q)
	else:F={}
	if I(R)not in F:F[R]={}
	if I(L)not in F[R]:F[R][I(L)]={}
	F[R][I(L)][I(X)]=T
	with E(H,U)as Q:D.dump(F,Q,indent=4)
	P=d.find(x,class_='icon Streamtape')
	if P is G:A('No streamtape download found, skipping...');return
	P=P.parent;P=P.get(AJ);P=A6+P;T=Au(P)
	if T is G:A(b);return
	if C.path.exists(H):
		with E(H,N)as Q:F=D.load(Q)
	else:F={}
	if I(Y)not in F:F[Y]={}
	if I(L)not in F[Y]:F[Y][I(L)]={}
	F[Y][I(L)][I(X)]=T
	with E(H,U)as Q:D.dump(F,Q,indent=4)
	if F[R][I(L)][I(X)]is not G:return F[R][I(L)][I(X)]
	else:return T
def Au(url):
	B=S.head(url)
	if B.status_code!=302 and B.status_code!=301:A('No redirect found');return
	else:
		C=B.headers['Location']
		if A5 in C:A('Something went wrong with the redirect');return
		else:return C
def Bo(url,season):B=url;B=B+f"/staffel-{season}";C=S.get(B);D=C.text;E=z.BeautifulSoup(D,t);A=E.find(AI,string=BQ).parent.parent.parent;A=A.find_all('li');A=b(A)-1;return A
def Bp(season,episode,info=G):
	H=episode;I=season;C=info;L();M()
	if C is G:
		with E(Ai,N)as F:J=D.load(F)
	else:
		B=f"{C[O]} ({C[V]}-{C[W]})";B=g.sub(v,K,B);B=f"anime/{B}"
		with E(B+A8,N)as F:J=D.load(F)
	A(f"Downloading season {I} episode {H}...");AQ(B,I,H)
def AV(season,info=G):
	C=info;F=season
	if C is G:
		with E(Ai,N)as J:P=D.load(J)
	else:
		B=f"{C[O]} ({C[V]}-{C[W]})";B=g.sub(v,K,B);B=f"anime/{B}"
		with E(B+A8,N)as J:P=D.load(J)
	for Q in P[R][I(F)]:L();M();A(f"Downloading season {F} episode {Q}...");AT(T(Q)/b(P[R][I(F)]));A(H);AQ(B,F,Q)
def Bq(season,start,end,info=G):
	P=season;F=start;C=info
	if C is G:
		with E(Ai,N)as I:Q=D.load(I)
	else:
		B=f"{C[O]} ({C[V]}-{C[W]})";B=g.sub(v,K,B);B=f"anime/{B}"
		with E(B+A8,N)as I:Q=D.load(I)
	for J in q(F,end+1):L();M();A(f"Downloading season {P} episode {J}...");AT((J-F)/(end-F));A(H);AQ(B,P,J)
def Av(query):
	E=query
	if E==K or E==G:A(B.WARNING+'No query entered'+B.ENDC);J.sleep(2);return
	F='https://aniworld.to/ajax/search';H={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':A6,'referer':f"https://aniworld.to/search?q={E}",'sec-ch-ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with':'XMLHttpRequest'};C={'keyword':E};C=S.post(F,headers=H,data=C);C=C.text
	try:C=D.loads(C)
	except:
		if Ae in C:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Af);J.sleep(2);return
		A(f"{B.WARNING}Error parsing JSON{B.ENDC}");A('Try again later');J.sleep(2);return
	return AW(E,C)
def AW(query,data):
	N='Invalid number, try again';I=query;E='link';C=data;C=[A for A in C if'/anime/stream/'in A[E]];C=[A for A in C if'/support/'not in A[E]];C=[A for A in C if'/user/'not in A[E]];C=[A for A in C if'/search/'not in A[E]];C=[A for A in C if Aj not in A[E]];C=[A for A in C if Ak not in A[E]];L();M();A('Search results for:',I);A(H)
	for(Q,G)in Ac(C):G[O]=G[O].replace('<em>',K).replace('</em>',K);A(Q+1,B.OK+G[O]+B.ENDC);A(G[k]);A('---')
	A(B.PRIMARY+'Select a number to continue, or press q to quit'+B.ENDC);D=F()
	if D=='q':return r
	elif not D.isnumeric():A(N);J.sleep(2);AW(I,C);return
	elif T(D)<1 or T(D)>b(C):A(N);J.sleep(2);AW(I,C);return
	D=T(D);R=C[D-1][E];A('Selected:',C[D-1][O]);P=A6+R;A('Aniworld URL:',P);return P
def Aw():
	B=3333;D=http.server.SimpleHTTPRequestHandler;E=C.path.join(C.getcwd(),Z);C.chdir(E)
	with http.server.HTTPServer((K,B),D)as F:A('serving at http://localhost:'+I(B)+'/');A('Press Ctrl+C to stop the server');F.serve_forever()
def AX():
	S='Removed:';T='index.html';L();M();A('Running cleanup...');Y=[C.path.join(B,A)for(B,E,D)in C.walk('./downloads')for A in D if A.endswith('.part')or A.endswith('.ytdl')]
	if Y:
		A(B.WARNING+'Do you want to delete non finished downloads? After deleting you have to restart the download'+B.ENDC);A('Do you want to continue? (y/N)');J=F()
		if J.lower()=='y':
			A('Deleting files...')
			for I in Y:C.remove(I);A('Deleted:',I)
	A('Rebuilding index.json...');P=[A for A in C.listdir(Z)if C.path.isdir(C.path.join(Z,A))];a=[]
	for H in P:
		if not C.listdir(f"anime/{H}"):C.rmdir(f"anime/{H}");continue
		if not C.path.exists(f"anime/{H}/info.json"):continue
		if C.path.exists(f"anime/{H}/stream.json"):C.remove(f"anime/{H}/stream.json")
		with E(f"anime/{H}/info.json",N)as R:G=D.load(R)
		if Ah not in G:
			A('No url found for:','/'+H+'/ ('+G[O]+')'+', should we remove it? (Y/n)');J=F()
			if J.lower()=='n':continue
			A('Removing:',G[O]);n.rmtree(f"anime/{H}");continue
		if A3 in G[w]:G[w]=G[w].replace(A3,K)
		b=[O,k,BN,c,d,l,e,V,W,A7,BO,u,BP,Ag,'imdb']
		if not all(A in G for A in b):A('Rebuilding info.json for:',G[O]);G=h(G[Ah]);AC(G)
		a.append({O:G[O],u:G[u],V:G[V],W:G[W],c:G[c],k:G[k],l:G[l],e:G[e],w:f"{H}"})
	with E(AK,U)as R:D.dump(a,R,indent=4)
	A('Cleaning file structure...')
	if C.path.exists(T):C.remove(T)
	f=['urls.txt','search.html','search.txt','temp.html',A9,'update.exe'];A('Removing unused files...')
	for I in f:
		if C.path.exists(I):C.remove(I);A(S,I)
	if C.path.exists(X):n.rmtree(X);A('Removed: assets/')
	if C.path.exists(AA):
		P=[A for A in C.listdir(AA)if C.path.isdir(C.path.join(AA,A))]
		for H in P:
			if not C.listdir(f"downloads/{H}"):C.rmdir(f"downloads/{H}");A(S,f"downloads/{H}")
	Br();A('Done');A(m);F();Q()
def Br():
	F='video';I=[A for A in C.listdir(C.path.join(C.getcwd(),Z))if C.path.isdir(C.path.join(C.getcwd(),Z,A))]
	if X in I:I.remove(X)
	G={}
	for B in I:
		O=[A for A in C.listdir(C.path.join(C.getcwd(),Z,B,F))if C.path.isfile(C.path.join(C.getcwd(),Z,B,F,A))];J=[A for A in C.listdir(C.path.join(C.getcwd(),Z,B,F))if C.path.isdir(C.path.join(C.getcwd(),Z,B,F,A))];G[B]={}
		for H in J:
			G[B][H]={};K=[A for A in C.listdir(C.path.join(C.getcwd(),Z,B,F,H))if C.path.isfile(C.path.join(C.getcwd(),Z,B,F,H,A))]
			for L in K:M=L.split('.')[0];G[B][H][M]='downloaded'
	if not C.path.exists(C.path.join(C.getcwd(),AA)):C.makedirs(C.path.join(C.getcwd(),AA))
	with E(C.path.join(C.getcwd(),'downloads/downloads.json'),U)as N:D.dump(G,N,indent=4)
	A('downloads.json rebuilt')
def Ax(url):
	C='episode';D='staffel';B=url
	if A5 not in B:A(Al);return r
	if D in B:B=B.split(D)[0]
	if C in B:B=B.split(C)[0]
	return B
def Bs():
	if not C.path.exists(a):Bv();return
	if C.path.exists(A9):C.remove(A9)
	elif not C.path.exists(AL):C.makedirs(AL)
def AD(key,value):
	if C.path.exists(a):
		with E(a,N)as A:B=D.load(A)
	else:B={}
	B[key]=value
	with E(a,U)as A:D.dump(B,A,indent=4)
def Bt():
	if C.path.exists(A9):C.remove(A9)
	L();M();A(B.PRIMARY+'Update finished'+B.ENDC);A('The program has been updated, YIPPIE!');A(m);F();AY()
def Bu():AZ()
def A0():return r
def o():
	B='./assets/animeList.json';return;A(BR);H='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database-minified.json';I='https://api.github.com/repos/manami-project/anime-offline-database/commits?path=anime-offline-database-minified.json&page=1&per_page=1';J=S.get(I);F=J.json();K=F[0]['commit']['committer']['date'][:10]
	if C.path.exists(B):
		with E(B,N)as G:F=D.load(G)
		L=F['lastUpdate']
		if L==K:A('Anime list is up to date');return
	A('Downloading anime list...');AR.download(H,B);F=D.load(E(B,N,encoding=Ad))
	with E(B,U)as G:D.dump(F,G,indent=4)
	A('Anime list downloaded')
def L():A('\x1b[H\x1b[J')
def Q():
	G='Info';I='\nPress enter to continue';K='Unsupported os';N='posix';O='Enter the url of the anime';P='Invalid key';L();M();A('Press one of the following keys:');A(BS);A(BT);A(BU);A(BV);A(BW);A(BX);A(BY);A(BZ);A(Ba);D=F()
	if D not in[s,'2','3','4','5','6','7','8','9','0','q','Q','h',x]:A(P);Q();return
	if D==s:B4()
	elif D=='x':
		A('This mode will download everything from the given url');A(O);E=F();E=Ax(E)
		if not E:A(B.WARNING+Al+B.ENDC);J.sleep(2);Q();return
		B3(E)
	elif D=='2':A('Not implemented yet');J.sleep(2);Q()
	elif D=='3':Aw()
	elif D=='4':AX()
	elif D=='5':
		if C.name==A4:C.system('start .\\anime')
		elif C.name==N:C.system('xdg-open .\\anime')
		else:A(K);A('The anime folder is located in the following directory:');A(C.getcwd()+'\\anime');A(I);F();Q()
		Q()
	elif D=='6':
		A(O);E=F();E=Ax(E)
		if not E:A(B.WARNING+Al+B.ENDC);J.sleep(2);Q();return
		A(h(E))
	elif D=='0':Bu();Q()
	elif D=='h'or D==x:
		L();M();A(B.PRIMARY+G+B.ENDC);A(H);A(f"{B.OK}This program was made by JMcrafter26 and published by Someone266 on Github{B.ENDC}");A(f"{B.OK}The program is open source and can be found here: https://github.com/Someone266/aniworld-downloader/{B.ENDC}");A(H);A('This program is still in development, so there might be some bugs');A('If you find a bug, please report it on the Github page');A(H);A(f"{B.OK}This program is for educational purposes only, the developer nor the publisher is responsible for any damage caused by the program. This program is not affiliated with any of the anime sites. This program is provided as is, without any warranty. Use at your own risk.{B.ENDC}");A(H);A('Press enter to continue (i to report a bug)');D=F()
		if D==x:
			A('Opening the Github page...')
			if C.name==A4:C.system('start https://github.com/Someone266/aniworld-downloader/issues');J.sleep(2)
			elif C.name==N:C.system('xdg-open https://github.com/Someone266/aniworld-downloader/issues');J.sleep(2)
			else:A(K);A('The Github page is located at the following link:');A('https://github.com/Someone266/aniworld-downloader/issues');A(I);F()
		L();M();A(B.PRIMARY+G+B.ENDC);A(H);A(f"{B.OK}Your Version is: {AG()}{B.ENDC}")
		if A0():A(f"{B.OK}You are running the windows version (Congratulations){B.ENDC}")
		A(f"{B.OK}Your mode is: "+A1(y)+f"{B.ENDC}");A(f"{B.OK}Your preferred host is: "+A1(j)+f"{B.ENDC}")
		if A1(AB)==Am:A(f"{B.OK}Auto update is enabled{B.ENDC}")
		else:A(f"{B.WARNING}Auto update is disabled{B.ENDC}");A(f"{B.WARNING}You might miss out on new features and bug fixes{B.ENDC}");A(f"{B.PRIMARY}Press SPACE to check and download updates{B.ENDC}")
		A(H);D=F()
		if D==i:B1(True);J.sleep(2);Q();return
		A_()
	elif D=='q'or D=='Q':A('Quitting, Bye!');A2()
	else:A(B.WARNING+P+B.ENDC);J.sleep(2);Q();return
def Bv():
	D='./assets';L();M();A(B.PRIMARY+'Hi and welcome to AniWorld-Down v'+AG()+B.ENDC);A('It looks like this is your first time running this program, or you have deleted some files :)');A('This guide will help you get started with the program\n');A(B.WARNING+'This directory will be used to store the anime and the assets'+B.ENDC);A(B.SECONDARY+m+B.ENDC);F()
	if not C.path.exists(AL):C.makedirs(AL)
	if not C.path.exists(D):C.makedirs(D)
	Bw()
def Bw():
	D='updateNotes';E='Update notes:';L();M();A(B.PRIMARY+'Step 1: Checking for updates and downloading assets'+B.ENDC);A('We promise, it will be quick');C=B2()
	if C is G:A('Hmm, something went wrong with the update check');A('Do you have an internet connection? \n');A(B.SECONDARY+'PS: We need an internet connection to download the assets'+B.ENDC);A(B.SECONDARY+AM+B.ENDC);F();A2()
	if C[c]=='error':A(B.WARNING+An+B.ENDC);A(Ao,C[Bb]);A('Please try again later\n');A(B.SECONDARY+AM+B.ENDC);F();A2()
	elif C[c]==Bc:A(Bd);A(B.SECONDARY+m+B.ENDC);F();AY();return
	else:
		if C[AN][X]:A(B.OK+Be+B.ENDC);A(E);A(C[D][X]+H);AE(X,C[AO][X])
		if C[AN][f]:A(B.OK+Bf+B.ENDC);A(E);A(C[D][f]+H);AE(f,C[AO][f])
		else:A('No program update available')
		A(B.SECONDARY+m+B.ENDC);F();AY();return
def AY():L();M();A(B.PRIMARY+'Step 2: Configuring the program'+B.ENDC);A('We need to configure the program before we can continue');A('It is very simple, just answer a few questions');A(B.SECONDARY+m+B.ENDC);F();Ay()
def Ay():
	L();M();A(B.PRIMARY+'Choose the option that describes you the best'+B.ENDC);A('1. I want to archive anime and have it nicely organized (with filestructure, prictures and an offline webserver)');A('2. I just want to download anime fast and continue watching (No filestructure, ready to watch or move)');A(H);A(B.SECONDARY+Bg+B.ENDC);C=F()
	if C==s:AD(y,Bh)
	elif C=='2':AD(y,Bi)
	else:A(Bj);Ay();return
	Az()
def Az():
	L();M();A(B.PRIMARY+'Select your preferred host'+B.ENDC);A('1. Voe (Recommended)');A('2. Streamtape');A(H);A(B.SECONDARY+Bg+B.ENDC);C=F()
	if C==s:AD(j,R)
	elif C=='2':AD(j,Y)
	else:A(Bj);Az();return
	Bx()
def Bx():
	L();M();A(B.PRIMARY+'Thats it, you are ready to go'+B.ENDC);A('You can now start downloading anime');A(H);A('Press i to read the instructions');A('Press enter to just freakin start the program');C=F()
	if C==x:A_()
	Q()
def A_():L();M();A(B.PRIMARY+'Instructions'+B.ENDC);A(BS);A('This option will guide you through the download process, you just need to enter the url of the anime');A(BT);A('This option is not implemented yet');A(BU);A('This option will start a webserver to serve the content - you can watch the anime in your browser (even offline and other devices)');A(BV);A('This option will clean up the program and the assets');A(BW);A('This option will open the anime folder where the anime is stored');A(BX);A('This option will get the info of the anime from the url');A(BY);A('This option will allow you to change the settings of the program');A(BZ);A('This is the current screen :)');A(Ba);A(H);A(m);F();Q()
B0={y:"The mode of AniDown\n'archive' will organize the anime with filestructure, pictures and an offline webserver\n'download' will download anime fast and continue watching",j:'The preferred host to download from',AB:'Automatically update the program on startup (Recommended, as this will fix bugs and add new features)'}
p={y:[Bh,Bi],j:[R,Y],AB:[Am,'no']}
type={y:AP,j:AP,AB:AP}
def AZ():
	K=f"{C.getcwd()}\\settings.json";L();A('Settings:');A('Path:',K);A(H)
	with E(a,N)as M:J=D.load(M)
	for(G,O)in J.items():P=list(J.keys()).index(G)+1;A(f"{B.PRIMARY}({P}) - {G}: {O}{B.ENDC}");A(f"{B.OK}Description: {B.ENDC}{B.SECONDARY}{B0[G]}{B.ENDC}");A(f"{B.OK}Options: {B.ENDC}{B.SECONDARY}{p[G]}{B.ENDC}");A('---')
	A('Choose an option by pressing the number (q to quit):');I=F()
	if not I or I=='q':return
	if not I.isdigit():return AZ()
	Aa(T(I),J);return AZ()
def Aa(option,data):
	H=data;C=option;G=list(H.keys())[C-1];L();A(f"Changing '{G}'")
	if type[G]==AP:
		A(f"{B.OK}Options:\n{B.ENDC}")
		for(I,C)in Ac(p[G]):A(f"({I+1}) - {C}")
		A('Choose an option by pressing the number:');C=F()
		if not C.isdigit():return Aa(C,H)
		if T(C)>b(p[G]):return Aa(C,H)
		H[G]=p[G][T(C)-1]
	else:
		if type[G]=='text':A('Enter the new value (Text/String):')
		elif type[G]=='number':A('Enter the new value (Number):')
		J=F();H[G]=J
	with E(a,U)as K:D.dump(H,K)
def A1(key):
	A=key
	with E(a,N)as C:B=D.load(C)
	if A not in B:
		B[A]=p[A][0]
		with E(a,U)as C:D.dump(B,C)
	return B[A]
def By():
	A={}
	with E(a,N)as B:A=D.load(B)
	for C in B0:
		if C not in A:A[C]=p[C][0]
	with E(a,U)as B:D.dump(A,B)
	return A
import zipfile
def B1(force=r):
	Bs();L();M();A('Loading...')
	try:By()
	except:A('Something went wrong with the settings file')
	if A1(AB)=='no'and not force:A('Skipping update check');J.sleep(2);return
	try:B=B2()
	except:A(An);J.sleep(2);return
	if B is G:A('No internet connection, skipping update check');return
	if B[c]=='error':A(An);A(Ao,B[Bb]);J.sleep(2);return
	elif B[c]==Bc:A(Bd);return
	else:
		if B[AN][X]:A(Be);AE(X,B[AO][X])
		if B[AN][f]:A(Bf);AE(f,B[AO][f])
def B2():
	F='anime/assets/.version';A(BR,end=K)
	try:S.get('https://api.jm26.net/status.txt',timeout=5)
	except S.exceptions.ConnectionError:A(' Skipped');A(B.WARNING+Bk+B.ENDC);J.sleep(2);return
	H='https://api.jm26.net/update/aniworld-down/check/';I=AG()
	if not C.path.exists(F):G='0.0.0'
	else:
		with E(F,N)as L:G=L.read()
	D={f:I,X:G};M=S.post(H,data=D);D=M.json();A(' Done');return D
def AE(type,hash):
	Q='anime/assets';R='Please try again later';G='./update';A('Downloading ..');L=f"https://api.jm26.net/update/aniworld-down/download/?type={type}&hash={hash}";M='./update/update.zip'
	if A0():L=L+'&os=windows'
	if not C.path.exists(G):C.makedirs(G)
	try:O=S.get(L)
	except S.exceptions.ConnectionError:A(B.WARNING+Bk+B.ENDC);A(R);A(AM);F();A2()
	if O.headers['Content-Type']=='application/json':A(B.WARNING+'Something went wrong with the download'+B.ENDC);A(Ao,O.text);A(R);A(AM);F();A2()
	A(B.OK+Bl+B.ENDC)
	with E(M,'wb')as I:I.write(O.content)
	with zipfile.ZipFile(M,N)as T:T.extractall(G)
	C.remove(M)
	if C.path.exists(Q):n.rmtree(Q)
	for D in C.listdir(G):
		if C.path.isdir(f"./update/{D}"):
			if not C.path.exists(f"./{D}"):C.makedirs(f"./{D}")
			for I in C.listdir(f"./update/{D}"):n.move(C.path.join(f"./update/{D}",I),C.path.join(f"./{D}",I))
			C.rmdir(f"./update/{D}")
		else:n.move(C.path.join(G,D),C.path.join('./',D))
	C.rmdir(G);A(B.OK+'Update complete'+B.ENDC);A(H);A(f"{B.WARNING}It is recommended to run the {B.ENDC}{B.OK}clean option{B.ENDC}{B.WARNING} after updating{B.ENDC}");A(H)
	if type==f:
		for U in q(3):A(f"\rRestarting in {3-U} seconds",end=K);J.sleep(1)
		A('\rRestarting program...')
		if not C.path.exists(a):
			if A0():C.system(f"start update.bat guideUpdateFinished")
			elif C.name==A4:C.system('py main.py guideUpdateFinished')
			else:C.system(f"python3 main.py guideUpdateFinished")
		elif A0():C.system(f"start update.bat "+i.join(P.argv[1:]))
		elif C.name==A4:C.system('py main.py '+i.join(P.argv[1:]))
		else:C.system('python3 main.py '+i.join(P.argv[1:]))
Bz='1.1.9'
class B:PURPLE='\x1b[95m';SECONDARY='\x1b[90m';PRIMARY='\x1b[94m';CYAN='\x1b[96m';OK='\x1b[92m';WARNING='\x1b[93m';FAIL='\x1b[91m';ENDC='\x1b[0m';BOLD='\x1b[1m';UNDERLINE='\x1b[4m'
def B3(url):
	o();C=h(url);AC(C)
	for D in C[d]:AS(url,D,C[d][D],C)
	E=C[e];A(E)
	for D in q(1,E+1):AV(D,C)
	AX();M();A(B.OK+'Finished downloading all episodes'+B.ENDC);A(H);A(B.PRIMARY+"Run 'serve' to watch the episodes in your browser"+B.ENDC)
def B4():
	L();M();o();A(B.OK+'This is the auto mode. It will ask you what to download.'+B.ENDC);A(H);A('Enter the name of the anime you want to search for or paste the url of the anime');D=F()
	if D.startswith('http'):
		C=D
		if A5 not in C:A(B.WARNING+BK+B.ENDC);J.sleep(2);return
		if not BL in C:A(B.WARNING+BM+B.ENDC);J.sleep(2);return
		if Aj in C:C=C.split(Aj)[0]
		if Ak in C:C=C.split(Ak)[0]
	elif D!=K and D!=G:
		C=Av(D)
		if C==r:A('Quit');Q();return
		elif A5 not in C:A(B.WARNING+'Invalid url! There was an error with the search'+B.ENDC);J.sleep(2);return
	else:Q();return
	E=h(C);AC(E)
	for I in E[d]:AS(C,I,E[d][I],E)
	AF(C,E)
def AF(url,info):
	L=url;C=info;M();A(B.OK+'Setup complete'+B.ENDC);A(H);A(B.OK+'We found '+I(C[e])+' seasons and a total of '+I(C[l])+' episodes'+B.ENDC);A(H);A('Do you want to download all episodes? (Y/n)');G=F()
	if G!='Y'and G!='y'and G!=Am and G!='Yes'and G!=K:
		A('Which season do you want to download?');D=T(F());A('What episode do you want to download? (Enter 0 to download all episodes; use - to download a range of episodes)');E=T(F())
		if D<1 or D>C[e]:A(B.FAIL+'Invalid season'+B.ENDC);J.sleep(2);AF(L,C);return
		if E==0:AV(D,C)
		elif'-'in I(E):
			N=T(E.split('-')[0]);O=T(E.split('-')[1])
			if N<1 or O>C[d][D]:A(B.FAIL+'Invalid range'+B.ENDC);J.sleep(2);AF(L,C);return
			Bq(D,N,O,C)
		else:
			if E<1 or E>C[d][D]:A(B.FAIL+'Invalid episode'+B.ENDC);J.sleep(2);AF(L,C);return
			Bp(D,E,C)
	else:
		A(B.OK+'Downloading all episodes'+B.ENDC)
		for D in q(1,C[e]+1):AV(D,C)
	A(B.OK+Bl+B.ENDC);A(H);A(B.PRIMARY+'Press enter to return to the main menu'+B.ENDC);F();Q()
def AG():return Bz
def B_(url):o();A=h(url);return A
def C0(url):o();A=h(url);AC(A)
def C1(url,season,info=G):
	A=season;o();B=G
	if info is not G:B=info[d][A]
	C=AS(url,A,B);return C
def C2(url,season,episode,info=G):
	C=season;A=info;B=episode;o()
	if A is not G:B=A[d][C][B]
	D=AU(url,C,B,A);return D
def C3():L();M();A('Enter the name of the anime you want to search for');B=F();return Av(B)
def M():
	A(H);C=AG()
	if A0():C=C+' (Windows)'
	A(B.CYAN+'    AA          W     W         ll     d     DDD                    '+B.ENDC);A(B.CYAN+'   A  A      ii W     W          l     d     D  D                   '+B.ENDC);A(B.CYAN+'   AAAA nnn     W  W  W ooo rrr  l   ddd     D  D ooo w   w nnn     '+B.ENDC);A(B.CYAN+'   A  A n  n ii  W W W  o o r    l  d  d     D  D o o w w w n  n    '+B.ENDC);A(B.CYAN+'   A  A n  n ii   W W   ooo r   lll  ddd     DDD  ooo  w w  n  n    '+B.ENDC);A(B.CYAN+'                                                                    '+B.ENDC);A('A powerful scraper and downloader for AniWorld');A(i);A('Version: '+C+'                                 Made by JMcrafter26');A(B.SECONDARY+'DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.'+B.ENDC);A(B.SECONDARY+'Please respect the laws of your country and the country of the website you are scraping.'+B.ENDC);A(H)
def C4():
	I='help';J='clean';K='serve';N='search'
	if b(P.argv)==1:P.argv.append('ui')
	C=P.argv[1]
	if C=='guideUpdateFinished':Bt();return
	B1();L();M();A(H)
	if C=='getinfo':D=P.argv[3];A(B_(D))
	elif C=='run':D=P.argv[2];B3(D)
	elif C=='ui':Q()
	elif C==N:C3();return
	elif C==K:Aw()
	elif C==J:AX()
	elif C=='setup':D=P.argv[3];C0(D)
	elif C=='auto':B4()
	elif C=='getseason':
		D=P.argv[3];F=P.argv[5];E=G
		if b(P.argv)>6:E=h(D)
		A(C1(D,F,E))
	elif C=='getepisode':
		D=P.argv[3];F=P.argv[5];O=P.argv[7];E=G
		if b(P.argv)>8:E=h(D)
		A(C2(D,F,O,E))
	elif C==I:A(B.PRIMARY+'Commands:'+B.ENDC);A('-----------------');A('run -url <url>');A(K);A(J);A(N);A('setup -url <url>');A('getinfo -url <url>');A('getseason -url <url> -season <season>');A('getepisode -url <url> -season <season> -episode <episode>');A(I)
	else:A(B.WARNING+'Invalid command'+B.ENDC)
	A(H)
if __name__=='__main__':C4()