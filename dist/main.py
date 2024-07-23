# Aniworld Scraper
# Author: JMcrafter26
# Description: A scraper for aniworld (german anime site)
# Version: see version variable below
# License: MIT License
# DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.
# Please respect the laws of your country and the country of the website you are scraping.

# This code was minified to save space. If you want to read the code, please read the original files.


Bf='Download complete'
Be='No internet connection'
Bd='Invalid option, try again'
Bc='download'
Bb='archive'
Ba='Choose an option by pressing the number'
BZ='There is a program update available'
BY='Downloading assets...'
BX='You are up to date'
BW='success'
BV='message'
BU='Something went wrong with the update check'
BT='q. Quit'
BS='h. Help/Info'
BR='0. Settings'
BQ='6. Get anime info'
BP='5. Open anime folder'
BO='4. Clean up'
BN='3. Serve content'
BM='2. Continue Download'
BL='1. Download Assistant'
BK='Checking for updates...'
BJ='Episoden:'
BI='producer'
BH='trailer'
BG='animeSeason'
BF='This type of url is not supported yet. It may be supported in the future'
BE='anime/stream'
BD='Invalid url! Please enter a valid aniworld.to url'
BC='content'
BB='og:title'
BA='navigate'
B9='document'
B8='de,en-US;q=0.7,en;q=0.3'
B7='Priority'
B6='Sec-Fetch-User'
B5='Sec-Fetch-Site'
B4='Sec-Fetch-Mode'
B3='Sec-Fetch-Dest'
B2='Upgrade-Insecure-Requests'
B1='Accept-Language'
B0='User-Agent'
A_='outtmpl'
Az=KeyError
Ak='option'
Aj='Error:'
Ai='Invalid url'
Ah='/staffel-'
Ag='/episode-'
Af='stream.json'
Ae='url'
Ad='fsk'
Ac='Or paste your cookie key in the settings'
Ab='DDoS-Guard'
Aa='utf-8'
AZ=False
AY=enumerate
AX=Exception
AJ='updateHash'
AI='update'
AH='Press enter to exit'
AG='./anime'
AF='./anime/index.json'
AE='href'
AD='strong'
AC='aniworld.to'
AB='nt'
AA='div'
A4='mode'
A3='downloads'
A2='update.bat'
A1='/stream.json'
A0='picture'
z='https://aniworld.to'
y='anime/'
x=exit
v='pathname'
u='[<>:"/\\\\|?*]'
t='tags'
s='prefHost'
r='html.parser'
q='1'
p=range
l='totalEpisodes'
k='description'
j=' '
i='Press enter to continue'
f='program'
e='settings.json'
d='seasons'
c='episodes'
b='status'
a='anime'
Z='streamtape'
Y='assets'
X='enddate'
W='startdate'
V=len
T='w'
S=int
Q='voe'
O='r'
N='title'
J=''
I='\n'
H=str
G=input
F=None
E=open
A=print
import requests as R,bs4 as w,js2py,re as g
from yt_dlp import YoutubeDL as Al
def Am(url,retry=AZ):
	try:E,C=Bg(url)
	except AX as D:
		A(D)
		if not retry:A(B.WARNING+'Error getting direct url, retrying...'+B.ENDC);return Am(url,True)
		else:A(B.FAIL+'Failed to get direct url! Try again later or switch to another hoster.'+B.ENDC);return
	C=C.replace('"',J);C=C.replace(j,'_');C=C.replace(I,J);C=C.replace('\r',J);F={A_:C}
	with Al(F)as G:
		try:G.download(E)
		except AX as D:pass;Ao()
	return C
def Bg(url):
	D='id=';H={B0:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',B1:B8,B2:q,B3:B9,B4:BA,B5:'none',B6:'?1',B7:'u=1'};K=R.get(url,headers=H);C=J;E=w.BeautifulSoup(K.content,r);L=E.find('meta',attrs={'name':BB})[BC];M=E.find(AA,id='robotlink').find_next('script');B=M.text;B=B.split(I);F=[]
	for G in B:
		if G.startswith("document.getElementById('ide"):F.append(G)
	B=F[-1];B=B.split('document.getElementById')[1];B=B.split('innerHTML = ')[1];B=B.rstrip(';');B=js2py.eval_js(B);B=B.split('?')[1]
	if not B.startswith(D):B=D+g.sub('^.*?=',J,B)
	C='https://streamtape.com/get_video?'+B;A(C);return C,L
import sys as P,os as C,glob,json as D,wget as AK
from bs4 import BeautifulSoup as Bh
import base64 as An
def Bi(URL):
	L='var sources';K=URL;K=H(K);S={B0:'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',B1:B8,B2:q,B3:B9,B4:BA,B5:'none',B6:'?1',B7:'u=1'};F=R.get(K,headers=S);M=Bh(F.content,r)
	if F.text.startswith('<script>'):N="window.location.href = '";O=V(N);P=F.text.find(N);T=F.text.find("'",P+O);U=F.text[P+O:T];return download(U)
	W=M.find('meta',attrs={'name':BB});E=W[BC];E=E.replace(j,'_');A('Name of file: '+E);G=M.find_all(string=g.compile(L));G=H(G);X=G.index(L);B=G[X:];Y=B.index(';');B=B[:Y];B=B.replace('var sources = ',J);B=B.replace("'",'"');B=B.replace('\\n',J);B=B.replace('\\',J);Z=',';a=J;B=a.join(B.rsplit(Z,1));Q=D.loads(B)
	try:C=Q['mp4'];C=An.b64decode(C);C=C.decode(Aa);AK.download(C,out=f"{E}_SS.mp4")
	except Az:
		try:
			C=Q['hls'];C=An.b64decode(C);C=C.decode(Aa);E=E+'_SS.mp4';b={A_:E}
			with Al(b)as c:
				try:c.download(C)
				except AX as d:pass
			Ao()
		except Az:A('Could not find downloadable URL. Voe might have change their site. Check that you are running the latest version of voe-dl, and if so file an issue on GitHub.');quit()
	A(I);return E
def Ao():
	A=C.getcwd()
	for B in glob.iglob(C.path.join(A,'*.part')):C.remove(B)
import os as C,shutil as m,time as K
def AL(path,season,episode):
	U='/downloads';R='downloads.json';J=path;I=episode;G=season
	if J is not F and G is not F and I is not F:
		if C.path.exists(f"{J}/video/{G}/{I}.mp4"):A(f"{B.WARNING}File {J}/video/{G}/{I}.mp4 already exists. Skipping...{B.ENDC}");return
	if not C.path.exists(C.getcwd()+U):C.makedirs(C.getcwd()+U)
	L=J.split(y)[1]
	if not C.path.exists(f"downloads/{L}"):C.makedirs(f"downloads/{L}")
	V=Bt(s)
	with E(f"{J}/stream.json",O)as M:W=D.load(M)
	C.chdir(f"downloads/")
	if not C.path.exists(R):
		with E(R,T)as M:D.dump({},M)
	with E(R,O)as M:N=D.load(M)
	if L in N and G in N[L]and I in N[L][G]:A()
	else:N.setdefault(L,{}).setdefault(G,{})[I]='downloading'
	with E(R,T)as M:D.dump(N,M)
	C.chdir(f"{L}")
	if V==Q:S=W[Q][H(G)][H(I)];P=Bi(S)
	elif V==Z:S=W[Z][H(G)][H(I)];P=Am(S)
	else:A('Invalid host');K.sleep(2);return
	if P is F:A(f"{B.FAIL}Download failed{B.ENDC}");K.sleep(2);return
	C.chdir('../../');C.makedirs(f"{J}/video/{G}",exist_ok=True);P=f"downloads/{L}/{P}";m.move(f"{P}",f"{J}/video/{G}/{I}.mp4");A(f"Moved to {J}/video/{G}/{I}.mp4")
import sys as P,http.server
def C1(title='AniWorld Scraper'):
	B=title
	if C.name==AB:C.system(f"title {B}")
	else:A(f"]0;{B}\a")
def h(url):
	Z='span';P='a';G=url
	if AC not in G:A(B.WARNING+BD+B.ENDC);K.sleep(2);return
	if not BE in G:A(B.WARNING+BF+B.ENDC);K.sleep(2);return
	g=R.get(G);a=g.text
	if Ab in a:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Ac);K.sleep(2);return
	D=w.BeautifulSoup(a,r);E=D.find(AA,class_='series-title').find('h1').string;E=E.strip();E=E.split(I)[0];A('Getting info for:',E);h=D.find('p',class_='seri_des').get('data-full-description');O=D.find(Z,itemprop='startDate').string;Q=D.find(Z,itemprop='endDate').string
	if Q=='heute':T='ONGOING'
	else:T='FINISHED'
	C=D.find(AD,string='Staffeln:').parent.parent.parent.find_all('li');C=[A.text for A in C];C=[A.replace(j,J)for A in C];C=[A for A in C if A];C=[A for A in C if A.isnumeric()];C=V(C);L={}
	for e in p(1,S(C)+1):L[e]=Bj(G,e)
	L=L;f=sum(L.values());U=D.find(AA,class_='seriesCoverBox').find('noscript').find('img').get('src');U=z+U;i=D.find(P,class_='trailerButton').get(AE);Y=D.find_all(P,itemprop='genre');Y=[A.string for A in Y];m=D.find(AD,class_='seriesProducer').text;n=D.find(AA,class_=Ad).get('data-fsk');M=D.find(P,class_='imdb-link')
	if M is not F:M=M.get(AE)
	else:M=J
	A(T+' ('+O+' - '+Q+') - '+H(f)+' episodes - '+H(C)+' seasons');o={N:E,k:h,BG:{'year':S(O[:4]),'season':O[5:]},b:T,c:L,l:f,d:C,W:O,X:Q,A0:U,BH:i,t:Y,BI:m,Ad:n,'imdb':M,Ae:G};return o
def A5(info):
	B=info;A('Setting up anime folder...');F=f"{B[N]} ({B[W]}-{B[X]})";F=g.sub(u,J,F);F=f"anime/{F}";I=f"./{F}"
	if not C.path.exists(F):C.makedirs(F)
	with E(f"{F}/info.json",T)as G:D.dump(B,G,indent=4)
	K=B[A0].split('.')[-1]
	if not C.path.exists(f"{I}/image.{K}"):AK.download(B[A0],f"{I}/image.{K}")
	B[A0]=f"image.{K}";B[v]=I
	with E(f"{F}/info.json",T)as G:D.dump(B,G,indent=4)
	if C.path.exists(AF):
		with E(AF,O)as G:H=D.load(G)
	else:H=[]
	L={N:B[N],t:B[t],W:B[W],X:B[X],b:B[b],k:B[k],l:B[l],d:B[d],v:I}
	for(M,P)in AY(H):
		if P[N]==B[N]:H[M]=L;break
	else:H.append(L)
	with E(AF,T)as G:D.dump(H,G,indent=4)
	A('Anime folder setup complete')
def AM(url,season,episodes=F,info=F):
	T='Season stream urls already exist';S=url;L=info;K=season;G=episodes
	if G is F:U=R.get(S);Y=U.text;a=w.BeautifulSoup(Y,r);G=a.find(AD,string=BJ).parent.parent.parent;G=G.find_all('li');G=V(G)-1
	A(f"Getting streams for season {K} with {G} episodes...");M=f"{L[N]} ({L[W]}-{L[X]})";M=g.sub(u,J,M);A('Path:',M)
	if C.path.exists(y+M+A1):
		with E(y+M+A1,O)as b:
			B=D.load(b);A('Found stream.json');A('Checking if season already exists...')
			if Q in B:
				if V(B[Q][H(K)])>=1:A(T);return B
			if Z in B:
				if V(B[Z][H(K)])>=1:A(T);return B
	else:B={}
	B={}
	for P in p(1,G+1):
		if L is not F:B[P]=AO(S,K,P,L)
		else:B[P]=AO(S,K,P)
		AN(P/G)
	A(I);A('Done with season',K);return B
def AN(percent):A=percent;B=50;C=S(round(B*A));D='='*C+'-'*(B-C);P.stdout.write(f"\rProgress: [{D}] {A*100:.2f}%");P.stdout.flush()
def AO(url,season,episode,info=F):
	b='No stream url found';a=url;Y=info;V=episode;L=season;a=a+f"/staffel-{L}/episode-{V}";e=R.get(a);c=e.text
	if Ab in c:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Ac);K.sleep(2);return
	d=w.BeautifulSoup(c,r)
	if Y is not F:I=f"{Y[N]} ({Y[W]}-{Y[X]})";I=g.sub(u,J,I);I=f"anime/{I}/stream.json"
	else:I=f"stream.json"
	M=d.find('i',class_='icon VOE')
	if M is F:A('No voe download found, skipping...');return
	M=M.parent;M=M.get(AE);M=z+M;U=Ap(M)
	if U is F:A(b);return
	if C.path.exists(I):
		with E(I,O)as S:G=D.load(S)
	else:G={}
	if H(Q)not in G:G[Q]={}
	if H(L)not in G[Q]:G[Q][H(L)]={}
	G[Q][H(L)][H(V)]=U
	with E(I,T)as S:D.dump(G,S,indent=4)
	P=d.find('i',class_='icon Streamtape')
	if P is F:A('No streamtape download found, skipping...');return
	P=P.parent;P=P.get(AE);P=z+P;U=Ap(P)
	if U is F:A(b);return
	if C.path.exists(I):
		with E(I,O)as S:G=D.load(S)
	else:G={}
	if H(Z)not in G:G[Z]={}
	if H(L)not in G[Z]:G[Z][H(L)]={}
	G[Z][H(L)][H(V)]=U
	with E(I,T)as S:D.dump(G,S,indent=4)
	if G[Q][H(L)][H(V)]is not F:return G[Q][H(L)][H(V)]
	else:return U
def Ap(url):
	B=R.head(url)
	if B.status_code!=302 and B.status_code!=301:A('No redirect found');return
	else:
		C=B.headers['Location']
		if AC in C:A('Something went wrong with the redirect');return
		else:return C
def Bj(url,season):B=url;B=B+f"/staffel-{season}";C=R.get(B);D=C.text;E=w.BeautifulSoup(D,r);A=E.find(AD,string=BJ).parent.parent.parent;A=A.find_all('li');A=V(A)-1;return A
def Bk(season,episode,info=F):
	H=episode;I=season;C=info;L();M()
	if C is F:
		with E(Af,O)as G:K=D.load(G)
	else:
		B=f"{C[N]} ({C[W]}-{C[X]})";B=g.sub(u,J,B);B=f"anime/{B}"
		with E(B+A1,O)as G:K=D.load(G)
	A(f"Downloading season {I} episode {H}...");AL(B,I,H)
def AP(season,info=F):
	C=info;G=season
	if C is F:
		with E(Af,O)as K:P=D.load(K)
	else:
		B=f"{C[N]} ({C[W]}-{C[X]})";B=g.sub(u,J,B);B=f"anime/{B}"
		with E(B+A1,O)as K:P=D.load(K)
	for R in P[Q][H(G)]:L();M();A(f"Downloading season {G} episode {R}...");AN(S(R)/V(P[Q][H(G)]));A(I);AL(B,G,R)
def Bl(season,start,end,info=F):
	P=season;G=start;C=info
	if C is F:
		with E(Af,O)as H:Q=D.load(H)
	else:
		B=f"{C[N]} ({C[W]}-{C[X]})";B=g.sub(u,J,B);B=f"anime/{B}"
		with E(B+A1,O)as H:Q=D.load(H)
	for K in p(G,end+1):L();M();A(f"Downloading season {P} episode {K}...");AN((K-G)/(end-G));A(I);AL(B,P,K)
def Aq(query):
	E=query
	if E==J or E==F:A(B.WARNING+'No query entered'+B.ENDC);K.sleep(2);return
	G='https://aniworld.to/ajax/search';H={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':z,'referer':f"https://aniworld.to/search?q={E}",'sec-ch-ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with':'XMLHttpRequest'};C={'keyword':E};C=R.post(G,headers=H,data=C);C=C.text
	try:C=D.loads(C)
	except:
		if Ab in C:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(Ac);K.sleep(2);return
		A(f"{B.WARNING}Error parsing JSON{B.ENDC}");A('Try again later');K.sleep(2);return
	return AQ(E,C)
def AQ(query,data):
	O='Invalid number, try again';H=query;E='link';C=data;C=[A for A in C if'/anime/stream/'in A[E]];C=[A for A in C if'/support/'not in A[E]];C=[A for A in C if'/user/'not in A[E]];C=[A for A in C if'/search/'not in A[E]];C=[A for A in C if Ag not in A[E]];C=[A for A in C if Ah not in A[E]];L();M();A('Search results for:',H);A(I)
	for(Q,F)in AY(C):F[N]=F[N].replace('<em>',J).replace('</em>',J);A(Q+1,B.OK+F[N]+B.ENDC);A(F[k]);A('---')
	A(B.PRIMARY+'Select a number to continue, or press q to quit'+B.ENDC);D=G()
	if D=='q':return
	elif not D.isnumeric():A(O);K.sleep(2);AQ(H,C);return
	elif S(D)<1 or S(D)>V(C):A(O);K.sleep(2);AQ(H,C);return
	D=S(D);R=C[D-1][E];A('Selected:',C[D-1][N]);P=z+R;A('Aniworld URL:',P);return P
def Ar():
	B=3333;D=http.server.SimpleHTTPRequestHandler;E=C.path.join(C.getcwd(),a);C.chdir(E)
	with http.server.HTTPServer((J,B),D)as F:A('serving at http://localhost:'+H(B)+'/');A('Press Ctrl+C to stop the server');F.serve_forever()
def AR():
	R='Removed:';S='index.html';L();M();A('Running cleanup...');V=[C.path.join(B,A)for(B,E,D)in C.walk('./downloads')for A in D if A.endswith('.part')or A.endswith('.ytdl')]
	if V:
		A(B.WARNING+'Do you want to delete non finished downloads? After deleting you have to restart the download'+B.ENDC);A('Do you want to continue? (y/N)');K=G()
		if K.lower()=='y':
			A('Deleting files...')
			for I in V:C.remove(I);A('Deleted:',I)
	A('Rebuilding index.json...');P=[A for A in C.listdir(a)if C.path.isdir(C.path.join(a,A))];Z=[]
	for H in P:
		if not C.listdir(f"anime/{H}"):C.rmdir(f"anime/{H}");continue
		if not C.path.exists(f"anime/{H}/info.json"):continue
		if C.path.exists(f"anime/{H}/stream.json"):C.remove(f"anime/{H}/stream.json")
		with E(f"anime/{H}/info.json",O)as Q:F=D.load(Q)
		if Ae not in F:
			A('No url found for:','/'+H+'/ ('+F[N]+')'+', should we remove it? (Y/n)');K=G()
			if K.lower()=='n':continue
			A('Removing:',F[N]);m.rmtree(f"anime/{H}");continue
		if y in F[v]:F[v]=F[v].replace(y,J)
		e=[N,k,BG,b,c,l,d,W,X,A0,BH,t,BI,Ad,'imdb']
		if not all(A in F for A in e):A('Rebuilding info.json for:',F[N]);F=h(F[Ae]);A5(F)
		Z.append({N:F[N],t:F[t],W:F[W],X:F[X],b:F[b],k:F[k],l:F[l],d:F[d],v:f"{H}"})
	with E(AF,T)as Q:D.dump(Z,Q,indent=4)
	A('Cleaning file structure...')
	if C.path.exists(S):C.remove(S)
	f=['urls.txt','search.html','search.txt','temp.html',A2,'update.exe'];A('Removing unused files...')
	for I in f:
		if C.path.exists(I):C.remove(I);A(R,I)
	if C.path.exists(Y):m.rmtree(Y);A('Removed: assets/')
	if C.path.exists(A3):
		P=[A for A in C.listdir(A3)if C.path.isdir(C.path.join(A3,A))]
		for H in P:
			if not C.listdir(f"downloads/{H}"):C.rmdir(f"downloads/{H}");A(R,f"downloads/{H}")
	Bm();A('Done');A(i);G();U()
def Bm():
	F='video';I=[A for A in C.listdir(C.path.join(C.getcwd(),a))if C.path.isdir(C.path.join(C.getcwd(),a,A))]
	if Y in I:I.remove(Y)
	G={}
	for B in I:
		O=[A for A in C.listdir(C.path.join(C.getcwd(),a,B,F))if C.path.isfile(C.path.join(C.getcwd(),a,B,F,A))];J=[A for A in C.listdir(C.path.join(C.getcwd(),a,B,F))if C.path.isdir(C.path.join(C.getcwd(),a,B,F,A))];G[B]={}
		for H in J:
			G[B][H]={};K=[A for A in C.listdir(C.path.join(C.getcwd(),a,B,F,H))if C.path.isfile(C.path.join(C.getcwd(),a,B,F,H,A))]
			for L in K:M=L.split('.')[0];G[B][H][M]='downloaded'
	if not C.path.exists(C.path.join(C.getcwd(),A3)):C.makedirs(C.path.join(C.getcwd(),A3))
	with E(C.path.join(C.getcwd(),'downloads/downloads.json'),T)as N:D.dump(G,N,indent=4)
	A('downloads.json rebuilt')
def As(url):
	C='episode';D='staffel';B=url
	if AC not in B:A(Ai);return AZ
	if D in B:B=B.split(D)[0]
	if C in B:B=B.split(C)[0]
	return B
def Bn():
	if not C.path.exists(e):Bq();return
	if C.path.exists(A2):C.remove(A2)
	elif not C.path.exists(AG):C.makedirs(AG)
def A6(key,value):
	if C.path.exists(e):
		with E(e,O)as A:B=D.load(A)
	else:B={}
	B[key]=value
	with E(e,T)as A:D.dump(B,A,indent=4)
def Bo():
	if C.path.exists(A2):C.remove(A2)
	L();M();A(B.PRIMARY+'Update finished'+B.ENDC);A('The program has been updated, YIPPIE!');A(i);G();AS()
def Bp():AT()
def A7():return AZ
def n():
	B='./assets/animeList.json';return;A(BK);H='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database-minified.json';I='https://api.github.com/repos/manami-project/anime-offline-database/commits?path=anime-offline-database-minified.json&page=1&per_page=1';J=R.get(I);F=J.json();K=F[0]['commit']['committer']['date'][:10]
	if C.path.exists(B):
		with E(B,O)as G:F=D.load(G)
		L=F['lastUpdate']
		if L==K:A('Anime list is up to date');return
	A('Downloading anime list...');AK.download(H,B);F=D.load(E(B,O,encoding=Aa))
	with E(B,T)as G:D.dump(F,G,indent=4)
	A('Anime list downloaded')
def L():A('\x1b[H\x1b[J')
def U():
	F='Enter the url of the anime';H='Invalid key';L();M();A('Press one of the following keys:');A(BL);A(BM);A(BN);A(BO);A(BP);A(BQ);A(BR);A(BS);A(BT);D=G()
	if D not in[q,'2','3','4','5','6','7','8','9','0','q','Q','h','i']:A(H);U();return
	if D==q:AV()
	elif D=='x':
		A('This mode will download everything from the given url');A(F);E=G();E=As(E)
		if not E:A(B.WARNING+Ai+B.ENDC);K.sleep(2);U();return
		Ay(E)
	elif D=='2':A('Not implemented yet');K.sleep(2);U()
	elif D=='3':Ar()
	elif D=='4':AR()
	elif D=='5':
		if C.name==AB:C.system('start .\\anime')
		elif C.name=='posix':C.system('xdg-open .\\anime')
		else:A('Unsupported os');A('The anime folder is located in the following directory:');A(C.getcwd()+'\\anime');A('\nPress enter to continue');G();U()
		U()
	elif D=='6':
		A(F);E=G();E=As(E)
		if not E:A(B.WARNING+Ai+B.ENDC);K.sleep(2);U();return
		A(h(E))
	elif D=='0':Bp();U()
	elif D=='h'or D=='i':L();M();A(B.PRIMARY+'Info'+B.ENDC);A(I);A(f"{B.OK}This program was made by JMcrafter26 and published by Someone266 on Github{B.ENDC}");A(f"{B.OK}The program is open source and can be found here: https://github.com/Someone266/aniworld-downloader/{B.ENDC}");A(I);A('This program is still in development, so there might be some bugs');A('If you find a bug, please report it on the Github page');A(I);A(f"{B.OK}This program is for educational purposes only, the developer nor the publisher is responsible for any damage caused by the program. This program is not affiliated with any of the anime sites. This program is provided as is, without any warranty. Use at your own risk.{B.ENDC}");A(I);A(i);G();Av()
	elif D=='q'or D=='Q':A('Quitting...');x()
	else:A(B.WARNING+H+B.ENDC);K.sleep(2);U();return
def Bq():
	D='./assets';L();M();A(B.PRIMARY+'Hi and welcome to AniWorld-Down v'+AW()+B.ENDC);A('It looks like this is your first time running this program, or you have deleted some files :)');A('This guide will help you get started with the program\n');A(B.WARNING+'This directory will be used to store the anime and the assets'+B.ENDC);A(B.SECONDARY+i+B.ENDC);G()
	if not C.path.exists(AG):C.makedirs(AG)
	if not C.path.exists(D):C.makedirs(D)
	Br()
def Br():
	D='updateNotes';E='Update notes:';L();M();A(B.PRIMARY+'Step 1: Checking for updates and downloading assets'+B.ENDC);A('We promise, it will be quick');C=Ax()
	if C is F:A('Hmm, something went wrong with the update check');A('Do you have an internet connection? \n');A(B.SECONDARY+'PS: We need an internet connection to download the assets'+B.ENDC);A(B.SECONDARY+AH+B.ENDC);G();x()
	if C[b]=='error':A(B.WARNING+BU+B.ENDC);A(Aj,C[BV]);A('Please try again later\n');A(B.SECONDARY+AH+B.ENDC);G();x()
	elif C[b]==BW:A(BX);A(B.SECONDARY+i+B.ENDC);G();AS();return
	else:
		if C[AI][Y]:A(B.OK+BY+B.ENDC);A(E);A(C[D][Y]+I);A8(Y,C[AJ][Y])
		if C[AI][f]:A(B.OK+BZ+B.ENDC);A(E);A(C[D][f]+I);A8(f,C[AJ][f])
		else:A('No program update available')
		A(B.SECONDARY+i+B.ENDC);G();AS();return
def AS():L();M();A(B.PRIMARY+'Step 2: Configuring the program'+B.ENDC);A('We need to configure the program before we can continue');A('It is very simple, just answer a few questions');A(B.SECONDARY+i+B.ENDC);G();At()
def At():
	L();M();A(B.PRIMARY+'Choose the option that describes you the best'+B.ENDC);A('1. I want to archive anime and have it nicely organized (with filestructure, prictures and an offline webserver)');A('2. I just want to download anime fast and continue watching (No filestructure, ready to watch or move)');A(I);A(B.SECONDARY+Ba+B.ENDC);C=G()
	if C==q:A6(A4,Bb)
	elif C=='2':A6(A4,Bc)
	else:A(Bd);At();return
	Au()
def Au():
	L();M();A(B.PRIMARY+'Select your preferred host'+B.ENDC);A('1. Voe (Recommended)');A('2. Streamtape');A(I);A(B.SECONDARY+Ba+B.ENDC);C=G()
	if C==q:A6(s,Q)
	elif C=='2':A6(s,Z)
	else:A(Bd);Au();return
	Bs()
def Bs():
	L();M();A(B.PRIMARY+'Thats it, you are ready to go'+B.ENDC);A('You can now start downloading anime');A(I);A('Press i to read the instructions');A('Press enter to just freakin start the program');C=G()
	if C=='i':Av()
	U()
def Av():L();M();A(B.PRIMARY+'Instructions'+B.ENDC);A(BL);A('This option will guide you through the download process, you just need to enter the url of the anime');A(BM);A('This option is not implemented yet');A(BN);A('This option will start a webserver to serve the content - you can watch the anime in your browser (even offline and other devices)');A(BO);A('This option will clean up the program and the assets');A(BP);A('This option will open the anime folder where the anime is stored');A(BQ);A('This option will get the info of the anime from the url');A(BR);A('This option will allow you to change the settings of the program');A(BS);A('This is the current screen :)');A(BT);A(I);A(i);G();U()
Aw={A4:"The mode of AniDown\n'archive' will organize the anime with filestructure, pictures and an offline webserver\n'download' will download anime fast and continue watching",s:'The preferred host to download from'}
o={A4:[Bb,Bc],s:[Q,Z]}
type={A4:Ak,s:Ak}
def AT():
	K=f"{C.getcwd()}\\settings.json";L();A('Settings:');A('Path:',K);A(I)
	with E(e,O)as M:J=D.load(M)
	for(F,N)in J.items():P=list(J.keys()).index(F)+1;A(f"{B.PRIMARY}({P}) - {F}: {N}{B.ENDC}");A(f"{B.OK}Description: {B.ENDC}{B.SECONDARY}{Aw[F]}{B.ENDC}");A(f"{B.OK}Options: {B.ENDC}{B.SECONDARY}{o[F]}{B.ENDC}");A('---')
	A('Choose an option by pressing the number (q to quit):');H=G()
	if not H or H=='q':return
	if not H.isdigit():return AT()
	AU(S(H),J);return AT()
def AU(option,data):
	H=data;C=option;F=list(H.keys())[C-1];L();A(f"Changing '{F}'")
	if type[F]==Ak:
		A(f"{B.OK}Options:\n{B.ENDC}")
		for(I,C)in AY(o[F]):A(f"({I+1}) - {C}")
		A('Choose an option by pressing the number:');C=G()
		if not C.isdigit():return AU(C,H)
		if S(C)>V(o[F]):return AU(C,H)
		H[F]=o[F][S(C)-1]
	else:
		if type[F]=='text':A('Enter the new value (Text/String):')
		elif type[F]=='number':A('Enter the new value (Number):')
		J=G();H[F]=J
	with E(e,T)as K:D.dump(H,K)
def Bt(key):
	A=key
	with E(e,O)as C:B=D.load(C)
	if A not in B:
		B[A]=o[A][0]
		with E(e,T)as C:D.dump(B,C)
	return B[A]
def C2():
	A={}
	for B in Aw:A[B]=o[B][0]
	with E(e,T)as C:D.dump(A,C)
	return A
import zipfile
def Bu():
	Bn();L();M();A('Loading...');B=Ax()
	if B is F:A('No internet connection, skipping update check');return
	if B[b]=='error':A(BU);A(Aj,B[BV]);K.sleep(2);return
	elif B[b]==BW:A(BX);return
	else:
		if B[AI][Y]:A(BY);A8(Y,B[AJ][Y])
		if B[AI][f]:A(BZ);A8(f,B[AJ][f])
def Ax():
	F='anime/assets/.version';A(BK,end=J)
	try:R.get('https://api.jm26.net/status.txt',timeout=5)
	except R.exceptions.ConnectionError:A(' Skipped');A(B.WARNING+Be+B.ENDC);K.sleep(2);return
	H='https://api.jm26.net/update/aniworld-down/check/';I=AW()
	if not C.path.exists(F):G='0.0.0'
	else:
		with E(F,O)as L:G=L.read()
	D={f:I,Y:G};M=R.post(H,data=D);D=M.json();A(' Done');return D
def A8(type,hash):
	Q='anime/assets';S='Please try again later';F='./update';A('Downloading ..');L=f"https://api.jm26.net/update/aniworld-down/download/?type={type}&hash={hash}";M='./update/update.zip'
	if A7():L=L+'&os=windows'
	if not C.path.exists(F):C.makedirs(F)
	try:N=R.get(L)
	except R.exceptions.ConnectionError:A(B.WARNING+Be+B.ENDC);A(S);A(AH);G();x()
	if N.headers['Content-Type']=='application/json':A(B.WARNING+'Something went wrong with the download'+B.ENDC);A(Aj,N.text);A(S);A(AH);G();x()
	A(B.OK+Bf+B.ENDC)
	with E(M,'wb')as H:H.write(N.content)
	with zipfile.ZipFile(M,O)as T:T.extractall(F)
	C.remove(M)
	if C.path.exists(Q):m.rmtree(Q)
	for D in C.listdir(F):
		if C.path.isdir(f"./update/{D}"):
			if not C.path.exists(f"./{D}"):C.makedirs(f"./{D}")
			for H in C.listdir(f"./update/{D}"):m.move(C.path.join(f"./update/{D}",H),C.path.join(f"./{D}",H))
			C.rmdir(f"./update/{D}")
		else:m.move(C.path.join(F,D),C.path.join('./',D))
	C.rmdir(F);A(B.OK+'Update complete'+B.ENDC);A(I);A(f"{B.WARNING}It is recommended to run the {B.ENDC}{B.OK}clean option{B.ENDC}{B.WARNING} after updating{B.ENDC}");A(I)
	if type==f:
		for U in p(3):A(f"\rRestarting in {3-U} seconds",end=J);K.sleep(1)
		A('\rRestarting program...')
		if not C.path.exists(e):
			if A7():C.system(f"start update.bat guideUpdateFinished")
			elif C.name==AB:C.system('py main.py guideUpdateFinished')
			else:C.system(f"python3 main.py guideUpdateFinished")
		elif A7():C.system(f"start update.bat "+j.join(P.argv[1:]))
		elif C.name==AB:C.system('py main.py '+j.join(P.argv[1:]))
		else:C.system('python3 main.py '+j.join(P.argv[1:]))
Bv='1.1.8'
class B:PURPLE='\x1b[95m';SECONDARY='\x1b[90m';PRIMARY='\x1b[94m';CYAN='\x1b[96m';OK='\x1b[92m';WARNING='\x1b[93m';FAIL='\x1b[91m';ENDC='\x1b[0m';BOLD='\x1b[1m';UNDERLINE='\x1b[4m'
def Ay(url):
	n();C=h(url);A5(C)
	for D in C[c]:AM(url,D,C[c][D],C)
	E=C[d];A(E)
	for D in p(1,E+1):AP(D,C)
	AR();M();A(B.OK+'Finished downloading all episodes'+B.ENDC);A(I);A(B.PRIMARY+"Run 'serve' to watch the episodes in your browser"+B.ENDC)
def AV():
	L();M();n();A(B.OK+'This is the auto mode. It will ask you what to '+B.ENDC);A(I);A('Enter the name of the anime you want to search for or paste the url of the anime');D=G()
	if D.startswith('http'):
		C=D
		if AC not in C:A(B.WARNING+BD+B.ENDC);K.sleep(2);return
		if not BE in C:A(B.WARNING+BF+B.ENDC);K.sleep(2);return
		if Ag in C:C=C.split(Ag)[0]
		if Ah in C:C=C.split(Ah)[0]
	elif D!=J and D!=F:C=Aq(D)
	else:A('Invalid input');K.sleep(2);AV();return
	E=h(C);A5(E)
	for H in E[c]:AM(C,H,E[c][H],E)
	A9(C,E)
def A9(url,info):
	L=url;C=info;M();A(B.OK+'Setup complete'+B.ENDC);A(I);A(B.OK+'We found '+H(C[d])+' seasons and a total of '+H(C[l])+' episodes'+B.ENDC);A(I);A('Do you want to download all episodes? (Y/n)');F=G()
	if F!='Y'and F!='y'and F!='yes'and F!='Yes'and F!=J:
		A('Which season do you want to download?');D=S(G());A('What episode do you want to download? (Enter 0 to download all episodes; use - to download a range of episodes)');E=S(G())
		if D<1 or D>C[d]:A(B.FAIL+'Invalid season'+B.ENDC);K.sleep(2);A9(L,C);return
		if E==0:AP(D,C)
		elif'-'in H(E):
			N=S(E.split('-')[0]);O=S(E.split('-')[1])
			if N<1 or O>C[c][D]:A(B.FAIL+'Invalid range'+B.ENDC);K.sleep(2);A9(L,C);return
			Bl(D,N,O,C)
		else:
			if E<1 or E>C[c][D]:A(B.FAIL+'Invalid episode'+B.ENDC);K.sleep(2);A9(L,C);return
			Bk(D,E,C)
	else:
		A(B.OK+'Downloading all episodes'+B.ENDC)
		for D in p(1,C[d]+1):AP(D,C)
	A(B.OK+Bf+B.ENDC);A(I);A(B.PRIMARY+'Press enter to return to the main menu'+B.ENDC);G();U()
def AW():return Bv
def Bw(url):n();A=h(url);return A
def Bx(url):n();A=h(url);A5(A)
def By(url,season,info=F):
	A=season;n();B=F
	if info is not F:B=info[c][A]
	C=AM(url,A,B);return C
def Bz(url,season,episode,info=F):
	C=season;A=info;B=episode;n()
	if A is not F:B=A[c][C][B]
	D=AO(url,C,B,A);return D
def B_():L();M();A('Enter the name of the anime you want to search for');B=G();return Aq(B)
def M():
	A(I);C=AW()
	if A7():C=C+' (Windows)'
	A(B.CYAN+'    AA          W     W         ll     d     DDD                    '+B.ENDC);A(B.CYAN+'   A  A      ii W     W          l     d     D  D                   '+B.ENDC);A(B.CYAN+'   AAAA nnn     W  W  W ooo rrr  l   ddd     D  D ooo w   w nnn     '+B.ENDC);A(B.CYAN+'   A  A n  n ii  W W W  o o r    l  d  d     D  D o o w w w n  n    '+B.ENDC);A(B.CYAN+'   A  A n  n ii   W W   ooo r   lll  ddd     DDD  ooo  w w  n  n    '+B.ENDC);A(B.CYAN+'                                                                    '+B.ENDC);A('A powerful scraper and downloader for AniWorld');A(j);A('Version: '+C+'                                 Made by JMcrafter26');A(B.SECONDARY+'DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.'+B.ENDC);A(B.SECONDARY+'Please respect the laws of your country and the country of the website you are scraping.'+B.ENDC);A(I)
def C0():
	H='help';J='clean';K='serve';N='search'
	if V(P.argv)==1:P.argv.append('ui')
	C=P.argv[1]
	if C=='guideUpdateFinished':Bo();return
	Bu();L();M();A(I)
	if C=='getinfo':D=P.argv[3];A(Bw(D))
	elif C=='run':D=P.argv[2];Ay(D)
	elif C=='ui':U()
	elif C==N:B_();return
	elif C==K:Ar()
	elif C==J:AR()
	elif C=='setup':D=P.argv[3];Bx(D)
	elif C=='auto':AV()
	elif C=='getseason':
		D=P.argv[3];G=P.argv[5];E=F
		if V(P.argv)>6:E=h(D)
		A(By(D,G,E))
	elif C=='getepisode':
		D=P.argv[3];G=P.argv[5];O=P.argv[7];E=F
		if V(P.argv)>8:E=h(D)
		A(Bz(D,G,O,E))
	elif C==H:A(B.PRIMARY+'Commands:'+B.ENDC);A('-----------------');A('run -url <url>');A(K);A(J);A(N);A('setup -url <url>');A('getinfo -url <url>');A('getseason -url <url> -season <season>');A('getepisode -url <url> -season <season> -episode <episode>');A(H)
	else:A(B.WARNING+'Invalid command'+B.ENDC)
	A(I)
if __name__=='__main__':C0()