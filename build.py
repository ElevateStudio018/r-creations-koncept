import re
H={'logo':'f8e2fb_2bfb1152f5934579974cc6b8b0857178~mv2.jpeg','rakesh_cam':'f8e2fb_0dbd831774bf4e0c8e5d7c2320b722c7~mv2.jpg','rings':'f8e2fb_1f6669bbe9c64085b5b18fc5caa5e59b~mv2.jpg',
'sthlm1':'f8e2fb_391a87b0e6db47ad9af845f6870ac6c1~mv2.jpg','mandap':'f8e2fb_40aa49058b954da69d7b56a30a78333b~mv2.jpeg',
'highland':'f8e2fb_4f65eb1f6b1544ff9db5b09090f36d62~mv2.jpg','sthlm2':'f8e2fb_80a48619fade422290f0b617b0478c30~mv2.jpg',
'confetti':'f8e2fb_8273bd17731c461189a47ac2934cc526~mv2.jpg','lights1':'f8e2fb_84128d18f31047908ed9ede20b9280d7~mv2.jpg',
'dubai1':'f8e2fb_bef28181dba8406da1e6bcfe6107583a~mv2.jpg','ayushi':'f8e2fb_c2dbded9f70c451fb1ccffb46e70add3~mv2.jpeg',
'lights2':'f8e2fb_e0ce8393ccfa432885214fd2fb7aaaac~mv2.jpg','rakesh':'f8e2fb_e0d1b7729f9f478e8cb06a936cf5b1f5~mv2.jpg',
'dubai2':'f8e2fb_f4c9590817884916849a5b9937a18e26~mv2.jpg','table':'f8e2fb_f773971b3a964ab3a65c7970640d8404~mv2.jpg'}
def I(k,w=1400): m=H[k];return f"https://static.wixstatic.com/media/{m}/v1/fit/w_{w},h_{w},q_85,enc_auto/{m}"
def V(i): return f"https://videos.pexels.com/video-files/{i}/{i}-hd_1920_1080_25fps.mp4"
ARR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
IG='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'
MAIL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M3 7l9 6 9-6"/></svg>'
PH='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2"/></svg>'
NAV=[('index.html','Hem'),('portfolio.html','Portfolio'),('tjanster.html','Tjänster'),('om.html','Om oss')]
def page(fn,title,desc,body):
  links=''.join(f'<li><a href="{h}"{" class=active" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
  return f'''<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#0b0b0b">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Cormorant+Garamond:ital,wght@1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css"></head><body>
<header class="nav"><div class="wrap"><a href="index.html" class="logo" aria-label="R Creations Films"><img class="logo-img" src="https://static.wixstatic.com/media/f8e2fb_2bfb1152f5934579974cc6b8b0857178~mv2.jpeg/v1/crop/x_112,y_0,w_425,h_425/fill/w_120,h_120,q_90/logo.jpg" alt="R-Creations logga"><span class="logo-txt">R·CREATIONS<small>FILMS · STOCKHOLM</small></span></a>
<nav><ul class="menu">{links}<li><a href="kontakt.html" class="btn btn-gold">Boka konsultation</a></li></ul></nav><button class="burger" aria-label="Meny"><span></span><span></span></button></div></header>
{body}
<footer class="footer"><div class="wrap"><div class="f-top">
<div><a href="index.html" class="logo"><img class="logo-img" src="https://static.wixstatic.com/media/f8e2fb_2bfb1152f5934579974cc6b8b0857178~mv2.jpeg/v1/crop/x_112,y_0,w_425,h_425/fill/w_120,h_120,q_90/logo.jpg" alt="R-Creations logga"><span class="logo-txt">R·CREATIONS<small>MAKING MOMENTS MEMORABLE</small></span></a>
<p class="f-big">Låt oss berätta<br>er historia.</p><a href="kontakt.html" class="btn btn-gold">Kontrollera ert datum {ARR}</a>
<div class="socials"><a href="https://www.instagram.com/rcreations_films" target="_blank" rel="noopener" aria-label="Instagram">{IG}</a><a href="mailto:rcreationsfilms@gmail.com" aria-label="E-post">{MAIL}</a><a href="tel:+46736172520" aria-label="Telefon">{PH}</a></div></div>
<div><h4>Utforska</h4><ul><li><a href="portfolio.html">Portfolio</a></li><li><a href="tjanster.html">Tjänster &amp; paket</a></li><li><a href="om.html">Om oss</a></li><li><a href="kontakt.html">Kontakt</a></li></ul></div>
<div><h4>Berättelser</h4><ul><li><a href="ayushi-tejbir.html">Ayushi &amp; Tejbir</a></li><li><a href="dubai.html">Dubai Skyline</a></li><li><a href="stockholm.html">Gamla stan</a></li><li><a href="highlands.html">Highlands</a></li></ul></div>
<div><h4>Kontakt</h4><ul><li>Rakesh Nagaraja</li><li>Stockholm, Sverige</li><li><a href="tel:+46736172520">+46 73 617 25 20</a></li><li><a href="mailto:rcreationsfilms@gmail.com">rcreationsfilms@gmail.com</a></li></ul></div>
</div><div class="f-bot"><span>© 2026 R Creations Films. Alla rättigheter förbehållna.</span><span>Foto · Film · Dekor · Eventplanering</span></div></div></footer>
<script src="main.js"></script></body></html>'''

def hero(vid,poster,eyebrow,h1,lead,b1,b2,cls=''):
  return f'''<section class="hero {cls}"><video autoplay muted loop playsinline preload="auto" poster="{poster}"><source src="{V(vid)}" type="video/mp4"></video>
<button class="hero-sound" aria-label="Ljud">♪</button>
<div class="wrap"><span class="eyebrow rv">{eyebrow}</span><h1 class="h-xl rv d1">{h1}</h1><p class="lead rv d2">{lead}</p>
<div class="hero-ctas rv d3"><a href="{b1[0]}" class="btn btn-gold">{b1[1]} {ARR}</a><a href="{b2[0]}" class="btn btn-ghost">{b2[1]}</a></div></div>
<div class="hero-meta"><span>Scrolla</span><div class="scroll-cue"></div></div></section>'''

def yt_hero(poster,eyebrow,h1,lead,b1,b2):
  return f'''<section class="hero"><img class="hero-img" src="{poster}" alt=""><div class="yt-bg" id="ytbg" data-clips='[["6uLsjLo05H8",4,10],["_J_B7MFWRCE",20,9],["4kQI4XJ8hCg",8,9],["_J_B7MFWRCE",95,9],["9AXDnD7KPv4",6,9],["6uLsjLo05H8",22,9],["_J_B7MFWRCE",150,9]]'><div id="ytA"></div><div id="ytB"></div></div>
<div class="wrap"><span class="eyebrow rv">{eyebrow}</span><h1 class="h-xl rv d1">{h1}</h1><p class="lead rv d2">{lead}</p>
<div class="hero-ctas rv d3"><a href="{b1[0]}" class="btn btn-gold">{b1[1]} {ARR}</a><a href="{b2[0]}" class="btn btn-ghost">{b2[1]}</a></div></div>
<div class="hero-meta"><span>Filmat av R-Creations</span><div class="scroll-cue"></div></div></section>'''

def marquee(words):
  s=''.join(f'<span>{w}</span>' for w in words)*2
  return f'<div class="marquee"><div class="marquee-track">{s}</div></div>'

def fig(k,cat,cap,loc):
  return f'<figure data-cat="{cat}"><img src="{I(k,900)}" data-full="{I(k,2000)}" alt="{cap}" loading="lazy"><figcaption><span>{cap}</span><span>{loc}</span></figcaption></figure>'

GALLERY=[('ayushi','indiskt brollop','Ayushi &amp; Tejbir','Sverige'),('dubai2','destination brollop','Skyline-porträtt','Dubai'),
('sthlm1','brollop','Utsikten','Stockholm'),('lights1','dekor event','Ljustunneln','Middag'),('confetti','brollop','Kronbladsregn','Ceremoni'),
('mandap','indiskt brollop dekor','Mandap','Sverige'),('highland','destination brollop','Highlands','Skottland'),('rings','brollop detaljer','Löftet','Detaljer'),
('sthlm2','brollop','Riddarholmen','Stockholm'),('table','dekor event','Långbordet','Trädgård'),('dubai1','destination brollop','Golden hour','Dubai'),('lights2','dekor event','Paviljongen','Kväll')]
def gallery(filters=True):
  f=''
  if filters:
    f='<div class="filters rv">'+''.join(f'<button class="chip{" on" if a=="all" else ""}" data-f="{a}">{b}</button>' for a,b in [('all','Alla'),('brollop','Bröllop'),('indiskt','Indiska bröllop'),('destination','Destination'),('dekor','Dekor &amp; event'),('detaljer','Detaljer')])+'</div>'
  return f, '<div class="masonry">'+''.join(fig(*g) for g in GALLERY)+'</div>'

STORIES={
'ayushi-tejbir':dict(title='Ayushi &amp; Tejbir',tag='Indiskt bröllop · Sverige',img='ayushi',vid=4446328,
 h='Sveriges största <span class="serif gold">indiska bröllop</span>',
 lead='En tidlös förening av tradition, elegans och oförglömliga ögonblick. Tre dagar, hundratals gäster och en mandap byggd från grunden.',
 facts=[('Plats','Sverige'),('Omfattning','Flerdagsfirande'),('Leverans','Foto, film &amp; dekor'),('Team','Foto · Film · Dekor')],
 chapters=[('Mehndi &amp; Haldi','Färg, skratt och familj. Vi dokumenterade de intima förberedelserna i naturligt ljus — henna som torkar, gurkmeja som sprids, mormödrar som sjunger.','rings'),
  ('Baraat &amp; Mandap','Brudgummens ankomst med musik och dans följdes av ceremonin under en blomsterklädd mandap som vårt dekorteam designat och byggt på plats.','mandap'),
  ('Kvällen','Ljusgirlanger, långbord och en dansgolvsenergi som höll till långt efter midnatt. Vi filmade både helheten och de små blickarna.','lights1')],
 gal=['ayushi','mandap','rings','lights1','table','lights2'],
 quote='Det kändes som att de var en del av familjen — och det syns i varje bild.'),
'dubai':dict(title='Dubai Skyline',tag='Destination · Dubai',img='dubai2',vid=8776123,
 h='Kärlek mot en <span class="serif gold">horisont av glas</span>',
 lead='En porträttsession vid vattnet med Dubais skyline i ryggen. Hav, stål och mjukt eftermiddagsljus — en kontrast som gör paret till hjältarna i bilden.',
 facts=[('Plats','Dubai, UAE'),('Typ','Porträtt &amp; pre-wedding'),('Ljus','Golden hour'),('Leverans','Foto + highlight-film')],
 chapters=[('Planeringen','Vi scoutade platsen dagen innan och tajmade sessionen efter solens vinkel för att få jämnt ljus på ansiktena och detaljrik skyline.','dubai1'),
  ('Sessionen','Inga stela poser. Vi guidar med små rörelser och låter resten hända — skratt, en viskning, ett tak av blå himmel.','dubai2')],
 gal=['dubai2','dubai1','sthlm1','highland'],quote='Vi reser gärna dit er kärlek tar er.'),
'stockholm':dict(title='Gamla stan',tag='Bröllop · Stockholm',img='sthlm1',vid=8776108,
 h='Stockholm i sitt <span class="serif gold">vackraste ljus</span>',
 lead='Med Riddarholmskyrkan och Gamla stans tak som kuliss fångade vi ett par på deras bröllopsdag — en klassisk stockholmsberättelse.',
 facts=[('Plats','Stockholm'),('Typ','Bröllopsdag'),('Säsong','Sommar'),('Leverans','Foto + film')],
 chapters=[('Porträtten','Vi använde stadens utsiktspunkter och vattnet för porträtt som känns både storslagna och personliga.','sthlm2'),
  ('Ceremonin','Kronbladsregn, vänner som jublar och en brudgum som inte kan sluta le — ögonblick man bara får en gång.','confetti')],
 gal=['sthlm1','sthlm2','confetti','rings'],quote='Vår hemstad är vår favoritkuliss.'),
'highlands':dict(title='Highlands',tag='Destination · Skottland',img='highland',vid=8776113,
 h='Där bergen <span class="serif gold">håller andan</span>',
 lead='Ett elopement i dramatiskt landskap. Vind, moln och ett par som bara hade ögon för varandra.',
 facts=[('Plats','Skottland'),('Typ','Elopement'),('Väder','Allt på en dag'),('Leverans','Foto')],
 chapters=[('Landskapet','Vi lät naturen vara medspelare och komponerade bilderna så att paret känns små i det stora — men centrala i berättelsen.','highland')],
 gal=['highland','dubai1','sthlm2','rings'],quote='Ingen plats är för långt bort för rätt berättelse.'),
}

def story_page(slug):
  s=STORIES[slug]
  facts=''.join(f'<div class="stat"><span>{a}</span><b style="font-size:1.25rem;margin-top:6px">{b}</b></div>' for a,b in s['facts'])
  ch=''
  for n,(t,p,k) in enumerate(s['chapters']):
    rev='style="direction:rtl"' if n%2 else ''
    ch+=f'<div class="split rv" {rev} style="margin-bottom:110px;{"direction:rtl" if n%2 else ""}"><div class="split-media" style="direction:ltr"><img src="{I(k,1400)}" alt="{t}" loading="lazy"></div><div style="direction:ltr"><span class="eyebrow">Kapitel 0{n+1}</span><h2 class="h-lg mt">{t}</h2><p class="lead mt">{p}</p></div></div>'
  gal=''.join(fig(k,'x',s['title'],'') for k in s['gal'])
  keys=list(STORIES);nxt=keys[(keys.index(slug)+1)%len(keys)];ns=STORIES[nxt]
  body=hero(s['vid'],I(s['img'],1800),s['tag'],s['h'],s['lead'],('#berattelse','Läs berättelsen'),('kontakt.html','Boka ert datum'),'page-hero')+f'''
<section id="berattelse"><div class="wrap"><div class="stats rv" style="grid-template-columns:repeat(4,1fr);margin:0 0 110px;border:none;padding:0">{facts}</div>{ch}</div></section>
<section class="dark"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Galleri</span><h2 class="h-lg">Ur <span class="serif gold">arkivet</span></h2></div><p class="lead">Klicka på en bild för att se den i helskärm.</p></div><div class="masonry">{gal}</div></div></section>
<section><div class="wrap quote rv"><span class="eyebrow">Från teamet</span><blockquote>“{s["quote"]}”</blockquote><cite>R Creations Films</cite></div></section>
<a href="{nxt}.html" class="feature wrap rv" style="margin-bottom:120px;min-height:460px"><img src="{I(ns["img"],1800)}" alt="" loading="lazy"><div class="feature-body"><span class="eyebrow">Nästa berättelse</span><h2 class="h-lg">{ns["title"]}</h2><span class="btn btn-ghost">Se berättelsen {ARR}</span></div></a>'''
  open(f'{slug}.html','w').write(page(f'{slug}.html',f'{s["title"]} — R Creations Films',s['lead'],body))
for k in STORIES: story_page(k)

CTA=f'''<section class="cta"><video autoplay muted loop playsinline poster="{I('rings',1600)}"><source src="{V(8776123)}" type="video/mp4"></video>
<div class="wrap rv"><span class="eyebrow">Begränsat antal datum per år</span><h2 class="h-lg">Er dag förtjänar att <span class="serif gold">minnas rätt.</span></h2>
<div class="hero-ctas"><a href="kontakt.html" class="btn btn-gold">Kontrollera ert datum {ARR}</a><a href="tel:+46736172520" class="btn btn-ghost">Ring Rakesh</a></div></div></section>'''
INSTA='<section style="padding:90px 0 0;background:var(--paper)"><div class="wrap s-head"><div><span class="eyebrow">Instagram</span><h2 class="h-md">@rcreations_films</h2></div><a class="btn btn-line" href="https://www.instagram.com/rcreations_films" target="_blank" rel="noopener">Följ oss '+ARR+'</a></div><div class="insta">'+''.join(f'<a href="https://www.instagram.com/rcreations_films" target="_blank" rel="noopener"><img src="{I(k,500)}" alt="" loading="lazy"></a>' for k in ['ayushi','confetti','dubai2','lights1','sthlm2','mandap'])+'</div></section>'

def projects(n=4):
  items=[('ayushi-tejbir','mandap','Indiskt bröllop','Ayushi &amp; Tejbir','Sverige','wide'),('dubai','dubai2','Destination','Dubai Skyline','UAE',''),
   ('stockholm','sthlm1','Bröllop','Gamla stan','Stockholm',''),('highlands','highland','Elopement','Highlands','Skottland','')]
  return '<div class="projects">'+''.join(f'<a href="{s}.html" class="proj {c} rv"><div class="proj-media"><img src="{I(k,1800)}" alt="{t}" loading="lazy"><span class="proj-tag">{tg}</span></div><div class="proj-info"><div><h3>{t}</h3><span>{l}</span></div><span class="arrow">{ARR}</span></div></a>' for s,k,tg,t,l,c in items[:n])+'</div>'

# INDEX
idx=yt_hero(I('sthlm2',1800),'Bröllopsfoto &amp; film · Stockholm','Kärlek, fångad <span class="serif gold">precis</span> som den kändes.',
 'Vi fotograferar, filmar och formger bröllop i Sverige och världen över — så att ni kan återuppleva dagen, ögonblick för ögonblick.',
 ('kontakt.html','Boka konsultation'),('portfolio.html','Se vårt arbete'))
idx+=marquee(['Making moments memorable','Bröllop','Indiska bröllop','Destination','Film','Dekor','Event'])
idx+=f'''<section><div class="wrap split"><div class="split-media rv"><img src="{I('rakesh',1200)}" alt="Rakesh Nagaraja, grundare"><img class="float" src="{I('rings',800)}" alt="" loading="lazy"><div class="badge"><div><b>3</b>tjänster<br>ett team</div></div></div>
<div class="rv d1"><span class="eyebrow">Om R Creations</span><h2 class="h-lg mt">Ett team. Hela <span class="serif">berättelsen.</span></h2>
<p class="lead mt">Vi är ett erfaret eventteam med passion för oförglömliga upplevelser. Med expertis inom dekor, fotografi och film tar vi hand om allt — från första skissen av ert tema till den sista bilden i ert album.</p>
<p class="lead mt">Varje detalj ska vara genomtänkt, vackert genomförd och dokumenterad så att den kan återupplevas om och om igen.</p>
<div class="stats"><div class="stat"><b>Foto</b><span>Dokumentärt &amp; redaktionellt</span></div><div class="stat"><b>Film</b><span>Highlights &amp; långfilm</span></div><div class="stat"><b>Dekor</b><span>Koncept till uppbyggnad</span></div></div>
<a href="om.html" class="btn btn-dark" style="margin-top:40px">Lär känna oss {ARR}</a></div></div></section>
<section class="dark"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Vad vi gör</span><h2 class="h-lg">Allt ni behöver, <span class="serif gold">under ett tak</span></h2></div><a href="tjanster.html" class="btn btn-ghost">Alla tjänster {ARR}</a></div>
<div class="services">{''.join(f'<a href="tjanster.html" class="svc rv d{n}"><img src="{I(k,1000)}" alt="" loading="lazy"><div class="svc-body"><span class="svc-num">0{n+1}</span><h3>{t}</h3><p>{p}</p></div></a>' for n,(k,t,p) in enumerate([('confetti','Bröllopsfoto','Tidlösa, äkta bilder av hela dagen — från förberedelser till sista dansen.'),('sthlm2','Bröllopsfilm','Filmiska berättelser med ljud, löften och tal. Highlight-film och full dokumentär.'),('lights1','Dekor &amp; event','Koncept, design och uppbyggnad av mandap, ljus, blommor och bordsdukning.')]))}</div></div></section>
<section><div class="wrap"><a href="ayushi-tejbir.html" class="feature rv"><img src="{I('ayushi',2000)}" alt="Ayushi och Tejbir"><div class="feature-body"><span class="eyebrow">Utvald berättelse</span><h2 class="h-lg">Sveriges största <span class="serif">indiska bröllop</span></h2><p class="lead" style="color:rgba(255,255,255,.8)">Ayushi &amp; Tejbir — en tidlös förening av tradition, elegans och oförglömliga ögonblick.</p><span class="btn btn-gold" style="margin-top:30px">Se berättelsen {ARR}</span></div></a></div></section>
<section style="padding-top:0"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Utvalt arbete</span><h2 class="h-lg">Berättelser vi <span class="serif">burit med oss</span></h2></div><a href="portfolio.html" class="btn btn-line">Hela portfolion {ARR}</a></div>{projects()}</div></section>
<section class="dark"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Så arbetar vi</span><h2 class="h-lg">Från första mejl till <span class="serif gold">färdigt album</span></h2></div></div>
<div class="steps">{''.join(f'<div class="step rv d{n}"><b>0{n+1}</b><h3>{t}</h3><p>{p}</p></div>' for n,(t,p) in enumerate([('Konsultation','Vi lär känna er, er vision och er dag — på plats i Stockholm eller via video.'),('Planering','Tidslinje, platsbesök, shotlist och dekorkoncept. Inga överraskningar.'),('Bröllopsdagen','Vi arbetar diskret och lugnt så att ni kan vara närvarande.'),('Leverans','Handredigerade bilder i ett privat onlinegalleri och er film i 4K.')]))}</div></div></section>
<section><div class="wrap quote rv"><span class="eyebrow">Vår filosofi</span><blockquote>“Vi fångar dagens ögonblick som kommer att röra ert hjärta i morgon.”</blockquote><cite>Rakesh Nagaraja · Grundare</cite></div></section>
{CTA}{INSTA}'''
open('index.html','w').write(page('index.html','R Creations Films — Bröllopsfotograf &amp; filmare i Stockholm','Bröllopsfoto, film och dekor i Stockholm och världen över. Making moments memorable.',idx))

# PORTFOLIO
f,m=gallery()
pf=hero(8776108,I('confetti',1800),'Portfolio','Ögonblick som <span class="serif gold">stannar kvar.</span>','Ett urval av bröllop, destinationer och event vi haft äran att berätta.',('#galleri','Utforska galleriet'),('kontakt.html','Boka ert datum'),'page-hero')
pf+=f'''<section><div class="wrap"><div class="s-head"><div><span class="eyebrow">Berättelser</span><h2 class="h-lg">Hela <span class="serif">bröllop</span>, kapitel för kapitel</h2></div><p class="lead">Varje berättelse är en egen sida med kapitel, galleri och film.</p></div>{projects()}</div></section>
<section class="dark" style="padding:0">{marquee(['Stockholm','Dubai','Skottland','Indiska bröllop','Elopements','Event'])}</section>
<section id="galleri"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Galleri</span><h2 class="h-lg">Ur <span class="serif">arkivet</span></h2></div>{f}</div>{m}</div></section>
<section class="dark"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Film</span><h2 class="h-lg">Rörliga <span class="serif gold">minnen</span></h2></div><p class="lead">Smakprov från ceremonier och fester. Håll muspekaren över för att spela.</p></div>
<div class="projects">{''.join(f'<div class="proj {c} rv"><div class="proj-media"><video muted loop playsinline preload="metadata" poster="{I(p,1400)}" onmouseenter="this.play()" onmouseleave="this.pause()"><source src="{V(v)}" type="video/mp4"></video><span class="proj-tag">{t}</span></div></div>' for v,p,t,c in [(4446328,'ayushi','Indiskt bröllop','wide'),(8776123,'rings','Ringarna',''),(8776113,'confetti','Ceremonin','')])}</div></div></section>
{CTA}'''
open('portfolio.html','w').write(page('portfolio.html','Portfolio — R Creations Films','Bröllop, destinationer och event fotograferade och filmade av R Creations Films.',pf))

# TJANSTER
tj=hero(8776119,I('lights1',1800),'Tjänster &amp; paket','Allt från <span class="serif gold">första ljuset</span> till sista dansen.','Foto, film och dekor — var för sig eller som en helhet med ett och samma team.',('#paket','Se paketen'),('kontakt.html','Begär offert'),'page-hero')
svc=[('confetti','Bröllopsfotografering','Dokumentära, naturliga bilder kombinerade med redaktionella porträtt. Vi följer dagen från förberedelser till fest.',['Förberedelser, ceremoni &amp; fest','Porträttsession med paret','Handredigerade högupplösta bilder','Privat onlinegalleri']),
 ('sthlm2','Bröllopsfilm','Filmiska berättelser med riktigt ljud — löften, tal och skratt — klippta till en film ni vill se igen och igen.',['Highlight-film 4–6 min','Dokumentär i full längd','Drönarfoto där tillåtet','Leverans i 4K']),
 ('mandap','Dekor &amp; design','Från moodboard till färdig scen. Mandap, ljusinstallationer, blommor, bordsdukning och skyltning.',['Koncept &amp; moodboard','Mandap &amp; scenbyggnation','Ljus- &amp; blomsterdesign','Uppbyggnad &amp; nedmontering']),
 ('table','Event &amp; företag','Konferenser, galor och firmafester. Vi har bland annat levererat eventfoto till Handelsbanken.',['Eventfoto &amp; film','Porträtt för personal','Snabb leverans för PR','Dekor &amp; produktion'])]
rows=''
for n,(k,t,p,l) in enumerate(svc):
  rows+=f'<div class="split rv" style="margin-bottom:110px;{"direction:rtl" if n%2 else ""}"><div class="split-media" style="direction:ltr"><img src="{I(k,1300)}" alt="{t}" loading="lazy"></div><div style="direction:ltr"><span class="eyebrow">0{n+1}</span><h2 class="h-lg mt">{t}</h2><p class="lead mt">{p}</p><ul class="svc-list">{"".join(f"<li>{x}</li>" for x in l)}</ul></div></div>'
tj+=f'''<section><div class="wrap">{rows}</div></section>
<section id="paket" style="background:var(--paper-2)"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Paket</span><h2 class="h-lg">Välj er <span class="serif">utgångspunkt</span></h2></div><p class="lead">Alla paket skräddarsys. Priserna är vägledande — kontakta oss för en exakt offert.</p></div>
<div class="packs">
<div class="pack rv"><span class="tag">Intimt</span><h3>Essence</h3><p class="price">Pris på förfrågan</p><ul><li>Upp till 6 timmars fotografering</li><li>Porträttsession med paret</li><li>Handredigerade bilder</li><li>Privat onlinegalleri</li></ul><a href="kontakt.html" class="btn btn-line">Begär offert</a></div>
<div class="pack hl rv d1"><span class="tag">Mest bokad</span><h3>Signature</h3><p class="price">Pris på förfrågan</p><ul><li>Heldag foto + film</li><li>Highlight-film 4–6 min</li><li>Två fotografer/filmare</li><li>Förlovnings- eller pre-wedding-session</li><li>Onlinegalleri &amp; 4K-leverans</li></ul><a href="kontakt.html" class="btn btn-gold">Begär offert</a></div>
<div class="pack rv d2"><span class="tag">Helhet</span><h3>Grand Celebration</h3><p class="price">Pris på förfrågan</p><ul><li>Flerdagars foto &amp; film</li><li>Dokumentär i full längd</li><li>Dekor, mandap &amp; ljusdesign</li><li>Eventkoordinering</li><li>Inbundet album</li></ul><a href="kontakt.html" class="btn btn-line">Begär offert</a></div>
</div></div></section>
<section><div class="wrap split" style="align-items:start"><div><span class="eyebrow">Vanliga frågor</span><h2 class="h-lg mt">Bra att <span class="serif">veta</span></h2><p class="lead mt">Hittar ni inte svaret? Ring eller mejla Rakesh direkt.</p><a href="kontakt.html" class="btn btn-dark" style="margin-top:30px">Ställ en fråga {ARR}</a></div>
<div class="faq">{''.join(f'<details><summary>{q}<i>+</i></summary><p>{a}</p></details>' for q,a in [('Hur långt i förväg bör vi boka?','För sommarbröllop rekommenderar vi 9–12 månader i förväg. Vi tar ett begränsat antal bröllop per år för att kunna ge varje par full uppmärksamhet.'),('Reser ni utomlands?','Ja. Vi har arbetat i bland annat Dubai och Skottland och reser gärna dit ni gifter er.'),('Fotograferar ni indiska bröllop över flera dagar?','Absolut — det är en av våra specialiteter. Vi täcker mehndi, haldi, sangeet, baraat, ceremoni och reception.'),('När får vi våra bilder och film?','Ett urval av förhandsbilder inom en vecka. Hela galleriet och filmen levereras normalt inom 6–10 veckor.'),('Kan vi boka endast dekor?','Ja, alla tjänster kan bokas var för sig — men många par uppskattar att ha ett team för helheten.')])}</div></div></section>{CTA}'''
open('tjanster.html','w').write(page('tjanster.html','Tjänster &amp; paket — R Creations Films','Bröllopsfoto, bröllopsfilm, dekor och event i Stockholm.',tj))

# OM
om=f'''<section class="hero page-hero"><img class="hero-img" src="{I('rakesh_cam',2000)}" alt="Rakesh med kamera"><div class="wrap"><span class="eyebrow rv">Om oss</span><h1 class="h-xl rv d1">Människorna bakom <span class="serif gold">linsen.</span></h1><p class="lead rv d2">Ett Stockholmsbaserat team för foto, film och dekor — grundat av Rakesh Nagaraja.</p><div class="hero-ctas rv d3"><a href="kontakt.html" class="btn btn-gold">Säg hej {ARR}</a><a href="portfolio.html" class="btn btn-ghost">Se portfolio</a></div></div></section>
<section><div class="wrap split"><div class="split-media rv"><img src="{I('rakesh',1200)}" alt="Rakesh Nagaraja"></div><div class="rv d1"><span class="eyebrow">Grundare</span><h2 class="h-lg mt">Hej, jag heter <span class="serif">Rakesh.</span></h2>
<p class="lead mt">Med ett skarpt öga för estetik, teknisk skicklighet och ett kreativt förhållningssätt skapar vi visuellt fängslande event som lämnar ett bestående intryck på gästerna.</p>
<p class="lead mt">Oavsett om det är ett bröllop, ett företagsevent eller ett annat särskilt firande arbetar vi nära våra kunder för att förstå deras vision — och levererar minnen som kan återupplevas genom bilder och film.</p>
<p class="f-big" style="color:var(--text);font-size:2.4rem">Rakesh Nagaraja</p></div></div></section>
<section class="dark"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Våra värderingar</span><h2 class="h-lg">Det vi <span class="serif gold">aldrig</span> kompromissar med</h2></div></div>
<div class="steps">{''.join(f'<div class="step rv d{n}"><b>0{n+1}</b><h3>{t}</h3><p>{p}</p></div>' for n,(t,p) in enumerate([('Äkthet','Riktiga känslor framför stela poser.'),('Detaljer','Varje blomma, varje ljus, varje blick.'),('Lugn','Vi är trygga i kaoset så att ni kan njuta.'),('Tidlöshet','Bilder som håller i generationer.')]))}</div></div></section>
<section><div class="wrap"><div class="s-head"><div><span class="eyebrow">Förtroende</span><h2 class="h-md">Anlitade av par och företag</h2></div></div><p class="lead">Från intima vigslar i Gamla stan till Sveriges största indiska bröllop och företagsuppdrag för Handelsbanken.</p></div></section>
{CTA}{INSTA}'''
open('om.html','w').write(page('om.html','Om oss — R Creations Films','Möt Rakesh Nagaraja och teamet bakom R Creations Films.',om))

# KONTAKT
kt=f'''<section class="hero" style="min-height:62svh"><img class="hero-img" src="{I('lights2',2000)}" alt=""><div class="wrap"><span class="eyebrow rv">Kontakt</span><h1 class="h-xl rv d1">Berätta om <span class="serif gold">er dag.</span></h1><p class="lead rv d2">Vi svarar personligen inom 24 timmar.</p></div></section>
<section><div class="wrap split" style="align-items:start">
<div class="rv"><span class="eyebrow">Direkt kontakt</span><h2 class="h-lg mt">Rakesh <span class="serif">Nagaraja</span></h2><p class="lead mt">Stockholm, Sverige — tillgänglig för uppdrag i hela världen.</p>
<div style="display:grid;gap:14px;margin-top:36px">
<a class="btn btn-line" style="justify-content:space-between" href="tel:+46736172520">+46 73 617 25 20 {PH}</a>
<a class="btn btn-line" style="justify-content:space-between" href="mailto:rcreationsfilms@gmail.com">rcreationsfilms@gmail.com {MAIL}</a>
<a class="btn btn-line" style="justify-content:space-between" href="https://www.instagram.com/rcreations_films" target="_blank" rel="noopener">@rcreations_films {IG}</a></div>
<img src="{I('rings',1000)}" alt="" style="border-radius:22px;margin-top:40px;aspect-ratio:16/10;object-fit:cover;width:100%" loading="lazy"></div>
<form class="form rv d1">
<div class="field"><label for="fn">Förnamn</label><input id="fn" required></div><div class="field"><label for="ln">Efternamn</label><input id="ln" required></div>
<div class="field"><label for="em">E-post</label><input id="em" type="email" required></div><div class="field"><label for="tel">Telefon</label><input id="tel" type="tel"></div>
<div class="field"><label for="dt">Datum</label><input id="dt" type="date"></div><div class="field"><label for="pl">Plats</label><input id="pl" placeholder="Stad eller lokal"></div>
<div class="field full"><label>Vad behöver ni?</label><div class="opts">{''.join(f'<input type="checkbox" id="o{n}"><label for="o{n}">{t}</label>' for n,t in enumerate(['Foto','Film','Dekor','Eventplanering','Företagsevent']))}</div></div>
<div class="field full"><label for="gs">Antal gäster</label><select id="gs"><option>Under 50</option><option>50–150</option><option>150–300</option><option>300+</option></select></div>
<div class="field full"><label for="ms">Berätta om er</label><textarea id="ms" placeholder="Hur träffades ni? Vad är viktigast för er på dagen?"></textarea></div>
<div class="field full"><button class="btn btn-dark" style="justify-content:center;width:100%">Skicka förfrågan {ARR}</button></div></form></div></section>'''
open('kontakt.html','w').write(page('kontakt.html','Kontakt — R Creations Films','Kontakta R Creations Films för bröllop, film, dekor och event.',kt))
print('built')
