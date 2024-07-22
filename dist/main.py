# Aniworld Scraper
# Author: JMcrafter26
# Description: A scraper for aniworld (german anime site)
# Version: see version variable below
# License: MIT License
# DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.
# Please respect the laws of your country and the country of the website you are scraping.

# This code was minified to save space. If you want to read the code, please read the original files.


BE='Download complete'
BD='No internet connection'
BC='Invalid option, try again'
BB='download'
BA='archive'
B9='Choose an option by pressing the number'
B8='There is a program update available'
B7='Downloading assets...'
B6='You are up to date'
B5='success'
B4='message'
B3='Something went wrong with the update check'
B2='q. Quit'
B1='h. Help/Info'
B0='0. Settings'
A_='6. Get anime info'
Az='5. Open anime folder'
Ay='4. Clean up'
Ax='3. Serve content'
Aw='2. Continue Download'
Av='1. Download Assistant'
Au='Checking for updates...'
At='Episoden:'
As='producer'
Ar='trailer'
Aq='animeSeason'
Ap=KeyError
Ad='option'
Ac='Error:'
Ab='utf-8'
Aa='Invalid url'
AZ='anime'
AY='stream.json'
AX='url'
AW='fsk'
AV='Or paste your cookie key in the settings'
AU='DDoS-Guard'
AT='aniworld.to'
AS=enumerate
AE='updateHash'
AD='update'
AC='Press enter to exit'
AB='./anime'
AA='update.bat'
A9='./anime/index.json'
A8='href'
A7='strong'
A6='nt'
A0='mode'
z='/stream.json'
y='picture'
x='https://aniworld.to'
w='html.parser'
v='anime/'
u='downloads'
t=exit
q='pathname'
p='[<>:"/\\\\|?*]'
o='tags'
n=' '
m='prefHost'
l=range
j='totalEpisodes'
i='description'
g='Press enter to continue'
e='program'
d='settings.json'
c='assets'
b='w'
a='seasons'
Z='episodes'
Y='status'
X='streamtape'
W='enddate'
V='startdate'
U=len
R=int
Q='voe'
P='r'
N='title'
M=''
I='\n'
H=str
G=open
E=input
D=None
A=print
import os as C,shutil as r,time as J,json as F
def AF(path,season,episode):
	K=episode;I=season;E=path
	if E is not D and I is not D and K is not D:
		if C.path.exists(f"{E}/video/{I}/{K}.mp4"):A(f"{B.WARNING}File {E}/video/{I}/{K}.mp4 already exists. Skipping...{B.ENDC}");return
	if not C.path.exists(u):C.makedirs(u)
	L=E.split(v)[1]
	if not C.path.exists(f"downloads/{L}"):C.makedirs(f"downloads/{L}")
	N=BP(m)
	with G(f"{E}/stream.json",P)as O:R=F.load(O)
	C.chdir(f"downloads/{L}");N=Q
	if N==Q:S=R[Q][H(I)][H(K)];M=An(S)
	elif N==X:0
	else:A('Invalid host');J.sleep(2);return
	if M is D:A(f"{B.FAIL}Download failed{B.ENDC}");J.sleep(2);return
	C.chdir('../../');C.makedirs(f"{E}/video/{I}",exist_ok=True);M=f"downloads/{L}/{M}";r.move(f"{M}",f"{E}/video/{I}/{K}.mp4");A(f"Moved to {E}/video/{I}/{K}.mp4")
import wget as AG,requests as S,re as h,sys as O,bs4,http.server,zipfile
def Bb(title='AniWorld Scraper'):
	B=title
	if C.name==A6:C.system(f"title {B}")
	else:A(f"]0;{B}\a")
def f(url):
	d='span';P='a';Q='div';G=url
	if'/filme/'in G:A(B.WARNING+'This type of url is not supported yet. It will probably be supported in the future'+B.ENDC);J.sleep(2);return
	if AT not in G:A(B.WARNING+'Invalid url! Please enter a valid aniworld.to url'+B.ENDC);J.sleep(2);return
	h=S.get(G);e=h.text
	if AU in e:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(AV);J.sleep(2);return
	E=bs4.BeautifulSoup(e,w);F=E.find(Q,class_='series-title').find('h1').string;F=F.strip();F=F.split(I)[0];A('Getting info for:',F);k=E.find('p',class_='seri_des').get('data-full-description');O=E.find(d,itemprop='startDate').string;T=E.find(d,itemprop='endDate').string
	if T=='heute':X='ONGOING'
	else:X='FINISHED'
	C=E.find(A7,string='Staffeln:').parent.parent.parent.find_all('li');C=[A.text for A in C];C=[A.replace(n,M)for A in C];C=[A for A in C if A];C=[A for A in C if A.isnumeric()];C=U(C);K={}
	for f in l(1,R(C)+1):K[f]=BF(G,f)
	K=K;g=sum(K.values());b=E.find(Q,class_='seriesCoverBox').find('noscript').find('img').get('src');b=x+b;m=E.find(P,class_='trailerButton').get(A8);c=E.find_all(P,itemprop='genre');c=[A.string for A in c];p=E.find(A7,class_='seriesProducer').text;q=E.find(Q,class_=AW).get('data-fsk');L=E.find(P,class_='imdb-link')
	if L is not D:L=L.get(A8)
	else:L=M
	A(X+' ('+O+' - '+T+') - '+H(g)+' episodes - '+H(C)+' seasons');r={N:F,i:k,Aq:{'year':R(O[:4]),'season':O[5:]},Y:X,Z:K,j:g,a:C,V:O,W:T,y:b,Ar:m,o:c,As:p,AW:q,'imdb':L,AX:G};return r
def A1(info):
	B=info;A('Setting up anime folder...');D=f"{B[N]} ({B[V]}-{B[W]})";D=h.sub(p,M,D);D=f"anime/{D}";I=f"./{D}"
	if not C.path.exists(D):C.makedirs(D)
	with G(f"{D}/info.json",b)as E:F.dump(B,E,indent=4)
	J=B[y].split('.')[-1]
	if not C.path.exists(f"{I}/image.{J}"):AG.download(B[y],f"{I}/image.{J}")
	B[y]=f"image.{J}";B[q]=I
	with G(f"{D}/info.json",b)as E:F.dump(B,E,indent=4)
	if C.path.exists(A9):
		with G(A9,P)as E:H=F.load(E)
	else:H=[]
	K={N:B[N],o:B[o],V:B[V],W:B[W],Y:B[Y],i:B[i],j:B[j],a:B[a],q:I}
	for(L,O)in AS(H):
		if O[N]==B[N]:H[L]=K;break
	else:H.append(K)
	with G(A9,b)as E:F.dump(H,E,indent=4)
	A('Anime folder setup complete')
def AH(url,season,episodes=D,info=D):
	T='Season stream urls already exist';R=url;K=info;J=season;E=episodes
	if E is D:Y=S.get(R);Z=Y.text;a=bs4.BeautifulSoup(Z,w);E=a.find(A7,string=At).parent.parent.parent;E=E.find_all('li');E=U(E)-1
	A(f"Getting streams for season {J} with {E} episodes...");L=f"{K[N]} ({K[V]}-{K[W]})";L=h.sub(p,M,L);A('Path:',L)
	if C.path.exists(v+L+z):
		with G(v+L+z,P)as b:
			B=F.load(b);A('Found stream.json');A('Checking if season already exists...')
			if Q in B:
				if U(B[Q][H(J)])>=1:A(T);return B
			if X in B:
				if U(B[X][H(J)])>=1:A(T);return B
	else:B={}
	B={}
	for O in l(1,E+1):
		if K is not D:B[O]=AJ(R,J,O,K)
		else:B[O]=AJ(R,J,O)
		AI(O/E)
	A(I);A('Done with season',J);return B
def AI(percent):A=percent;B=50;C=R(round(B*A));D='='*C+'-'*(B-C);O.stdout.write(f"\rProgress: [{D}] {A*100:.2f}%");O.stdout.flush()
def AJ(url,season,episode,info=D):
	a='No stream url found';Z=url;Y=info;U=episode;K=season;Z=Z+f"/staffel-{K}/episode-{U}";e=S.get(Z);c=e.text
	if AU in c:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(AV);J.sleep(2);return
	d=bs4.BeautifulSoup(c,w)
	if Y is not D:I=f"{Y[N]} ({Y[V]}-{Y[W]})";I=h.sub(p,M,I);I=f"anime/{I}/stream.json"
	else:I=f"stream.json"
	L=d.find('i',class_='icon VOE')
	if L is D:A('No voe download found, skipping...');return
	L=L.parent;L=L.get(A8);L=x+L;T=Ae(L)
	if T is D:A(a);return
	if C.path.exists(I):
		with G(I,P)as R:E=F.load(R)
	else:E={}
	if H(Q)not in E:E[Q]={}
	if H(K)not in E[Q]:E[Q][H(K)]={}
	E[Q][H(K)][H(U)]=T
	with G(I,b)as R:F.dump(E,R,indent=4)
	O=d.find('i',class_='icon Streamtape')
	if O is D:A('No streamtape download found, skipping...');return
	O=O.parent;O=O.get(A8);O=x+O;T=Ae(O)
	if T is D:A(a);return
	if C.path.exists(I):
		with G(I,P)as R:E=F.load(R)
	else:E={}
	if H(X)not in E:E[X]={}
	if H(K)not in E[X]:E[X][H(K)]={}
	E[X][H(K)][H(U)]=T
	with G(I,b)as R:F.dump(E,R,indent=4)
	if E[Q][H(K)][H(U)]is not D:return E[Q][H(K)][H(U)]
	else:return T
def Ae(url):
	B=S.head(url)
	if B.status_code!=302 and B.status_code!=301:A('No redirect found');return
	else:
		C=B.headers['Location']
		if AT in C:A('Something went wrong with the redirect');return
		else:return C
def BF(url,season):B=url;B=B+f"/staffel-{season}";C=S.get(B);D=C.text;E=bs4.BeautifulSoup(D,w);A=E.find(A7,string=At).parent.parent.parent;A=A.find_all('li');A=U(A)-1;return A
def BG(season,episode,info=D):
	H=episode;I=season;C=info;K();L()
	if C is D:
		with G(AY,P)as E:J=F.load(E)
	else:
		B=f"{C[N]} ({C[V]}-{C[W]})";B=h.sub(p,M,B);B=f"anime/{B}"
		with G(B+z,P)as E:J=F.load(E)
	A(f"Downloading season {I} episode {H}...");AF(B,I,H)
def AK(season,info=D):
	C=info;E=season
	if C is D:
		with G(AY,P)as J:O=F.load(J)
	else:
		B=f"{C[N]} ({C[V]}-{C[W]})";B=h.sub(p,M,B);B=f"anime/{B}"
		with G(B+z,P)as J:O=F.load(J)
	for S in O[Q][H(E)]:K();L();A(f"Downloading season {E} episode {S}...");AI(R(S)/U(O[Q][H(E)]));A(I);AF(B,E,S)
def BH(season,start,end,info=D):
	O=season;E=start;C=info
	if C is D:
		with G(AY,P)as H:Q=F.load(H)
	else:
		B=f"{C[N]} ({C[V]}-{C[W]})";B=h.sub(p,M,B);B=f"anime/{B}"
		with G(B+z,P)as H:Q=F.load(H)
	for J in l(E,end+1):K();L();A(f"Downloading season {O} episode {J}...");AI((J-E)/(end-E));A(I);AF(B,O,J)
def Af(query):
	E=query
	if E==M or E==D:A(B.WARNING+'No query entered'+B.ENDC);J.sleep(2);return
	G='https://aniworld.to/ajax/search';H={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':x,'referer':f"https://aniworld.to/search?q={E}",'sec-ch-ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with':'XMLHttpRequest'};C={'keyword':E};C=S.post(G,headers=H,data=C);C=C.text
	try:C=F.loads(C)
	except:
		if AU in C:A(f"{B.WARNING}DDoS-Guard detected{B.ENDC}");A(AV);J.sleep(2);return
		A(f"{B.WARNING}Error parsing JSON{B.ENDC}");A('Try again later');J.sleep(2);return
	return AL(E,C)
def AL(query,data):
	O='Invalid number, try again';H=query;F='link';C=data;C=[A for A in C if'/anime/stream/'in A[F]];C=[A for A in C if'/support/'not in A[F]];C=[A for A in C if'/user/'not in A[F]];C=[A for A in C if'/search/'not in A[F]];C=[A for A in C if'/episode-'not in A[F]];C=[A for A in C if'/staffel-'not in A[F]];K();L();A('Search results for:',H);A(I)
	for(S,G)in AS(C):G[N]=G[N].replace('<em>',M).replace('</em>',M);A(S+1,B.OK+G[N]+B.ENDC);A(G[i]);A('---')
	A(B.PRIMARY+'Select a number to continue, or press q to quit'+B.ENDC);D=E()
	if D=='q':return
	elif not D.isnumeric():A(O);J.sleep(2);AL(H,C);return
	elif R(D)<1 or R(D)>U(C):A(O);J.sleep(2);AL(H,C);return
	D=R(D);P=C[D-1][F];A('Selected:',C[D-1][N]);A(P);Q=x+P;A('url:',Q);return Q
def Ag():
	B=3333;D=http.server.SimpleHTTPRequestHandler;E=C.path.join(C.getcwd(),AZ);C.chdir(E)
	with http.server.HTTPServer((M,B),D)as F:A('serving at http://localhost:'+H(B)+'/');A('Press Ctrl+C to stop the server');F.serve_forever()
def AM():
	R='Removed:';S='index.html';K();L();A('Running cleanup...');U=[C.path.join(B,A)for(B,E,D)in C.walk('./downloads')for A in D if A.endswith('.part')or A.endswith('.ytdl')]
	if U:
		A(B.WARNING+'Do you want to delete non finished downloads? After deleting you have to restart the download'+B.ENDC);A('Do you want to continue? (y/N)');J=E()
		if J.lower()=='y':
			A('Deleting files...')
			for I in U:C.remove(I);A('Deleted:',I)
	A('Rebuilding index.json...');O=[A for A in C.listdir(AZ)if C.path.isdir(C.path.join(AZ,A))];X=[]
	for H in O:
		if not C.listdir(f"anime/{H}"):C.rmdir(f"anime/{H}");continue
		if not C.path.exists(f"anime/{H}/info.json"):continue
		if C.path.exists(f"anime/{H}/stream.json"):C.remove(f"anime/{H}/stream.json")
		with G(f"anime/{H}/info.json",P)as Q:D=F.load(Q)
		if AX not in D:
			A('No url found for:','/'+H+'/ ('+D[N]+')'+', should we remove it? (Y/n)');J=E()
			if J.lower()=='n':continue
			A('Removing:',D[N]);r.rmtree(f"anime/{H}");continue
		if v in D[q]:D[q]=D[q].replace(v,M)
		d=[N,i,Aq,Y,Z,j,a,V,W,y,Ar,o,As,AW,'imdb']
		if not all(A in D for A in d):A('Rebuilding info.json for:',D[N]);D=f(D[AX]);A1(D)
		X.append({N:D[N],o:D[o],V:D[V],W:D[W],Y:D[Y],i:D[i],j:D[j],a:D[a],q:f"{H}"})
	with G(A9,b)as Q:F.dump(X,Q,indent=4)
	A('Cleaning file structure...')
	if C.path.exists(S):C.remove(S)
	e=['assets/bootstrap.min.css','assets/css','assets/js','assets/plyr.css','assets/plyr.js','assets/animeList.json','assets/placeholder.jpg','assets/fuse.min.js','assets/.version'];A('Removing unused files...')
	for I in e:
		if C.path.exists(I):C.remove(I);A(R,I)
	if C.path.exists(c):C.rmdir(c);A('Removed: assets/')
	if C.path.exists(u):
		O=[A for A in C.listdir(u)if C.path.isdir(C.path.join(u,A))]
		for H in O:
			if not C.listdir(f"downloads/{H}"):C.rmdir(f"downloads/{H}");A(R,f"downloads/{H}")
	A('Done');A(g);E();T()
def Ah(url):
	C='episode';D='staffel';B=url
	if AT not in B:A(Aa);return False
	if D in B:B=B.split(D)[0]
	if C in B:B=B.split(C)[0]
	return B
def BI():
	if not C.path.exists(d):BL();return
	if C.path.exists(AA):C.remove(AA)
	elif not C.path.exists(AB):C.makedirs(AB)
def A2(key,value):
	if C.path.exists(d):
		with G(d,P)as A:B=F.load(A)
	else:B={}
	B[key]=value
	with G(d,b)as A:F.dump(B,A,indent=4)
def BJ():
	if C.path.exists(AA):C.remove(AA)
	K();L();A(B.PRIMARY+'Update finished'+B.ENDC);A('The program has been updated, YIPPIE!');A(g);E();AN()
def BK():AO()
def A3():return False
def k():
	B='./assets/animeList.json';return;A(Au);H='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database-minified.json';I='https://api.github.com/repos/manami-project/anime-offline-database/commits?path=anime-offline-database-minified.json&page=1&per_page=1';J=S.get(I);D=J.json();K=D[0]['commit']['committer']['date'][:10]
	if C.path.exists(B):
		with G(B,P)as E:D=F.load(E)
		L=D['lastUpdate']
		if L==K:A('Anime list is up to date');return
	A('Downloading anime list...');AG.download(H,B);D=F.load(G(B,P,encoding=Ab))
	with G(B,b)as E:F.dump(D,E,indent=4)
	A('Anime list downloaded')
def K():A('\x1b[H\x1b[J')
def T():
	G='Enter the url of the anime';H='Invalid key';K();L();A('Press one of the following keys:');A(Av);A(Aw);A(Ax);A(Ay);A(Az);A(A_);A(B0);A(B1);A(B2);D=E()
	if D not in['1','2','3','4','5','6','7','8','9','0','q','Q','h','i']:A(H);T();return
	if D=='1':AQ()
	elif D=='x':
		A('This mode will download everything from the given url');A(G);F=E();F=Ah(F)
		if not F:A(B.WARNING+Aa+B.ENDC);J.sleep(2);T();return
		Ao(F)
	elif D=='2':A('Not implemented yet');J.sleep(2);T()
	elif D=='3':Ag()
	elif D=='4':AM()
	elif D=='5':
		if C.name==A6:C.system('start .\\anime')
		elif C.name=='posix':C.system('xdg-open .\\anime')
		else:A('Unsupported os');A('The anime folder is located in the following directory:');A(C.getcwd()+'\\anime');A('\nPress enter to continue');E();T()
		T()
	elif D=='6':
		A(G);F=E();F=Ah(F)
		if not F:A(B.WARNING+Aa+B.ENDC);J.sleep(2);T();return
		A(f(F))
	elif D=='0':BK();T()
	elif D=='h'or D=='i':K();L();A(B.PRIMARY+'Info'+B.ENDC);A(I);A(f"{B.OK}This program was made by JMcrafter26 and published by Someone266 on Github{B.ENDC}");A(f"{B.OK}The program is open source and can be found here: https://github.com/Someone266/aniworld-downloader/{B.ENDC}");A(I);A('This program is still in development, so there might be some bugs');A('If you find a bug, please report it on the Github page');A(I);A(f"{B.OK}This program is for educational purposes only, the developer nor the publisher is responsible for any damage caused by the program. This program is not affiliated with any of the anime sites. This program is provided as is, without any warranty. Use at your own risk.{B.ENDC}");A(I);A(g);E();Ak()
	elif D=='q'or D=='Q':A('Quitting...');t()
	else:A(B.WARNING+H+B.ENDC);J.sleep(2);T();return
def BL():
	D='./assets';K();L();A(B.PRIMARY+'Hi and welcome to AniWorld-Down v'+AR()+B.ENDC);A('It looks like this is your first time running this program, or you have deleted some files :)');A('This guide will help you get started with the program\n');A(B.WARNING+'This directory will be used to store the anime and the assets'+B.ENDC);A(B.SECONDARY+g+B.ENDC);E()
	if not C.path.exists(AB):C.makedirs(AB)
	if not C.path.exists(D):C.makedirs(D)
	BM()
def BM():
	F='updateNotes';G='Update notes:';K();L();A(B.PRIMARY+'Step 1: Checking for updates and downloading assets'+B.ENDC);A('We promise, it will be quick');C=Al()
	if C is D:A('Hmm, something went wrong with the update check');A('Do you have an internet connection? \n');A(B.SECONDARY+'PS: We need an internet connection to download the assets'+B.ENDC);A(B.SECONDARY+AC+B.ENDC);E();t()
	if C[Y]=='error':A(B.WARNING+B3+B.ENDC);A(Ac,C[B4]);A('Please try again later\n');A(B.SECONDARY+AC+B.ENDC);E();t()
	elif C[Y]==B5:A(B6);A(B.SECONDARY+g+B.ENDC);E();AN();return
	else:
		if C[AD][c]:A(B.OK+B7+B.ENDC);A(G);A(C[F][c]+I);A4(c,C[AE][c])
		if C[AD][e]:A(B.OK+B8+B.ENDC);A(G);A(C[F][e]+I);A4(e,C[AE][e])
		else:A('No program update available')
		A(B.SECONDARY+g+B.ENDC);E();AN();return
def AN():K();L();A(B.PRIMARY+'Step 2: Configuring the program'+B.ENDC);A('We need to configure the program before we can continue');A('It is very simple, just answer a few questions');A(B.SECONDARY+g+B.ENDC);E();Ai()
def Ai():
	K();L();A(B.PRIMARY+'Choose the option that describes you the best'+B.ENDC);A('1. I want to archive anime and have it nicely organized (with filestructure, prictures and an offline webserver)');A('2. I just want to download anime fast and continue watching (No filestructure, ready to watch or move)');A(I);A(B.SECONDARY+B9+B.ENDC);C=E()
	if C=='1':A2(A0,BA)
	elif C=='2':A2(A0,BB)
	else:A(BC);Ai();return
	Aj()
def Aj():
	K();L();A(B.PRIMARY+'Select your preferred host'+B.ENDC);A('1. Voe (Recommended)');A('2. Streamtape');A(I);A(B.SECONDARY+B9+B.ENDC);C=E()
	if C=='1':A2(m,Q)
	elif C=='2':A2(m,X)
	else:A(BC);Aj();return
	BN()
def BN():
	K();L();A(B.PRIMARY+'Thats it, you are ready to go'+B.ENDC);A('You can now start downloading anime');A(I);A('Press i to read the instructions');A('Press enter to just freakin start the program');C=E()
	if C=='i':Ak()
	T()
def Ak():K();L();A(B.PRIMARY+'Instructions'+B.ENDC);A(Av);A('This option will guide you through the download process, you just need to enter the url of the anime');A(Aw);A('This option is not implemented yet');A(Ax);A('This option will start a webserver to serve the content - you can watch the anime in your browser (even offline and other devices)');A(Ay);A('This option will clean up the program and the assets');A(Az);A('This option will open the anime folder where the anime is stored');A(A_);A('This option will get the info of the anime from the url');A(B0);A('This option will allow you to change the settings of the program');A(B1);A('This is the current screen :)');A(B2);A(I);A(g);E();T()
BO={A0:"The mode of AniDown\n'archive' will organize the anime with filestructure, pictures and an offline webserver\n'download' will download anime fast and continue watching",m:'The preferred host to download from'}
s={A0:[BA,BB],m:[Q,X]}
type={A0:Ad,m:Ad}
def AO():
	L=f"{C.getcwd()}\\settings.json";K();A('Settings:');A('Path:',L);A(I)
	with G(d,P)as M:J=F.load(M)
	for(D,N)in J.items():O=list(J.keys()).index(D)+1;A(f"{B.PRIMARY}({O}) - {D}: {N}{B.ENDC}");A(f"{B.OK}Description: {B.ENDC}{B.SECONDARY}{BO[D]}{B.ENDC}");A(f"{B.OK}Options: {B.ENDC}{B.SECONDARY}{s[D]}{B.ENDC}");A('---')
	A('Choose an option by pressing the number (q to quit):');H=E()
	if not H or H=='q':return
	if not H.isdigit():return AO()
	AP(R(H),J);return AO()
def AP(option,data):
	H=data;C=option;D=list(H.keys())[C-1];K();A(f"Changing '{D}'")
	if type[D]==Ad:
		A(f"{B.OK}Options:\n{B.ENDC}")
		for(I,C)in AS(s[D]):A(f"({I+1}) - {C}")
		A('Choose an option by pressing the number:');C=E()
		if not C.isdigit():return AP(C,H)
		if R(C)>U(s[D]):return AP(C,H)
		H[D]=s[D][R(C)-1]
	else:
		if type[D]=='text':A('Enter the new value (Text/String):')
		elif type[D]=='number':A('Enter the new value (Number):')
		J=E();H[D]=J
	with G(d,b)as L:F.dump(H,L)
def BP(key):
	A=key
	with G(d,P)as C:B=F.load(C)
	if A not in B:
		B[A]=s[A][0]
		with G(d,b)as C:F.dump(B,C)
	return B[A]
def BQ():
	BI();K();L();A('Loading...');B=Al()
	if B is D:A('No internet connection, skipping update check');return
	if B[Y]=='error':A(B3);A(Ac,B[B4]);J.sleep(2);return
	elif B[Y]==B5:A(B6);return
	else:
		if B[AD][c]:A(B7);A4(c,B[AE][c])
		if B[AD][e]:A(B8);A4(e,B[AE][e])
def Al():
	E='anime/assets/.version';A(Au,end=M)
	try:S.get('https://api.jm26.net/status.txt',timeout=5)
	except S.exceptions.ConnectionError:A(' Skipped');A(B.WARNING+BD+B.ENDC);J.sleep(2);return
	H='https://api.jm26.net/update/aniworld-down/check/';I=AR()
	if not C.path.exists(E):F='0.0.0'
	else:
		with G(E,P)as K:F=K.read()
	D={e:I,c:F};L=S.post(H,data=D);D=L.json();A(' Done');return D
def A4(type,hash):
	Q='anime/assets';R='Please try again later';F='./update';A('Downloading ..');K=f"https://api.jm26.net/update/aniworld-down/download/?type={type}&hash={hash}";L='./update/update.zip'
	if A3():K=K+'&os=windows'
	if not C.path.exists(F):C.makedirs(F)
	try:N=S.get(K)
	except S.exceptions.ConnectionError:A(B.WARNING+BD+B.ENDC);A(R);A(AC);E();t()
	if N.headers['Content-Type']=='application/json':A(B.WARNING+'Something went wrong with the download'+B.ENDC);A(Ac,N.text);A(R);A(AC);E();t()
	A(B.OK+BE+B.ENDC)
	with G(L,'wb')as H:H.write(N.content)
	with zipfile.ZipFile(L,P)as T:T.extractall(F)
	C.remove(L)
	if C.path.exists(Q):r.rmtree(Q)
	for D in C.listdir(F):
		if C.path.isdir(f"./update/{D}"):
			if not C.path.exists(f"./{D}"):C.makedirs(f"./{D}")
			for H in C.listdir(f"./update/{D}"):r.move(C.path.join(f"./update/{D}",H),C.path.join(f"./{D}",H))
			C.rmdir(f"./update/{D}")
		else:r.move(C.path.join(F,D),C.path.join('./',D))
	C.rmdir(F);A(B.OK+'Update complete'+B.ENDC);A(I);A(f"{B.WARNING}It is recommended to run the {B.ENDC}{B.OK}clean option{B.ENDC}{B.WARNING} after updating{B.ENDC}");A(I)
	if type==e:
		for U in l(3):A(f"\rRestarting in {3-U} seconds",end=M);J.sleep(1)
		A('\rRestarting program...')
		if not C.path.exists(d):
			if A3():C.system(f"start update.bat guideUpdateFinished")
			elif C.name==A6:C.system('py main.py guideUpdateFinished')
			else:C.system(f"python3 main.py guideUpdateFinished")
		elif A3():C.system(f"start update.bat "+n.join(O.argv[1:]))
		elif C.name==A6:C.system('py main.py '+n.join(O.argv[1:]))
		else:C.system('python3 main.py '+n.join(O.argv[1:]))
import sys as O,os as C,glob
from bs4 import BeautifulSoup as BR
from yt_dlp import YoutubeDL as BS
import base64 as Am
def An(URL):
	K='var sources';J=URL;J=H(J);R={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language':'de,en-US;q=0.7,en;q=0.3','Upgrade-Insecure-Requests':'1','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Priority':'u=1'};E=S.get(J,headers=R);L=BR(E.content,w)
	if E.text.startswith('<script>'):N="window.location.href = '";O=U(N);P=E.text.find(N);T=E.text.find("'",P+O);V=E.text[P+O:T];return An(V)
	W=L.find('meta',attrs={'name':'og:title'});D=W['content'];D=D.replace(n,'_');A('Name of file: '+D);G=L.find_all(string=h.compile(K));G=H(G);X=G.index(K);B=G[X:];Y=B.index(';');B=B[:Y];B=B.replace('var sources = ',M);B=B.replace("'",'"');B=B.replace('\\n',M);B=B.replace('\\',M);Z=',';a=M;B=a.join(B.rsplit(Z,1));Q=F.loads(B)
	try:C=Q['mp4'];C=Am.b64decode(C);C=C.decode(Ab);AG.download(C,out=f"{D}_SS.mp4")
	except Ap:
		try:
			C=Q['hls'];C=Am.b64decode(C);C=C.decode(Ab);D=D+'_SS.mp4';b={'outtmpl':D}
			with BS(b)as c:
				try:c.download(C)
				except Exception as d:pass
			BT()
		except Ap:A('Could not find downloadable URL. Voe might have change their site. Check that you are running the latest version of voe-dl, and if so file an issue on GitHub.');quit()
	A(I);return D
def BT():
	A=C.getcwd()
	for B in glob.iglob(C.path.join(A,'*.part')):C.remove(B)
BU='1.1.7'
class B:PURPLE='\x1b[95m';SECONDARY='\x1b[90m';PRIMARY='\x1b[94m';CYAN='\x1b[96m';OK='\x1b[92m';WARNING='\x1b[93m';FAIL='\x1b[91m';ENDC='\x1b[0m';BOLD='\x1b[1m';UNDERLINE='\x1b[4m'
def Ao(url):
	k();C=f(url);A1(C)
	for D in C[Z]:AH(url,D,C[Z][D],C)
	E=C[a];A(E)
	for D in l(1,E+1):AK(D,C)
	AM();L();A(B.OK+'Finished downloading all episodes'+B.ENDC);A(I);A(B.PRIMARY+"Run 'serve' to watch the episodes in your browser"+B.ENDC)
def AQ():
	K();L();k();A(B.OK+'This is the auto mode. It will ask you what to '+B.ENDC);A(I);A('Enter the name of the anime you want to search for or paste the url of the anime');F=E()
	if F.startswith('http'):A(G)
	elif F!=M and F!=D:G=Af(F)
	else:A('Invalid input');J.sleep(2);AQ();return
	C=f(G);A1(C)
	for H in C[Z]:AH(G,H,C[Z][H],C)
	A5(G,C)
def A5(url,info):
	K=url;C=info;L();A(B.OK+'Setup complete'+B.ENDC);A(I);A(B.OK+'We found '+H(C[a])+' seasons and a total of '+H(C[j])+' episodes'+B.ENDC);A(I);A('Do you want to download all episodes? (Y/n)');G=E()
	if G!='Y'and G!='y'and G!='yes'and G!='Yes'and G!=M:
		A('Which season do you want to download?');D=R(E());A('What episode do you want to download? (Enter 0 to download all episodes; use - to download a range of episodes)');F=R(E())
		if D<1 or D>C[a]:A(B.FAIL+'Invalid season'+B.ENDC);J.sleep(2);A5(K,C);return
		if F==0:AK(D,C)
		elif'-'in H(F):
			N=R(F.split('-')[0]);O=R(F.split('-')[1])
			if N<1 or O>C[Z][D]:A(B.FAIL+'Invalid range'+B.ENDC);J.sleep(2);A5(K,C);return
			BH(D,N,O,C)
		else:
			if F<1 or F>C[Z][D]:A(B.FAIL+'Invalid episode'+B.ENDC);J.sleep(2);A5(K,C);return
			BG(D,F,C)
	else:
		A(B.OK+'Downloading all episodes'+B.ENDC)
		for D in l(1,C[a]+1):AK(D,C)
	A(B.OK+BE+B.ENDC);A(I);A(B.PRIMARY+'Press enter to return to the main menu'+B.ENDC);E();T()
def AR():return BU
def BV(url):k();A=f(url);return A
def BW(url):k();A=f(url);A1(A)
def BX(url,season,info=D):
	A=season;k();B=D
	if info is not D:B=info[Z][A]
	C=AH(url,A,B);return C
def BY(url,season,episode,info=D):
	C=season;A=info;B=episode;k()
	if A is not D:B=A[Z][C][B]
	E=AJ(url,C,B,A);return E
def BZ():K();L();A('Enter the name of the anime you want to search for');B=E();return Af(B)
def L():
	A(I);C=AR()
	if A3():C=C+' (Windows)'
	A(B.CYAN+'    AA          W     W         ll     d     DDD                    '+B.ENDC);A(B.CYAN+'   A  A      ii W     W          l     d     D  D                   '+B.ENDC);A(B.CYAN+'   AAAA nnn     W  W  W ooo rrr  l   ddd     D  D ooo w   w nnn     '+B.ENDC);A(B.CYAN+'   A  A n  n ii  W W W  o o r    l  d  d     D  D o o w w w n  n    '+B.ENDC);A(B.CYAN+'   A  A n  n ii   W W   ooo r   lll  ddd     DDD  ooo  w w  n  n    '+B.ENDC);A(B.CYAN+'                                                                    '+B.ENDC);A('A powerful scraper and downloader for AniWorld');A(n);A('Version: '+C+'                                 Made by JMcrafter26');A(B.SECONDARY+'DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.'+B.ENDC);A(B.SECONDARY+'Please respect the laws of your country and the country of the website you are scraping.'+B.ENDC);A(I)
def Ba():
	H='help';J='clean';M='serve';N='search'
	if U(O.argv)==1:O.argv.append('ui')
	C=O.argv[1]
	if C=='guideUpdateFinished':BJ();return
	BQ();K();L();A(I)
	if C=='getinfo':E=O.argv[3];A(BV(E))
	elif C=='run':E=O.argv[2];Ao(E)
	elif C=='ui':T()
	elif C==N:BZ();return
	elif C==M:Ag()
	elif C==J:AM()
	elif C=='setup':E=O.argv[3];BW(E)
	elif C=='auto':AQ()
	elif C=='getseason':
		E=O.argv[3];G=O.argv[5];F=D
		if U(O.argv)>6:F=f(E)
		A(BX(E,G,F))
	elif C=='getepisode':
		E=O.argv[3];G=O.argv[5];P=O.argv[7];F=D
		if U(O.argv)>8:F=f(E)
		A(BY(E,G,P,F))
	elif C==H:A(B.PRIMARY+'Commands:'+B.ENDC);A('-----------------');A('run -url <url>');A(M);A(J);A(N);A('setup -url <url>');A('getinfo -url <url>');A('getseason -url <url> -season <season>');A('getepisode -url <url> -season <season> -episode <episode>');A(H)
	else:A(B.WARNING+'Invalid command'+B.ENDC)
	A(I)
if __name__=='__main__':Ba()