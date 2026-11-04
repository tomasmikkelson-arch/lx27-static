/* Зоряне небо у футері: мерехтливі зірки, сузірʼя Персея й рідкісна падаюча зірка.
   Малюється на <canvas> за вмістом картки #fcard. Анімація працює, лише поки футер видно на екрані;
   на телефонах зірок менше; з prefers-reduced-motion малюється один статичний кадр. */
(function(){
  var card=document.getElementById('fcard');
  if(!card||!window.requestAnimationFrame)return;
  var cv=document.createElement('canvas');cv.className='fsky';cv.setAttribute('aria-hidden','true');
  card.insertBefore(cv,card.firstChild);
  var x=cv.getContext('2d');if(!x)return;
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  var PLANET=card.hasAttribute('data-planet');
  var W=0,H=0,dpr=1,stars=[],cons=[],seed=11,running=false,t0=0,shoot=null,nextShoot=0;
  function rnd(){seed=(seed*16807)%2147483647;return seed/2147483647}
  // Сузірʼя Персея (стилізовано): точки в частках області, де воно малюється
  var P=[[.10,.06],[.24,.20],[.40,.28],[.36,.48],[.54,.56],[.70,.50],[.44,.70],[.24,.80],[.62,.82],[.82,.94],[.12,.44]];
  var L=[[0,1],[1,2],[2,3],[3,4],[4,5],[3,6],[6,7],[6,8],[8,9],[3,10]];
  function layout(){
    var r=card.getBoundingClientRect();W=r.width;H=r.height;dpr=Math.min(window.devicePixelRatio||1,2);
    cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr);x.setTransform(dpr,0,0,dpr,0,0);
    seed=11;stars=[];var n=W<700?55:130;
    for(var i=0;i<n;i++)stars.push({x:rnd()*W,y:rnd()*H*.86,r:rnd()*1.1+.3,a:.12+rnd()*.5,s:.6+rnd()*1.8,p:rnd()*6.3});
    // область сузірʼя – вільне місце у футері: на ПК під колонкою «Соцмережі», на телефоні праворуч від навігації
    var cols=card.querySelectorAll('.fcard__bottom>*'),bx,by,bw,bh,cr=card.getBoundingClientRect();
    if(W>=700&&cols.length){var lc=cols[cols.length-1],c=(lc.lastElementChild||lc).getBoundingClientRect(),cl=lc.getBoundingClientRect(),wm=card.querySelector('.giant-foot');
      var bottom=(wm?wm.getBoundingClientRect().top:cr.bottom-cr.height*.14)-cr.top-16;
      by=c.bottom-cr.top+28;bh=Math.max(120,bottom-by);bw=Math.min(bh*1.15,cr.right-cl.left-40);bx=cl.left-cr.left;bh=Math.min(bh,bw*.95)}
    else if(cols.length>1){var n2=cols[1].getBoundingClientRect();bx=W*.5;bw=W*.42;by=n2.top-cr.top+20;bh=Math.min(n2.height-40,bw*1.1)}
    else{bw=W*.3;bh=bw;bx=W*.65;by=H*.6}
    cons=P.map(function(p){return [bx+p[0]*bw,by+p[1]*bh]});
  }
  function star(px,py,rad,al){
    var g=x.createRadialGradient(px,py,0,px,py,rad*5);
    g.addColorStop(0,'rgba(255,255,255,'+al+')');g.addColorStop(.25,'rgba(205,176,255,'+al*.55+')');g.addColorStop(1,'rgba(205,176,255,0)');
    x.fillStyle=g;x.beginPath();x.arc(px,py,rad*5,0,6.283);x.fill();
    x.fillStyle='rgba(255,255,255,'+al+')';x.beginPath();x.arc(px,py,rad,0,6.283);x.fill();
  }
  function planet(t){
    var px=W*(W<700?.18:.9),py=H*(W<700?.42:.12),R=W<700?14:22,dy=Math.sin(t/5200)*4;
    var g=x.createRadialGradient(px-R*.4,py+dy-R*.4,R*.1,px,py+dy,R);
    g.addColorStop(0,'#E7D7FF');g.addColorStop(.55,'#8A31EF');g.addColorStop(1,'#2b1748');
    x.save();x.translate(px,py+dy);x.rotate(-.35);
    x.strokeStyle='rgba(205,176,255,.55)';x.lineWidth=1.4;x.beginPath();x.ellipse(0,0,R*1.9,R*.5,0,Math.PI,2*Math.PI);x.stroke();
    x.restore();x.fillStyle=g;x.beginPath();x.arc(px,py+dy,R,0,6.283);x.fill();
    x.save();x.translate(px,py+dy);x.rotate(-.35);x.beginPath();x.ellipse(0,0,R*1.9,R*.5,0,0,Math.PI);x.stroke();x.restore();
  }
  function frame(now){
    if(!t0)t0=now;var t=now-t0;
    x.clearRect(0,0,W,H);
    for(var i=0;i<stars.length;i++){var s=stars[i],a=reduce?s.a:s.a*(.55+.45*Math.sin(t/1000*s.s+s.p));
      x.fillStyle='rgba(244,239,249,'+a.toFixed(3)+')';x.beginPath();x.arc(s.x,s.y,s.r,0,6.283);x.fill()}
    if(PLANET)planet(t);
    // лінії сузірʼя проявляються по черзі за ~3 с
    var k=reduce?L.length:Math.min(L.length,t/280);
    x.strokeStyle='rgba(205,176,255,.38)';x.lineWidth=1;
    for(var j=0;j<L.length&&j<k;j++){var A=cons[L[j][0]],B=cons[L[j][1]],f=Math.min(1,k-j);
      x.beginPath();x.moveTo(A[0],A[1]);x.lineTo(A[0]+(B[0]-A[0])*f,A[1]+(B[1]-A[1])*f);x.stroke()}
    for(var m=0;m<cons.length;m++){var pulse=reduce?1:.75+.25*Math.sin(t/900+m);star(cons[m][0],cons[m][1],m===2?2.2:1.5,.9*pulse)}
    // падаюча зірка раз на 7–13 с
    if(!reduce){
      if(!shoot&&t>nextShoot){var sx=W*(.15+rnd()*.5),sy=H*(.02+rnd()*.18);shoot={x:sx,y:sy,t:t,d:900}}
      if(shoot){var q=(t-shoot.t)/shoot.d;
        if(q>=1){shoot=null;nextShoot=t+7000+rnd()*6000}
        else{var len=Math.min(W*.16,180),hx=shoot.x+q*W*.22,hy=shoot.y+q*W*.11,tx=hx-len*.9,ty=hy-len*.45,al=Math.sin(q*Math.PI);
          var g2=x.createLinearGradient(tx,ty,hx,hy);g2.addColorStop(0,'rgba(255,201,74,0)');g2.addColorStop(1,'rgba(255,244,214,'+(.9*al).toFixed(3)+')');
          x.strokeStyle=g2;x.lineWidth=1.8;x.beginPath();x.moveTo(tx,ty);x.lineTo(hx,hy);x.stroke()}}
    }
    if(running&&!reduce)requestAnimationFrame(frame);
  }
  function start(){if(running)return;running=true;requestAnimationFrame(frame)}
  function stop(){running=false}
  layout();nextShoot=2500;
  if(reduce){requestAnimationFrame(frame);}
  else if('IntersectionObserver' in window){new IntersectionObserver(function(e){e[0].isIntersecting?start():stop()},{rootMargin:'100px'}).observe(card)}
  else start();
  var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(function(){layout();if(reduce||!running)requestAnimationFrame(frame)},150)});
  document.addEventListener('visibilitychange',function(){if(document.hidden)stop();else if(card.getBoundingClientRect().top<innerHeight)start()});
})();
