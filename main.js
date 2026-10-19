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
      navigator.clipboard.writeText('06 22 62 31 86').then(function(){done('Numéro copié.')},function(){selectPhone();done('Numéro sélectionné, copiez-le.')});
    }catch(e){selectPhone();done('Numéro sélectionné, copiez-le.')}
  });

  var form=document.getElementById('contact-form');
  if(form){
    var recap=document.getElementById('recap'),txt=document.getElementById('recap-text'),
        sms=document.getElementById('recap-sms'),stat=document.getElementById('recap-status');
    var val=function(id){return document.getElementById(id).value.trim()};
    var setErr=function(f,e,msg){
      var wrap=document.getElementById(f).closest('.field');
      wrap.classList.toggle('invalid',!!msg);
      document.getElementById(e).textContent=msg||'';
    };
    form.addEventListener('submit',function(ev){
      ev.preventDefault();
      var ok=true,digits=val('f-tel').replace(/\D/g,'');
      if(!val('f-nom')){setErr('f-nom','e-nom','Indiquez votre nom.');ok=false}else setErr('f-nom','e-nom','');
      if(digits.length<9||digits.length>13){setErr('f-tel','e-tel','Indiquez un numéro valide.');ok=false}else setErr('f-tel','e-tel','');
      if(!val('f-besoin')){setErr('f-besoin','e-besoin','Choisissez une option.');ok=false}else setErr('f-besoin','e-besoin','');
      if(!ok){var bad=form.querySelector('.invalid input,.invalid select');if(bad)bad.focus();return}
      var presta=[].map.call(form.querySelectorAll('input[name=prestations]:checked'),function(c){return c.value});
      var lines=['Bonjour, je souhaite vous contacter pour mon jardin.','Besoin : '+val('f-besoin')+'.'];
      if(presta.length)lines.push('Prestations : '+presta.join(', ')+'.');
      if(val('f-commune'))lines.push('Commune : '+val('f-commune')+'.');
      if(val('f-message'))lines.push('Message : '+val('f-message'));
      lines.push('Merci de me rappeler au '+val('f-tel')+'. '+val('f-nom'));
      txt.value=lines.join('\n');
      sms.href='sms:+33622623186?&body='+encodeURIComponent(txt.value);
      document.getElementById('recap-mail').href='mailto:ace.paysage@hotmail.com?subject='+encodeURIComponent('Demande via le site : '+val('f-besoin'))+'&body='+encodeURIComponent(txt.value);
      form.hidden=true;recap.hidden=false;
      txt.style.height='auto';txt.style.height=(txt.scrollHeight+4)+'px';
      recap.scrollIntoView({block:'nearest'});
    });
    document.getElementById('recap-edit').addEventListener('click',function(){recap.hidden=true;form.hidden=false;document.getElementById('f-nom').focus()});
    document.getElementById('recap-copy').addEventListener('click',function(){
      var done=function(t){stat.textContent=t};
      var fallback=function(){txt.select();done('Texte sélectionné : copiez-le avec Ctrl+C ou Cmd+C.')};
      try{navigator.clipboard.writeText(txt.value).then(function(){done('Demande copiée.')},fallback)}catch(e){fallback()}
    });
    ['f-nom','f-tel','f-besoin'].forEach(function(id){
      document.getElementById(id).addEventListener('input',function(){var f=this.closest('.field');f.classList.remove('invalid');var e=f.querySelector('.err');if(e)e.textContent=''});
    });
  }
})();

