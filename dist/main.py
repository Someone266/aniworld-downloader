# Aniworld Scraper
# Author: JMcrafter26
# Description: A scraper for aniworld (german anime site)
# Version: see version variable below
# License: MIT License
# DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.
# Please respect the laws of your country and the country of the website you are scraping.

# This code was minified to save space. If you want to read the code, please read the original files.


Az='Enter the name of the anime you want to search for'
Ay='No internet connection'
Ax='There is a program update available'
Aw='Downloading assets...'
Av='You are up to date'
Au='success'
At='message'
As='Something went wrong with the update check'
Ar='q. Quit'
Aq='0. Settings'
Ap='7. Get anime info'
Ao='6. Setup anime folder'
An='5. Clean up'
Am='4. Serve content'
Al='3. Continue Download'
Ak='2. Manual Download'
Aj='1. Download Assistant'
Ai='Checking for updates...'
Ah='aniworld.to'
Ag='Episoden:'
Af='animeSeason'
Ae=enumerate
Ad=KeyError
AU='Error:'
AT='anime'
AS='/stream.json'
AR='stream.json'
AQ='url'
AP='imdb'
AO='producer'
AN='trailer'
AM='href'
AL='utf-8'
AB='updateHash'
AA='update'
A9='Press enter to exit'
A8='./assets'
A7='./anime'
A6='update.bat'
A5='Invalid url'
A4='./anime/index.json'
A3='fsk'
A2='https://aniworld.to'
A1='strong'
A0=False
u='settings.json'
t='[<>:"/\\\\|?*]'
s='picture'
r='a'
q='html.parser'
p=exit
n='Press enter to continue'
m='pathname'
l=' '
k=range
f='tags'
e='assets'
d='totalEpisodes'
c='description'
b='program'
a='w'
Z=len
W='episodes'
V='seasons'
U='status'
T=int
S='enddate'
R='startdate'
O='r'
M=''
J='title'
I='\n'
H=str
F=input
E=open
D=None
A=print
import sys as K,os as C,glob,re as g,requests as P,json as G,wget as v
from bs4 import BeautifulSoup as A_
from yt_dlp import YoutubeDL as B0
import shutil as h,base64 as AV
def BL():
	B=K.argv
	try:B[1]
	except IndexError:A('Please use a parameter. Use -h for Help');quit()
	if B[1]=='-h':help()
	elif B[1]=='-u':C=B[2];i(C)
	elif B[1]=='-l':D=B[2];B1(D)
	else:C=B[1];i(C)
def help():A('Version v1.1.0');A(M);A('______________');A('Arguments:');A('-h shows this help');A('-u <URL> downloads the <URL> you specify');A('-l <doc> opens the <doc> you specify and downloads every URL line after line');A('<URL> just the URL as Argument works the same as with -u Argument')
def B1(doc):
	C=0;D=E(doc).readlines()
	for B in D:C+=1;A('Download %s / '%C+H(Z(D)));B=B.replace(I,M);A('echo Link: %s'%B);i(B)
def i(URL,path=D,Season=D,Episode=D):
	X='/urls.txt';Y='var sources';T=URL;Q=True;N=Episode;K=Season;F=path;T=H(T)
	if F is not D and K is not D and N is not D:
		if C.path.exists(f"{F}/video/{K}/{N}.mp4"):A(f"File {F}/video/{K}/{N}.mp4 already exists. Skipping...");return
	c=P.get(T);Z=A_(c.content,q);a=Z.find(J).text;U=a.index('Watch ')+6;B=a[U:];V=B.index(' - VOE');B=B[:V];B=B.replace(l,'_');A(B)
	if C.path.exists(f"{B}"):
		A(f"File {B} already exists. Skipping...")
		if K is not D and N is not D:C.makedirs(f"{F}/video/{K}",exist_ok=Q);h.move(f"{B}",f"{F}/video/{K}/{N}.mp4");A(f"Moved to {F}/video/{K}/{N}.mp4")
		return
	if C.path.exists(f"{B}_SS.mp4"):
		A(f"File {B}_SS.mp4 already exists. Skipping...")
		if K is not D and N is not D:C.makedirs(f"{F}/video/{K}",exist_ok=Q);h.move(f"{B}_SS.mp4",f"{F}/video/{K}/{N}.mp4");A(f"Moved to {F}/video/{K}/{N}.mp4")
		return
	R=Z.find_all(string=g.compile(Y));R=H(R);U=R.index(Y);L=R[U:];V=L.index(';');L=L[:V];L=L.replace('var sources = ',M);L=L.replace("'",'"');L=L.replace('\\n',M);L=L.replace('\\',M);d=',';e=M;L=e.join(L.rsplit(d,1));b=G.loads(L)
	try:
		O=b['mp4'];O=AV.b64decode(O);A(B)
		if F is D:S=A0;F=C.getcwd()
		else:S=Q
		with E(F+X,r)as W:W.write(O+I)
		if S:v.download(O,out=f"{F}/{B}.mp4")
		else:v.download(O,out=f"{B}.mp4")
	except Ad:
		try:
			O=b['hls'];O=AV.b64decode(O);O=O.decode(AL);B=B+'_SS.mp4'
			if F is D:S=A0;F=C.getcwd()
			else:S=Q
			with E(F+X,r)as W:W.write(O+I)
			f={'outtmpl':B}
			with B0(f)as i:i.download(O)
			B2()
		except Ad:A('Could not find downloadable URL. Voe might have change their site. Check that you are running the latest version of voe-dl, and if so file an issue on GitHub.');quit()
	A('Downloaded: '+B)
	if K is not D and N is not D:C.makedirs(f"{F}/video/{K}",exist_ok=Q);h.move(f"{B}",f"{F}/video/{K}/{N}.mp4");A(f"Moved to {F}/video/{K}/{N}.mp4")
	A(I)
def B2(animePath=D):
	A=C.getcwd()
	for B in glob.iglob(C.path.join(A,'*.part')):C.remove(B)
import os as C,time as Q,sys as K,bs4 as w,http.server,zipfile
def BM(title='AniWorld Scraper'):
	B=title
	if C.name=='nt':C.system(f"title {B}")
	else:A(f"]0;{B}\a")
def X(url):
	a='span';L='div';N=url;g=P.get(N);h=g.text;C=w.BeautifulSoup(h,q);E=C.find(L,class_='series-title').text;E=E.strip();E=E.split(I)[0];A('Getting info for:',E);i=C.find('p',class_='seri_des').get('data-full-description');K=C.find(a,itemprop='startDate').text;O=C.find(a,itemprop='endDate').text
	if O=='heute':Q='ONGOING'
	else:Q='FINISHED'
	B=C.find(A1,text='Staffeln:').parent.parent.parent.find_all('li');B=[A.text for A in B];B=[A.replace(l,M)for A in B];B=[A for A in B if A];B=[A for A in B if A.isnumeric()];B=Z(B);F={}
	for b in k(1,T(B)+1):F[b]=B4(N,b)
	F=F;e=sum(F.values());X=C.find(L,class_='seriesCoverBox').find('noscript').find('img').get('src');X=A2+X;j=C.find(r,class_='trailerButton').get(AM);Y=C.find_all(r,itemprop='genre');Y=[A.text for A in Y];m=C.find(A1,class_='seriesProducer').text;n=C.find(L,class_=A3).get('data-fsk');G=C.find(r,class_='imdb-link')
	if G is not D:G=G.get(AM)
	else:G=M
	A(Q+' ('+K+' - '+O+') - '+H(e)+' episodes - '+H(B)+' seasons');o={J:E,c:i,Af:{'year':T(K[:4]),'season':K[5:]},U:Q,W:F,d:e,V:B,R:K,S:O,s:X,AN:j,f:Y,AO:m,A3:n,AP:G,AQ:N};return o
def o(info):
	B=info;A('Setting up anime folder...');F=f"{B[J]} ({B[R]}-{B[S]})";F=g.sub(t,M,F);F=f"anime/{F}"
	if not C.path.exists(F):C.makedirs(F)
	with E(f"{F}/info.json",a)as I:G.dump(B,I,indent=4)
	L=B[s].split('.')[-1]
	if not C.path.exists(f"{F}/image.{L}"):v.download(B[s],f"{F}/image.{L}")
	B[s]=f"image.{L}";B[m]=F
	with E(f"{F}/info.json",a)as I:G.dump(B,I,indent=4)
	if C.path.exists(A4):
		with E(A4,O)as I:K=G.load(I)
	else:K=[]
	N={J:B[J],f:B[f],R:B[R],S:B[S],U:B[U],c:B[c],d:B[d],V:B[V],m:F}
	for(P,Q)in Ae(K):
		if Q[J]==B[J]:K[P]=N;break
	else:K.append(N)
	with E(A4,a)as I:G.dump(K,I,indent=4)
	with E('./assets/template.html',O)as I:D=I.read()
	D=D.replace('%title%',B[J]);D=D.replace('%description%',B[c]);D=D.replace('%startDate%',B[R]);D=D.replace('%endDate%',B[S]);D=D.replace('%status%',B[U]);D=D.replace('%totalEpisodes%',H(B[d]));D=D.replace('%seasons%',H(B[V]));D=D.replace('%picture%',f"image.{L}");D=D.replace('%trailer%',B[AN]);D=D.replace('%producer%',B[AO]);D=D.replace('%fsk%',B[A3]);D=D.replace('%imdb%',B[AP]);D=D.replace('%tags%',', '.join(B[f]));D=D.encode(AL)
	with E(f"{F}/info.html",'wb')as I:I.write(D)
	A('Anime folder setup complete')
def AC(url,season,episodes=D,info=D):
	F=url;E=season;B=episodes
	if B is D:H=P.get(F);J=H.text;K=w.BeautifulSoup(J,q);B=K.find(A1,text=Ag).parent.parent.parent;B=B.find_all('li');B=Z(B)-1
	A(f"Getting streams for season {E} with {B} episodes...");G={}
	for C in k(1,B+1):
		if info is not D:G[C]=AE(F,E,C,info)
		else:G[C]=AE(F,E,C)
		AD(C/B)
	A(I);A('Done with season',E);return G
def AD(percent):A=percent;B=50;C=T(round(B*A));D='='*C+'-'*(B-C);K.stdout.write(f"\rProgress: [{D}] {A*100:.2f}%");K.stdout.flush()
def AE(url,season,episode,info=D):
	U=episode;N=url;K=info;L=season;N=N+f"/staffel-{L}/episode-{U}";V=P.get(N);W=V.text;X=w.BeautifulSoup(W,q);B=X.find('i',class_='icon VOE')
	if B is D:A('No voe download found, skipping...');return
	B=B.parent;B=B.get(AM);B=A2+B;Q=B3(B)
	if Q is D:A('No stream url found');return
	if K is not D:F=f"{K[J]} ({K[R]}-{K[S]})";F=g.sub(t,M,F);F=f"anime/{F}/stream.json"
	else:F=f"stream.json"
	if C.path.exists(F):
		with E(F,O)as T:I=G.load(T)
	else:I={}
	if H(L)not in I:I[H(L)]={}
	I[H(L)][H(U)]=Q
	with E(F,a)as T:G.dump(I,T,indent=4)
	return Q
def B3(url):
	B=P.head(url)
	if B.status_code!=302 and B.status_code!=301:A('No redirect found');return
	else:
		C=B.headers['Location']
		if Ah in C:A('Something went wrong with the redirect');return
		else:return C
def B4(url,season):B=url;B=B+f"/staffel-{season}";C=P.get(B);D=C.text;E=w.BeautifulSoup(D,q);A=E.find(A1,text=Ag).parent.parent.parent;A=A.find_all('li');A=Z(A)-1;return A
def B5(season,episode,info=D):
	F=episode;I=season;C=info;N();L()
	if C is D:
		with E(AR,O)as K:P=G.load(K)
	else:
		B=f"{C[J]} ({C[R]}-{C[S]})";B=g.sub(t,M,B);B=f"anime/{B}"
		with E(B+AS,O)as K:P=G.load(K)
	A(f"Downloading season {I} episode {F}...");Q=P[H(I)][H(F)];A(Q);i(Q,B,I,F)
def AF(season,info=D):
	F=info;C=season
	if F is D:
		with E(AR,O)as Q:K=G.load(Q)
	else:
		B=f"{F[J]} ({F[R]}-{F[S]})";B=g.sub(t,M,B);B=f"anime/{B}"
		with E(B+AS,O)as Q:K=G.load(Q)
	for P in K[H(C)]:U=K[H(C)][P];N();L();A(f"Downloading season {C} episode {P}...");AD(T(P)/Z(K[H(C)]));A(I);i(U,B,C,P)
def B6(season,start,end,info=D):
	K=start;P=season;C=info
	if C is D:
		with E(AR,O)as Q:T=G.load(Q)
	else:
		B=f"{C[J]} ({C[R]}-{C[S]})";B=g.sub(t,M,B);B=f"anime/{B}"
		with E(B+AS,O)as Q:T=G.load(Q)
	for F in k(K,end+1):U=T[H(P)][H(F)];N();L();A(f"Downloading season {P} episode {F}...");AD((F-K)/(end-K));A(I);i(U,B,P,F)
def AW(query):
	D=query
	if D==M:A(B.WARNING+'No query entered'+B.ENDC);return
	E='https://aniworld.to/ajax/search';F={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':A2,'referer':f"https://aniworld.to/search?q={D}",'sec-ch-ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with':'XMLHttpRequest'};C={'keyword':D};C=P.post(E,headers=F,data=C);C=C.text;C=G.loads(C);return AG(D,C)
def AG(query,data):
	P='Invalid number, try again';O=query;H='link';C=data;C=[A for A in C if'/anime/stream/'in A[H]];C=[A for A in C if'/support/'not in A[H]];C=[A for A in C if'/user/'not in A[H]];C=[A for A in C if'/search/'not in A[H]];C=[A for A in C if'/episode-'not in A[H]];C=[A for A in C if'/staffel-'not in A[H]]
	with E('search.txt',a)as U:G.dump(C,U,indent=4)
	N();L();A('Search results for:',O);A(I)
	for(V,K)in Ae(C):K[J]=K[J].replace('<em>',M).replace('</em>',M);A(V+1,B.OK+K[J]+B.ENDC);A(K[c]);A('---')
	A(B.PRIMARY+'Select a number to continue, or press q to quit'+B.ENDC);D=F()
	if D=='q':return
	elif not D.isnumeric():A(P);Q.sleep(2);AG(O,C);return
	elif T(D)<1 or T(D)>Z(C):A(P);Q.sleep(2);AG(O,C);return
	D=T(D);R=C[D-1][H];A('Selected:',C[D-1][J]);A(R);S=A2+R;A('url:',S);return S
def AX():
	B=3333;D=http.server.SimpleHTTPRequestHandler;E=C.path.join(C.path.dirname(__file__),AT);C.chdir(E)
	with http.server.HTTPServer((M,B),D)as F:A('serving at http://localhost:'+H(B)+'/');A('Press Ctrl+C to stop the server');F.serve_forever()
def AH():
	Q='index.html';T='anime/';N();L();A('Running cleanup...');Y=[A for A in C.listdir('.')if A.endswith('.part')or A.endswith('.ytdl')]
	if Y:
		A(B.WARNING+'Do you want to delete non finished downloads? After deleting you have to restart the download'+B.ENDC);A('Do you want to continue? (y/N)');K=F()
		if K.lower()=='y':
			A('Deleting files...')
			for I in Y:C.remove(I);A('Deleted:',I)
	A('Rebuilding index.json...');b=[A for A in C.listdir(AT)if C.path.isdir(C.path.join(AT,A))];Z=[]
	for H in b:
		if not C.listdir(f"anime/{H}"):C.rmdir(f"anime/{H}");continue
		if not C.path.exists(f"anime/{H}/info.json"):continue
		with E(f"anime/{H}/info.json",O)as P:D=G.load(P)
		if AQ not in D:
			A('No url found for:','/'+H+'/ ('+D[J]+')'+', should we remove it? (Y/n)');K=F()
			if K.lower()=='n':continue
			A('Removing:',D[J]);h.rmtree(f"anime/{H}");continue
		if T in D[m]:D[m]=D[m].replace(T,M)
		e=[J,c,Af,U,W,d,V,R,S,s,AN,f,AO,A3,AP]
		if not all(A in D for A in e):A('Rebuilding info.json for:',D[J]);D=X(D[AQ]);o(D)
		Z.append({J:D[J],f:D[f],R:D[R],S:D[S],U:D[U],c:D[c],d:D[d],V:D[V],m:f"{H}"})
	with E(A4,a)as P:G.dump(Z,P,indent=4)
	A('Cleaning file structure...')
	if C.path.exists(Q):C.remove(Q)
	g=['assets/bootstrap.min.css','assets/css','assets/js','assets/plyr.css','assets/plyr.js','assets/animeList.json','assets/placeholder.jpg','assets/fuse.min.js','functions.py','dl_a.py'];A('Removing unused files...')
	for I in g:
		if C.path.exists(I):C.remove(I);A('Removed:',I)
	A('Done')
def AI(url):
	C='episode';D='staffel';B=url
	if Ah not in B:A(A5);return A0
	if D in B:B=B.split(D)[0]
	if C in B:B=B.split(C)[0]
	return B
def B7():
	if not C.path.exists(u):B9();return
	if C.path.exists(A6):C.remove(A6)
	else:
		if not C.path.exists(A7):C.makedirs(A7)
		if not C.path.exists(A8):C.makedirs(A8)
def AY(key,value):
	if C.path.exists(u):
		with E(u,O)as A:B=G.load(A)
	else:B={}
	B[key]=value
	with E(u,a)as A:G.dump(B,A,indent=4)
def B8():
	if C.path.exists(A6):C.remove(A6)
	N();L();A(B.PRIMARY+'Update finished'+B.ENDC);A('The program has been updated, YIPPIE!');A(n);F();AJ()
def x():return A0
def j():
	B='./assets/animeList.json';return;A(Ai);H='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database-minified.json';I='https://api.github.com/repos/manami-project/anime-offline-database/commits?path=anime-offline-database-minified.json&page=1&per_page=1';J=P.get(I);D=J.json();K=D[0]['commit']['committer']['date'][:10]
	if C.path.exists(B):
		with E(B,O)as F:D=G.load(F)
		L=D['lastUpdate']
		if L==K:A('Anime list is up to date');return
	A('Downloading anime list...');v.download(H,B);D=G.load(E(B,O,encoding=AL))
	with E(B,a)as F:G.dump(D,F,indent=4)
	A('Anime list downloaded')
def N():A('\x1b[H\x1b[J')
def Y():
	G='Invalid key';E='Enter the url of the anime';N();L();A('Press one of the following keys:');A(Aj);A(Ak);A(Al);A(Am);A(An);A(Ao);A(Ap);A(Aq);A(Ar);D=F()
	if D not in['1','2','3','4','5','6','7','8','9','0','q','Q']:A(G);Y();return
	if D=='1':Ac()
	elif D=='2':
		A('This mode will download everything from the given url');A(E);C=F();C=AI(C)
		if not C:A(B.WARNING+A5+B.ENDC);Q.sleep(2);Y();return
		Ab(C)
	elif D=='3':A('Not implemented yet');Q.sleep(2);Y()
	elif D=='4':AX()
	elif D=='5':AH()
	elif D=='6':
		A(E);C=F();C=AI(C)
		if not C:A(B.WARNING+A5+B.ENDC);Q.sleep(2);Y();return
		H=X(C);o(H)
	elif D=='7':
		A(E);C=F();C=AI(C)
		if not C:A(B.WARNING+A5+B.ENDC);Q.sleep(2);Y();return
		A(X(C))
	elif D=='q'or D=='Q':A('Quitting...');p()
	else:A(B.WARNING+G+B.ENDC);Q.sleep(2);Y();return
def B9():
	N();L();A(B.PRIMARY+'Hi and welcome to AniWorld-Down v'+AK()+B.ENDC);A('It looks like this is your first time running this program, or you have deleted some files :)');A('This guide will help you get started with the program\n');A(B.WARNING+'This directory will be used to store the anime and the assets'+B.ENDC);A(B.SECONDARY+n+B.ENDC);F()
	if not C.path.exists(A7):C.makedirs(A7)
	if not C.path.exists(A8):C.makedirs(A8)
	BA()
def BA():
	E='updateNotes';G='Update notes:';N();L();A(B.PRIMARY+'Step 1: Checking for updates and downloading assets'+B.ENDC);A('We promise, it will be quick');C=Aa()
	if C is D:A('Hmm, something went wrong with the update check');A('Do you have an internet connection? \n');A(B.SECONDARY+'PS: We need an internet connection to download the assets'+B.ENDC);A(B.SECONDARY+A9+B.ENDC);F();p()
	if C[U]=='error':A(B.WARNING+As+B.ENDC);A(AU,C[At]);A('Please try again later\n');A(B.SECONDARY+A9+B.ENDC);F();p()
	elif C[U]==Au:A(Av);A(B.SECONDARY+n+B.ENDC);F();AJ();return
	else:
		if C[AA][e]:A(B.OK+Aw+B.ENDC);A(G);A(C[E][e]+I);y(e,C[AB][e])
		if C[AA][b]:A(B.OK+Ax+B.ENDC);A(G);A(C[E][b]+I);y(b,C[AB][b])
		else:A('No program update available')
		A(B.SECONDARY+n+B.ENDC);F();AJ();return
def AJ():N();L();A(B.PRIMARY+'Step 2: Configuring the program'+B.ENDC);A('We need to configure the program before we can continue');A('It is very simple, just answer a few questions');A(B.SECONDARY+n+B.ENDC);F();AZ()
def AZ():
	C='mode';N();L();A(B.PRIMARY+'Choose the option that describes you the best'+B.ENDC);A('1. I want to archive anime and have it nicely organized (with filestructure, prictures and an offline webserver)');A('2. I just want to download anime fast and continue watching (No filestructure, ready to watch or move)');A(I);A(B.SECONDARY+'Choose an option by pressing the number'+B.ENDC);D=F()
	if D=='1':AY(C,'archive')
	elif D=='2':AY(C,'download')
	else:A('Invalid option, try again');AZ();return
	BB()
def BB():
	N();L();A(B.PRIMARY+'Thats it, you are ready to go'+B.ENDC);A('You can now start downloading anime');A(I);A('Press i to read the instructions');A('Press enter to just freakin start the program');C=F()
	if C=='i':BC()
	Y()
def BC():N();L();A(B.PRIMARY+'Instructions'+B.ENDC);A(Aj);A('This option will guide you through the download process, you just need to enter the url of the anime');A(Ak);A('This option will download everything from the given url');A(Al);A('This option will continue the download from the last download');A(Am);A('This option will start a http server with document root to the anime folder');A(An);A("This option will delete non finished downloads, after deleting you can't resume the download");A(Ao);A('This option will setup the anime folder with the given url');A(Ap);A('This option will get the anime info from the given url');A(Aq);A('This option will show the settings');A(Ar);A(I);A(n);F();Y()
def BD():
	B7();N();L();A('Loading...');B=Aa()
	if B is D:A('No internet connection, skipping update check');return
	if B[U]=='error':A(As);A(AU,B[At]);Q.sleep(2);return
	elif B[U]==Au:A(Av);return
	else:
		if B[AA][e]:A(Aw);y(e,B[AB][e])
		if B[AA][b]:A(Ax);y(b,B[AB][b])
def Aa():
	D='./assets/.version';A(Ai,end=M)
	try:P.get('https://api.jm26.net/status.txt')
	except P.exceptions.ConnectionError:A(' Skipped');A(B.WARNING+Ay+B.ENDC);Q.sleep(2);return
	H='https://api.jm26.net/update/aniworld-down/check/';I=AK()
	if not C.path.exists(D):
		with E(D,a)as F:F.write('0.0.0')
	with E(D,O)as F:J=F.read()
	G={b:I,e:J};K=P.post(H,data=G);G=K.json();A(' Done');return G
def y(type,hash):
	N='Please try again later';G='./update';A('Downloading ..');I=f"https://api.jm26.net/update/aniworld-down/download/?type={type}&hash={hash}";J='./update/update.zip'
	if x():I=I+'&os=windows'
	if not C.path.exists(G):C.makedirs(G)
	try:L=P.get(I)
	except P.exceptions.ConnectionError:A(B.WARNING+Ay+B.ENDC);A(N);A(A9);F();p()
	if L.headers['Content-Type']=='application/json':A(B.WARNING+'Something went wrong with the download'+B.ENDC);A(AU,L.text);A(N);A(A9);F();p()
	A(B.OK+'Download complete'+B.ENDC)
	with E(J,'wb')as H:H.write(L.content)
	with zipfile.ZipFile(J,O)as R:R.extractall(G)
	C.remove(J)
	for D in C.listdir(G):
		if C.path.isdir(f"./update/{D}"):
			if not C.path.exists(f"./{D}"):C.makedirs(f"./{D}")
			for H in C.listdir(f"./update/{D}"):h.move(C.path.join(f"./update/{D}",H),C.path.join(f"./{D}",H))
			C.rmdir(f"./update/{D}")
		else:h.move(C.path.join(G,D),C.path.join('./',D))
	C.rmdir(G);A(B.OK+'Update complete'+B.ENDC)
	if type==b:
		for S in k(3):A(f"\rRestarting in {3-S} seconds",end=M);Q.sleep(1)
		A('\rRestarting program...')
		if not C.path.exists(u):
			if x():C.system(f"start update.bat guideUpdateFinished")
			elif C.name=='nt':C.system('py main.py guideUpdateFinished')
			else:C.system(f"python3 main.py guideUpdateFinished")
		elif x():C.system(f"start update.bat "+l.join(K.argv[1:]))
		elif C.name=='nt':C.system('py main.py '+l.join(K.argv[1:]))
		else:C.system('python3 main.py '+l.join(K.argv[1:]))
BE='1.1.4'
class B:PURPLE='\x1b[95m';SECONDARY='\x1b[90m';PRIMARY='\x1b[94m';CYAN='\x1b[96m';OK='\x1b[92m';WARNING='\x1b[93m';FAIL='\x1b[91m';ENDC='\x1b[0m';BOLD='\x1b[1m';UNDERLINE='\x1b[4m'
def Ab(url):
	j();C=X(url);o(C)
	for D in C[W]:AC(url,D,C[W][D],C)
	E=C[V];A(E)
	for D in k(1,E+1):AF(D,C)
	AH();L();A(B.OK+'Finished downloading all episodes'+B.ENDC);A(I);A(B.PRIMARY+"Run 'serve' to watch the episodes in your browser"+B.ENDC)
def Ac():
	N();L();j();A(B.OK+'This is the auto mode. It will ask you what to download.'+B.ENDC);A(I);A('Do you want to search for an anime or enter the url directly? (S/u)');E=F()
	if E=='S'or E=='s':N();L();A(Az);H=F();C=AW(H)
	else:C=F('Enter the url of the anime: ')
	A(C);D=X(C);o(D)
	for G in D[W]:AC(C,G,D[W][G],D)
	z(C,D)
def z(url,info):
	J=url;C=info;L();A(B.OK+'Setup complete'+B.ENDC);A(I);A(B.OK+'We found '+H(C[V])+' seasons and a total of '+H(C[d])+' episodes'+B.ENDC);A(I);A('Do you want to download all episodes? (Y/n)');G=F()
	if G=='Y'or G=='y'or G=='yes'or G=='Yes':
		A(B.OK+'Downloading all episodes'+B.ENDC)
		for D in k(1,C[V]+1):AF(D,C)
	else:
		A('Which season do you want to download?');D=T(F());A('What episode do you want to download? (Enter 0 to download all episodes; use - to download a range of episodes)');E=T(F())
		if D<1 or D>C[V]:A(B.FAIL+'Invalid season'+B.ENDC);Q.sleep(2);z(J,C);return
		if E==0:AF(D,C)
		elif'-'in H(E):
			K=T(E.split('-')[0]);M=T(E.split('-')[1])
			if K<1 or M>C[W][D]:A(B.FAIL+'Invalid range'+B.ENDC);Q.sleep(2);z(J,C);return
			B6(D,K,M,C)
		else:
			if E<1 or E>C[W][D]:A(B.FAIL+'Invalid episode'+B.ENDC);Q.sleep(2);z(J,C);return
			B5(D,E,C)
	A(B.OK+'Script finished! Press any key to exit'+B.ENDC);F()
def AK():return BE
def BF(url):j();A=X(url);return A
def BG(url):j();A=X(url);o(A)
def BH(url,season,info=D):
	A=season;j();B=D
	if info is not D:B=info[W][A]
	C=AC(url,A,B);return C
def BI(url,season,episode,info=D):
	C=season;A=info;B=episode;j()
	if A is not D:B=A[W][C][B]
	E=AE(url,C,B,A);return E
def BJ():N();L();A(Az);B=F();return AW(B)
def L():
	A(I);C=AK()
	if x():C=C+' (Windows)'
	A(B.CYAN+'    AA          W     W         ll     d     DDD                    '+B.ENDC);A(B.CYAN+'   A  A      ii W     W          l     d     D  D                   '+B.ENDC);A(B.CYAN+'   AAAA nnn     W  W  W ooo rrr  l   ddd     D  D ooo w   w nnn     '+B.ENDC);A(B.CYAN+'   A  A n  n ii  W W W  o o r    l  d  d     D  D o o w w w n  n    '+B.ENDC);A(B.CYAN+'   A  A n  n ii   W W   ooo r   lll  ddd     DDD  ooo  w w  n  n    '+B.ENDC);A(B.CYAN+'                                                                    '+B.ENDC);A('A powerful scraper and downloader for AniWorld');A(l);A('Version: '+C+'                                 Made by JMcrafter26');A(B.SECONDARY+'DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.'+B.ENDC);A(B.SECONDARY+'Please respect the laws of your country and the country of the website you are scraping.'+B.ENDC);A(I)
def BK():
	H='help';J='clean';M='serve';O='search'
	if Z(K.argv)==1:K.argv.append('ui')
	C=K.argv[1]
	if C=='guideUpdateFinished':B8();return
	BD();N();L();A(I)
	if C=='getinfo':E=K.argv[3];A(BF(E))
	elif C=='run':E=K.argv[2];Ab(E)
	elif C=='ui':Y()
	elif C==O:BJ();return
	elif C==M:AX()
	elif C==J:AH()
	elif C=='setup':E=K.argv[3];BG(E)
	elif C=='auto':Ac()
	elif C=='getseason':
		E=K.argv[3];G=K.argv[5];F=D
		if Z(K.argv)>6:F=X(E)
		A(BH(E,G,F))
	elif C=='getepisode':
		E=K.argv[3];G=K.argv[5];P=K.argv[7];F=D
		if Z(K.argv)>8:F=X(E)
		A(BI(E,G,P,F))
	elif C==H:A(B.PRIMARY+'Commands:'+B.ENDC);A('-----------------');A('run -url <url>');A(M);A(J);A(O);A('setup -url <url>');A('getinfo -url <url>');A('getseason -url <url> -season <season>');A('getepisode -url <url> -season <season> -episode <episode>');A(H)
	else:A(B.WARNING+'Invalid command'+B.ENDC)
	A(I)
if __name__=='__main__':BK()