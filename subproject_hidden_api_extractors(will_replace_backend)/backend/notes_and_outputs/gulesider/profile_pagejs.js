(function(){
    function aa(a){
    var b=0;
    return function(){
        return b<a.length?{done:!1,value:a[b++]
            }:{done:!0}
        }
    }

    function p(a){
        var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];
        return b?b.call(a):{
        next:aa(a)
        }
    }

    function ba(a){
            if(!(a instanceof Array)){
            a=p(a);
            for(var b,c=[];
                !(b=a.next()).done;
            )c.push(b.value);
            a=c
            }
        return a
    }
    var ca="function"==typeof Object.create?Object.create:function(a){
        function b(){}
        b.prototype=a;
        return new b
    },
    r;

if("function"==typeof Object.setPrototypeOf)r=Object.setPrototypeOf;
else{
    var da;
    a:{
    var ea={
    Ya:!0
    }
    ,fa={
    

        }
        ;
try{
    fa.__proto__=ea;
    da=fa.Ya;
    break a
    }
    catch(a){
    

        }
        da=!1
    }
    r=da?function(a,b){
    a.__proto__=b;
    if(a.__proto__!==b)throw new TypeError(a+" is not extensible");
    return a
    }
    :null
    }
    var t=r;
    
function u(a,b){
    a.prototype=ca(b.prototype);
    a.prototype.constructor=a;
    if(t)t(a,b);
    else for(var c in b)if("prototype"!=c)if(Object.defineProperties){
    var d=Object.getOwnPropertyDescriptor(b,c);
    d&&Object.defineProperty(a,c,d)
    }
    else a[c]=b[c];
    a.Rb=b.prototype
    }
    var ha="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){
    a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)
    }
    ,v="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this;
    
function ka(){
    ka=function(){
    

        }
        ;
v.Symbol||(v.Symbol=la)
    }
    function ma(a,b){
    this.a=a;
    ha(this,"description",{
    configurable:!0,writable:!0,value:b
    }
    )
    }
    ma.prototype.toString=function(){
    return this.a
    }
    ;
    var la=function(){
    function a(c){
    if(this instanceof a)throw new TypeError("Symbol is not a constructor");
    return new ma("jscomp_symbol_"+(c||"")+"_"+b++,c)
    }
    var b=0;
    return a
    }
    ();
    
function na(){
    ka();
    var a=v.Symbol.iterator;
    a||(a=v.Symbol.iterator=v.Symbol("Symbol.iterator"));
    "function"!=typeof Array.prototype[a]&&ha(Array.prototype,a,{
    configurable:!0,writable:!0,value:function(){
    return oa(aa(this))
    }

    }
    );
    na=function(){
    

        }

    }
    function oa(a){
    na();
    a={
    next:a
    }
    ;
    a[v.Symbol.iterator]=function(){
    return this
    }
    ;
    return a
    }
    function pa(){
    this.I=!1;
    this.u=null;
    this.c=void 0;
    this.a=1;
    this.ba=this.W=0;
    this.B=null
    }
    function qa(a){
    if(a.I)throw new TypeError("Generator is already running");
    a.I=!0
    }

pa.prototype.T=function(a){
    this.c=a
    }
    ;
    function ra(a,b){
    a.B={
    eb:b,mb:!0
    }
    ;
    a.a=a.W||a.ba
    }
    pa.prototype.return=function(a){
    this.B={
    return:a
    }
    ;
    this.a=this.ba
    }
    ;
    function w(a,b,c){
    a.a=c;
    return{
    value:b
    }

    }
    function sa(a){
    this.a=new pa;
    this.c=a
    }
    function ta(a,b){
    qa(a.a);
    var c=a.a.u;
    if(c)return ua(a,"return"in c?c["return"]:function(d){
    return{
    value:d,done:!0
    }

    }
    ,b,a.a.return);
    a.a.return(b);
    return y(a)
    }

function ua(a,b,c,d){
    try{
    var g=b.call(a.a.u,c);
    if(!(g instanceof Object))throw new TypeError("Iterator result "+g+" is not an object");
    if(!g.done)return a.a.I=!1,g;
    var f=g.value
    }
    catch(e){
    return a.a.u=null,ra(a.a,e),y(a)
    }
    a.a.u=null;
    d.call(a.a,f);
    return y(a)
    }
    function y(a){
    for(;
        a.a.a;
        )try{
    var b=a.c(a.a);
    if(b)return a.a.I=!1,{
    value:b.value,done:!1
    }

    }
    catch(c){
    a.a.c=void 0,ra(a.a,c)
    }
    a.a.I=!1;
    if(a.a.B){
    b=a.a.B;
    a.a.B=null;
    if(b.mb)throw b.eb;
    return{
    value:b.return,done:!0
    }

    }
    return{
    value:void 0,done:!0
    }

    }

function va(a){
    this.next=function(b){
    qa(a.a);
    a.a.u?b=ua(a,a.a.u.next,b,a.a.T):(a.a.T(b),b=y(a));
    return b
    }
    ;
    this.throw=function(b){
    qa(a.a);
    a.a.u?b=ua(a,a.a.u["throw"],b,a.a.T):(ra(a.a,b),b=y(a));
    return b
    }
    ;
    this.return=function(b){
    return ta(a,b)
    }
    ;
    na();
    this[Symbol.iterator]=function(){
    return this
    }

    }
    function z(a,b){
    b=new va(new sa(b));
    t&&t(b,a.prototype);
    return b
    }

function A(a,b){
    if(b){
    var c=v;
    a=a.split(".");
    for(var d=0;
        d<a.length-1;
        d++){
    var g=a[d];
    g in c||(c[g]={
    

        }
        );
c=c[g]
    }
    a=a[a.length-1];
d=c[a];
b=b(d);
b!=d&&null!=b&&ha(c,a,{
    configurable:!0,writable:!0,value:b
    }
    )
    }

    }

A("Promise",function(a){
    function b(e){
    this.c=0;
    this.I=void 0;
    this.a=[];
    var k=this.u();
    try{
    e(k.resolve,k.reject)
    }
    catch(m){
    k.reject(m)
    }

    }
    function c(){
    this.a=null
    }
    function d(e){
    return e instanceof b?e:new b(function(k){
    k(e)
    }
    )
    }
    if(a)return a;
    c.prototype.c=function(e){
    if(null==this.a){
    this.a=[];
    var k=this;
    this.u(function(){
    k.I()
    }
    )
    }
    this.a.push(e)
    }
    ;
    var g=v.setTimeout;
    c.prototype.u=function(e){
    g(e,0)
    }
    ;
    c.prototype.I=function(){
    for(;
        this.a&&this.a.length;
        ){
    var e=this.a;
    this.a=[];
    for(var k=0;
        k<e.length;
        ++k){
    var m=
e[k];
e[k]=null;
try{
    m()
    }
    catch(l){
    this.B(l)
    }

    }

    }
    this.a=null
    }
    ;
    c.prototype.B=function(e){
    this.u(function(){
    throw e;

    }
    )
    }
    ;
    b.prototype.u=function(){
    function e(l){
    return function(h){
    m||(m=!0,l.call(k,h))
    }

    }
    var k=this,m=!1;
    return{
    resolve:e(this.ob),reject:e(this.B)
    }

    }
    ;
    b.prototype.ob=function(e){
    if(e===this)this.B(new TypeError("A Promise cannot resolve to itself"));
    else if(e instanceof b)this.ub(e);
    else{
    a:switch(typeof e){
    case "object":var k=null!=e;
    break a;
    case "function":k=!0;
    break a;
    default:k=!1
    }
    k?this.nb(e):
this.T(e)
    }

    }
    ;
b.prototype.nb=function(e){
    var k=void 0;
    try{
    k=e.then
    }
    catch(m){
    this.B(m);
    return
    }
    "function"==typeof k?this.yb(k,e):this.T(e)
    }
    ;
    b.prototype.B=function(e){
    this.W(2,e)
    }
    ;
    b.prototype.T=function(e){
    this.W(1,e)
    }
    ;
    b.prototype.W=function(e,k){
    if(0!=this.c)throw Error("Cannot settle("+e+", "+k+"): Promise already settled in state"+this.c);
    this.c=e;
    this.I=k;
    this.ba()
    }
    ;
    b.prototype.ba=function(){
    if(null!=this.a){
    for(var e=0;
        e<this.a.length;
        ++e)f.c(this.a[e]);
    this.a=null
    }

    }
    ;
    var f=new c;
    b.prototype.ub=function(e){
    var k=
this.u();
e.fa(k.resolve,k.reject)
    }
    ;
b.prototype.yb=function(e,k){
    var m=this.u();
    try{
    e.call(k,m.resolve,m.reject)
    }
    catch(l){
    m.reject(l)
    }

    }
    ;
    b.prototype.then=function(e,k){
    function m(q,x){
    return"function"==typeof q?function(ia){
    try{
    l(q(ia))
    }
    catch(ja){
    h(ja)
    }

    }
    :x
    }
    var l,h,n=new b(function(q,x){
    l=q;
    h=x
    }
    );
    this.fa(m(e,l),m(k,h));
    return n
    }
    ;
    b.prototype.catch=function(e){
    return this.then(void 0,e)
    }
    ;
    b.prototype.fa=function(e,k){
    function m(){
    switch(l.c){
    case 1:e(l.I);
    break;
    case 2:k(l.I);
    break;
    default:throw Error("Unexpected state: "+
l.c);

    }

    }
    var l=this;
null==this.a?f.c(m):this.a.push(m)
    }
    ;
b.resolve=d;
b.reject=function(e){
    return new b(function(k,m){
    m(e)
    }
    )
    }
    ;
    b.race=function(e){
    return new b(function(k,m){
    for(var l=p(e),h=l.next();
    !h.done;
    h=l.next())d(h.value).fa(k,m)
    }
    )
    }
    ;
    b.all=function(e){
    var k=p(e),m=k.next();
    return m.done?d([]):new b(function(l,h){
    function n(ia){
    return function(ja){
    q[ia]=ja;
    x--;
    0==x&&l(q)
    }

    }
    var q=[],x=0;
    do q.push(void 0),x++,d(m.value).fa(n(q.length-1),h),m=k.next();
    while(!m.done)
    }
    )
    }
    ;
    return b
    }
    );
    
var wa="function"==typeof Object.assign?Object.assign:function(a,b){
    for(var c=1;
        c<arguments.length;
        c++){
    var d=arguments[c];
    if(d)for(var g in d)Object.prototype.hasOwnProperty.call(d,g)&&(a[g]=d[g])
    }
    return a
    }
    ;
    A("Object.assign",function(a){
    return a||wa
    }
    );
    A("Object.values",function(a){
    return a?a:function(b){
    var c=[],d;
    for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&c.push(b[d]);
    return c
    }

    }
    );
    A("Object.is",function(a){
    return a?a:function(b,c){
    return b===c?0!==b||1/b===1/c:b!==b&&c!==c
    }

    }
    );
    
A("Array.prototype.includes",function(a){
    return a?a:function(b,c){
    var d=this;
    d instanceof String&&(d=String(d));
    var g=d.length;
    c=c||0;
    for(0>c&&(c=Math.max(c+g,0));
    c<g;
    c++){
    var f=d[c];
    if(f===b||Object.is(f,b))return!0
    }
    return!1
    }

    }
    );
    
var xa={
    Db:"connect_debug",Za:"https://signal-beacon.s-onetag.com/beacon.min.js",Bb:"https://ap.lijit.com/readerinfo/v2",sb:"https://get.s-onetag.com/container-polyfills.js",rb:["fetch","Promise"],jb:"https://onetag-geo.s-onetag.com/",Gb:"https://onetag-geo-grouping.s-onetag.com/",Hb:"https://geo-location.s-onetag.com/",vb:"https://signal-segments.s-onetag.com/",Fb:"https://signal-floors.s-onetag.com/",hb:86400,gb:200,Mb:"EU",xa:10,Ab:"https://ap.lijit.com/www/delivery/fpi.js?z=",Pb:{
    Ib:"https://get.s-onetag.com/safeframe-urls/1.0.0/safe-frame-internal.html",
Kb:"https://get.s-onetag.com/safeframe-urls/1.0.0/safe-frame.js"
    }
    ,Ob:"https://prebid.s-onetag.com",pa:"https://dfp-gateway.s-onetag.com/1",va:86400,Ia:"https://connect-metrics-collector.s-onetag.com/metrics",Sb:5E3,Nb:"https://get.s-onetag.com/underground-sync-portal/Portal.html",Cb:"https://data-beacons.s-onetag.com/dataBeacons.min.js",ta:["hb_","ix_","amzn"],Lb:7E3
    }
    ;
var ya;
function B(){
    if(ya)return ya;
    throw Error("Not initialized");

    }
    ;
    function za(){
    this.window=window
    }
    var Aa;
    function C(){
    Aa||(Aa=new za);
    return Aa
    }
    za.prototype.get=function(){
    var a=this.window.top;
    try{
    a=Ba(a),a.__connect.state="FRIENDLY"
    }
    catch(b){
    a=Ba(this.window),a.__connect.state="UNFRIENDLY",a.Ha&&a.Ha.ext&&(a.__connect.state="SAFEFRAME")
    }
    return a
    }
    ;
    function Ba(a){
    a.__connect||(a.__connect={
    

        }
        );
return a
    }
    ;
var Ca=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function Da(){
    this.window=C().get();
    this.M=B()
    }

function Ea(a){
    Ca(Fa,void 0,void 0,function c(){
    var d=this,g;
    return z(c,function(f){
    g=d;
    d.window.__connect=d.window.__connect||{
    

        }
        ;
d.window.__connect.beacon=d.window.__connect.beacon||{
    containerId:a.containerId,affiliateId:a.aa,enableIpCollection:!!a.Ma,disablePIITracking:!!a.La
    }
    ;
    return f.return(new Promise(function(e){
    var k=g.window.document.createElement("script");
    k.onload=function(){
    e()
    }
    ;
    k.src=g.M.Za;
    g.window.document.head.appendChild(k)
    }
    ))
    }
    )
    }
    )
    }
    var Fa=null;
    function Ga(a){
    this.a=a
    }
    Ga.prototype.create=function(a){
    return new this.a[a.f](a.b)
    }
    ;
    var Ha=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function Ia(a){
    this.fb=new Ga(a)
    }

function Ja(a,b){
    return Ha(a,void 0,void 0,function d(){
    var g=this,f,e,k,m,l,h;
    return z(d,function(n){
    switch(n.a){
    case 1:if(!b||0===b.length)return n.return(!0);
    f=Ka(b);
    e=[];
    k=p(Object.keys(f));
    m=k.next();
    case 2:if(m.done){
    n.a=4;
    break
    }
    l=m.value;
    return w(n,La(g,f[l]),5);
    case 5:h=n.c;
    e.push(h);
    m=k.next();
    n.a=2;
    break;
    case 4:return n.return(e.every(function(q){
    return q
    }
    ))
    }

    }
    )
    }
    )
    }

function La(a,b){
    return Ha(a,void 0,void 0,function d(){
    var g=this,f,e,k,m,l,h,n;
    return z(d,function(q){
    switch(q.a){
    case 1:f="EXCLUDE"===b[0].b.g,e=p(b),k=e.next();
    case 2:if(k.done){
    q.a=4;
    break
    }
    m=k.value;
    l=g.fb.create(m);
    return w(q,l.Qa(),5);
    case 5:h=q.c;
    n=m.b.g;
    f="EXCLUDE"===n?f&&!h:f||h;
    k=e.next();
    q.a=2;
    break;
    case 4:return q.return(f)
    }

    }
    )
    }
    )
    }
    function Ka(a){
    return a.reduce(function(b,c){
    var d=c.f;
    b[d]||(b[d]=[]);
    b[d].push(c);
    return b
    }
    ,{
    

        }
        )
    }
    ;
C().get();
function Ma(){
    this.N=!0
    }
    ;
    function D(a){
    this.N=!0;
    this.window=a;
    this.window.addEventListener("focus",this.c.bind(this));
    this.window.addEventListener("focusin",this.c.bind(this));
    this.window.addEventListener("blur",this.a.bind(this));
    this.window.addEventListener("focusout",this.a.bind(this))
    }
    u(D,Ma);
    D.prototype.c=function(){
    this.N=!0
    }
    ;
    D.prototype.a=function(){
    this.window.document.hasFocus()?this.N=!0:this.N=!1
    }
    ;
    function E(a,b){
    this.N=!0;
    this.window=a;
    this.u=void 0===b?10:b;
    this.I="mousemove mousedown scroll keyup keypress keydown touchstart touchmove touchend".split(" ");
    a=p(this.I);
    for(b=a.next();
    !b.done;
    b=a.next())this.window.addEventListener(b.value,this.a.bind(this));
    this.a()
    }
    u(E,Ma);
    E.prototype.a=function(){
    var a=this;
    this.c||(this.c=this.window.setTimeout(function(){
    clearTimeout(a.T);
    a.T=a.window.setTimeout(a.B.bind(a),1E3*a.u);
    a.c=null
    }
    ,50),this.N=!0)
    }
    ;
    E.prototype.B=function(){
    this.N=!1
    }
    ;
    function Na(a,b){
    this.a=a;
    this.c=b
    }
    var Oa;
    function Pa(){
    if(!Oa){
    var a=C().get(),b=new D(a);
    a=new E(a);
    Oa=new Na(b,a)
    }
    return Oa
    }
    Na.prototype.N=function(){
    return this.a.N&&this.c.N
    }
    ;
    function Qa(){
    

        }
        Qa.prototype.create=function(){
    return new XMLHttpRequest
    }
    ;
    function Ra(){
    this.a=new Qa
    }
    Ra.prototype.send=function(a,b){
    var c=this.a.create();
    c.open("POST",a,!1);
    c.setRequestHeader("Content-Type","text/plain");
    c.send(JSON.stringify(b))
    }
    ;
    function Sa(a,b){
    a=Error.call(this,JSON.stringify(b));
    this.message=a.message;
    "stack"in a&&(this.stack=a.stack)
    }
    u(Sa,Error);
    var Ta=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function F(){
    

        }

function G(a,b){
    var c=void 0===c?{
    

        }
        :c;
return Ta(a,void 0,void 0,function g(){
    var f,e,k;
    return z(g,function(m){
    if(1==m.a)return w(m,fetch(b,c),2);
    if(3!=m.a)return f=m.c,w(m,f.json(),3);
    e=m.c;
    k=f.status.toString();
    if("4"===k[0]||"5"===k[0])throw new Sa(k,e);
    return m.return(e)
    }
    )
    }
    )
    }
    ;
    var H=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function I(){
    this.M=B();
    this.window=C().get();
    this.X=new F;
    this.ja=!1
    }
    var Ua;
    
function Va(a){
    return H(a,void 0,void 0,function c(){
    var d=this,g;
    return z(c,function(f){
    if(1==f.a)return w(f,d.getData(),2);
    g=f.c;
    return f.return(g.country)
    }
    )
    }
    )
    }

I.prototype.getData=function(){
    return H(this,void 0,void 0,function b(){
    var c=this,d,g;
    return z(b,function(f){
    switch(f.a){
    case 1:try{
    var e=JSON.parse(c.window.localStorage.getItem("connect-location-data"));
    var k=e.expiresAt>Date.now()?e.value:!1
    }
    catch(m){
    k=!1
    }
    if(d=k)return f.return(d);
    if(!c.ja){
    f.a=2;
    break
    }
    return w(f,c.wait(c.M.gb),3);
    case 3:return f.return(c.getData());
    case 2:return c.ja=!0,w(f,Wa(c),4);
    case 4:return g=f.c,c.Ea("connect-location-data",g),c.ja=!1,f.return(g)
    }

    }
    )
    }
    )
    }
    ;
    
function Wa(a){
    return H(a,void 0,void 0,function c(){
    var d=this,g;
    return z(c,function(f){
    if(1==f.a)return w(f,G(d.X,d.M.jb),2);
    g=f.c;
    if(!g.country)throw d.ja=!1,Error("Location not found");
    return f.return(g)
    }
    )
    }
    )
    }
    I.prototype.Ea=function(a,b){
    b={
    value:b,expiresAt:Date.now()+1E3*this.M.hb
    }
    ;
    try{
    this.window.localStorage.setItem(a,JSON.stringify(b))
    }
    catch(c){
    

        }

    }
    ;

I.prototype.wait=function(a){
    return H(this,void 0,void 0,function c(){
    return z(c,function(d){
    return d.return(new Promise(function(g){
    return setTimeout(g,a)
    }
    ))
    }
    )
    }
    )
    }
    ;
    var Xa=function(){
    function a(){
    

        }
        a.kb=function(){
    var b=C().get();
    b=b[a.a]=b[a.a]||{
    

        }
        ;
b.pageViewId||(b.pageViewId=a.c());
return b.pageViewId
    }
    ;
a.c=function(){
    return+new Date+Math.floor(1E3*Math.random())
    }
    ;
    a.a="__connect";
    return a
    }
    ();
    var Ya=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    
function Za(){
    Ua||(Ua=new I);
    this.ib=Ua;
    this.window=C().get();
    this.wa={
    pageViewId:Xa.kb(),domain:this.window.location.hostname,path:this.window.location.pathname,isSafeFrame:"FRIENDLY"!==this.window.__connect.state,location:"",query:this.window.location.search.slice(0,100),referrer:this.window.document.referrer.slice(0,100)
    }
    ;
    $a(this)
    }
    Za.prototype.Da=function(a){
    this.wa.affiliateId=a
    }
    ;
    Za.prototype.get=function(){
    return this.wa
    }
    ;
    
function $a(a){
    Ya(a,void 0,void 0,function c(){
    var d=this,g;
    return z(c,function(f){
    g=d;
    Va(d.ib).then(function(e){
    g.wa.location=e
    }
    );
    f.a=0
    }
    )
    }
    )
    }
    ;
    function J(){
    this.a=[];
    this.I={
    

        }
        ;
this.c=!1;
this.M=B();
this.W=Pa();
this.window=C().get();
this.T=new Za;
this.ba=new Ra;
this.Fa()
    }
    var ab;
J.prototype.Da=function(a){
    this.T.Da(a)
    }
    ;
    function K(){
    ab||(ab=new J);
    return ab
    }
    function L(a,b,c){
    b={
    contentId:b,type:"activation"
    }
    ;
    c&&(b.contentMetadata=c);
    a.a.push(Object.assign({
    

        }
        ,b))
    }
    function M(a,b,c){
    a.I[b]||(a.I[b]=!0,a.a.push(Object.assign({
    

        }
        ,{
    containerId:b,type:"adoption"
    }
    )));
    c&&a.a.push(Object.assign({
    

        }
        ,{
    containerId:b,contentId:c,type:"adoption"
    }
    ))
    }

J.prototype.Fa=function(){
    var a=this;
    bb(this);
    this.window.setInterval(function(){
    a.W.N()||cb(a)
    }
    ,1E3)
    }
    ;
    function bb(a){
    a.window.addEventListener("pageshow",a.u.bind(a));
    a.window.addEventListener("beforeunload",a.B.bind(a));
    a.window.addEventListener("pagehide",a.B.bind(a));
    a.window.document.addEventListener("visibilitychange",function(){
    if(a.window.document.hidden)return a.B();
    a.u()
    }
    )
    }
    J.prototype.B=function(){
    this.c||(this.c=!0,cb(this),this.window.setTimeout(this.u.bind(this),3E3))
    }
    ;
    
J.prototype.u=function(){
    this.c=!1
    }
    ;
    function cb(a){
    if(a.a.length){
    var b=a.window.navigator,c={
    metadata:a.T.get(),payloads:a.a
    }
    ;
    a.a=[];
    var d=!1;
    b.sendBeacon&&(d=b.sendBeacon(a.M.Ia,JSON.stringify(c)));
    d||a.ba.send(a.M.Ia,JSON.stringify(c))
    }

    }
    ;
    var db=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function eb(a,b){
    this.L=a;
    this.$a=b;
    this.ea=[];
    this.J=K();
    this.window=C().get();
    this.Oa=new Ia(b)
    }

eb.prototype.start=function(){
    return db(this,void 0,void 0,function b(){
    var c=this,d,g,f,e,k,m,l;
    return z(b,function(h){
    switch(h.a){
    case 1:d=p(c.L.groups),g=d.next();
    case 2:if(g.done){
    h.a=4;
    break
    }
    f=g.value;
    return w(h,Ja(c.Oa,f.filters),5);
    case 5:e=h.c;
    if(!e){
    h.a=3;
    break
    }
    k=p(f.ab);
    m=k.next();
    case 7:if(m.done){
    h.a=3;
    break
    }
    l=m.value;
    return w(h,fb(c,l),8);
    case 8:m=k.next();
    h.a=7;
    break;
    case 3:g=d.next();
    h.a=2;
    break;
    case 4:c.ea.length&&gb(c),h.a=0
    }

    }
    )
    }
    )
    }
    ;
    
function fb(a,b){
    return db(a,void 0,void 0,function d(){
    var g=this,f,e,k;
    return z(d,function(m){
    if(1==m.a)return w(m,Ja(g.Oa,b.filters),2);
    f=m.c;
    if(!f)return m.return();
    var l=b.contentType,h=b.b,n=b.h,q=g.L.containerId;
    h.aa=g.L.Ga.aa;
    e=new g.$a[l](h,n,q);
    k=b.h;
    e.Na?(M(g.J,g.L.containerId,k),e.ha()):"loading"!==g.window.document.readyState?(M(g.J,g.L.containerId,k),e.ha()):g.ea.push({
    implementation:e,id:k
    }
    );
    m.a=0
    }
    )
    }
    )
    }

function gb(a){
    a.window.document.addEventListener("readystatechange",function(){
    if("loading"!==a.window.document.readyState){
    for(var b=p(a.ea),c=b.next();
    !c.done;
    c=b.next()){
    c=c.value;
    var d=c.implementation;
    M(a.J,a.L.containerId,c.id);
    d.ha()
    }
    a.ea=[]
    }

    }
    )
    }
    ;
    function hb(){
    var a={
    Ga:{
    Tb:"7f8eb570-ee01-4e61-921e-b21a663350e3",aa:360687
    }
    ,containerId:"c4461679-72c1-467b-af75-dba675ac116e",groups:[{
    groupId:"b6f5af66-b135-40f7-8097-df2e60b1863f",enabled:!0,filters:[],b:{
    

        }
        ,ab:[{
    h:"68486692-49ba-4a21-88f3-b0ea5439436a",filters:[],b:{
    wb:["gam"]
    }
    ,contentType:"signal-segments",enabled:!0
    }
    ,{
    h:"f3f4c2a9-f615-4503-a79f-a93ddd9265bb",filters:[{
    i:"e668a746-adad-4a89-83f3-1140cb22b7ca",f:"screensize",b:{
    g:"EXCLUDE",name:"Mobile",min:"0",max:"992"
    }

    }
    ,{
    i:"ab88bf05-f529-40cc-900d-d3a8d045fe7e",
f:"url",b:{
    pattern:"fagligsenior.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:15,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"c3feb623-b419-4cdc-b6d1-39d97cc8261b",filters:[{
    i:"4fc9b553-0a20-4194-a15d-605048439376",f:"screensize",b:{
    g:"EXCLUDE",name:"Desktop",min:"993",max:"999"
    }

    }
    ,{
    i:"3843e926-1b6a-4865-99e6-b1d4de03245d",f:"url",b:{
    pattern:"fagligsenior.dk",
match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:30,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"46d2c622-5bd3-426a-abc6-4971344031d8",filters:[{
    i:"59628530-cbe8-4049-a480-5592d2165110",f:"screensize",b:{
    g:"EXCLUDE",name:"Mobile",min:"0",max:"992"
    }

    }
    ,{
    i:"caf1713b-1e70-46aa-8867-773db1022781",f:"url",b:{
    pattern:"seniornews.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:15,s:!0,
A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"31144c4a-3c0f-4165-879d-cb4b5955fc61",filters:[{
    i:"121f5a77-65eb-4d5b-8443-489fa3469ae6",f:"screensize",b:{
    g:"EXCLUDE",name:"Desktop",min:"993",max:"9999"
    }

    }
    ,{
    i:"34ee2caa-3bf7-4663-8208-ebb2b947e9eb",f:"url",b:{
    pattern:"seniornews.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:12,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,
{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"645639b4-3b51-4b22-8f9b-7cfdba96deaf",filters:[{
    i:"42d2a0b0-c05c-4d20-b64b-931186469977",f:"screensize",b:{
    g:"EXCLUDE",name:"Mobile",min:"0",max:"992"
    }

    }
    ,{
    i:"9a0c0eec-6d0b-477a-90fb-45eae40c662a",f:"url",b:{
    pattern:"travservice.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:15,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,
G:!0,R:{
    

    }
    ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"7ca06b64-2aa4-4354-8259-70ca1f5c11ea",filters:[{
    i:"62aae078-8256-4912-85a0-19226af1c22a",f:"screensize",b:{
    g:"EXCLUDE",name:"Desktop",min:"993",max:"9999"
    }

    }
    ,{
    i:"d50402a2-4d89-4e21-a566-1d845cf41c16",f:"url",b:{
    pattern:"travservice.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:12,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,
l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"5c53b78c-2d50-4000-969e-1b1cd9b6fb39",filters:[{
    i:"83193f3a-f5fd-4b9c-a328-dcaf587fd740",f:"screensize",b:{
    g:"EXCLUDE",name:"Mobile",min:"0",max:"992"
    }

    }
    ,{
    i:"339d289d-683e-4ff2-9977-0fba37c16bb1",f:"url",b:{
    pattern:"galopservice.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:15,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,
{
    h:"2bdbc70a-f2b3-48bc-9c47-6b459fc5af55",filters:[{
    i:"5d5fd665-fedb-4128-aa3b-b169633d357e",f:"screensize",b:{
    g:"EXCLUDE",name:"Desktop",min:"993",max:"9999"
    }

    }
    ,{
    i:"446e9af6-b9fd-4185-8be8-3272450e609b",f:"url",b:{
    pattern:"galopservice.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:12,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"97536838-43c7-4420-945d-8dbd74dd5c97",
filters:[{
    i:"f23a8927-0559-41ff-afa4-6a54e9b2cf38",f:"screensize",b:{
    g:"EXCLUDE",name:"Mobile",min:"000",max:"992"
    }

    }
    ,{
    i:"7bd4f8c5-8b08-45e2-8a5b-102c98e72ca2",f:"url",b:{
    pattern:"heste-nettet.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:15,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"5615cd5c-aa90-491e-97d3-0a6c33cf5b70",filters:[{
    i:"3efd0ae3-2ffd-4885-af17-18862ae0f49d",
f:"screensize",b:{
    g:"EXCLUDE",name:"Desktop",min:"993",max:"9999"
    }

    }
    ,{
    i:"9626479f-45b9-43ac-ad2f-7e7528060f5f",f:"url",b:{
    pattern:"heste-nettet.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    m:12,s:!0,A:[],o:[],j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],w:!0,K:!1,G:!0,R:{
    

        }
        ,V:!0,P:[],C:{
    D:{
    

        }
        ,O:{
    

    }
    ,F:{
    

    }

    }
    ,l:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"60b06946-3ed8-4df3-8f00-2d6cb191e0f7",filters:[{
    i:"288f0af8-8225-4d4c-b534-8c1710b6931a",f:"screensize",b:{
    g:"EXCLUDE",name:"MOBILE",
min:1,max:992
    }

    }
    ,{
    i:"888b3a9c-cd3a-4178-b7dc-ac3b00a1ff7d",f:"url",b:{
    pattern:"degulesider.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    A:[],reload:!0,m:15,s:!0,j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],o:["#div-gpt-ad-1639556518400-0"],C:{
    D:{
    

        }
        ,F:{
    

    }

    }
    ,Y:"include",l:[],H:[],w:!0,G:!0
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"9ffa08fe-9f47-4d36-bed4-9dbb1d715aea",filters:[{
    i:"a4e54620-35c2-44de-bb60-8480a7c2e495",f:"screensize",b:{
    g:"EXCLUDE",name:"DESKTOP",min:993,max:9999
    }

    }
    ,
{
    i:"51f6b2d6-abc4-4df9-a1dc-f3cc84a62a9e",f:"url",b:{
    pattern:"degulesider.dk",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    A:[],reload:!0,m:10,s:!0,j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],o:["#div-gpt-ad-1639556518400-0"],C:{
    D:{
    

        }
        ,F:{
    

    }
    ,O:{
    

    }

    }
    ,Y:"include",l:[],H:[],w:!0,G:!0
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"e2f658b5-32ce-4a33-9436-2e3941a45f6b",filters:[{
    i:"54ee30a6-4331-44cb-adb7-22386e8fe00a",f:"screensize",b:{
    g:"EXCLUDE",name:"MOBILE",min:1,max:992
    }

    }
    ,{
    i:"cb8635ff-7925-4218-a974-abef70855871",
f:"url",b:{
    pattern:"gulesider.no",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    A:[],reload:!0,m:15,s:!0,j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],o:["#div-gpt-ad-1639752484121-0"],C:{
    D:{
    

        }
        ,F:{
    

    }
    ,O:{
    

    }

    }
    ,Y:"include",l:[],H:[],G:!0,w:!0
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"2e7e023d-ae04-45c1-ae24-630df1a394f9",filters:[{
    i:"43c97597-b86d-4228-9555-2f992ae84a94",f:"screensize",b:{
    g:"EXCLUDE",name:"DESKTOP",min:993,max:99999
    }

    }
    ,{
    i:"7e37a335-92ad-4a0c-9de9-e20c7f5f8a03",f:"url",
b:{
    pattern:"gulesider.no",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    A:[],reload:!0,m:12,s:!0,j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],o:["#div-gpt-ad-1639752484121-0"],C:{
    D:{
    

        }
        ,F:{
    

    }

    }
    ,Y:"include",l:[],H:[],w:!0,G:!0
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"b0214f03-1c59-49f2-97bb-800518d2ae53",filters:[{
    i:"06d9f711-732d-4b75-a0e6-6dc573baf3fe",f:"screensize",b:{
    g:"EXCLUDE",name:"MOBILE",min:1,max:999
    }

    }
    ,{
    i:"d7090fef-d809-42c3-bd1c-7c8090dafc38",f:"url",b:{
    pattern:"krak.dk",
match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    A:[],reload:!0,m:15,s:!0,j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],o:["#div-gpt-ad-1639041046459-0"],C:{
    D:{
    

        }
        ,F:{
    

    }

    }
    ,Y:"include",l:[],H:[],w:!0,G:!0
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"1f6c9e0f-2441-4c42-89b6-bbe8a8d35e0b",filters:[{
    i:"095bdc37-c32a-4c4f-b648-bd2757b6fe6c",f:"screensize",b:{
    g:"EXCLUDE",name:"DESKTOP",min:999,max:99999
    }

    }
    ,{
    i:"490120d5-4b1a-4011-a7d1-fd61c2060ffc",f:"url",b:{
    pattern:"krak.dk",match:"PARTIAL",
g:"INCLUDE"
    }

    }
],b:{
    A:[],reload:!0,m:12,s:!0,j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],o:["#div-gpt-ad-1639041046459-0"],C:{
    D:{
    

        }
        ,F:{
    

    }

    }
    ,Y:"include",l:[],H:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"306553cc-ee3f-4bcb-9004-f1de82406a89",filters:[{
    i:"fdc11cc6-3f61-4630-b0a7-5c809c35076b",f:"screensize",b:{
    g:"EXCLUDE",name:"DESKTOP",min:999,max:99999
    }

    }
    ,{
    i:"bae7e539-fc8b-4a87-8a19-5440b4a22e33",f:"url",b:{
    pattern:"eniro.se",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    A:[],reload:!0,
m:12,s:!0,j:[{
    type:"SPONSORSHIP",priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],o:["#div-gpt-ad-1639048789799-0"],C:{
    D:{
    

        }
        ,F:{
    

    }

    }
    ,Y:"include",l:[],H:[]
    }
    ,contentType:"signal-licensing",enabled:!0
    }
    ,{
    h:"275726bf-9ffb-4352-be95-2d0835f154d1",filters:[{
    i:"e11addc9-7be0-4bda-950a-b009e7155446",f:"screensize",b:{
    g:"EXCLUDE",name:"MOBILE",min:1,max:998
    }

    }
    ,{
    i:"af189502-546c-453b-a341-6bdf09c7aad3",f:"url",b:{
    pattern:"eniro.se",match:"PARTIAL",g:"INCLUDE"
    }

    }
],b:{
    A:[],reload:!0,m:15,s:!0,j:[{
    type:"SPONSORSHIP",
priority:"ALL"
    }
    ,{
    type:"STANDARD",priority:"ALL"
    }
],o:["#div-gpt-ad-1639048789799-0"],C:{
    D:{
    

        }
        ,F:{
    

    }

    }
    ,Y:"include",l:[],H:[],w:!0,G:!0
    }
    ,contentType:"signal-licensing",enabled:!0
    }
]
    }
],b:{
    

    }

    }
    ,b={
    "signal-segments":ib,"signal-licensing":jb,screensize:kb,url:lb
    }
    ;
    this.L=a;
    ya=xa;
    this.window=C().get();
    this.J=K();
    this.J.Da(a.Ga.aa);
    this.a=new eb(a,b);
    b=a.containerId;
    this.window.__connect=this.window.__connect||{
    

        }
        ;
this.window.__connect.containerIds=this.window.__connect.containerIds||{
    

    }
    ;
this.window.__connect.containerIds[b]||
(a=a.containerId,M(this.J,this.L.containerId),this.window.__connect.containerIds[a]=!0,mb(this)?nb(this):this.start())
    }
    hb.prototype.start=function(){
    this.L.b.Eb||(Fa||(Fa=new Da),Ea({
    aa:this.L.Ga.aa,containerId:this.L.containerId,La:this.L.b.La,Ma:this.L.b.Ma
    }
    ));
    this.a.start()
    }
    ;
    function mb(a){
    var b=a.window;
    return B().rb.some(function(c){
    return!b[c]
    }
    )
    }
    function nb(a){
    var b=a.window.document.createElement("script");
    b.src=B().sb;
    b.onload=function(){
    a.start()
    }
    ;
    a.window.document.head.appendChild(b)
    }
    ;
    function ob(){
    this.window=C().get();
    this.X=new F;
    this.a=Math.floor(Date.now()/1E3)
    }
    function pb(a,b){
    return G(a.X,b).catch(function(){
    return null
    }
    )
    }
    function qb(a,b){
    var c=JSON.parse(a.window.localStorage.getItem(b));
    return!c||a.a>c.ttl?(rb(a,b),null):c.domainData
    }
    function rb(a,b){
    G(a.X,b).then(function(c){
    var d={
    

        }
        ;
a.window.localStorage.setItem(b,JSON.stringify((d.domainData=c,d.ttl=a.a+86400,d)))
    }
    ).catch(function(){
    return Promise.resolve(null)
    }
    )
    }
    ;
    function N(a){
    this.a=a
    }
    N.prototype.get=function(a,b,c){
    return{
    integrationType:this.a,passed:a,source:O,segment:{
    viewability:b||"",engagement:c||""
    }

    }

    }
    ;
    var O=null;
    var sb={
    "0.8":["SVNHV80"],"0.7":"Sovrn_HV1_US Sovrn_HV1 SVNHV70 RTB_HV_70_SOVRN_3 RTB_HV_70_SOVRN_2 Adelphic_Display_70_Sovrn MFSVN70 Sovrn_70_Viewable HV_70".split(" "),"0.6":["SVN_HV_60"],"0.4":["SVN_HV_40"]
    }
    ,tb={
    "0.5":["ENGAGE5_SOVRN"]
    }
    ,ub=["HV_TEST"];
    var vb=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    
function P(a){
    this.h=a;
    this.c={
    

        }
        ;
this.U={
    

    }
    ;
this.window=C().get();
this.J=K();
this.S=this.window.googletag=this.window.googletag||{
    

    }
    ;
this.v=this.window.pbjs=this.window.pbjs||{
    

    }
    ;
this.v.que=this.v.que||[];
this.a=new N("prebid")
    }

P.prototype.start=function(a,b){
    return vb(this,void 0,void 0,function d(){
    var g=this,f,e,k;
    return z(d,function(m){
    if(1==m.a)return f=g,(e=void 0===g.S.cmd.length)&&wb(g),g.U=b,k=g.Va.bind(g,"Set from domain cache"),xb(g,"requestBids",k),xb(g,"bidRequested",g.za.bind(g)),w(m,a,2);
    g.U=m.c;
    g.U&&0<Object.keys(g.U).length&&(O="url");
    xb(g,"requestBids",g.Va.bind(g,"Set URL data"));
    g.v.que.push(function(){
    return f.v.offEvent("requestBids",k)
    }
    );
    m.a=0
    }
    )
    }
    )
    }
    ;
    P.prototype.ya=function(a){
    yb(this,a)
    }
    ;
    
function wb(a){
    a.S.pubads().getSlots().forEach(function(b){
    yb(a,b)
    }
    )
    }
    function yb(a,b){
    var c=b.getSlotElementId();
    b=b.getAdUnitPath();
    a.c[c]=b
    }
    function xb(a,b,c){
    a.v.que.push(function(){
    a.v.onEvent(b,c)
    }
    )
    }

P.prototype.Va=function(){
    var a=this,b=this.U;
    b&&0!==Object.keys(b).length&&this.v.adUnits.forEach(function(c){
    var d=a.ia(c.code),g=b[d];
    c.bids.forEach(function(f){
    if("sovrn"===f.bidder){
    var e="viewability",k="engagement";
    "string"===typeof f.params.segments&&(e="reloadedViewability",k="reloadedEngagement");
    f.params.segments="";
    e=zb(g,e,sb);
    k=zb(g,k,tb);
    if(0<e.length||0<k.length)f.params.segments=ub.concat(e,k).join(", ")
    }

    }
    )
    }
    )
    }
    ;
    
P.prototype.za=function(a){
    a=p(a.bids);
    for(var b=a.next();
    !b.done;
    b=a.next()){
    var c=b.value;
    if("sovrn"===c.bidder){
    a=void 0;
    b=c.params.segments;
    c=this.ia(c.adUnitCode);
    c=null===(a=this.U)||void 0===a?void 0:a[c];
    b&&c?L(this.J,this.h,this.a.get(!0,c.viewability,c.engagement)):L(this.J,this.h,this.a.get(!1));
    break
    }

    }

    }
    ;
    P.prototype.ia=function(a){
    return this.c[a]||a
    }
    ;
    function zb(a,b,c){
    var d=a?a[b]:0;
    return Object.keys(c).reduce(function(g,f){
    d>=f&&(g=g.concat.apply(g,ba(c[f])));
    return g
    }
    ,[])
    }
    ;
    var Ab=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function Q(a){
    this.window=C().get();
    this.S=this.window.googletag=this.window.googletag||{
    

        }
        ;
this.J=K();
this.h=a;
this.a=new N("gam")
    }

Q.prototype.start=function(a,b){
    return Ab(this,void 0,void 0,function d(){
    var g=this,f;
    return z(d,function(e){
    if(1==e.a)return 0<Object.keys(b).length&&(g.U=b),g.za(),w(e,a,2);
    if(f=e.c)g.U=f,O="url";
    Bb(g,g.U);
    Cb(g,g.U);
    e.a=0
    }
    )
    }
    )
    }
    ;
    Q.prototype.ya=function(a){
    this.ma(a,this.U)
    }
    ;
    
Q.prototype.za=function(){
    var a=this;
    this.S.pubads().addEventListener("slotRequested",function(b){
    var c=Db(b.slot);
    c.$&&"NA"!==c.$&&c.ga&&"NA"!==c.ga?(b=Db(b.slot),b=a.a.get(!0,b.$,b.ga),L(a.J,a.h,b)):(b=a.a.get(!1),L(a.J,a.h,b))
    }
    )
    }
    ;
    function Db(a){
    var b=a.getTargeting("sovrn-viewability");
    a=a.getTargeting("sovrn-engagement");
    var c={
    $:null,ga:null
    }
    ;
    0<b.length&&(c.$=b[0]);
    0<a.length&&(c.ga=a[0]);
    return c
    }
    function Bb(a,b){
    a.S.pubads().getSlots().forEach(function(c){
    a.ma(c,b)
    }
    )
    }

Q.prototype.ma=function(a,b){
    var c=a.getAdUnitPath();
    (b=null===b||void 0===b?void 0:b[c])?(a.setTargeting("sovrn-viewability",b.viewability),a.setTargeting("sovrn-engagement",b.engagement),this.log("Targeting Set",c,"sovrn-engagement",b.engagement),this.log("Targeting Set",c,"sovrn-engagement",b.engagement)):(a.setTargeting("sovrn-viewability","NA"),a.setTargeting("sovrn-engagement","NA"))
    }
    ;
    
function Cb(a,b){
    a.S.pubads().addEventListener("impressionViewable",function(c){
    c=c.slot;
    var d=null===b||void 0===b?void 0:b[c.getAdUnitPath()],g=c.getAdUnitPath();
    d&&"0.0"!==d.reloadedViewability&&(c.setTargeting("sovrn-viewability",d.reloadedViewability),a.log("Reload Targeting Set",g,"sovrn-viewability",d.viewability));
    d&&"0.0"!==d.reloadedEngagement&&(c.setTargeting("sovrn-engagement",d.reloadedEngagement),a.log("Reload Targeting Set",g,"sovrn-engagement",d.engagement))
    }
    )
    }
    Q.prototype.log=function(){
    

        }
        ;
var Eb=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function Fb(a){
    this.h=a;
    this.window=C().get();
    this.window.properSpecialOps=this.window.properSpecialOps||{
    

        }
        ;
this.a=new N("sms");
this.J=K()
    }

Fb.prototype.start=function(a,b){
    return Eb(this,void 0,void 0,function d(){
    var g=this,f;
    return z(d,function(e){
    if(1==e.a)return Gb(g,b),w(e,a,2);
    f=e.c;
    Gb(g,f);
    e.a=0
    }
    )
    }
    )
    }
    ;
    function Hb(a,b){
    if(!a||1>Object.values(a).length)return"";
    a=Object.values(a);
    var c=0;
    a.forEach(function(d){
    c+=parseFloat(d[b])
    }
    );
    return(c/a.length).toString().slice(0,3)
    }
    function Ib(a,b){
    return Object.keys(b).reduce(function(c,d){
    a>=d&&(c=c.concat.apply(c,ba(b[d])));
    return c
    }
    ,[])
    }

function Gb(a,b){
    var c=Hb(b,"viewability");
    b=Hb(b,"engagement");
    var d=Ib(c,sb),g=Ib(b,tb);
    d=d.concat(g);
    a.window.properSpecialOps.signal_deal_id=ub.concat(d).join(",");
    g=!1;
    0<d.length&&(g=!0);
    c=a.a.get(g,c,b);
    L(a.J,a.h,c)
    }
    ;
    function Jb(a,b){
    var c=[];
    a.forEach(function(d){
    Kb[d]&&(d=new Kb[d](b),c.push(d))
    }
    );
    return c
    }
    var Kb={
    prebid:P,gam:Q,sms:Fb
    }
    ;
    var Lb=this&&this.c||function(a,b,c,d){
    var g=arguments.length,f=3>g?b:null===d?d=Object.getOwnPropertyDescriptor(b,c):d,e;
    if("object"===typeof Reflect&&"function"===typeof Reflect.oa)f=Reflect.oa(a,b,c,d);
    else for(var k=a.length-1;
        0<=k;
        k--)if(e=a[k])f=(3>g?e(f):3<g?e(b,c,f):e(b,c))||f;
    return 3<g&&f&&Object.defineProperty(b,c,f),f
    }
    ,Mb=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }

function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function Nb(a,b){
    this.b=a;
    this.h=b;
    this.window=C().get();
    this.M=B();
    this.Ja=new ob
    }

Nb.prototype.ha=function(){
    Mb(this,void 0,void 0,function b(){
    var c=this,d,g,f,e,k,m,l;
    return z(b,function(h){
    d=c;
    g=""+c.M.vb+Ob(c)+"/"+c.window.location.host;
    f=encodeURIComponent(c.window.location.pathname.slice(0,100));
    e=g+"/"+f;
    k=pb(c.Ja,e);
    (m=qb(c.Ja,g))&&(O="domain");
    c.Wa=Jb(c.b.wb,c.h);
    c.S=c.window.googletag=c.window.googletag||{
    

        }
        ;
c.S.cmd=c.S.cmd||[];
l=c.S.cmd.unshift?"unshift":"push";
c.S.cmd[l](function(){
    d.Ka||(d.Ka=d.window.googletag.defineSlot,d.window.googletag.defineSlot=d.bb.bind(d));
    
d.Wa.forEach(function(n){
    n.start(k,m||{
    

        }
        )
    }
    )
    }
    );
h.a=0
    }
    )
    }
    )
    }
    ;
Nb.prototype.bb=function(a,b,c){
    var d=this.Ka(a,b,c);
    try{
    this.Wa.forEach(function(g){
    g.ya&&g.ya(d)
    }
    )
    }
    catch(g){
    

        }
        return d
    }
    ;
function Ob(a){
    a=a.window.innerWidth;
    return 992<=a?"desktop":768<=a?"tablet":"mobile"
    }
    var Pb=Nb,ib=Pb=Lb([function(a){
    function b(){
    var c=a.apply(this,arguments)||this;
    c.Na=!0;
    return c
    }
    u(b,a);
    return b
    }
],Pb);
    var R=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function S(){
    this.window=C().get();
    this.X=new F;
    this.tb=5E3;
    this.Ua=200;
    this.cb=2E3;
    this.pa=B().pa;
    this.va=B().va
    }
    var T;
    
S.prototype.ka=function(a,b){
    return R(this,void 0,void 0,function d(){
    var g=this,f,e,k,m;
    return z(d,function(l){
    switch(l.a){
    case 1:a:if(T)var h=T;
    else{
    h=a.getAdUnitPath().split("/");
    for(var n=0;
        n<h.length;
        n++){
    var q=h[n];
    -1<q.indexOf(",")&&(q=q.split(",")[0]);
    if(q=Number(q)){
    h=T=q;
    break a
    }

    }
    h=0
    }
    h?(h=b.H||[],n=b.j||[],q=b.w||!1,h=!!((b.l||[]).length||h.length||n.length||q)):h=!1;
    return(f=h)?w(l,Qb(g,a),2):l.return(!1);
    case 2:e=l.c;
    k=e.lineItemId||e.sourceAgnosticLineItemId;
    if((null===(h=b.H)||void 0===
h?0:h.length)?-1===b.H.indexOf(String(e.campaignId)):-1<(b.l||[]).indexOf(String(e.campaignId)))return l.return(!0);
if(!k){
    a:{
    h=b.j||[];
    for(n=0;
        n<h.length;
        n++)if("AD_EXCHANGE"===h[n].type||"ADSENSE"===h[n].type){
    h=!0;
    break a
    }
    h=!1
    }
    return l.return(h)
    }
    l.W=3;
    return w(l,Rb(g,k),5);
    case 5:return m=l.c,l.return(Sb(m,b));
    case 3:return l.W=0,l.B=null,l.return(!0)
    }

    }
    )
    }
    )
    }
    ;
        
function Qb(a,b,c){
    c=void 0===c?0:c;
    return R(a,void 0,void 0,function g(){
    var f=this,e;
    return z(g,function(k){
    if(1==k.a){
    if(c>=f.tb/f.Ua)return k.return({
    

        }
        );
(e=b.getResponseInformation())?(k.a=2,k=void 0):k=w(k,f.wait(f.Ua),3);
return k
    }
    return 2!=k.a?k.return(Qb(f,b,++c)):k.return(e)
    }
    )
    }
    )
    }

function Rb(a,b){
    return R(a,void 0,void 0,function d(){
    var g=this,f,e;
    return z(d,function(k){
    switch(k.a){
    case 1:try{
    var m=JSON.parse(g.window.localStorage.getItem("connect-"+b));
    var l=m.expiresAt>Date.now()?m.lineItemInfo:!1
    }
    catch(h){
    l=!1
    }
    if(f=l)return k.return(f);
    if(!U[b]){
    k.a=2;
    break
    }
    return w(k,g.wait(200),3);
    case 3:return w(k,Rb(g,b),4);
    case 4:return k.return(k.c);
    case 2:return U[b]=!0,w(k,Tb(g,b),5);
    case 5:return e=k.c,g.Ea(b,e),U[b]=!1,k.return(e)
    }

    }
    )
    }
    )
    }

S.prototype.Ea=function(a,b){
    b={
    lineItemInfo:b,expiresAt:Date.now()+1E3*this.va
    }
    ;
    try{
    this.window.localStorage.setItem("connect-"+a,JSON.stringify(b))
    }
    catch(c){
    

        }

    }
    ;

function Tb(a,b){
    return R(a,void 0,void 0,function d(){
    var g=this,f,e;
    return z(d,function(k){
    switch(k.a){
    case 1:return f=g.pa+"/"+T+"/"+b,w(k,G(g.X,f),2);
    case 2:e=k.c;
    if("PENDING"!==e.state){
    k.a=3;
    break
    }
    return w(k,g.wait(g.cb),4);
    case 4:return k.return(Tb(g,b));
    case 3:if("READY"===e.state)return k.return(e);
    U[b]=!1;
    throw Error("Dfp gateway response: "+e.state);

    }

    }
    )
    }
    )
    }

function Sb(a,b){
    var c;
    if(!(c=b.H.length?-1===b.H.indexOf(a.orderId):-1<(b.l||[]).indexOf(a.orderId)))a:{
    c=["ALL","all"];
    for(var d=p(b.j||[]),g=d.next();
    !g.done;
    g=d.next()){
    var f=g.value;
    g=a.lineItemType===f.type;
    var e=c.includes(f.priority);
    f=a.priority===Number(f.priority);
    if(g&&(e||f)){
    c=!0;
    break a
    }

    }
    c=!1
    }
    return c||(b.w?"CREATIVE_SET"===a.roadblockingType:!1)
    }

S.prototype.wait=function(a){
    return R(this,void 0,void 0,function c(){
    return z(c,function(d){
    return d.return(new Promise(function(g){
    return setTimeout(g,a)
    }
    ))
    }
    )
    }
    )
    }
    ;
    var U={
    

        }
        ;
function Ub(a,b){
    var c=a.Qb||10;
    return Vb(a).some(function(d){
    var g=Math.abs(b.height-d.height)<c;
    return Math.abs(b.width-d.width)<c&&g
    }
    )
    }
    function Wb(a){
    return Vb(a).reduce(function(b,c){
    return b.width*b.height<c.width*c.height?c:b
    }
    ,{
    width:0,height:0
    }
    )
    }
    function Xb(a){
    return(a=Yb(a,"iframe")||Yb(a,"img"))?a.getBoundingClientRect():{
    width:0,height:0
    }

    }

function Yb(a,b){
    a=p(a.getElementsByTagName(b));
    for(b=a.next();
    !b.done;
    b=a.next()){
    b=b.value;
    var c=b.getBoundingClientRect();
    if(c.width&&c.height)return b
    }

    }
    function Vb(a){
    return a.sizes?a.sizes.map(function(b){
    b=b.split("x");
    return{
    width:Number(b[0]),height:Number(b[1])
    }

    }
    ):[{
    height:a.height,width:a.width
    }
]
    }
    ;
    var Zb=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function V(){
    this.window=C().get();
    this.xb=new S;
    this.window.googletag=this.window.googletag||{
    

        }
        ;
this.window.googletag.cmd=this.window.googletag.cmd||[]
    }

V.prototype.a=function(a,b){
    var c=this;
    if(!$b(this))return this.window.setTimeout(this.a.bind(this,a,b),500),null;
    if(a.K)return ac(this,"impressionViewable",b);
    bc(this).forEach(function(d){
    d=cc(d);
    dc(c,d)&&b(d)
    }
    );
    ac(this,"slotRenderEnded",b)
    }
    ;
    V.prototype.ka=function(a,b){
    return Zb(this,void 0,void 0,function d(){
    var g=this,f;
    return z(d,function(e){
    if(1==e.a)return $b(g)?(e.a=2,e=void 0):e=w(e,g.wait(200),3),e;
    if(2!=e.a)return e.return(g.ka(a,b));
    f=ec(g,a);
    return e.return(g.xb.ka(f,b))
    }
    )
    }
    )
    }
    ;
    
function ec(a,b){
    return bc(a).filter(function(c){
    return b===cc(c)
    }
    )[0]
    }
    function ac(a,b,c){
    a.window.googletag.cmd.push(function(){
    a.window.googletag.pubads().addEventListener(b,function(d){
    d=cc(d.slot);
    dc(a,d)&&c(d)
    }
    )
    }
    )
    }
    function $b(a){
    a=a.window.googletag;
    return!!a&&a.pubadsReady
    }
    function dc(a,b){
    a=a.window.document.querySelector("#"+b);
    if(!a)return!1;
    a=Xb(a);
    return 50<=a.width&&50<=a.height
    }
    function bc(a){
    return a.window.googletag.pubads().getSlots()
    }

function cc(a){
    a=a.getSlotElementId();
    !isNaN(Number(parseInt(a.charAt(0))))&&(a="\\3"+a.charAt(0)+" "+a.slice(1));
    return a.replace(/\//g,"\\/").replace(/\./g,"\\.").replace(/,/g,"\\,")
    }
    V.prototype.wait=function(a){
    return Zb(this,void 0,void 0,function c(){
    return z(c,function(d){
    return d.return(new Promise(function(g){
    return setTimeout(g,a)
    }
    ))
    }
    )
    }
    )
    }
    ;
    function fc(){
    this.window=C().get()
    }
    function gc(a,b,c){
    c=void 0===c?.5:c;
    if(a.window.Xa&&"SAFEFRAME"===a.window.Xa.state)return a.window.Ha.ext.Jb()/100>=c;
    b=b.getBoundingClientRect();
    var d=a.window.innerWidth;
    a=a.window.innerHeight;
    return(Math.max(0,Math.min(b.right,d))-Math.max(0,Math.min(b.left,d)))*(Math.max(0,Math.min(b.bottom,a))-Math.max(0,Math.min(b.top,a)))/(b.width*b.height)>=c
    }
    ;
    function hc(){
    this.window=C().get();
    this.$=new fc;
    this.a=Pa();
    this.da={
    

        }
        ;
ic(this)
    }
    var jc;
hc.prototype.Fa=function(a,b,c,d){
    var g=a.id;
    this.da[g+c]||(this.da[g+c]={
    h:c,element:a,Ta:b,qa:0,Ba:0,Sa:0,pb:d
    }
    )
    }
    ;
    
function ic(a){
    a.window.setInterval(function(){
    for(var b=p(Object.keys(a.da)),c=b.next();
    !c.done;
    c=b.next()){
    c=a.da[c.value];
    var d;
    if(!(d=!c.ca)){
    a:{
    for(d=c.ca;
        d.parentNode;
        )if(d=d.parentNode,d===c.element){
    d=!0;
    break a
    }
    d=!1
    }
    d=!d
    }
    d&&(d=kc(c.element,"iframe"),c.ca=d||kc(c.element,"img"));
    var g=c.ca?c.ca:c.element;
    c.Ba++;
    d=gc(a.$,g,c.Ta.Z);
    a.a.N()&&d&&c.qa++;
    d=c.Ta;
    g=gc(a.$,g,d.Z);
    var f=c.qa>=d.m,e=c.Ba>=d.xa;
    d=c.Sa>=d.la;
    g&&f&&!d&&e&&(c.pb(c.element),c.Sa++,c.qa=0,c.Ba=0,c.ca=null)
    }

    }
    ,1E3)
    }

function kc(a,b){
    a=a.getElementsByTagName(b);
    for(b=0;
        b<a.length;
        b++){
    var c=a[b].getBoundingClientRect();
    if(c.width&&c.height)return a[b]
    }

    }
    ;
    var lc=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function W(a){
    this.b=a;
    jc||(jc=new hc);
    this.Ra=jc;
    this.Pa=new V;
    this.window=C().get();
    a.o=a.o||[];
    a.j=a.j||[];
    a.H=a.H||[];
    a.l=a.l||[];
    a.Z=a.Z||.5
    }

W.prototype.start=function(a){
    var b=this;
    mc(this,function(c,d){
    if(!b.b.s)return nc(b,c,a);
    oc(b,c,d,a)
    }
    )
    }
    ;
    function mc(a,b){
    if(a.b.s)a.Pa.a({
    K:a.b.K
    }
    ,function(d){
    b("#"+d,d)
    }
    );
    else{
    a=p(a.b.A);
    for(var c=a.next();
    !c.done;
    c=a.next())b(c.value)
    }

    }

function oc(a,b,c,d){
    lc(a,void 0,void 0,function f(){
    var e=this,k,m;
    return z(f,function(l){
    if(1==l.a){
    a:{
    var h=p(e.b.o);
    for(var n=h.next();
    !n.done;
    n=h.next()){
    if((n=e.querySelector(e.window.document,n.value))&&n.id===c){
    h=!0;
    break a
    }
    if(e.querySelector(n,"#"+c)){
    h=!0;
    break a
    }

    }
    h=!1
    }
    h||((h=e.querySelector(e.window.document,b))?(h=Xb(h),h=!e.b.sizes&&-1!==(e.b.P||[]).indexOf(h.width+"x"+h.height)||e.b.sizes&&!Ub(e.b,h)?!0:!1):h=!0);
    if(h)return l.return();
    k=nc(e,b,d);
    return w(l,pc(e,c),2)
    }
    (m=l.c)||delete e.Ra.da[k.id+
e.b.h];
l.a=0
    }
    )
    }
    )
    }
    function nc(a,b,c){
    var d=a.querySelector(a.window.document,b),g={
    Z:a.b.Z,m:a.b.m,la:a.b.la,xa:B().xa
    }
    ;
    if(d)return a.Ra.Fa(d,g,a.b.h,a.a.bind(a,c,b)),d
    }
    function pc(a,b){
    return lc(a,void 0,void 0,function d(){
    var g=this;
    return z(d,function(f){
    return 1==f.a?qc(g)?w(f,g.Pa.ka(b,g.b),2):f.return(!0):f.return(!f.c)
    }
    )
    }
    )
    }

W.prototype.a=function(a,b,c){
    return lc(this,void 0,void 0,function g(){
    var f=this,e;
    return z(g,function(k){
    if(1==k.a)return w(k,a(f.b.h,b,c),2);
    if(e=k.c){
    var m=f.querySelector(c,"iframe"),l=Wb(f.b),h=l.width;
    l=l.height;
    m.style.width=e.width+"px";
    m.style.height=e.height+"px";
    m.style.marginTop=(l-e.height)/2+"px";
    m.style.marginLeft=(h-e.width)/2+"px"
    }
    k.a=0
    }
    )
    }
    )
    }
    ;
    function qc(a){
    return[0<a.b.j.length,0<a.b.l.length,0<a.b.H.length,!!a.b.w].some(function(b){
    return!!b
    }
    )
    }

W.prototype.querySelector=function(a,b){
    if(!a)return null;
    try{
    return a.querySelector(b)
    }
    catch(c){
    return null
    }

    }
    ;
    var rc=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function X(){
    this.X=new F;
    this.M=B();
    this.window=C().get();
    this.Aa={
    

        }
        ;
this.na={
    

    }
    ;
this.ta=this.M.ta||[];
sc(this)
    }
    var tc;
function uc(){
    tc||(tc=new X);
    return tc
    }

X.prototype.reload=function(a,b,c){
    return rc(this,void 0,void 0,function g(){
    var f=this,e;
    return z(g,function(k){
    if((e=Y(f,vc(a)))&&c){
    var m=c.G,l=c.R,h=e.getSlotElementId();
    m&&(f.na[h]=f.na[h]||0,f.na[h]++,e.setTargeting("sovrn-signal",f.na[h]));
    l&&wc(e,l);
    wc(e,{
    "sovrn-reload":["true"]
    }
    );
    if(!f.Aa[h]){
    m=f.Aa;
    var n=c.R;
    l=[];
    c.G&&l.push("sovrn-signal");
    n&&(n=Object.keys(n),l=l.concat(n));
    m[h]=l
    }

    }
    f.window.googletag.pubads().refresh([e]);
    k.a=0
    }
    )
    }
    )
    }
    ;
    
X.prototype.ia=function(a){
    return(a=Y(this,a))?a.getAdUnitPath():""
    }
    ;
    X.prototype.qb=function(a){
    var b=a.slot;
    a=b.getSlotElementId();
    (a=this.Aa[a])&&a.forEach(function(c){
    "sovrn-reload"!==c&&b.clearTargeting(c)
    }
    )
    }
    ;
    function vc(a){
    "\\3"===a.substr(0,2)&&(a=a.substr(2),a=a.charAt(0)+a.substr(2));
    return a.replace(/\\\//g,"/").replace(/\\\./g,".").replace(/\\,/g,",")
    }

function xc(a,b){
    var c=Y(a,b);
    c&&c.getTargetingKeys&&c.clearTargeting&&c.getTargetingKeys().forEach(function(d){
    a.ta.forEach(function(g){
    -1<d.indexOf(g)&&c.clearTargeting(d)
    }
    )
    }
    )
    }
    function Y(a,b){
    a=a.window.googletag.pubads().getSlots();
    for(var c=0;
        c<a.length;
        c++)if(b===a[c].getSlotElementId())return a[c]
        }

function sc(a){
    rc(a,void 0,void 0,function c(){
    var d=this,g;
    return z(c,function(f){
    if(1==f.a)return(g=d.window.googletag)&&g.pubadsReady?f.return(g.pubads().addEventListener("slotRenderEnded",d.qb.bind(d))):w(f,d.wait(1E3),2);
    sc(d);
    f.a=0
    }
    )
    }
    )
    }
    function wc(a,b){
    Object.keys(b).forEach(function(c){
    a.setTargeting(c,b[c])
    }
    )
    }
    X.prototype.wait=function(a){
    return rc(this,void 0,void 0,function c(){
    return z(c,function(d){
    return d.return(new Promise(function(g){
    return setTimeout(g,a)
    }
    ))
    }
    )
    }
    )
    }
    ;
    var yc=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function Z(a){
    this.b=a;
    this.name="Prebid";
    this.window=C().get();
    zc(this)
    }
    Z.prototype.ua=function(){
    return!!this.v&&"function"===typeof this.v.requestBids&&"function"===typeof this.v.setTargetingForGPTAsync
    }
    ;
    
Z.prototype.Ca=function(a,b){
    return yc(this,void 0,void 0,function d(){
    var g=this,f;
    return z(d,function(e){
    f=g;
    return e.return(new Promise(function(k){
    var m,l=Ac(f,a,b);
    if(!l)return k();
    f.v.requestBids({
    adUnits:[l],bidsBackHandler:function(){
    f.ma(l.code);
    k()
    }

    }
    );
    var h=(null===(m=f.v.getConfig())||void 0===m?void 0:m.bidderTimeout)||1E3;
    setTimeout(k,h)
    }
    ))
    }
    )
    }
    )
    }
    ;
    
function zc(a,b){
    b=void 0===b?0:b;
    var c=a.window.pbjs;
    if(c&&"function"===typeof c.requestBids)a.v=c;
    else{
    if(5<=b)return null;
    setTimeout(function(){
    return zc(a,++b)
    }
    ,1E3)
    }

    }
    function Ac(a,b,c){
    a=a.v.adUnits;
    if(!a||1>a.length)return null;
    for(var d=0;
        d<a.length;
        d++)if(a[d].code===b||a[d].code===c){
    b=a[d];
    c=b.bids;
    for(a=0;
        a<c.length;
        a++)"sovrn"===c[a].bidder&&(c[a].params.iv="reload");
    return b
    }

    }
    Z.prototype.ma=function(a){
    this.v.setTargetingForGPTAsync([a])
    }
    ;
    var Bc=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function Cc(a){
    this.b=a;
    this.name="Rubicon";
    this.window=C().get();
    this.sa=uc();
    Dc(this)
    }
    Cc.prototype.ua=function(){
    return!!this.v&&"function"===typeof this.v.rp.requestBids
    }
    ;
    
Cc.prototype.Ca=function(a){
    return Bc(this,void 0,void 0,function c(){
    var d=this,g;
    return z(c,function(f){
    g=d;
    return f.return(new Promise(function(e){
    var k=Y(g.sa,a),m=g.v.getConfig(["bidderTimeout"])||1E3;
    if(!k)return e();
    g.v.rp.requestBids({
    callback:e,gptSlotObjects:[k]
    }
    );
    setTimeout(e,m)
    }
    ))
    }
    )
    }
    )
    }
    ;
    
function Dc(a,b){
    b=void 0===b?0:b;
    var c,d=a.window.pbjs;
    if(d&&"function"===typeof(null===(c=d.rp)||void 0===c?void 0:c.requestBids))a.v=d;
    else{
    if(5<=b)return null;
    setTimeout(function(){
    return Dc(a,++b)
    }
    ,1E3)
    }

    }
    ;
    function Ec(a){
    this.b=a;
    this.name="TAM";
    this.window=C().get();
    this.sa=uc()
    }
    Ec.prototype.ua=function(){
    this.a||(this.a=this.window.apstag);
    return this.a&&"function"===typeof this.a.fetchBids&&"function"===typeof this.a.setDisplayBids
    }
    ;
    Ec.prototype.Ca=function(a,b){
    var c=this;
    return new Promise(function(d){
    var g={
    slots:[{
    slotID:a,slotName:b,sizes:Fc(c,a)
    }
],timeout:c.b.timeout||1E3
    }
    ;
    c.a.fetchBids(g,function(){
    c.a.setDisplayBids();
    d()
    }
    )
    }
    )
    }
    ;
    
function Fc(a,b){
    var c=Y(a.sa,b);
    return c.getSizes?c.getSizes().map(function(d){
    return Object.values(d)
    }
    ):(a=a.window.document.querySelector("#"+b))?(a=Xb(a),Object.values(a)):[]
    }
    ;
    function Gc(a){
    a=void 0===a?{
    

        }
        :a;
var b=[];
Object.keys(a).forEach(function(c){
    Hc[c]&&(c=new Hc[c](a[c]),b.push(c))
    }
    );
    return b
    }
    var Hc={
    D:Z,O:Cc,F:Ec
    }
    ;
    var Ic=this&&this.c||function(a,b,c,d){
    var g=arguments.length,f=3>g?b:null===d?d=Object.getOwnPropertyDescriptor(b,c):d,e;
    if("object"===typeof Reflect&&"function"===typeof Reflect.oa)f=Reflect.oa(a,b,c,d);
    else for(var k=a.length-1;
        0<=k;
        k--)if(e=a[k])f=(3>g?e(f):3<g?e(b,c,f):e(b,c))||f;
    return 3<g&&f&&Object.defineProperty(b,c,f),f
    }
    ,Jc=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }

function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function Kc(a,b){
    this.b=a;
    this.h=b;
    a={
    h:b,s:a.s,A:a.A,m:a.m,la:a.la,Z:a.Z,K:a.K,j:a.j,H:a.H,l:a.l,w:a.w,o:a.o,P:a.P
    }
    ;
    this.window=C().get();
    this.c=new W(a);
    this.J=K()
    }
    Kc.prototype.ha=function(){
    this.lb=Gc(this.b.C);
    this.ra=uc();
    this.c.start(this.a.bind(this))
    }
    ;
    
Kc.prototype.a=function(a,b){
    return Jc(this,void 0,void 0,function d(){
    var g=this,f,e,k,m,l,h,n;
    return z(d,function(q){
    if(1==q.a){
    f=vc(b.substring(1));
    e=g.ra.ia(f);
    k=[];
    xc(g.ra,f);
    L(g.J,a);
    m=p(g.lb);
    for(l=m.next();
    !l.done;
    l=m.next())h=l.value,h.ua()&&(n=h.Ca(f,e),k.push(n));
    return w(q,Promise.allSettled(k),2)
    }
    g.ra.reload(f,a,g.b);
    q.a=0
    }
    )
    }
    )
    }
    ;
    var Lc=Kc,jb=Lc=Ic([function(a){
    function b(){
    var c=a.apply(this,arguments)||this;
    c.Na=!1;
    return c
    }
    u(b,a);
    return b
    }
],Lc);
    var Mc=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ;
    function kb(a){
    this.max=a.max;
    this.min=a.min;
    this.window=C().get()
    }

kb.prototype.Qa=function(){
    return Mc(this,void 0,void 0,function b(){
    var c=this,d;
    return z(b,function(g){
    d=c.window.innerWidth;
    return g.return(d<=c.max&&d>=c.min)
    }
    )
    }
    )
    }
    ;
    var Nc=this&&this.a||function(a,b,c,d){
    function g(f){
    return f instanceof c?f:new c(function(e){
    e(f)
    }
    )
    }
    return new (c||(c=Promise))(function(f,e){
    function k(h){
    try{
    l(d.next(h))
    }
    catch(n){
    e(n)
    }

    }
    function m(h){
    try{
    l(d["throw"](h))
    }
    catch(n){
    e(n)
    }

    }
    function l(h){
    h.done?f(h.value):g(h.value).then(k,m)
    }
    l((d=d.apply(a,b||[])).next())
    }
    )
    }
    ,Oc,Pc=Oc||(Oc={
    

        }
        );
Pc.EXACT="EXACT";
Pc.PARTIAL="PARTIAL";
function lb(a){
    this.window=C().get();
    this.pattern=a.pattern.toLowerCase();
    this.match=a.match
    }

lb.prototype.Qa=function(){
    return Nc(this,void 0,void 0,function b(){
    var c=this;
    return z(b,function(d){
    return d.return(c.match===Oc.zb?Qc(c)===c.pattern:-1<Qc(c).indexOf(c.pattern))
    }
    )
    }
    )
    }
    ;
    function Qc(a){
    a=a.window.location;
    return(a.origin+a.pathname).toLowerCase()
    }
    ;
    new hb;

    }
    ).call({
    

    }
    )
