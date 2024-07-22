# Aniworld Scraper
# Author: JMcrafter26
# Description: A scraper for aniworld (german anime site)
# Version: see version variable below
# License: MIT License
# DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.
# Please respect the laws of your country and the country of the website you are scraping.

# This code was minified to save space. If you want to read the code, please read the original files.


BG='Download complete'
BF='No internet connection'
BE='Invalid option, try again'
BD='download'
BC='archive'
BB='Choose an option by pressing the number'
BA='There is a program update available'
B9='Downloading assets...'
B8='You are up to date'
B7='success'
B6='message'
B5='Something went wrong with the update check'
B4='q. Quit'
B3='h. Help/Info'
B2='0. Settings'
B1='6. Get anime info'
B0='5. Open anime folder'
A_='4. Clean up'
Az='3. Serve content'
Ay='2. Continue Download'
Ax='1. Download Assistant'
Aw='Checking for updates...'
Av='Episoden:'
Au='producer'
At='trailer'
As='animeSeason'
Ar=KeyError
Af='option'
Ae='Error:'
Ad='Invalid url'
Ac='anime'
Ab='stream.json'
Aa='url'
AZ='fsk'
AY='Or paste your cookie key in the settings'
AX='DDoS-Guard'
AW='aniworld.to'
AV=enumerate
AH='updateHash'
AG='update'
AF='Press enter to exit'
AE='./anime'
AD='update.bat'
AC='./anime/index.json'
AB='href'
AA='strong'
A9='nt'
A8='downloads'
A0='mode'
z='1'
y='i'
x='/stream.json'
w='picture'
v='https://aniworld.to'
u='html.parser'
t='utf-8'
s='anime/'
r=exit
q='pathname'
p='[<>:"/\\\\|?*]'
o='tags'
n=' '
m='prefHost'
l=range
j='totalEpisodes'
i='description'
g='settings.json'
f='Press enter to continue'
e='streamtape'
c='program'
b='assets'
a='seasons'
Z='episodes'
Y='status'
X='w'
W=len
V='enddate'
U='startdate'
R=int
Q='voe'
P='r'
N='title'
M=''
I='\n'
H=str
F=open
E=input
D=None
A=print
import os as C,shutil as A1,time as J,json as G
def AI(path,season,episode):
	K=episode;I=season;E=path
	if E is not D and I is not D and K is not D:
		if C.path.exists(f"{E}/video/{I}/{K}.mp4"):A(f"{B.WARNING}File {E}/video/{I}/{K}.mp4 already exists. Skipping...{B.ENDC}");return
	if not C.path.exists(A8):C.makedirs(A8)
	L=E.split(s)[1]
	if not C.path.exists(f"downloads/{L}"):C.makedirs(f"downloads/{L}")
	N=BR(m)
	with F(f"{E}/stream.json",P)as O:R=G.load(O)
	C.chdir(f"downloads/{L}");N=Q
	if N==Q:S=R[Q][H(I)][H(K)];M=Ap(S)
	elif N==e:0
	else:A('Invalid host');J.sleep(2);return
	if M is D:A(f"{B.FAIL}Download failed{B.ENDC}");J.sleep(2);return
	C.chdir('../../');C.makedirs(f"{E}/video/{I}",exist_ok=True);M=f"downloads/{L}/{M}";A1.move(f"{M}",f"{E}/video/{I}/{K}.mp4");A(f"Moved to {E}/video/{I}/{K}.mp4")
import wget as AJ,requests as S,re as h,sys as O,bs4,http.server,zipfile
def Bd(title='AniWorld Scraper'):
	B=title
	if C.name==A9:C.system(f"title {B}")
	else:A(f"]0;{B}\a")
def d(url):
	g='span';Q='a';T='div';K=url
	if'/filme/'in K:A(B.WARNING+'This type of url is not supported yet. It will probably be supported in the future'+B.ENDC);J.sleep(2);return
	if AW not in K:A(B.WARNING+'Invalid url! Please enter a valid aniworld.to url'+B.ENDC);J.sleep(2);return
	m=S.get(K);b=m.text
	with F('temp.html',X,encoding=t)as p:p.write(b)
	if AX in b:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(AY);J.sleep(2);return
	E=bs4.BeautifulSoup(b,u);G=E.find(T,class_='series-title').find('h1').string;G=G.strip();G=G.split(I)[0];A('Getting info for:',G);q=E.find('p',class_='seri_des').get('data-full-description');P=E.find(g,itemprop='startDate').string;c=E.find(g,itemprop='endDate').string
	if c=='heute':d='ONGOING'
	else:d='FINISHED'
	C=E.find(AA,string='Staffeln:').parent.parent.parent.find_all('li');C=[A.text for A in C];C=[A.replace(n,M)for A in C];C=[A for A in C if A];C=[A for A in C if A.isnumeric()];C=W(C);L={}
	for h in l(1,R(C)+1):L[h]=BH(K,h)
	L=L;k=sum(L.values());e=E.find(T,class_='seriesCoverBox').find('noscript').find('img').get('src');e=v+e;r=E.find(Q,class_='trailerButton').get(AB);f=E.find_all(Q,itemprop='genre');f=[A.string for A in f];s=E.find(AA,class_='seriesProducer').text;x=E.find(T,class_=AZ).get('data-fsk');O=E.find(Q,class_='imdb-link')
	if O is not D:O=O.get(AB)
	else:O=M
	A(d+' ('+P+' - '+c+') - '+H(k)+' episodes - '+H(C)+' seasons');y={N:G,i:q,As:{'year':R(P[:4]),'season':P[5:]},Y:d,Z:L,j:k,a:C,U:P,V:c,w:e,At:r,o:f,Au:s,AZ:x,'imdb':O,Aa:K};return y
def A2(info):
	B=info;A('Setting up anime folder...');D=f"{B[N]} ({B[U]}-{B[V]})";D=h.sub(p,M,D);D=f"anime/{D}";I=f"./{D}"
	if not C.path.exists(D):C.makedirs(D)
	with F(f"{D}/info.json",X)as E:G.dump(B,E,indent=4)
	J=B[w].split('.')[-1]
	if not C.path.exists(f"{I}/image.{J}"):AJ.download(B[w],f"{I}/image.{J}")
	B[w]=f"image.{J}";B[q]=I
	with F(f"{D}/info.json",X)as E:G.dump(B,E,indent=4)
	if C.path.exists(AC):
		with F(AC,P)as E:H=G.load(E)
	else:H=[]
	K={N:B[N],o:B[o],U:B[U],V:B[V],Y:B[Y],i:B[i],j:B[j],a:B[a],q:I}
	for(L,O)in AV(H):
		if O[N]==B[N]:H[L]=K;break
	else:H.append(K)
	with F(AC,X)as E:G.dump(H,E,indent=4)
	A('Anime folder setup complete')
def AK(url,season,episodes=D,info=D):
	R=url;K=info;J=season;B=episodes
	if B is D:T=S.get(R);X=T.text;Y=bs4.BeautifulSoup(X,u);B=Y.find(AA,string=Av).parent.parent.parent;B=B.find_all('li');B=W(B)-1
	A(f"Getting streams for season {J} with {B} episodes...");L=f"{K[N]} ({K[U]}-{K[V]})";L=h.sub(p,M,L);A('Path:',L)
	if C.path.exists(s+L+x):
		with F(s+L+x,P)as Z:
			E=G.load(Z);A('Found stream.json');A('Checking if season already exists...')
			if H(J)in E:
				if W(E[Q][H(J)])>=1:A('Season stream urls already exist');return E
	else:E={}
	E={}
	for O in l(1,B+1):
		if K is not D:E[O]=AM(R,J,O,K)
		else:E[O]=AM(R,J,O)
		AL(O/B)
	A(I);A('Done with season',J);return E
def AL(percent):A=percent;B=50;C=R(round(B*A));D='='*C+'-'*(B-C);O.stdout.write(f"\rProgress: [{D}] {A*100:.2f}%");O.stdout.flush()
def AM(url,season,episode,info=D):
	a='No stream url found';Z=url;Y=info;W=episode;K=season;Z=Z+f"/staffel-{K}/episode-{W}";d=S.get(Z);b=d.text
	if AX in b:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(AY);J.sleep(2);return
	c=bs4.BeautifulSoup(b,u)
	if Y is not D:I=f"{Y[N]} ({Y[U]}-{Y[V]})";I=h.sub(p,M,I);I=f"anime/{I}/stream.json"
	else:I=f"stream.json"
	L=c.find(y,class_='icon VOE')
	if L is D:A('No voe download found, skipping...');return
	L=L.parent;L=L.get(AB);L=v+L;T=Ag(L)
	if T is D:A(a);return
	if C.path.exists(I):
		with F(I,P)as R:E=G.load(R)
	else:E={}
	if H(Q)not in E:E[Q]={}
	if H(K)not in E[Q]:E[Q][H(K)]={}
	E[Q][H(K)][H(W)]=T
	with F(I,X)as R:G.dump(E,R,indent=4)
	O=c.find(y,class_='icon Streamtape')
	if O is D:A('No streamtape download found, skipping...');return
	O=O.parent;O=O.get(AB);O=v+O;T=Ag(O)
	if T is D:A(a);return
	if C.path.exists(I):
		with F(I,P)as R:E=G.load(R)
	else:E={}
	if H(e)not in E:E[e]={}
	if H(K)not in E[e]:E[e][H(K)]={}
	E[e][H(K)][H(W)]=T
	with F(I,X)as R:G.dump(E,R,indent=4)
	if E[Q][H(K)][H(W)]is not D:return E[Q][H(K)][H(W)]
	else:return T
def Ag(url):
	B=S.head(url)
	if B.status_code!=302 and B.status_code!=301:A('No redirect found');return
	else:
		C=B.headers['Location']
		if AW in C:A('Something went wrong with the redirect');return
		else:return C
def BH(url,season):B=url;B=B+f"/staffel-{season}";C=S.get(B);D=C.text;E=bs4.BeautifulSoup(D,u);A=E.find(AA,string=Av).parent.parent.parent;A=A.find_all('li');A=W(A)-1;return A
def BI(season,episode,info=D):
	H=episode;I=season;C=info;K();L()
	if C is D:
		with F(Ab,P)as E:J=G.load(E)
	else:
		B=f"{C[N]} ({C[U]}-{C[V]})";B=h.sub(p,M,B);B=f"anime/{B}"
		with F(B+x,P)as E:J=G.load(E)
	A(f"Downloading season {I} episode {H}...");AI(B,I,H)
def AN(season,info=D):
	C=info;E=season
	if C is D:
		with F(Ab,P)as J:O=G.load(J)
	else:
		B=f"{C[N]} ({C[U]}-{C[V]})";B=h.sub(p,M,B);B=f"anime/{B}"
		with F(B+x,P)as J:O=G.load(J)
	for S in O[Q][H(E)]:K();L();A(f"Downloading season {E} episode {S}...");AL(R(S)/W(O[Q][H(E)]));A(I);AI(B,E,S)
def BJ(season,start,end,info=D):
	O=season;E=start;C=info
	if C is D:
		with F(Ab,P)as H:Q=G.load(H)
	else:
		B=f"{C[N]} ({C[U]}-{C[V]})";B=h.sub(p,M,B);B=f"anime/{B}"
		with F(B+x,P)as H:Q=G.load(H)
	for J in l(E,end+1):K();L();A(f"Downloading season {O} episode {J}...");AL((J-E)/(end-E));A(I);AI(B,O,J)
def Ah(query):
	E=query
	if E==M or E==D:A(B.WARNING+'No query entered'+B.ENDC);J.sleep(2);return
	H='https://aniworld.to/ajax/search';I={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':v,'referer':f"https://aniworld.to/search?q={E}",'sec-ch-ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with':'XMLHttpRequest'};C={'keyword':E};C=S.post(H,headers=I,data=C);C=C.text
	with F('search.html',X,encoding=t)as K:K.write(C)
	try:C=G.loads(C)
	except:
		if AX in C:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(AY);J.sleep(2);return
		A(f"{B.WARNING}Error parsing JSON{B.ENDC}");A('Try again later');J.sleep(2);return
	return AO(E,C)
def AO(query,data):
	O='Invalid number, try again';H=query;F='link';C=data;C=[A for A in C if'/anime/stream/'in A[F]];C=[A for A in C if'/support/'not in A[F]];C=[A for A in C if'/user/'not in A[F]];C=[A for A in C if'/search/'not in A[F]];C=[A for A in C if'/episode-'not in A[F]];C=[A for A in C if'/staffel-'not in A[F]];K();L();A('Search results for:',H);A(I)
	for(S,G)in AV(C):G[N]=G[N].replace('<em>',M).replace('</em>',M);A(S+1,B.OK+G[N]+B.ENDC);A(G[i]);A('---')
	A(B.PRIMARY+'Select a number to continue, or press q to quit'+B.ENDC);D=E()
	if D=='q':return
	elif not D.isnumeric():A(O);J.sleep(2);AO(H,C);return
	elif R(D)<1 or R(D)>W(C):A(O);J.sleep(2);AO(H,C);return
	D=R(D);P=C[D-1][F];A('Selected:',C[D-1][N]);A(P);Q=v+P;A('url:',Q);return Q
def Ai():
	B=3333;D=http.server.SimpleHTTPRequestHandler;E=C.path.join(C.getcwd(),Ac);C.chdir(E)
	with http.server.HTTPServer((M,B),D)as F:A('serving at http://localhost:'+H(B)+'/');A('Press Ctrl+C to stop the server');F.serve_forever()
def AP():
	R='Removed:';S='index.html';K();L();A('Running cleanup...');W=[C.path.join(B,A)for(B,E,D)in C.walk('./downloads')for A in D if A.endswith('.part')or A.endswith('.ytdl')]
	if W:
		A(B.WARNING+'Do you want to delete non finished downloads? After deleting you have to restart the download'+B.ENDC);A('Do you want to continue? (y/N)');J=E()
		if J.lower()=='y':
			A('Deleting files...')
			for I in W:C.remove(I);A('Deleted:',I)
	A('Rebuilding index.json...');O=[A for A in C.listdir(Ac)if C.path.isdir(C.path.join(Ac,A))];c=[]
	for H in O:
		if not C.listdir(f"anime/{H}"):C.rmdir(f"anime/{H}");continue
		if not C.path.exists(f"anime/{H}/info.json"):continue
		if C.path.exists(f"anime/{H}/stream.json"):C.remove(f"anime/{H}/stream.json")
		with F(f"anime/{H}/info.json",P)as Q:D=G.load(Q)
		if Aa not in D:
			A('No url found for:','/'+H+'/ ('+D[N]+')'+', should we remove it? (Y/n)');J=E()
			if J.lower()=='n':continue
			A('Removing:',D[N]);A1.rmtree(f"anime/{H}");continue
		if s in D[q]:D[q]=D[q].replace(s,M)
		e=[N,i,As,Y,Z,j,a,U,V,w,At,o,Au,AZ,'imdb']
		if not all(A in D for A in e):A('Rebuilding info.json for:',D[N]);D=d(D[Aa]);A2(D)
		c.append({N:D[N],o:D[o],U:D[U],V:D[V],Y:D[Y],i:D[i],j:D[j],a:D[a],q:f"{H}"})
	with F(AC,X)as Q:G.dump(c,Q,indent=4)
	A('Cleaning file structure...')
	if C.path.exists(S):C.remove(S)
	g=['assets/bootstrap.min.css','assets/css','assets/js','assets/plyr.css','assets/plyr.js','assets/animeList.json','assets/placeholder.jpg','assets/fuse.min.js','assets/.version'];A('Removing unused files...')
	for I in g:
		if C.path.exists(I):C.remove(I);A(R,I)
	if not C.listdir(b):C.rmdir(b);A('Removed: assets/')
	O=[A for A in C.listdir(A8)if C.path.isdir(C.path.join(A8,A))]
	for H in O:
		if not C.listdir(f"downloads/{H}"):C.rmdir(f"downloads/{H}");A(R,f"downloads/{H}")
	A('Done');A(f);E();T()
def Aj(url):
	C='episode';D='staffel';B=url
	if AW not in B:A(Ad);return False
	if D in B:B=B.split(D)[0]
	if C in B:B=B.split(C)[0]
	return B
def BK():
	if not C.path.exists(g):BN();return
	if C.path.exists(AD):C.remove(AD)
	elif not C.path.exists(AE):C.makedirs(AE)
def A3(key,value):
	if C.path.exists(g):
		with F(g,P)as A:B=G.load(A)
	else:B={}
	B[key]=value
	with F(g,X)as A:G.dump(B,A,indent=4)
def BL():
	if C.path.exists(AD):C.remove(AD)
	K();L();A(B.PRIMARY+'Update finished'+B.ENDC);A('The program has been updated, YIPPIE!');A(f);E();AQ()
def BM():AR()
def A4():return False
def k():
	B='./assets/animeList.json';return;A(Aw);H='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database-minified.json';I='https://api.github.com/repos/manami-project/anime-offline-database/commits?path=anime-offline-database-minified.json&page=1&per_page=1';J=S.get(I);D=J.json();K=D[0]['commit']['committer']['date'][:10]
	if C.path.exists(B):
		with F(B,P)as E:D=G.load(E)
		L=D['lastUpdate']
		if L==K:A('Anime list is up to date');return
	A('Downloading anime list...');AJ.download(H,B);D=G.load(F(B,P,encoding=t))
	with F(B,X)as E:G.dump(D,E,indent=4)
	A('Anime list downloaded')
def K():A('\x1b[H\x1b[J')
def T():
	G='Enter the url of the anime';H='Invalid key';K();L();A('Press one of the following keys:');A(Ax);A(Ay);A(Az);A(A_);A(B0);A(B1);A(B2);A(B3);A(B4);D=E()
	if D not in[z,'2','3','4','5','6','7','8','9','0','q','Q','h',y]:A(H);T();return
	if D==z:AT()
	elif D=='x':
		A('This mode will download everything from the given url');A(G);F=E();F=Aj(F)
		if not F:A(B.WARNING+Ad+B.ENDC);J.sleep(2);T();return
		Aq(F)
	elif D=='2':A('Not implemented yet');J.sleep(2);T()
	elif D=='3':Ai()
	elif D=='4':AP()
	elif D=='5':
		if C.name==A9:C.system('start .\\anime')
		elif C.name=='posix':C.system('xdg-open .\\anime')
		else:A('Unsupported os');A('The anime folder is located in the following directory:');A(C.getcwd()+'\\anime');A('\nPress enter to continue');E();T()
		T()
	elif D=='6':
		A(G);F=E();F=Aj(F)
		if not F:A(B.WARNING+Ad+B.ENDC);J.sleep(2);T();return
		A(d(F))
	elif D=='0':BM();T()
	elif D=='h'or D==y:K();L();A(B.PRIMARY+'Info'+B.ENDC);A(I);A(f"{B.OK}This program was made by JMcrafter26 and published by Someone266 on Github{B.ENDC}");A(f"{B.OK}The program is open source and can be found here: https://github.com/Someone266/aniworld-downloader/{B.ENDC}");A(I);A('This program is still in development, so there might be some bugs');A('If you find a bug, please report it on the Github page');A(I);A(f"{B.OK}This program is for educational purposes only, the developer nor the publisher is responsible for any damage caused by the program. This program is not affiliated with any of the anime sites. This program is provided as is, without any warranty. Use at your own risk.{B.ENDC}");A(I);A(f);E();Am()
	elif D=='q'or D=='Q':A('Quitting...');r()
	else:A(B.WARNING+H+B.ENDC);J.sleep(2);T();return
def BN():
	D='./assets';K();L();A(B.PRIMARY+'Hi and welcome to AniWorld-Down v'+AU()+B.ENDC);A('It looks like this is your first time running this program, or you have deleted some files :)');A('This guide will help you get started with the program\n');A(B.WARNING+'This directory will be used to store the anime and the assets'+B.ENDC);A(B.SECONDARY+f+B.ENDC);E()
	if not C.path.exists(AE):C.makedirs(AE)
	if not C.path.exists(D):C.makedirs(D)
	BO()
def BO():
	F='updateNotes';G='Update notes:';K();L();A(B.PRIMARY+'Step 1: Checking for updates and downloading assets'+B.ENDC);A('We promise, it will be quick');C=An()
	if C is D:A('Hmm, something went wrong with the update check');A('Do you have an internet connection? \n');A(B.SECONDARY+'PS: We need an internet connection to download the assets'+B.ENDC);A(B.SECONDARY+AF+B.ENDC);E();r()
	if C[Y]=='error':A(B.WARNING+B5+B.ENDC);A(Ae,C[B6]);A('Please try again later\n');A(B.SECONDARY+AF+B.ENDC);E();r()
	elif C[Y]==B7:A(B8);A(B.SECONDARY+f+B.ENDC);E();AQ();return
	else:
		if C[AG][b]:A(B.OK+B9+B.ENDC);A(G);A(C[F][b]+I);A6(b,C[AH][b])
		if C[AG][c]:A(B.OK+BA+B.ENDC);A(G);A(C[F][c]+I);A6(c,C[AH][c])
		else:A('No program update available')
		A(B.SECONDARY+f+B.ENDC);E();AQ();return
def AQ():K();L();A(B.PRIMARY+'Step 2: Configuring the program'+B.ENDC);A('We need to configure the program before we can continue');A('It is very simple, just answer a few questions');A(B.SECONDARY+f+B.ENDC);E();Ak()
def Ak():
	K();L();A(B.PRIMARY+'Choose the option that describes you the best'+B.ENDC);A('1. I want to archive anime and have it nicely organized (with filestructure, prictures and an offline webserver)');A('2. I just want to download anime fast and continue watching (No filestructure, ready to watch or move)');A(I);A(B.SECONDARY+BB+B.ENDC);C=E()
	if C==z:A3(A0,BC)
	elif C=='2':A3(A0,BD)
	else:A(BE);Ak();return
	Al()
def Al():
	K();L();A(B.PRIMARY+'Select your preferred host'+B.ENDC);A('1. Voe (Recommended)');A('2. Streamtape');A(I);A(B.SECONDARY+BB+B.ENDC);C=E()
	if C==z:A3(m,Q)
	elif C=='2':A3(m,e)
	else:A(BE);Al();return
	BP()
def BP():
	K();L();A(B.PRIMARY+'Thats it, you are ready to go'+B.ENDC);A('You can now start downloading anime');A(I);A('Press i to read the instructions');A('Press enter to just freakin start the program');C=E()
	if C==y:Am()
	T()
def Am():K();L();A(B.PRIMARY+'Instructions'+B.ENDC);A(Ax);A('This option will guide you through the download process, you just need to enter the url of the anime');A(Ay);A('This option is not implemented yet');A(Az);A('This option will start a webserver to serve the content - you can watch the anime in your browser (even offline and other devices)');A(A_);A('This option will clean up the program and the assets');A(B0);A('This option will open the anime folder where the anime is stored');A(B1);A('This option will get the info of the anime from the url');A(B2);A('This option will allow you to change the settings of the program');A(B3);A('This is the current screen :)');A(B4);A(I);A(f);E();T()
BQ={A0:"The mode of AniDown\n'archive' will organize the anime with filestructure, pictures and an offline webserver\n'download' will download anime fast and continue watching",m:'The preferred host to download from'}
A5={A0:[BC,BD],m:[Q,e]}
type={A0:Af,m:Af}
def AR():
	L=f"{C.getcwd()}\\settings.json";K();A('Settings:');A('Path:',L);A(I)
	with F(g,P)as M:J=G.load(M)
	for(D,N)in J.items():O=list(J.keys()).index(D)+1;A(f"{B.PRIMARY}({O}) - {D}: {N}{B.ENDC}");A(f"{B.OK}Description: {B.ENDC}{B.SECONDARY}{BQ[D]}{B.ENDC}");A(f"{B.OK}Options: {B.ENDC}{B.SECONDARY}{A5[D]}{B.ENDC}");A('---')
	A('Choose an option by pressing the number (q to quit):');H=E()
	if not H or H=='q':return
	if not H.isdigit():return AR()
	AS(R(H),J);return AR()
def AS(option,data):
	H=data;C=option;D=list(H.keys())[C-1];K();A(f"Changing '{D}'")
	if type[D]==Af:
		A(f"{B.OK}Options:\n{B.ENDC}")
		for(I,C)in AV(A5[D]):A(f"({I+1}) - {C}")
		A('Choose an option by pressing the number:');C=E()
		if not C.isdigit():return AS(C,H)
		if R(C)>W(A5[D]):return AS(C,H)
		H[D]=A5[D][R(C)-1]
	else:
		if type[D]=='text':A('Enter the new value (Text/String):')
		elif type[D]=='number':A('Enter the new value (Number):')
		J=E();H[D]=J
	with F(g,X)as L:G.dump(H,L)
def BR(key):
	with F(g,P)as A:B=G.load(A)
	return B[key]
def BS():
	BK();K();L();A('Loading...');B=An()
	if B is D:A('No internet connection, skipping update check');return
	if B[Y]=='error':A(B5);A(Ae,B[B6]);J.sleep(2);return
	elif B[Y]==B7:A(B8);return
	else:
		if B[AG][b]:A(B9);A6(b,B[AH][b])
		if B[AG][c]:A(BA);A6(c,B[AH][c])
def An():
	E='./anime/assets/.version';A(Aw,end=M)
	try:S.get('https://api.jm26.net/status.txt',timeout=5)
	except S.exceptions.ConnectionError:A(' Skipped');A(B.WARNING+BF+B.ENDC);J.sleep(2);return
	H='https://api.jm26.net/update/aniworld-down/check/';I=AU()
	if not C.path.exists(E):G='0.0.0'
	else:
		with F(E,P)as K:G=K.read()
	D={c:I,b:G};L=S.post(H,data=D);D=L.json();A(' Done');return D
def A6(type,hash):
	Q='Please try again later';G='./update';A('Downloading ..');K=f"https://api.jm26.net/update/aniworld-down/download/?type={type}&hash={hash}";L='./update/update.zip'
	if A4():K=K+'&os=windows'
	if not C.path.exists(G):C.makedirs(G)
	try:N=S.get(K)
	except S.exceptions.ConnectionError:A(B.WARNING+BF+B.ENDC);A(Q);A(AF);E();r()
	if N.headers['Content-Type']=='application/json':A(B.WARNING+'Something went wrong with the download'+B.ENDC);A(Ae,N.text);A(Q);A(AF);E();r()
	A(B.OK+BG+B.ENDC)
	with F(L,'wb')as H:H.write(N.content)
	with zipfile.ZipFile(L,P)as R:R.extractall(G)
	C.remove(L)
	for D in C.listdir(G):
		if C.path.isdir(f"./update/{D}"):
			if not C.path.exists(f"./{D}"):C.makedirs(f"./{D}")
			for H in C.listdir(f"./update/{D}"):A1.move(C.path.join(f"./update/{D}",H),C.path.join(f"./{D}",H))
			C.rmdir(f"./update/{D}")
		else:A1.move(C.path.join(G,D),C.path.join('./',D))
	C.rmdir(G);A(B.OK+'Update complete'+B.ENDC);A(I);A(f"{B.WARNING}It is recommended to run the {B.ENDC}{B.OK}clean option{B.ENDC}{B.WARNING} after updating{B.ENDC}");A(I)
	if type==c:
		for T in l(3):A(f"\rRestarting in {3-T} seconds",end=M);J.sleep(1)
		A('\rRestarting program...')
		if not C.path.exists(g):
			if A4():C.system(f"start update.bat guideUpdateFinished")
			elif C.name==A9:C.system('py main.py guideUpdateFinished')
			else:C.system(f"python3 main.py guideUpdateFinished")
		elif A4():C.system(f"start update.bat "+n.join(O.argv[1:]))
		elif C.name==A9:C.system('py main.py '+n.join(O.argv[1:]))
		else:C.system('python3 main.py '+n.join(O.argv[1:]))
import sys as O,os as C,glob
from bs4 import BeautifulSoup as BT
from yt_dlp import YoutubeDL as BU
import base64 as Ao
def Ap(URL):
	K='var sources';J=URL;J=H(J);R={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language':'de,en-US;q=0.7,en;q=0.3','Upgrade-Insecure-Requests':z,'Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Priority':'u=1'};E=S.get(J,headers=R);L=BT(E.content,u)
	if E.text.startswith('<script>'):N="window.location.href = '";O=W(N);P=E.text.find(N);T=E.text.find("'",P+O);U=E.text[P+O:T];return Ap(U)
	V=L.find('meta',attrs={'name':'og:title'});D=V['content'];D=D.replace(n,'_');A('Name of file: '+D);F=L.find_all(string=h.compile(K));F=H(F);X=F.index(K);B=F[X:];Y=B.index(';');B=B[:Y];B=B.replace('var sources = ',M);B=B.replace("'",'"');B=B.replace('\\n',M);B=B.replace('\\',M);Z=',';a=M;B=a.join(B.rsplit(Z,1));Q=G.loads(B)
	try:C=Q['mp4'];C=Ao.b64decode(C);C=C.decode(t);AJ.download(C,out=f"{D}_SS.mp4")
	except Ar:
		try:
			C=Q['hls'];C=Ao.b64decode(C);C=C.decode(t);D=D+'_SS.mp4';b={'outtmpl':D}
			with BU(b)as c:
				try:c.download(C)
				except Exception as d:pass
			BV()
		except Ar:A('Could not find downloadable URL. Voe might have change their site. Check that you are running the latest version of voe-dl, and if so file an issue on GitHub.');quit()
	A(I);return D
def BV():
	A=C.getcwd()
	for B in glob.iglob(C.path.join(A,'*.part')):C.remove(B)
BW='1.1.6'
class B:PURPLE='\x1b[95m';SECONDARY='\x1b[90m';PRIMARY='\x1b[94m';CYAN='\x1b[96m';OK='\x1b[92m';WARNING='\x1b[93m';FAIL='\x1b[91m';ENDC='\x1b[0m';BOLD='\x1b[1m';UNDERLINE='\x1b[4m'
def Aq(url):
	k();C=d(url);A2(C)
	for D in C[Z]:AK(url,D,C[Z][D],C)
	E=C[a];A(E)
	for D in l(1,E+1):AN(D,C)
	AP();L();A(B.OK+'Finished downloading all episodes'+B.ENDC);A(I);A(B.PRIMARY+"Run 'serve' to watch the episodes in your browser"+B.ENDC)
def AT():
	K();L();k();A(B.OK+'This is the auto mode. It will ask you what to '+B.ENDC);A(I);A('Enter the name of the anime you want to search for or paste the url of the anime');F=E()
	if F.startswith('http'):A(G)
	elif F!=M and F!=D:G=Ah(F)
	else:A('Invalid input');J.sleep(2);AT();return
	C=d(G);A2(C)
	for H in C[Z]:AK(G,H,C[Z][H],C)
	A7(G,C)
def A7(url,info):
	K=url;C=info;L();A(B.OK+'Setup complete'+B.ENDC);A(I);A(B.OK+'We found '+H(C[a])+' seasons and a total of '+H(C[j])+' episodes'+B.ENDC);A(I);A('Do you want to download all episodes? (Y/n)');G=E()
	if G!='Y'and G!='y'and G!='yes'and G!='Yes'and G!=M:
		A('Which season do you want to download?');D=R(E());A('What episode do you want to download? (Enter 0 to download all episodes; use - to download a range of episodes)');F=R(E())
		if D<1 or D>C[a]:A(B.FAIL+'Invalid season'+B.ENDC);J.sleep(2);A7(K,C);return
		if F==0:AN(D,C)
		elif'-'in H(F):
			N=R(F.split('-')[0]);O=R(F.split('-')[1])
			if N<1 or O>C[Z][D]:A(B.FAIL+'Invalid range'+B.ENDC);J.sleep(2);A7(K,C);return
			BJ(D,N,O,C)
		else:
			if F<1 or F>C[Z][D]:A(B.FAIL+'Invalid episode'+B.ENDC);J.sleep(2);A7(K,C);return
			BI(D,F,C)
	else:
		A(B.OK+'Downloading all episodes'+B.ENDC)
		for D in l(1,C[a]+1):AN(D,C)
	A(B.OK+BG+B.ENDC);A(I);A(B.PRIMARY+'Press enter to return to the main menu'+B.ENDC);E();T()
def AU():return BW
def BX(url):k();A=d(url);return A
def BY(url):k();A=d(url);A2(A)
def BZ(url,season,info=D):
	A=season;k();B=D
	if info is not D:B=info[Z][A]
	C=AK(url,A,B);return C
def Ba(url,season,episode,info=D):
	C=season;A=info;B=episode;k()
	if A is not D:B=A[Z][C][B]
	E=AM(url,C,B,A);return E
def Bb():K();L();A('Enter the name of the anime you want to search for');B=E();return Ah(B)
def L():
	A(I);C=AU()
	if A4():C=C+' (Windows)'
	A(B.CYAN+'    AA          W     W         ll     d     DDD                    '+B.ENDC);A(B.CYAN+'   A  A      ii W     W          l     d     D  D                   '+B.ENDC);A(B.CYAN+'   AAAA nnn     W  W  W ooo rrr  l   ddd     D  D ooo w   w nnn     '+B.ENDC);A(B.CYAN+'   A  A n  n ii  W W W  o o r    l  d  d     D  D o o w w w n  n    '+B.ENDC);A(B.CYAN+'   A  A n  n ii   W W   ooo r   lll  ddd     DDD  ooo  w w  n  n    '+B.ENDC);A(B.CYAN+'                                                                    '+B.ENDC);A('A powerful scraper and downloader for AniWorld');A(n);A('Version: '+C+'                                 Made by JMcrafter26');A(B.SECONDARY+'DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.'+B.ENDC);A(B.SECONDARY+'Please respect the laws of your country and the country of the website you are scraping.'+B.ENDC);A(I)
def Bc():
	H='help';J='clean';M='serve';N='search'
	if W(O.argv)==1:O.argv.append('ui')
	C=O.argv[1]
	if C=='guideUpdateFinished':BL();return
	BS();K();L();A(I)
	if C=='getinfo':E=O.argv[3];A(BX(E))
	elif C=='run':E=O.argv[2];Aq(E)
	elif C=='ui':T()
	elif C==N:Bb();return
	elif C==M:Ai()
	elif C==J:AP()
	elif C=='setup':E=O.argv[3];BY(E)
	elif C=='auto':AT()
	elif C=='getseason':
		E=O.argv[3];G=O.argv[5];F=D
		if W(O.argv)>6:F=d(E)
		A(BZ(E,G,F))
	elif C=='getepisode':
		E=O.argv[3];G=O.argv[5];P=O.argv[7];F=D
		if W(O.argv)>8:F=d(E)
		A(Ba(E,G,P,F))
	elif C==H:A(B.PRIMARY+'Commands:'+B.ENDC);A('-----------------');A('run -url <url>');A(M);A(J);A(N);A('setup -url <url>');A('getinfo -url <url>');A('getseason -url <url> -season <season>');A('getepisode -url <url> -season <season> -episode <episode>');A(H)
	else:A(B.WARNING+'Invalid command'+B.ENDC)
	A(I)
if __name__=='__main__':Bc()