<!DOCTYPE html>
<html class="no" lang="no">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport"/>       
  <meta content="wSbVnOyV7IMQp3j7e_R4t4WFVvfDlZC5S0ALb9ISpRQ" name="google-site-verification"/>
  <meta content="5A16DE54E81BB9F830B0878110CF2F8E" name="msvalidate.01"/>
  <meta content="yes" name="mobile-web-app-capable"/>
  <meta content="unsafe-url" name="referrer"/>
  <meta content="on" http-equiv="x-dns-prefetch-control"/>
  <meta content="python-requests/2.28.1" name="renderer"/>
  <meta content="1656699580790" name="rendering_time"/>
  <meta content="false" name="isBot"/>
  <meta content="false" name="isGoogleBot"/>
  <meta content="no" name="useJS"/>
  <meta content="unknown" name="resolution"/>
  <link crossorigin="" href="https://fonts.googleapis.com/" rel="preconnect"/>
  <link crossorigin="" href="https://www.google-analytics.com/" rel="preconnect"/>
  <link crossorigin="" href="https://static.eniro.com" rel="preconnect"/>
  <link crossorigin="" href="https://julio-cdn.eniro.com" rel="preconnect"/>
  <link crossorigin="" href="https://pixel-profile-cloud.eniro.com/" rel="preconnect"/>        
  <link crossorigin="" href="https://static1.eniro.com/" rel="preconnect"/>
  <link crossorigin="" href="https://static5.eniro.com/" rel="preconnect"/>
  <link crossorigin="" href="https://images.eniro.com/" rel="preconnect"/>
  <link crossorigin="" href="https://map01.eniro.no/" rel="preconnect"/>
  <link crossorigin="" href="https://map02.eniro.no/" rel="preconnect"/>
  <link crossorigin="" href="https://map03.eniro.no/" rel="preconnect"/>
  <link crossorigin="" href="https://map04.eniro.no/" rel="preconnect"/>
  <link crossorigin="" href="https://firehose.eu-west-1.amazonaws.com/" rel="preconnect"/>     
  <link crossorigin="" href="https://attributionservice.enirocdn.com/" rel="preconnect"/>
  <link crossorigin="" href="https://tileversion.eniro.com/" rel="preconnect"/>
  <link crossorigin="" href="https://s1.adform.net/" rel="preconnect"/>
  <link crossorigin="" href="https://adx.adform.net/" rel="preconnect"/>
  <link crossorigin="" href="https://track.adform.net/" rel="preconnect"/>
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,500&amp;display=swap" rel="stylesheet"/>
  <link href="https://static.eniro.com/font/eniro-icon/v61.1/eniro-icon.css" rel="stylesheet" type="text/css"/>
  <link href="https://static.eniro.com/font/eniro-icon-commercial/v16.1/eniro-icon-commercial.css" rel="stylesheet" type="text/css"/>
  <!-- Start Additional Helmet -->
  <link data-rh="true" href="//static5.eniro.com/no/img/favicon/favicon.ico?v=20190619" rel="shortcut icon">
   <link data-rh="true" href="https://www.gulesider.no" rel="canonical">
    <title data-rh="true">
     Gulesider.no - Oppdag nærheten.
    </title>
    <meta content="Finn telefonnummer og adresse til firmaer og personer. Søk etter tjenester, produkter, kontaktinformasjon, kart og veibeskrivelser og gatebilder." data-rh="true" name="description"/>
    <meta content="#ffe000" data-rh="true" name="theme-color"/>
    <!-- End Additional Helmet -->
    <!-- Quantcast Choice. Consent Manager Tag v2.0 (for TCF 2.0) -->
    <script async="true" type="text/javascript">
     (function() {
                                        var hostName = window.location.hostname
                                        var host = hostName.substring(hostName.lastIndexOf('.', hostName.lastIndexOf('.') - 1) + 1)
                                        var element = document.createElement('script')
                                        var firstScript = document.getElementsByTagName('script')[0]
                                        var url = 'https://quantcast.mgr.consensu.org'
                                                .concat('/choice/', 'M3utcP_nzMhcr', '/', host, '/choice.js')
                                        var uspTries = 0
                                        var uspTriesLimit = 3
                                        element.async = true
                                        element.type = 'text/javascript'
                                        element.src = url

                                        firstScript.parentNode.insertBefore(element, firstScript)

                                        function makeStub() {
                                                var TCF_LOCATOR_NAME = '__tcfapiLocator'
                                                var queue = []
                                                var win = window
                                                var cmpFrame

                                                function addFrame() {
                                                        var doc = win.document
                                                        var otherCMP = !!(win.frames[TCF_LOCATOR_NAME])

                                                        if (!otherCMP) {
                                                                if (doc.body) {
                                                                        var iframe = doc.createElement('iframe')

                                                                        iframe.style.cssText = 'display:none'
                                                                        iframe.name = TCF_LOCATOR_NAME
                                                                        doc.body.appendChild(iframe)
                                                                } else {
                                                                        setTimeout(addFrame, 5)
                                                                }
                                                        }
                                                        return !otherCMP
                                                }

                                                function tcfAPIHandler() {
                                                        var gdprApplies
                                                        var args = arguments

                                                        if (!args.length) {
                                                                return queue
                                                        } else if (args[0] === 'setGdprApplies') {
                                                                if (
                                                                        args.length > 3 &&
                                                                        args[2] === 2 &&
                                                                        typeof args[3] === 'boolean'
                                                                ) {
                                                                        gdprApplies = args[3]
                                                                        if (typeof args[2] === 'function') {
                                                                                args[2]('set', true)
                                                                        }
                                                                }
                                                        } else if (args[0] === 'ping') {
                                                                var retr = {
                                                                        gdprApplies: gdprApplies,
                                                                        cmpLoaded: false,
                                                                        cmpStatus: 'stub'
                                                                }

                                                                if (typeof args[2] === 'function') {
                                                                        args[2](retr)
                                                                }
                                                        } else {
                                                                queue.push(args)
                                                        }
                                                }

                                                function postMessageEventHandler(event) {
                                                        var msgIsString = typeof event.data === 'string'
                                                        var json = {}

                                                        try {
                                                                if (msgIsString) {
                                                                        json = JSON.parse(event.data)
                                                                } else {
                                                                        json = event.data
                                                                }
                                                        } catch (ignore) {
                                                        }

                                                        var payload = json.__tcfapiCall

                                                        if (payload) {
                                                                window.__tcfapi(
                                                                        payload.command,
                                                                        payload.version,
                                                                        function(retValue, success) {
                                                                                var returnMsg = {
                                                                                        __tcfapiReturn: {
                                                                                                returnValue: retValue,
                                                                                                success: success,
                                                                                                callId: payload.callId
                                                                                        }
                                                                                }
                                                                                if (msgIsString) {
                                                                                        returnMsg = JSON.stringify(returnMsg)
                                                                                }
                                                                                event.source.postMessage(returnMsg, '*')
                                                                        },
                                                                        payload.parameter
                                                                )
                                                        }
                                                }

                                                while (win) {
                                                        try {
                                                                if (win.frames[TCF_LOCATOR_NAME]) {
                                                                        cmpFrame = win
                                                                        break
                                                                }
                                                        } catch (ignore) {
                                                        }

                                                        if (win === window.top) {
                                                                break
                                                        }
                                                        win = win.parent
                                                }
                                                if (!cmpFrame) {
                                                        addFrame()
                                                        win.__tcfapi = tcfAPIHandler
                                                        win.addEventListener('message', postMessageEventHandler, false)
                                                }
                                        }

                                        makeStub()

                                        var uspStubFunction = function() {
                                                var arg = arguments
                                                if (typeof window.__uspapi !== uspStubFunction) {
                                                        setTimeout(function() {
                                                                if (typeof window.__uspapi !== 'undefined') {
                                                                        window.__uspapi.apply(window.__uspapi, arg)
                                                                }
                                                        }, 500)
                                                }
                                        }

                                        var checkIfUspIsReady = function() {
                                                uspTries++
                                                if (window.__uspapi === uspStubFunction && uspTries < uspTriesLimit) {
                                                        console.warn('USP is not accessible')
                                                } else {
                                                        clearInterval(uspInterval)
                                                }
                                        }

                                        if (typeof window.__uspapi === 'undefined') {
                                                window.__uspapi = uspStubFunction
                                                var uspInterval = setInterval(checkIfUspIsReady, 6000)
                                        }
                                })()
    </script>
    <!-- End Quantcast Choice. Consent Manager Tag v2.0 (for TCF 2.0) -->
    <!-- Google Tag Manager -->
    <script>
     try {
                                var cmpLoaded = false
                                var gdprApplies = ''
                                window.__tcfapi('getTCData', 2, function(tcData, success) {
                                        if ((tcData.eventStatus === 'useractioncomplete' || tcData.eventStatus === 'tcloaded') && !!tcData.gdprApplies) {
                                                gdprApplies = !!tcData.gdprApplies
                                                window.__tcfapi('ping', 2, function(pingData) {
                                                        // Is tcfapi operational
                                                        cmpLoaded = pingData.cmpLoaded
                                                        if (typeof cmpLoaded === 'boolean' && cmpLoaded === true && typeof gdprApplies === 'boolean' && gdprApplies === true) {
                                                                window.__tcf2 = {
                                                                        'tcData': tcData,
                                                                        'pingData': pingData
                                                                };
                                                                (function(w, d, s, l, i) {
                                                                        w[l] = w[l] || []
                                                                        w[l].push({
                                                                                'gtm.start': new Date().getTime(),
                                                                                event: 'gtm.js'
                                                                        })
                                                                        var f = d.getElementsByTagName(s)[0],
                                                                                j = d.createElement(s),
                                                                                dl = l != 'dataLayer' ? '&l=' + l : ''
                                                                        j.async = true
                                                                        j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl
                                                                        f.parentNode.insertBefore(j, f)
                                                                })(window, document, 'script', 'dataLayer', 'GTM-PZQ45KS')
                                                        }
                                                })
                                        } else {
                                                window.__tcf2 = null;
                                                (function(w, d, s, l, i) {
                                                        w[l] = w[l] || []
                                                        w[l].push({
                                                                'gtm.start': new Date().getTime(),
                                                                event: 'gtm.js'
                                                        })
                                                        var f = d.getElementsByTagName(s)[0],
                                                                j = d.createElement(s),
                                                                dl = l != 'dataLayer' ? '&l=' + l : ''
                                                        j.async = true
                                                        j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl
                                                        f.parentNode.insertBefore(j, f)
                                                })(window, document, 'script', 'dataLayer', 'GTM-PZQ45KS')
                                        }
                                })
                        } catch (exception) {
                                // exception handler...
                        }
    </script>
    <!-- End Google Tag Manager -->
    <!-- Google Ads -->
    <script async="" src="//www.googletagservices.com/tag/js/gpt.js">
    </script>
    <script async="" src="//ads.rubiconproject.com/prebid/11192_Gulesider_no.js">
    </script>
    <!-- End Google Ads -->
    <!-- Julio + helmet scripts -->
    <script async="" defer="" type="text/javascript">
     try {
                        localStorage.setItem('firstPageViewReferrer', "")
                    } catch(e) {

                    }
                    (function (w, d, r) {
                        w['JulioEventObject'] = r;
                        w[r] = w[r] || function () {
                            (w[r].q = w[r].q || []).push(arguments)
                        }
                    })(window, document, "julio");

                    (function () {
                        var swDc = document.createElement('script');
                        swDc.type = 'text/javascript';
                        swDc.charset = 'UTF-8';
                        swDc.async = true;
                        swDc.src = "https://julio-cdn.eniro.com/corefront/entag.2.0.js";
                        var a = document.getElementsByTagName('script')[0];
                        a.parentNode.insertBefore(swDc, a);
                    }());
    </script>
    <!-- End Julio -->
    <script data-rh="true" type="application/ld+json">
     {"@context":"http://schema.org","@type":"Organization","url":"https://www.gulesider.no","logo":"https://static.eniro.com/img/profiles/no/gulesider-logo-desktop-v2-min.png","sameAs":["https://www.facebook.com/gulesider","https://twitter.com/gulesider","https://www.instagram.com/gulesider/","https://www.pinterest.com/gulesider/","https://www.youtube.com/gulesider"]}     
    </script>
    <script data-rh="true" type="application/ld+json">
     {"@context":"http://schema.org","@type":"Website","url":"https://www.gulesider.no","potentialAction":{"@type":"SearchAction","target":"https://www.gulesider.no/search?searchQuery={search_term_string}","query-input":"required name=search_term_string"}}
    </script>
    <script>
     document.querySelector('meta[name="useJS"]').setAttribute('content', 'yes')
                document.querySelector('meta[name="resolution"]').setAttribute('content', window.innerWidth + ',' + window.innerHeight)
                window.__PRELOADED_STATE__ = {"corefront":{"device":"desktop","pageType":"firstPage","isBot":false,"consentComplete":false,"displayConsentDialog":true},"searchPage":{"query":null,"groupId":null,"structuredQuery":null,"id":null,"limit":25,"page":null,"latFrom":null,"latTo":null,"lngFrom":null,"lngTo":null,"searchResult":null,"hoveredItem":null,"selectedItem":null,"selectedItemLoading":false,"countResult":null,"wordCloudResult":null,"isSearching":false,"sortOrder":"default","bboxNoHit":false,"noHit":false,"searchHeaderCollapsed":false,"profilePage":true,"shouldSearch":false,"indexChanged":false,"review":null,"nearby":false,"webshop":false,"needToSendStatistics":false,"profileListStatistics":null,"noHitSearchStatistics":null,"timeoutSearchStatistics":null,"timeout":false,"locationError":false,"viewportWidth":0,"searchFromHere":null,"axInfo":false,"campaign":null,"discovery":null,"postkodlotteriet":null,"repeatSearch":false,"geoHash":""},"searchBox":{"suggest":null,"isFocused":false,"isCleared":false,"isChanged":false},"loginDialog":{"displayed":false},"reviewReportDialog":{"visible":false,"review":null,"reviewReported":false,"text":""},"companyAnswerDialog":{"visible":false,"answer":null,"answerReported":false,"text":""},"emailDialog":{"visible":false,"emailTo":null,"emailFrom":"","reCaptcha":null,"emailPosted":false,"error":false},"reviewDialog":{"visible":false,"name":null,"id":null,"user":null,"rating":null,"reviewLength":0,"reviewPosted":false,"isAccepted":false,"reviewText":""},"shareDialog":{"visible":false,"item":null,"showEmail":false,"showSMS":false,"shared":false,"error":false},"marketingDialog":{"visible":false,"item":null},"personContentDialog":{"visible":false},"profile":{"id":"no","lang":"no","country":"no","siteName":"gulesider","themeColor":"#ffe000","titleTemplate":"%s | %s1 | gulesider.no","titleTemplateWithPage":"%s 
| %s1 | gulesider.no | sida %s2","titleTemplateNohit":"Ingen treff | %s | gulesider.no","titleTemplateFirstPage":"Gulesider.no - Oppdag nærheten.","logo_white":"\u002F\u002Fstatic.eniro.com\u002Fimg\u002Fprofiles\u002Fno\u002Fgulesider_logo_white.svg","logo_gray":"\u002F\u002Fstatic.eniro.com\u002Fimg\u002Fprofiles\u002Fno\u002Fgulesider_logo_gray.svg","productionURL":"https:\u002F\u002Fwww.gulesider.no","canonicalURL":"https:\u002F\u002Fwww.gulesider.no","mapURL":"https:\u002F\u002Fkart.gulesider.no","routeLink":"\u002F\u002Fkart.gulesider.no\u002Fveibeskrivelse","nauticalWebLink":"https:\u002F\u002Fpasjoen.gulesider.no","proff":"\u002F\u002Fwww.proff.no\u002Finfopage\u002F","psWeb":"http:\u002F\u002Fps-no.prod.eniro.net\u002Fps-web","phoneListing":"\u002Fhvem+har+ringt","yextPID":"j8uFzxqN02","googleTagManagerId":"GTM-PZQ45KS","googleSiteVerification":"wSbVnOyV7IMQp3j7e_R4t4WFVvfDlZC5S0ALb9ISpRQ","display":{"google":{"enabled":true,"id":21842951927,"prebid":"11192_Gulesider_no","relevantDigital":true},"adnami":{"enabled":true,"id":"41249494-c681-42f1-a422-220ed6e90771"},"adsense":{"enabled":true,"id":"pub-8476020322808825","showOnNoHit":false}},"SEOData":{"url":"https:\u002F\u002Fwww.gulesider.no","logo":"https:\u002F\u002Fstatic.eniro.com\u002Fimg\u002Fprofiles\u002Fno\u002Fgulesider-logo-desktop-v2-min.png","sameAs":["https:\u002F\u002Fwww.facebook.com\u002Fgulesider","https:\u002F\u002Ftwitter.com\u002Fgulesider","https:\u002F\u002Fwww.instagram.com\u002Fgulesider\u002F","https:\u002F\u002Fwww.pinterest.com\u002Fgulesider\u002F","https:\u002F\u002Fwww.youtube.com\u002Fgulesider"],"target":"https:\u002F\u002Fwww.gulesider.no\u002Fsearch?searchQuery={search_term_string}"},"appPromo":{"enabled":false,"activeApp":"core","apps":{"cor