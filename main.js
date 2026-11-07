const nav=document.querySelector('.nav');
const onScroll=()=>nav.classList.toggle('scrolled',scrollY>40);onScroll();addEventListener('scroll',onScroll,{passive:true});
document.querySelector('.burger')?.addEventListener('click',()=>{nav.classList.toggle('open');document.body.style.overflow=nav.classList.contains('open')?'hidden':''});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
// counters
document.querySelectorAll('[data-count]').forEach(el=>{const o=new IntersectionObserver(([e])=>{if(!e.isIntersecting)return;o.disconnect();const t=+el.dataset.count,s=performance.now();const f=n=>{const p=Math.min((n-s)/1600,1);el.textContent=Math.round(t*(1-Math.pow(1-p,3)))+(el.dataset.suffix||'');p<1&&requestAnimationFrame(f)};requestAnimationFrame(f)});o.observe(el)});
// filters
document.querySelectorAll('.filters').forEach(g=>g.addEventListener('click',e=>{const b=e.target.closest('.chip');if(!b)return;g.querySelectorAll('.chip').forEach(c=>c.classList.toggle('on',c===b));const f=b.dataset.f;document.querySelectorAll('.masonry figure').forEach(fi=>fi.classList.toggle('hide',f!=='all'&&!fi.dataset.cat.includes(f)))}));
// lightbox
const figs=[...document.querySelectorAll('.masonry figure')];
if(figs.length){const lb=document.createElement('div');lb.className='lb';lb.innerHTML='<img alt=""><button class="x" aria-label="Stäng">✕</button><button class="pv" aria-label="Föregående">←</button><button class="nx" aria-label="Nästa">→</button><div class="cnt"></div>';document.body.append(lb);
let i=0;const vis=()=>figs.filter(f=>!f.classList.contains('hide'));
const show=n=>{const v=vis();i=(n+v.length)%v.length;const im=v[i].querySelector('img');lb.querySelector('img').src=im.dataset.full||im.src;lb.querySelector('.cnt').textContent=String(i+1).padStart(2,'0')+' / '+String(v.length).padStart(2,'0')};
figs.forEach(f=>f.addEventListener('click',()=>{show(vis().indexOf(f));lb.classList.add('on')}));
lb.querySelector('.x').onclick=()=>lb.classList.remove('on');lb.querySelector('.pv').onclick=()=>show(i-1);lb.querySelector('.nx').onclick=()=>show(i+1);
lb.addEventListener('click',e=>{if(e.target===lb)lb.classList.remove('on')});
addEventListener('keydown',e=>{if(!lb.classList.contains('on'))return;if(e.key==='Escape')lb.classList.remove('on');if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)})}
// testimonials
const qs=document.querySelector('[data-quotes]');
if(qs){const items=JSON.parse(qs.dataset.quotes),bq=qs.querySelector('blockquote'),ci=qs.querySelector('cite'),d=qs.querySelector('.q-dots');let k=0;
items.forEach((_,n)=>{const b=document.createElement('button');b.ariaLabel='Citat '+(n+1);b.onclick=()=>go(n);d.append(b)});
const go=n=>{k=n;bq.style.opacity=0;setTimeout(()=>{bq.textContent='“'+items[n][0]+'”';ci.textContent=items[n][1];bq.style.opacity=1},300);[...d.children].forEach((b,j)=>b.classList.toggle('on',j===n))};
bq.style.transition='opacity .3s';go(0);setInterval(()=>go((k+1)%items.length),7000)}
// sound toggle
document.querySelectorAll('.hero-sound').forEach(b=>b.onclick=()=>{const v=b.parentElement.querySelector('video');v.muted=!v.muted;b.textContent=v.muted?'♪':'❚❚'});
// form
document.querySelector('form.form')?.addEventListener('submit',e=>{e.preventDefault();const f=e.target;f.innerHTML='<div class="field full" style="padding:60px 0;text-align:center"><p class="eyebrow" style="justify-content:center">Tack</p><h3 class="h-md mt">Vi har tagit emot din förfrågan.</h3><p class="lead mt" style="margin-inline:auto">Rakesh återkommer personligen inom 24 timmar med tillgänglighet och ett förslag.</p></div>'});
// YouTube montage hero
const ytbg=document.getElementById('ytbg');
if(ytbg){const clips=JSON.parse(ytbg.dataset.clips);let k=0,cur=0,ready=0;const P=[];
const s=document.createElement('script');s.src='https://www.youtube.com/iframe_api';document.head.append(s);
const since=[0,0];const vis=()=>P.forEach((p,n)=>{const st=p.getPlayerState&&p.getPlayerState(),f=p.getIframe();if(st!==1){since[n]=0;f.classList.remove('show');return}if(!since[n])since[n]=Date.now();f.classList.toggle('show',n===cur&&Date.now()-since[n]>1500&&p.getCurrentTime()>(p._s||0)+1)});
window.onYouTubeIframeAPIReady=()=>['ytA','ytB'].forEach((id,n)=>{P[n]=new YT.Player(id,{playerVars:{autoplay:0,mute:1,controls:0,rel:0,playsinline:1,modestbranding:1,iv_load_policy:3,disablekb:1,fs:0},
 events:{onReady:e=>{e.target.mute();if(++ready===2)start()},onStateChange:e=>{vis();if(e.data===0&&P[cur]===e.target)next()}}})});
let timer;
function cue(n,c){P[n]._s=c[1];P[n].loadVideoById({videoId:c[0],startSeconds:c[1]});}
function start(){cue(0,clips[0]);cue(1,clips[1]);setTimeout(()=>P[1].pauseVideo(),900);timer=setTimeout(next,clips[0][2]*1000)}
function next(){clearTimeout(timer);const old=cur;cur=1-cur;k++;P[cur].playVideo();
 const go=()=>{if(P[cur].getPlayerState()===1){vis();setTimeout(()=>{P[old].pauseVideo();cue(old,clips[(k+1)%clips.length]);setTimeout(()=>P[old].pauseVideo(),900)},1400);timer=setTimeout(next,clips[k%clips.length][2]*1000)}else setTimeout(go,150)};go()}
setInterval(vis,200)}
