# Aniworld Scraper
# Author: JMcrafter26
# Description: A scraper for aniworld (german anime site)
# Version: see version variable below
# License: MIT License
# DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.
# Please respect the laws of your country and the country of the website you are scraping.

# This code was minified to save space. If you want to read the code, please read the original files.


Bm='Download complete'
Bl='No internet connection'
Bk='number'
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
An='Error:'
Am='Something went wrong with the update check'
Al='yes'
Ak='Invalid url'
Aj='/staffel-'
Ai='/episode-'
Ah='stream.json'
Ag='url'
Af='fsk'
Ae='Or paste your cookie key in the settings'
Ad='DDoS-Guard'
Ac='utf-8'
Ab=enumerate
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
AA='update.bat'
A9='/stream.json'
A8='picture'
A7='https://aniworld.to'
A6='aniworld.to'
A5='nt'
A4='threads'
A3='anime/'
A2=exit
A0='mode'
z='pathname'
y='[<>:"/\\\\|?*]'
x='tags'
w='html.parser'
v='1'
u=Exception
q='Press enter to continue'
p='totalEpisodes'
o='episodes'
n='description'
m=False
l='prefHost'
k=range
i=' '
f='program'
e=len
d='anime'
c='seasons'
b='status'
a='downloads'
Z='settings.json'
Y='streamtape'
X='assets'
W='enddate'
V='startdate'
U='voe'
T='w'
S=int
O='title'
N='r'
K=''
J='\n'
H=input
G=str
F=open
D=None
A=print
import os as C,shutil as r,time as I,json as E,threading as Ao
def AQ(path,season,episode):
	b='/downloads';R='downloads.json';K=path;J=episode;H=season
	if K is not D and H is not D and J is not D:
		if C.path.exists(f"{K}/video/{H}/{J}.mp4"):A(f"{B.WARNING}File {K}/video/{H}/{J}.mp4 already exists. Skipping...{B.ENDC}");return
	if not C.path.exists(C.getcwd()+b):C.makedirs(C.getcwd()+b)
	L=K.split(A3)[1]
	if not C.path.exists(f"downloads/{L}"):C.makedirs(f"downloads/{L}")
	P=j(l);c=j(A4)
	with F(f"{K}/stream.json",N)as M:O=E.load(M)
	if not C.path.exists(C.path.join(C.getcwd(),a,R)):
		with F(C.path.join(C.getcwd(),a,R),T)as M:E.dump({},M)
	with F(C.path.join(C.getcwd(),a,R),N)as M:Q=E.load(M)
	if L in Q and H in Q[L]and J in Q[L][H]:A()
	else:Q.setdefault(L,{}).setdefault(H,{})[J]='downloading'
	with F(C.path.join(C.getcwd(),a,R),T)as M:E.dump(Q,M)
	if P not in O:
		for S in O:
			if S==P:continue
			if G(H)in O[S]and G(J)in O[S][G(H)]:P=S;break
		else:A(f"{B.FAIL}No host available for {H}x{J}{B.ENDC}");I.sleep(2);return
	V=C.path.join(C.getcwd(),a,L)
	if P==U:
		W=O[U][G(H)][G(J)]
		try:X=As(W,V)
		except u as Z:A(f"{B.FAIL}Download failed ({H}x{J}){B.ENDC}");A(Z);I.sleep(2);return
	elif P==Y:
		W=O[Y][G(H)][G(J)]
		try:X=Aq(W,m,V)
		except u as Z:A(f"{B.FAIL}Download failed ({H}x{J}){B.ENDC}");A(Z);I.sleep(2);return
	else:A('Invalid host');I.sleep(2);return
	if X is D:A(f"{B.FAIL}Download failed{B.ENDC}");I.sleep(2);return
	C.makedirs(f"{K}/video/{H}",exist_ok=True);r.move(C.path.join(V,X),f"{K}/video/{H}/{J}.mp4");A(f"Moved to {K}/video/{H}/{J}.mp4")
import requests as R,bs4,js2py,re as g
from yt_dlp import YoutubeDL as Ap
def Aq(url,retry=m,download_folder=D):
	E=download_folder
	try:G,D=Bn(url)
	except u as F:
		A(F)
		if not retry:A(B.WARNING+'Error getting direct url, retrying...'+B.ENDC);return Aq(url,True,E)
		else:A(B.FAIL+'Failed to get direct url! Try again later or switch to another hoster.'+B.ENDC);return
	D=D.replace('"',K);D=D.replace(i,'_');D=D.replace(J,K);D=D.replace('\r',K);H={B6:C.path.join(E,D)}
	with Ap(H)as I:
		try:I.download(G)
		except u as F:pass;delpartfiles()
	return D
def Bn(url):
	D='id=';H={B7:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',B8:BF,B9:v,BA:BG,BB:BH,BC:'none',BD:'?1',BE:'u=1'};I=R.get(url,headers=H);C=K;E=bs4.BeautifulSoup(I.content,w);L=E.find('meta',attrs={'name':BI})[BJ];M=E.find(AH,id='robotlink').find_next('script');B=M.text;B=B.split(J);F=[]
	for G in B:
		if G.startswith("document.getElementById('ide"):F.append(G)
	B=F[-1];B=B.split('document.getElementById')[1];B=B.split('innerHTML = ')[1];B=B.rstrip(';');B=js2py.eval_js(B);B=B.split('?')[1]
	if not B.startswith(D):B=D+g.sub('^.*?=',K,B)
	C='https://streamtape.com/get_video?'+B;A(C);return C,L
import sys as P,os as C,glob,wget as AR
from bs4 import BeautifulSoup as Bo
import base64 as Ar
def As(URL,folderName):
	N='var sources';L=folderName;M=URL;M=G(M);U={B7:'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',B8:BF,B9:v,BA:BG,BB:BH,BC:'none',BD:'?1',BE:'u=1'};H=R.get(M,headers=U);O=Bo(H.content,w)
	if H.text.startswith('<script>'):P="window.location.href = '";Q=e(P);S=H.text.find(P);V=H.text.find("'",S+Q);W=H.text[S+Q:V];return As(W,L)
	X=O.find('meta',attrs={'name':BI});F=X[BJ];F=F.replace(i,'_');A('Name of file: '+F);I=O.find_all(string=g.compile(N));I=G(I);Y=I.index(N);B=I[Y:];Z=B.index(';');B=B[:Z];B=B.replace('var sources = ',K);B=B.replace("'",'"');B=B.replace('\\n',K);B=B.replace('\\',K);a=',';b=K;B=b.join(B.rsplit(a,1));T=E.loads(B)
	try:D=T['mp4'];D=Ar.b64decode(D);D=D.decode(Ac);AR.download(D,out=f"{C.path.join(L,F)}_SS.mp4")
	except B5:
		try:
			D=T['hls'];D=Ar.b64decode(D);D=D.decode(Ac);F=F+'_SS.mp4';c={B6:C.path.join(L,F)}
			with Ap(c)as d:
				try:d.download(D)
				except u as f:pass
		except B5:A('Could not find downloadable URL. Voe might have change their site. Check that you are running the latest version of voe-dl, and if so file an issue on GitHub.');quit()
	A(J);return F
import sys as P,http.server
global Bp
Bp=0
def C5(title='AniWorld Scraper'):
	B=title
	if C.name==A5:C.system(f"title {B}")
	else:A(f"]0;{B}\a")
def h(url):
	Y='span';P='a';H=url
	if A6 not in H:A(B.WARNING+BK+B.ENDC);I.sleep(2);return
	if not BL in H:A(B.WARNING+BM+B.ENDC);I.sleep(2);return
	g=R.get(H);Z=g.text
	if Ad in Z:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Ae);I.sleep(2);return
	E=bs4.BeautifulSoup(Z,w);F=E.find(AH,class_='series-title').find('h1').string;F=F.strip();F=F.split(J)[0];A('Getting info for:',F);h=E.find('p',class_='seri_des').get('data-full-description');N=E.find(Y,itemprop='startDate').string;Q=E.find(Y,itemprop='endDate').string
	if Q=='heute':T='ONGOING'
	else:T='FINISHED'
	C=E.find(AI,string='Staffeln:').parent.parent.parent.find_all('li');C=[A.text for A in C];C=[A.replace(i,K)for A in C];C=[A for A in C if A];C=[A for A in C if A.isnumeric()];C=e(C);L={}
	for a in k(1,S(C)+1):L[a]=Bq(H,a)
	L=L;d=sum(L.values());U=E.find(AH,class_='seriesCoverBox').find('noscript').find('img').get('src');U=A7+U
	try:f=E.find(P,class_='trailerButton').get(AJ)
	except:f=K
	X=E.find_all(P,itemprop='genre');X=[A.string for A in X];j=E.find(AI,class_='seriesProducer').text;l=E.find(AH,class_=Af).get('data-fsk');M=E.find(P,class_='imdb-link')
	if M is not D:M=M.get(AJ)
	else:M=K
	A(T+' ('+N+' - '+Q+') - '+G(d)+' episodes - '+G(C)+' seasons');m={O:F,n:h,BN:{'year':S(N[:4]),'season':N[5:]},b:T,o:L,p:d,c:C,V:N,W:Q,A8:U,BO:f,x:X,BP:j,Af:l,'imdb':M,Ag:H};return m
def AC(info):
	B=info;A('Setting up anime folder...');D=f"{B[O]} ({B[V]}-{B[W]})";D=g.sub(y,K,D);J=f"./{D}";D=f"anime/{D}"
	if not C.path.exists(D):C.makedirs(D)
	with F(f"{D}/info.json",T)as G:E.dump(B,G,indent=4)
	I=B[A8].split('.')[-1]
	if not C.path.exists(f"{D}/image.{I}"):AR.download(B[A8],f"{D}/image.{I}")
	B[A8]=f"image.{I}";B[z]=J
	with F(f"{D}/info.json",T)as G:E.dump(B,G,indent=4)
	if C.path.exists(AK):
		with F(AK,N)as G:H=E.load(G)
	else:H=[]
	L={O:B[O],x:B[x],V:B[V],W:B[W],b:B[b],n:B[n],p:B[p],c:B[c],z:J}
	for(M,P)in Ab(H):
		if P[O]==B[O]:H[M]=L;break
	else:H.append(L)
	with F(AK,T)as G:E.dump(H,G,indent=4)
	A('Anime folder setup complete')
def AS(url,season,episodes=D,info=D):
	S='Season stream urls already exist';Q=url;L=info;I=season;H=episodes
	if H is D:T=R.get(Q);X=T.text;Z=bs4.BeautifulSoup(X,w);H=Z.find(AI,string=BQ).parent.parent.parent;H=H.find_all('li');H=e(H)-1
	A(f"Getting streams for season {I} with {H} episodes...");M=f"{L[O]} ({L[V]}-{L[W]})";M=g.sub(y,K,M);A('Path:',M)
	if C.path.exists(A3+M+A9):
		with F(A3+M+A9,N)as a:
			B=E.load(a);A('Found stream.json');A('Checking if season already exists...')
			if U in B:
				if G(I)in B[U]:A(S);return B
			if Y in B:
				if G(I)in B[Y]:A(S);return B
	else:B={}
	B={}
	for P in k(1,H+1):
		if L is not D:B[P]=AD(Q,I,P,L)
		else:B[P]=AD(Q,I,P)
		At(P/H)
	A(J);A('Done with season',I);return B
def At(percent):A=percent;B=50;C=S(round(B*A));D='='*C+'-'*(B-C);P.stdout.write(f"\rProgress: [{D}] {A*100:.2f}%");P.stdout.flush()
def AD(url,season,episode,info=D):
	b='No stream url found';a=url;Z=info;X=episode;L=season;a=a+f"/staffel-{L}/episode-{X}";e=R.get(a);c=e.text
	if Ad in c:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Ae);I.sleep(2);return
	d=bs4.BeautifulSoup(c,w)
	if Z is not D:J=f"{Z[O]} ({Z[V]}-{Z[W]})";J=g.sub(y,K,J);J=f"anime/{J}/stream.json"
	else:J=f"stream.json"
	M=d.find('i',class_='icon VOE')
	if M is D:A('No voe download found, skipping...');return
	M=M.parent;M=M.get(AJ);M=A7+M;S=Au(M)
	if S is D:A(b);return
	if C.path.exists(J):
		with F(J,N)as Q:H=E.load(Q)
	else:H={}
	if G(U)not in H:H[U]={}
	if G(L)not in H[U]:H[U][G(L)]={}
	H[U][G(L)][G(X)]=S
	with F(J,T)as Q:E.dump(H,Q,indent=4)
	P=d.find('i',class_='icon Streamtape')
	if P is D:A('No streamtape download found, skipping...');return
	P=P.parent;P=P.get(AJ);P=A7+P;S=Au(P)
	if S is D:A(b);return
	if C.path.exists(J):
		with F(J,N)as Q:H=E.load(Q)
	else:H={}
	if G(Y)not in H:H[Y]={}
	if G(L)not in H[Y]:H[Y][G(L)]={}
	H[Y][G(L)][G(X)]=S
	with F(J,T)as Q:E.dump(H,Q,indent=4)
	if H[U][G(L)][G(X)]is not D:return H[U][G(L)][G(X)]
	else:return S
def Au(url):
	B=R.head(url)
	if B.status_code!=302 and B.status_code!=301:A('No redirect found');return
	else:
		C=B.headers['Location']
		if A6 in C:A('Something went wrong with the redirect');return
		else:return C
def Bq(url,season):B=url;B=B+f"/staffel-{season}";C=R.get(B);D=C.text;E=bs4.BeautifulSoup(D,w);A=E.find(AI,string=BQ).parent.parent.parent;A=A.find_all('li');A=e(A)-1;return A
def AT(season,episode,info=D,url=D):
	G=episode;H=season;C=info
	if url is not D:J=AD(url,H,G,info=C)
	L();M()
	if C is D:
		with F(Ah,N)as I:J=E.load(I)
	else:
		B=f"{C[O]} ({C[V]}-{C[W]})";B=g.sub(y,K,B);B=f"anime/{B}"
		with F(B+A9,N)as I:J=E.load(I)
	A(f"Downloading season {H} episode {G}...");AQ(B,H,G)
def AU(season,info=D,url=D):
	H=season;C=info
	if url is not D:P=AS(url,H,info=C)
	if C is D:
		with F(Ah,N)as Q:P=E.load(Q)
	else:
		B=f"{C[O]} ({C[V]}-{C[W]})";B=g.sub(y,K,B);B=f"anime/{B}"
		with F(B+A9,N)as Q:P=E.load(Q)
	R=j(A4)
	for S in P[U][G(H)]:
		L();M()
		def T(season,episode):
			D=season;C=episode
			try:A(f"Downloading season {D} episode {C}...");A(J);AQ(B,D,C)
			except u as E:A(E);A(f"Error downloading episode {C}");return
		X=Ao.Thread(target=T,args=(H,S));X.start()
		while Ao.active_count()>R:I.sleep(1)
def C6(season,start,end,info=D):
	P=season;G=start;C=info
	if C is D:
		with F(Ah,N)as H:Q=E.load(H)
	else:
		B=f"{C[O]} ({C[V]}-{C[W]})";B=g.sub(y,K,B);B=f"anime/{B}"
		with F(B+A9,N)as H:Q=E.load(H)
	for I in k(G,end+1):L();M();A(f"Downloading season {P} episode {I}...");At((I-G)/(end-G));A(J);AQ(B,P,I)
def Av(query):
	F=query
	if F==K or F==D:A(B.WARNING+'No query entered'+B.ENDC);I.sleep(2);return
	G='https://aniworld.to/ajax/search';H={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':A7,'referer':f"https://aniworld.to/search?q={F}",'sec-ch-ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with':'XMLHttpRequest'};C={'keyword':F};C=R.post(G,headers=H,data=C);C=C.text
	try:C=E.loads(C)
	except:
		if Ad in C:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Ae);I.sleep(2);return
		A(f"{B.WARNING}Error parsing JSON{B.ENDC}");A('Try again later');I.sleep(2);return
	return AV(F,C)
def AV(query,data):
	N='Invalid number, try again';G=query;E='link';C=data;C=[A for A in C if'/anime/stream/'in A[E]];C=[A for A in C if'/support/'not in A[E]];C=[A for A in C if'/user/'not in A[E]];C=[A for A in C if'/search/'not in A[E]];C=[A for A in C if Ai not in A[E]];C=[A for A in C if Aj not in A[E]];L();M();A('Search results for:',G);A(J)
	for(Q,F)in Ab(C):F[O]=F[O].replace('<em>',K).replace('</em>',K);A(Q+1,B.OK+F[O]+B.ENDC);A(F[n]);A('---')
	A(B.PRIMARY+'Select a number to continue, or press q to quit'+B.ENDC);D=H()
	if D=='q':return m
	elif not D.isnumeric():A(N);I.sleep(2);AV(G,C);return
	elif S(D)<1 or S(D)>e(C):A(N);I.sleep(2);AV(G,C);return
	D=S(D);R=C[D-1][E];A('Selected:',C[D-1][O]);P=A7+R;A('Aniworld URL:',P);return P
def Aw():
	B=3333;D=http.server.SimpleHTTPRequestHandler;E=C.path.join(C.getcwd(),d);C.chdir(E)
	with http.server.HTTPServer(('0.0.0.0',B),D)as F:A('serving at http://localhost:'+G(B)+'/');A('Press Ctrl+C to stop the server');F.serve_forever()
def AW():
	S='Removed:';U='index.html';L();M();A('Running cleanup...');Y=[C.path.join(B,A)for(B,E,D)in C.walk('./downloads')for A in D if A.endswith('.part')or A.endswith('.ytdl')]
	if Y:
		A(B.WARNING+'Do you want to delete non finished downloads? After deleting you have to restart the download'+B.ENDC);A('Do you want to continue? (y/N)');J=H()
		if J.lower()=='y':
			A('Deleting files...')
			for I in Y:C.remove(I);A('Deleted:',I)
	A('Rebuilding index.json...');P=[A for A in C.listdir(d)if C.path.isdir(C.path.join(d,A))];Z=[]
	for G in P:
		if not C.listdir(f"anime/{G}"):C.rmdir(f"anime/{G}");continue
		if not C.path.exists(f"anime/{G}/info.json"):continue
		if C.path.exists(f"anime/{G}/stream.json"):C.remove(f"anime/{G}/stream.json")
		with F(f"anime/{G}/info.json",N)as R:D=E.load(R)
		if Ag not in D:
			A('No url found for:','/'+G+'/ ('+D[O]+')'+', should we remove it? (Y/n)');J=H()
			if J.lower()=='n':continue
			A('Removing:',D[O]);r.rmtree(f"anime/{G}");continue
		if A3 in D[z]:D[z]=D[z].replace(A3,K)
		e=[O,n,BN,b,o,p,c,V,W,A8,BO,x,BP,Af,'imdb']
		if not all(A in D for A in e):A('Rebuilding info.json for:',D[O]);D=h(D[Ag]);AC(D)
		Z.append({O:D[O],x:D[x],V:D[V],W:D[W],b:D[b],n:D[n],p:D[p],c:D[c],z:f"{G}"})
	with F(AK,T)as R:E.dump(Z,R,indent=4)
	A('Cleaning file structure...')
	if C.path.exists(U):C.remove(U)
	f=['urls.txt','search.html','search.txt','temp.html',AA,'update.exe'];A('Removing unused files...')
	for I in f:
		if C.path.exists(I):C.remove(I);A(S,I)
	if C.path.exists(X):r.rmtree(X);A('Removed: assets/')
	if C.path.exists(a):
		P=[A for A in C.listdir(a)if C.path.isdir(C.path.join(a,A))]
		for G in P:
			if not C.listdir(f"downloads/{G}"):C.rmdir(f"downloads/{G}");A(S,f"downloads/{G}")
	Br();A('Done');A(q);H();Q()
def Br():
	D='video';I=[A for A in C.listdir(C.path.join(C.getcwd(),d))if C.path.isdir(C.path.join(C.getcwd(),d,A))]
	if X in I:I.remove(X)
	G={}
	for B in I:
		if not C.path.exists(C.path.join(C.getcwd(),d,B,D)):continue
		J=[A for A in C.listdir(C.path.join(C.getcwd(),d,B,D))if C.path.isdir(C.path.join(C.getcwd(),d,B,D,A))];G[B]={}
		for H in J:
			G[B][H]={};K=[A for A in C.listdir(C.path.join(C.getcwd(),d,B,D,H))if C.path.isfile(C.path.join(C.getcwd(),d,B,D,H,A))]
			for L in K:M=L.split('.')[0];G[B][H][M]='downloaded'
	if not C.path.exists(C.path.join(C.getcwd(),a)):C.makedirs(C.path.join(C.getcwd(),a))
	with F(C.path.join(C.getcwd(),'downloads/downloads.json'),T)as N:E.dump(G,N,indent=4)
	A('downloads.json rebuilt')
def Ax(url):
	C='episode';D='staffel';B=url
	if A6 not in B:A(Ak);return m
	if D in B:B=B.split(D)[0]
	if C in B:B=B.split(C)[0]
	return B
def Bs():
	if not C.path.exists(Z):Bv();return
	if C.path.exists(AA):C.remove(AA)
	elif not C.path.exists(AL):C.makedirs(AL)
def AE(key,value):
	if C.path.exists(Z):
		with F(Z,N)as A:B=E.load(A)
	else:B={}
	B[key]=value
	with F(Z,T)as A:E.dump(B,A,indent=4)
def Bt():
	if C.path.exists(AA):C.remove(AA)
	L();M();A(B.PRIMARY+'Update finished'+B.ENDC);A('The program has been updated, YIPPIE!');A(q);H();AX()
def Bu():AY()
def A1():return m
def s():
	B='./assets/animeList.json';return;A(BR);H='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database-minified.json';I='https://api.github.com/repos/manami-project/anime-offline-database/commits?path=anime-offline-database-minified.json&page=1&per_page=1';J=R.get(I);D=J.json();K=D[0]['commit']['committer']['date'][:10]
	if C.path.exists(B):
		with F(B,N)as G:D=E.load(G)
		L=D['lastUpdate']
		if L==K:A('Anime list is up to date');return
	A('Downloading anime list...');AR.download(H,B);D=E.load(F(B,N,encoding=Ac))
	with F(B,T)as G:E.dump(D,G,indent=4)
	A('Anime list downloaded')
def L():A('\x1b[H\x1b[J')
def Q():
	F='Info';G='\nPress enter to continue';K='Unsupported os';N='posix';O='Enter the url of the anime';P='Invalid key';L();M();A('Press one of the following keys:');A(BS);A(BT);A(BU);A(BV);A(BW);A(BX);A(BY);A(BZ);A(Ba);D=H()
	if D not in[v,'2','3','4','5','6','7','8','9','0','q','Q','h','i']:A(P);Q();return
	if D==v:B4()
	elif D=='x':
		A('This mode will download everything from the given url');A(O);E=H();E=Ax(E)
		if not E:A(B.WARNING+Ak+B.ENDC);I.sleep(2);Q();return
		B3(E)
	elif D=='2':A('Not implemented yet');I.sleep(2);Q()
	elif D=='3':Aw()
	elif D=='4':AW()
	elif D=='5':
		if C.name==A5:C.system('start .\\anime')
		elif C.name==N:C.system('xdg-open .\\anime')
		else:A(K);A('The anime folder is located in the following directory:');A(C.getcwd()+'\\anime');A(G);H();Q()
		Q()
	elif D=='6':
		A(O);E=H();E=Ax(E)
		if not E:A(B.WARNING+Ak+B.ENDC);I.sleep(2);Q();return
		A(h(E))
	elif D=='0':Bu();Q()
	elif D=='h'or D=='i':
		L();M();A(B.PRIMARY+F+B.ENDC);A(J);A(f"{B.OK}This program was made by JMcrafter26 and published by Someone266 on Github{B.ENDC}");A(f"{B.OK}The program is open source and can be found here: https://github.com/Someone266/aniworld-downloader/{B.ENDC}");A(J);A('This program is still in development, so there might be some bugs');A('If you find a bug, please report it on the Github page');A(J);A(f"{B.OK}This program is for educational purposes only, the developer nor the publisher is responsible for any damage caused by the program. This program is not affiliated with any of the anime sites. This program is provided as is, without any warranty. Use at your own risk.{B.ENDC}");A(J);A('Press enter to continue (i to report a bug)');D=H()
		if D=='i':
			A('Opening the Github page...')
			if C.name==A5:C.system('start https://github.com/Someone266/aniworld-downloader/issues');I.sleep(2)
			elif C.name==N:C.system('xdg-open https://github.com/Someone266/aniworld-downloader/issues');I.sleep(2)
			else:A(K);A('The Github page is located at the following link:');A('https://github.com/Someone266/aniworld-downloader/issues');A(G);H()
		L();M();A(B.PRIMARY+F+B.ENDC);A(J);A(f"{B.OK}Your Version is: {AG()}{B.ENDC}")
		if A1():A(f"{B.OK}You are running the windows version (Congratulations){B.ENDC}")
		A(f"{B.OK}Your mode is: "+j(A0)+f"{B.ENDC}");A(f"{B.OK}Your preferred host is: "+j(l)+f"{B.ENDC}")
		if j(AB)==Al:A(f"{B.OK}Auto update is enabled{B.ENDC}")
		else:A(f"{B.WARNING}Auto update is disabled{B.ENDC}");A(f"{B.WARNING}You might miss out on new features and bug fixes{B.ENDC}");A(f"{B.PRIMARY}Press SPACE to check and download updates{B.ENDC}")
		A(J);D=H()
		if D==i:B1(True);I.sleep(2);Q();return
		A_()
	elif D=='q'or D=='Q':A('Quitting, Bye!');A2()
	else:A(B.WARNING+P+B.ENDC);I.sleep(2);Q();return
def Bv():
	D='./assets';L();M();A(B.PRIMARY+'Hi and welcome to AniWorld-Down v'+AG()+B.ENDC);A('It looks like this is your first time running this program, or you have deleted some files :)');A('This guide will help you get started with the program\n');A(B.WARNING+'This directory will be used to store the anime and the assets'+B.ENDC);A(B.SECONDARY+q+B.ENDC);H()
	if not C.path.exists(AL):C.makedirs(AL)
	if not C.path.exists(D):C.makedirs(D)
	Bw()
def Bw():
	E='updateNotes';F='Update notes:';L();M();A(B.PRIMARY+'Step 1: Checking for updates and downloading assets'+B.ENDC);A('We promise, it will be quick');C=B2()
	if C is D:A('Hmm, something went wrong with the update check');A('Do you have an internet connection? \n');A(B.SECONDARY+'PS: We need an internet connection to download the assets'+B.ENDC);A(B.SECONDARY+AM+B.ENDC);H();A2()
	if C[b]=='error':A(B.WARNING+Am+B.ENDC);A(An,C[Bb]);A('Please try again later\n');A(B.SECONDARY+AM+B.ENDC);H();A2()
	elif C[b]==Bc:A(Bd);A(B.SECONDARY+q+B.ENDC);H();AX();return
	else:
		if C[AN][X]:A(B.OK+Be+B.ENDC);A(F);A(C[E][X]+J);AF(X,C[AO][X])
		if C[AN][f]:A(B.OK+Bf+B.ENDC);A(F);A(C[E][f]+J);AF(f,C[AO][f])
		else:A('No program update available')
		A(B.SECONDARY+q+B.ENDC);H();AX();return
def AX():L();M();A(B.PRIMARY+'Step 2: Configuring the program'+B.ENDC);A('We need to configure the program before we can continue');A('It is very simple, just answer a few questions');A(B.SECONDARY+q+B.ENDC);H();Ay()
def Ay():
	L();M();A(B.PRIMARY+'Choose the option that describes you the best'+B.ENDC);A('1. I want to archive anime and have it nicely organized (with filestructure, prictures and an offline webserver)');A('2. I just want to download anime fast and continue watching (No filestructure, ready to watch or move)');A(J);A(B.SECONDARY+Bg+B.ENDC);C=H()
	if C==v:AE(A0,Bh)
	elif C=='2':AE(A0,Bi)
	else:A(Bj);Ay();return
	Az()
def Az():
	L();M();A(B.PRIMARY+'Select your preferred host'+B.ENDC);A('1. Voe (Recommended)');A('2. Streamtape');A(J);A(B.SECONDARY+Bg+B.ENDC);C=H()
	if C==v:AE(l,U)
	elif C=='2':AE(l,Y)
	else:A(Bj);Az();return
	Bx()
def Bx():
	L();M();A(B.PRIMARY+'Thats it, you are ready to go'+B.ENDC);A('You can now start downloading anime');A(J);A('Press i to read the instructions');A('Press enter to just freakin start the program');C=H()
	if C=='i':A_()
	Q()
def A_():L();M();A(B.PRIMARY+'Instructions'+B.ENDC);A(BS);A('This option will guide you through the download process, you just need to enter the url of the anime');A(BT);A('This option is not implemented yet');A(BU);A('This option will start a webserver to serve the content - you can watch the anime in your browser (even offline and other devices)');A(BV);A('This option will clean up the program and the assets');A(BW);A('This option will open the anime folder where the anime is stored');A(BX);A('This option will get the info of the anime from the url');A(BY);A('This option will allow you to change the settings of the program');A(BZ);A('This is the current screen :)');A(Ba);A(J);A(q);H();Q()
B0={A0:"The mode of AniDown\n'archive' will organize the anime with filestructure, pictures and an offline webserver\n'download' will download anime fast and continue watching",l:'The preferred host to download from',AB:'Automatically update the program on startup (Recommended, as this will fix bugs and add new features)',A4:'Number of threads to use for downloading (Default: 5)'}
t={A0:[Bh,Bi],l:[U,Y],AB:[Al,'no'],A4:[5,1,2,3,4,6,7,8,9,10]}
type={A0:AP,l:AP,AB:AP,A4:Bk}
def AY():
	K=f"{C.getcwd()}\\settings.json";L();A('Settings:');A('Path:',K);A(J)
	with F(Z,N)as M:I=E.load(M)
	for(D,O)in I.items():P=list(I.keys()).index(D)+1;A(f"{B.PRIMARY}({P}) - {D}: {O}{B.ENDC}");A(f"{B.OK}Description: {B.ENDC}{B.SECONDARY}{B0[D]}{B.ENDC}");A(f"{B.OK}Options: {B.ENDC}{B.SECONDARY}{t[D]}{B.ENDC}");A('---')
	A('Choose an option by pressing the number (q to quit):');G=H()
	if not G or G=='q':return
	if not G.isdigit():return AY()
	AZ(S(G),I);return AY()
def AZ(option,data):
	G=data;C=option;D=list(G.keys())[C-1];L();A(f"Changing '{D}'")
	if type[D]==AP:
		A(f"{B.OK}Options:\n{B.ENDC}")
		for(I,C)in Ab(t[D]):A(f"({I+1}) - {C}")
		A('Choose an option by pressing the number:');C=H()
		if not C.isdigit():return AZ(C,G)
		if S(C)>e(t[D]):return AZ(C,G)
		G[D]=t[D][S(C)-1]
	else:
		if type[D]=='text':A('Enter the new value (Text/String):')
		elif type[D]==Bk:A('Enter the new value (Number):')
		J=H();G[D]=J
	with F(Z,T)as K:E.dump(G,K)
def j(key):
	A=key
	with F(Z,N)as C:B=E.load(C)
	if A not in B:
		B[A]=t[A][0]
		with F(Z,T)as C:E.dump(B,C)
	return B[A]
def By():
	A={}
	with F(Z,N)as B:A=E.load(B)
	for C in B0:
		if C not in A:A[C]=t[C][0]
	with F(Z,T)as B:E.dump(A,B)
	return A
import zipfile
def B1(force=m):
	Bs();L();M();A('Loading...')
	try:By()
	except:A('Something went wrong with the settings file')
	if j(AB)=='no'and not force:A('Skipping update check');I.sleep(2);return
	try:B=B2()
	except:A(Am);I.sleep(2);return
	if B is D:A('No internet connection, skipping update check');return
	if B[b]=='error':A(Am);A(An,B[Bb]);I.sleep(2);return
	elif B[b]==Bc:A(Bd);return
	else:
		if B[AN][X]:A(Be);AF(X,B[AO][X])
		if B[AN][f]:A(Bf);AF(f,B[AO][f])
def B2():
	E='anime/assets/.version';A(BR,end=K)
	try:R.get('https://api.jm26.net/status.txt',timeout=5)
	except R.exceptions.ConnectionError:A(' Skipped');A(B.WARNING+Bl+B.ENDC);I.sleep(2);return
	H='https://api.jm26.net/update/aniworld-down/check/';J=AG()
	if not C.path.exists(E):G='0.0.0'
	else:
		with F(E,N)as L:G=L.read()
	D={f:J,X:G};M=R.post(H,data=D);D=M.json();A(' Done');return D
def AF(type,hash):
	Q='anime/assets';S='Please try again later';E='./update';A('Downloading ..');L=f"https://api.jm26.net/update/aniworld-down/download/?type={type}&hash={hash}";M='./update/update.zip'
	if A1():L=L+'&os=windows'
	if not C.path.exists(E):C.makedirs(E)
	try:O=R.get(L)
	except R.exceptions.ConnectionError:A(B.WARNING+Bl+B.ENDC);A(S);A(AM);H();A2()
	if O.headers['Content-Type']=='application/json':A(B.WARNING+'Something went wrong with the download'+B.ENDC);A(An,O.text);A(S);A(AM);H();A2()
	A(B.OK+Bm+B.ENDC)
	with F(M,'wb')as G:G.write(O.content)
	with zipfile.ZipFile(M,N)as T:T.extractall(E)
	C.remove(M)
	if C.path.exists(Q):r.rmtree(Q)
	for D in C.listdir(E):
		if C.path.isdir(f"./update/{D}"):
			if not C.path.exists(f"./{D}"):C.makedirs(f"./{D}")
			for G in C.listdir(f"./update/{D}"):r.move(C.path.join(f"./update/{D}",G),C.path.join(f"./{D}",G))
			C.rmdir(f"./update/{D}")
		else:r.move(C.path.join(E,D),C.path.join('./',D))
	C.rmdir(E);A(B.OK+'Update complete'+B.ENDC);A(J);A(f"{B.WARNING}It is recommended to run the {B.ENDC}{B.OK}clean option{B.ENDC}{B.WARNING} after updating{B.ENDC}");A(J)
	if type==f:
		for U in k(3):A(f"\rRestarting in {3-U} seconds",end=K);I.sleep(1)
		A('\rRestarting program...')
		if not C.path.exists(Z):
			if A1():C.system(f"start update.bat guideUpdateFinished")
			elif C.name==A5:C.system('py main.py guideUpdateFinished')
			else:C.system(f"python3 main.py guideUpdateFinished")
		elif A1():C.system(f"start update.bat "+i.join(P.argv[1:]))
		elif C.name==A5:C.system('py main.py '+i.join(P.argv[1:]))
		else:C.system('python3 main.py '+i.join(P.argv[1:]))
Bz='1.2.0'
class B:PURPLE='\x1b[95m';SECONDARY='\x1b[90m';PRIMARY='\x1b[94m';CYAN='\x1b[96m';OK='\x1b[92m';WARNING='\x1b[93m';FAIL='\x1b[91m';ENDC='\x1b[0m';BOLD='\x1b[1m';UNDERLINE='\x1b[4m'
def B3(url):
	E=url;s();C=h(E);AC(C)
	for D in C[o]:AS(E,D,C[o][D],C)
	F=C[c];A(F)
	for D in k(1,F+1):AU(D,C,E)
	AW();M();A(B.OK+'Finished downloading all episodes'+B.ENDC);A(J);A(B.PRIMARY+"Run 'serve' to watch the episodes in your browser"+B.ENDC)
def B4():
	L();M();s();A(B.OK+'This is the auto mode. It will ask you what to download.'+B.ENDC);A(J);A('Enter the name of the anime you want to search for or paste the url of the anime');E=H()
	if E.startswith('http'):
		C=E
		if A6 not in C:A(B.WARNING+BK+B.ENDC);I.sleep(2);return
		if not BL in C:A(B.WARNING+BM+B.ENDC);I.sleep(2);return
		if Ai in C:C=C.split(Ai)[0]
		if Aj in C:C=C.split(Aj)[0]
	elif E!=K and E!=D:
		C=Av(E)
		if C==m:A('Quit');Q();return
		elif A6 not in C:A(B.WARNING+'Invalid url! There was an error with the search'+B.ENDC);I.sleep(2);return
	else:Q();return
	F=h(C);AC(F);Aa(C,F)
def Aa(url,info):
	F=url;C=info;M();A(B.OK+'Setup complete'+B.ENDC);A(J);A(B.OK+'We found '+G(C[c])+' seasons and a total of '+G(C[p])+' episodes'+B.ENDC);A(J);A('Do you want to download all episodes? (Y/n)');L=H()
	if L!='Y'and L!='y'and L!=Al and L!='Yes'and L!=K:
		A('Which season do you want to download?');E=S(H());A('What episode do you want to download? (Enter 0 to download all episodes; use - to download a range of episodes)');D=S(H())
		if E<1 or E>C[c]:A(B.FAIL+'Invalid season'+B.ENDC);I.sleep(2);Aa(F,C);return
		if D==0:AU(E,C,F)
		elif'-'in G(D)or','in G(D):
			if'-'in G(D):
				O=S(D.split('-')[0]);P=S(D.split('-')[1])
				for N in k(O,P+1):AT(E,N,C,F)
			elif','in G(D):
				R=D.split(',')
				for N in R:AT(E,S(N),C,F)
		else:
			if D<1 or D>C[o][E]:A(B.FAIL+'Invalid episode'+B.ENDC);I.sleep(2);Aa(F,C);return
			AT(E,D,C,F)
	else:
		A(B.OK+'Downloading all episodes'+B.ENDC)
		for E in k(1,C[c]+1):AU(E,C,F)
	A(B.OK+Bm+B.ENDC);A(J);A(B.PRIMARY+'Press enter to return to the main menu'+B.ENDC);H();Q()
def AG():return Bz
def B_(url):s();A=h(url);return A
def C0(url):s();A=h(url);AC(A)
def C1(url,season,info=D):
	A=season;s();B=D
	if info is not D:B=info[o][A]
	C=AS(url,A,B);return C
def C2(url,season,episode,info=D):
	C=season;A=info;B=episode;s()
	if A is not D:B=A[o][C][B]
	E=AD(url,C,B,A);return E
def C3():L();M();A('Enter the name of the anime you want to search for');B=H();return Av(B)
def M():
	A(J);C=AG()
	if A1():C=C+' (Windows)'
	A(B.CYAN+'    AA          W     W         ll     d     DDD                    '+B.ENDC);A(B.CYAN+'   A  A      ii W     W          l     d     D  D                   '+B.ENDC);A(B.CYAN+'   AAAA nnn     W  W  W ooo rrr  l   ddd     D  D ooo w   w nnn     '+B.ENDC);A(B.CYAN+'   A  A n  n ii  W W W  o o r    l  d  d     D  D o o w w w n  n    '+B.ENDC);A(B.CYAN+'   A  A n  n ii   W W   ooo r   lll  ddd     DDD  ooo  w w  n  n    '+B.ENDC);A(B.CYAN+'                                                                    '+B.ENDC);A('A powerful scraper and downloader for AniWorld');A(i);A('Version: '+C+'                                 Made by JMcrafter26');A(B.SECONDARY+'DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.'+B.ENDC);A(B.SECONDARY+'Please respect the laws of your country and the country of the website you are scraping.'+B.ENDC);A(J)
def C4():
	H='help';I='clean';K='serve';N='search'
	if e(P.argv)==1:P.argv.append('ui')
	C=P.argv[1]
	if C=='guideUpdateFinished':Bt();return
	B1();L();M();A(J)
	if C=='getinfo':E=P.argv[3];A(B_(E))
	elif C=='run':E=P.argv[2];B3(E)
	elif C=='ui':Q()
	elif C==N:C3();return
	elif C==K:Aw()
	elif C==I:AW()
	elif C=='setup':E=P.argv[3];C0(E)
	elif C=='auto':B4()
	elif C=='getseason':
		E=P.argv[3];G=P.argv[5];F=D
		if e(P.argv)>6:F=h(E)
		A(C1(E,G,F))
	elif C=='getepisode':
		E=P.argv[3];G=P.argv[5];O=P.argv[7];F=D
		if e(P.argv)>8:F=h(E)
		A(C2(E,G,O,F))
	elif C==H:A(B.PRIMARY+'Commands:'+B.ENDC);A('-----------------');A('run -url <url>');A(K);A(I);A(N);A('setup -url <url>');A('getinfo -url <url>');A('getseason -url <url> -season <season>');A('getepisode -url <url> -season <season> -episode <episode>');A(H)
	else:A(B.WARNING+'Invalid command'+B.ENDC)
	A(J)
if __name__=='__main__':C4()