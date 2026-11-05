/* Зоряне небо у футері: мерехтливі зірки й рідкісна падаюча зірка.
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
  var W=0,H=0,dpr=1,stars=[],seed=11,running=false,t0=0,shoot=null,nextShoot=0;
  function rnd(){seed=(seed*16807)%2147483647;return seed/2147483647}
  function layout(){
    var r=card.getBoundingClientRect();W=r.width;H=r.height;dpr=Math.min(window.devicePixelRatio||1,2);
    cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr);x.setTransform(dpr,0,0,dpr,0,0);
    seed=11;stars=[];var n=W<700?55:130;
    for(var i=0;i<n;i++)stars.push({x:rnd()*W,y:rnd()*H*.86,r:rnd()*1.1+.3,a:.12+rnd()*.5,s:.6+rnd()*1.8,p:rnd()*6.3});
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
