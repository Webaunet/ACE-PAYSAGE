(function(){
  var burger=document.getElementById('burger'),nav=document.getElementById('nav');
  function setMenu(open){
    nav.classList.toggle('open',open);
    burger.setAttribute('aria-expanded',open?'true':'false');
    burger.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');
  }
  burger.addEventListener('click',function(){setMenu(!nav.classList.contains('open'))});
  nav.addEventListener('click',function(e){if(e.target.closest('a.link'))setMenu(false)});

  var copy=document.getElementById('copy'),msg=document.getElementById('copied'),phone=document.getElementById('phone');
  function selectPhone(){
    try{var r=document.createRange();r.selectNodeContents(phone);var s=window.getSelection();s.removeAllRanges();s.addRange(r)}catch(e){}
  }
  if(copy&&msg&&phone)copy.addEventListener('click',function(){
    var done=function(t){msg.textContent=t;setTimeout(function(){msg.textContent=''},3000)};
    try{
      navigator.clipboard.writeText('06 99 20 18 49').then(function(){done('Numéro copié.')},function(){selectPhone();done('Numéro sélectionné, copiez-le.')});
    }catch(e){selectPhone();done('Numéro sélectionné, copiez-le.')}
  });
})();
