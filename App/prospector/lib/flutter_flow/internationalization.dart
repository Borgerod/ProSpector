import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';

class FFLocalizations {
  FFLocalizations(this.locale);

  final Locale locale;

  static FFLocalizations of(BuildContext context) =>
      Localizations.of<FFLocalizations>(context, FFLocalizations)!;

  static List<String> languages() => ['en', 'nb'];

  String get languageCode => locale.toString();
  int get languageIndex => languages().contains(languageCode)
      ? languages().indexOf(languageCode)
      : 0;

  String getText(String key) =>
      (kTranslationsMap[key] ?? {})[locale.toString()] ?? '';

  String getVariableText({
    String? enText = '',
    String? nbText = '',
  }) =>
      [enText, nbText][languageIndex] ?? '';
}

class FFLocalizationsDelegate extends LocalizationsDelegate<FFLocalizations> {
  const FFLocalizationsDelegate();

  @override
  bool isSupported(Locale locale) =>
      FFLocalizations.languages().contains(locale.toString());

  @override
  Future<FFLocalizations> load(Locale locale) =>
      SynchronousFuture<FFLocalizations>(FFLocalizations(locale));

  @override
  bool shouldReload(FFLocalizationsDelegate old) => false;
}

Locale createLocale(String language) => language.contains('_')
    ? Locale.fromSubtags(
        languageCode: language.split('_').first,
        scriptCode: language.split('_').last,
      )
    : Locale(language);

final kTranslationsMap = <Map<String, Map<String, String>>>[
  //  FFLocalizations.of(context).getText('' /*  */);

  // 'ib1c322a': {
  //     'en':'',
  //     'nb':'',
  //   },

  // Notes
  {
    '8mdtm5jj': {
      'en': 'Notes',
      'nb': 'Notater',
    },
    // 'tp7ux297': {
    //   'en': '[Some hint text...]',
    //   'nb': '',
    // },
    'h2ktoqmf': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // HomePage
  {
    'uof8wdmp': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // CallList
  {
    'nhdfcp17': {
      'en': 'Call List',
      'nb': 'RingeListe',
    },
    'nydqnbie': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },

  // RenewList

  {
    'x3f7fyl2': {
      'en':
          'Denied \n Please finish the current Call list before requesting a new one.',
      'nb':
          'Avvist \n Vennligst fullfør gjeldende anropsliste før du ber om en ny.',
    },
    'x3f7fyl1': {
      'en': 'Approved, Renewing List',
      'nb': 'Godkjent, Fornyer listen',
    },
    'x3f7fyl8': {
      'en': 'Renew Call List',
      'nb': 'Forny Ringelisten',
    },
    'b49vk2i6': {
      'en':
          'Causion: You are about to replace the old call list, with a new one. \n\nAre you sure you want to proceed?',
      'nb':
          'Vær oppmerksom: Du er i ferd med å erstatte den gamle anropslisten med en ny.\n\nEr du sikker på at du vil fortsette?',
    },
    'yvgcz68b': {
      'en': 'Cancel',
      'nb': 'Avbryt',
    },
    'ggnjl4yp': {
      'en': 'Renew',
      'nb': 'Forny',
    },
    'hjwv2rv6': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // Instructions
  {
    'rtlzy4ms': {
      'en': 'Instructions',
      'nb': 'Instruksjoner',
    },
    'j9hnq0ql': {
      'en': 'Step 1',
      'nb': 'Steg 1',
    },
    'obwwgp74': {
      'en':
          'Cross out the prospects from the call list as you call them.\n\n PS: \nPlease do not press the check box more than necessary, every time changes are made to the call list a request is sent to the database. The database has a limit on how many requests you can have in a year before the price rises, which could get expensive after a while. ',
      'nb':
          'Kryss ut prospektene fra ringelisten etterhvert som du ringer dem.\n\n PS: Vær snill å ikke trykk på checkboksen mer enn nødvendig, hver gang det gjøres endringer i ringelisten sendes det en forespørsel til databasen. Databasen har en grense på hvor mange forespørseler man kan ha i året før prisen stiger, som kan bli dyrt.',
    },
    'xnz45xlp': {
      'en': 'Step 2',
      'nb': 'Steg 2',
    },
    'rj07qb0g': {
      'en':
          'After you have crossed off the entire list, you can press "Renew CallList". \n\nNote that you can only renew the call list if you have crossed off all the prospects.',
      'nb':
          'Etter du har krysset ut hele listen, kan du trykke på "Forny Ringelisten".\n\nMerk at du kan bare fornye ringelisten om du har krysset ut alle prospektene.',
    },
    'tsty4p9e': {
      'en': 'Important',
      'nb': 'Viktig',
    },
    'uheh63gf': {
      'en':
          "When you renew the list, the prospects will be considered finished and removed from the database. \n\nSo be careful not to tick off prospects who haven't been called yet.",
      'nb':
          'Når du fornyer listen vil prospektene bli ansett som ferdigbehandlet og fjernet fra databasen. \n\nSå vær forsiktig å ikke kryss av prospektere som ikke enda er ringt.',
    },
    'n5u9bk2y': {
      'en': 'Step 4',
      'nb': 'Steg 4',
    },
    'isy3wrek': {
      'en':
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \n\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      'nb': '',
    },
    'pno6pvus': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // About
  {
    'bp5npad7': {
      'en': 'About',
      'nb': 'Om ProSpector',
    },
    'vv6vetv9': {
      'en': 'Terms & Conditions',
      'nb': 'Brukervilkår',
    },
    '3isuhbch': {
      'en':
          'By downloading or using the app, these terms will automatically apply to you – you should make sure therefore that you read them carefully before using the app. You’re not allowed to copy or modify the app, any part of the app, or our trademarks in any way. You’re not allowed to attempt to extract the source code of the app, and you also shouldn’t try to translate the app into other languages or make derivative versions. The app itself, and all the trademarks, copyright, database rights, and other intellectual property rights related to it, still belong to A.Borgerød.\n\nA.Borgerød is committed to ensuring that the app is as useful and efficient as possible. For that reason, we reserve the right to make changes to the app or to charge for its services, at any time and for any reason. We will never charge you for the app or its services without making it very clear to you exactly what you’re paying for.\n\nThe ProSpector app stores and processes personal data that you have provided to us, to provide our Service. It’s your responsibility to keep your phone and access to the app secure. We therefore recommend that you do not jailbreak or root your phone, which is the process of removing software restrictions and limitations imposed by the official operating system of your device. It could make your phone vulnerable to malware/viruses/malicious programs, compromise your phone’s security features and it could mean that the ProSpector app won’t work properly or at all.\n\nYou should be aware that there are certain things that A.Borgerød will not take responsibility for. Certain functions of the app will require the app to have an active internet connection. The connection can be Wi-Fi or provided by your mobile network provider, but A.Borgerød cannot take responsibility for the app not working at full functionality if you don’t have access to Wi-Fi, and you don’t have any of your data allowance left.\n\nIf you’re using the app outside of an area with Wi-Fi, you should remember that the terms of the agreement with your mobile network provider will still apply. As a result, you may be charged by your mobile provider for the cost of data for the duration of the connection while accessing the app, or other third-party charges. In using the app, you’re accepting responsibility for any such charges, including roaming data charges if you use the app outside of your home territory (i.e. region or country) without turning off data roaming. If you are not the bill payer for the device on which you’re using the app, please be aware that we assume that you have received permission from the bill payer for using the app.\n\nAlong the same lines, A.Borgerød cannot always take responsibility for the way you use the app i.e. You need to make sure that your device stays charged – if it runs out of battery and you can’t turn it on to avail the Service, A.Borgerød cannot accept responsibility.\n\nWith respect to A.Borgerød’s responsibility for your use of the app, when you’re using the app, it’s important to bear in mind that although we endeavor to ensure that it is updated and correct at all times, we do rely on third parties to provide information to us so that we can make it available to you. A.Borgerød accepts no liability for any loss, direct or indirect, you experience as a result of relying wholly on this functionality of the app.\n\nAt some point, we may wish to update the app. The app is currently available on – the requirements for the system(and for any additional systems we decide to extend the availability of the app to) may change, and you’ll need to download the updates if you want to keep using the app. A.Borgerød does not promise that it will always update the app so that it is relevant to you and/or works with the version that you have installed on your device. However, you promise to always accept updates to the application when offered to you, We may also wish to stop providing the app, and may terminate use of it at any time without giving notice of termination to you. Unless we tell you otherwise, upon any termination, (a) the rights and licenses granted to you in these terms will end; (b) you must stop using the app, and (if needed) delete it from your device.\n\nChanges to This Terms and Conditions\n\nWe may update our Terms and Conditions from time to time. Thus, you are advised to review this page periodically for any changes. We will notify you of any changes by posting the new Terms and Conditions on this page.\n\nThese terms and conditions are effective as of 2022-08-22\n\nContact Us\n\nIf you have any questions or suggestions about our Terms and Conditions, do not hesitate to contact us at borgerod@hotmail.com.',
      'nb':
          'Ved å laste ned eller bruke appen vil disse vilkårene automatisk gjelde for deg – du bør derfor sørge for at du leser dem nøye før du bruker appen. Du har ikke lov til å kopiere eller endre appen, noen del av appen eller varemerkene våre på noen måte. Du har ikke lov til å prøve å trekke ut kildekoden til appen, og du bør heller ikke prøve å oversette appen til andre språk eller lage avledede versjoner. Selve appen, og alle varemerker, opphavsrett, databaserettigheter og andre immaterielle rettigheter knyttet til den, tilhører fortsatt A.Borgerød.\n\nA.Borgerød er opptatt av å sikre at appen er så nyttig og effektiv som mulig. Av den grunn forbeholder vi oss retten til å gjøre endringer i appen eller ta betalt for dens tjenester, når som helst og uansett årsak. Vi vil aldri belaste deg for appen eller dens tjenester uten å gjøre det veldig klart for deg nøyaktig hva du betaler for.\n\nProSpector-appen lagrer og behandler personopplysninger som du har gitt oss, for å yte tjenesten vår. Det er ditt ansvar å holde telefonen og tilgangen til appen sikker. Vi anbefaler derfor at du ikke jailbreaker eller roter telefonen din, som er prosessen med å fjerne programvarerestriksjoner og begrensninger pålagt av det offisielle operativsystemet til enheten din. Det kan gjøre telefonen sårbar for skadelig programvare/virus/ondsinnede programmer, kompromittere telefonens sikkerhetsfunksjoner, og det kan bety at ProSpector-appen ikke fungerer som den skal eller i det hele tatt.\n\nDu bør være klar over at det er visse ting A.Borgerød ikke vil ta ansvar for. Enkelte funksjoner i appen krever at appen har en aktiv internettforbindelse. Tilkoblingen kan være Wi-Fi eller levert av mobilnettleverandøren din, men A.Borgerød kan ikke ta ansvar for at appen ikke fungerer med full funksjonalitet dersom du ikke har tilgang til Wi-Fi, og du ikke har noen av datatillegget ditt igjen.\n\nHvis du bruker appen utenfor et område med Wi-Fi, bør du huske at vilkårene i avtalen med mobilnettleverandøren din fortsatt gjelder. Som et resultat kan du bli belastet av mobilleverandøren din for kostnaden for data for varigheten av forbindelsen mens du bruker appen, eller andre tredjepartskostnader. Når du bruker appen, påtar du deg ansvar for slike avgifter, inkludert roamingdatagebyrer hvis du bruker appen utenfor hjemmeterritoriet ditt (dvs. region eller land) uten å slå av dataroaming. Hvis du ikke er regningsbetaler for enheten du bruker appen på, vær oppmerksom på at vi antar at du har fått tillatelse fra regningsbetaleren til å bruke appen.\n\nPå samme måte kan ikke A.Borgerød alltid ta ansvar for måten du bruker appen på, dvs. du må sørge for at enheten din forblir ladet – hvis den går tom for batteri og du ikke kan slå den på for å benytte tjenesten, A.Borgerød kan ikke ta ansvar.\n\nMed hensyn til A.Borgerøds ansvar for din bruk av appen, når du bruker appen, er det viktig å huske på at selv om vi bestreber oss på å sikre at den er oppdatert og korrekt til enhver tid, er vi avhengige av tredjeparter å gi oss informasjon slik at vi kan gjøre den tilgjengelig for deg. A.Borgerød påtar seg intet ansvar for tap, direkte eller indirekte, du opplever som et resultat av å stole helt på denne funksjonaliteten til appen.\n\nPå et tidspunkt vil vi kanskje oppdatere appen. Appen er for øyeblikket tilgjengelig på – kravene til systemet (og for eventuelle tilleggssystemer vi bestemmer oss for å utvide tilgjengeligheten til appen til) kan endres, og du må laste ned oppdateringene hvis du vil fortsette å bruke appen. A.Borgerød lover ikke at de alltid vil oppdatere appen slik at den er relevant for deg og/eller fungerer med den versjonen du har installert på enheten din. Du lover imidlertid å alltid godta oppdateringer til applikasjonen når den tilbys deg. Vi kan også ønske å slutte å levere appen, og kan avslutte bruken av den når som helst uten å gi deg varsel om oppsigelse. Med mindre vi forteller deg noe annet, ved enhver oppsigelse, (a) opphører rettighetene og lisensene som er gitt deg i disse vilkårene; (b) du må slutte å bruke appen og (om nødvendig) slette den fra enheten din.\n\nEndringer i disse vilkårene og betingelsene\n\nVi kan oppdatere våre vilkår og betingelser fra tid til annen. Derfor anbefales det å gå gjennom denne siden med jevne mellomrom for eventuelle endringer. Vi vil varsle deg om eventuelle endringer ved å legge ut de nye vilkårene og betingelsene på denne siden.\n\nDisse vilkårene trer i kraft fra 2022-08-22\n\nKontakt oss\n\nHvis du har spørsmål eller forslag til våre vilkår og betingelser, ikke nøl med å kontakte oss på borgerod@hotmail.com.',
    },
    'n4s4txwp': {
      'en': 'Privacy Policy',
      'nb': 'Personvernerklæring',
    },
    'wu0izus2': {
      'en':
          'A.Borgerød built the ProSpector app as a Commercial app. This SERVICE is provided by A.Borgerød and is intended for use as is.\n\nThis page is used to inform visitors regarding our policies with the collection, use, and disclosure of Personal Information if anyone decided to use our Service.\n\nIf you choose to use our Service, then you agree to the collection and use of information in relation to this policy. The Personal Information that we collect is used for providing and improving the Service. We will not use or share your information with anyone except as described in this Privacy Policy.\n\nThe terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which are accessible at ProSpector unless otherwise defined in this Privacy Policy.\n\nInformation Collection and Use\n\nFor a better experience, while using our Service, we may require you to provide us with certain personally identifiable information. The information that we request will be retained by us and used as described in this privacy policy.\n\nLog Data\n\nWe want to inform you that whenever you use our Service, in a case of an error in the app we collect data and information (through third-party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (“IP”) address, device name, operating system version, the configuration of the app when utilizing our Service, the time and date of your use of the Service, and other statistics.\n\nCookies\n\nCookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device\'s internal memory.\n\nThis Service does not use these “cookies” explicitly. However, the app may use third-party code and libraries that use “cookies” to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies, you may not be able to use some portions of this Service.\n\nService Providers\n\nWe may employ third-party companies and individuals due to the following reasons:\n\nTo facilitate our Service;\nTo provide the Service on our behalf;\nTo perform Service-related services; or\nTo assist us in analyzing how our Service is used.\nWe want to inform users of this Service that these third parties have access to their Personal Information. The reason is to perform the tasks assigned to them on our behalf. However, they are obligated not to disclose or use the information for any other purpose.\n\nSecurity\n\nWe value your trust in providing us your Personal Information, thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet, or method of electronic storage is 100% secure and reliable, and we cannot guarantee its absolute security.\n\nLinks to Other Sites\n\nThis Service may contain links to other sites. If you click on a third-party link, you will be directed to that site. Note that these external sites are not operated by us. Therefore, we strongly advise you to review the Privacy Policy of these websites. We have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party sites or services.\n\nChildren’s Privacy\n\nWe do not knowingly collect personally identifiable information from children. We encourage all children to never submit any personally identifiable information through the Application and/or Services. We encourage parents and legal guardians to monitor their children\'s Internet usage and to help enforce this Policy by instructing their children never to provide personally identifiable information through the Application and/or Services without their permission. If you have reason to believe that a child has provided personally identifiable information to us through the Application and/or Services, please contact us. You must also be at least 16 years of age to consent to the processing of your personally identifiable information in your country (in some countries we may allow your parent or guardian to do so on your behalf).\n\nChanges to This Privacy Policy\n\nWe may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. We will notify you of any changes by posting the new Privacy Policy on this page.\n\nThis policy is effective as of 2022-08-22\n\nContact Us\n\nIf you have any questions or suggestions about our Privacy Policy, do not hesitate to contact us at borgerod@hotmail.com.',
      'nb':
          'A.Borgerød bygget ProSpector-appen som en kommersiell app. Denne TJENESTEN leveres av A.Borgerød og er beregnet for bruk som den er.\n\nDenne siden brukes til å informere besøkende om våre retningslinjer for innsamling, bruk og avsløring av personlig informasjon hvis noen bestemte seg for å bruke tjenesten vår.\n\nHvis du velger å bruke tjenesten vår, godtar du innsamling og bruk av informasjon i forhold til denne policyen. Personopplysningene vi samler inn brukes til å tilby og forbedre tjenesten. Vi vil ikke bruke eller dele informasjonen din med noen unntatt som beskrevet i denne personvernerklæringen.\n\nBegrepene som brukes i denne personvernerklæringen har samme betydning som i våre vilkår og betingelser, som er tilgjengelige hos ProSpector med mindre annet er definert i denne personvernerklæringen.\n\nInformasjonsinnsamling og bruk\n\nFor en bedre opplevelse, mens du bruker tjenesten vår, kan vi kreve at du gir oss visse personlig identifiserbare opplysninger. Informasjonen vi ber om vil bli oppbevart av oss og brukt som beskrevet i denne personvernerklæringen.\n\nLogg data\n\nVi ønsker å informere deg om at når du bruker tjenesten vår, i tilfelle feil i appen samler vi inn data og informasjon (gjennom tredjepartsprodukter) på telefonen din kalt Loggdata. Disse loggdataene kan inkludere informasjon som enhetens Internett-protokoll (“IP”)-adresse, enhetsnavn, operativsystemversjon, konfigurasjonen av appen når du bruker tjenesten vår, klokkeslett og dato for din bruk av tjenesten og annen statistikk .\n\nInformasjonskapsler\n\nInformasjonskapsler er filer med en liten mengde data som vanligvis brukes som anonyme unike identifikatorer. Disse sendes til nettleseren din fra nettsidene du besøker og lagres i enhetens interne minne.\n\nDenne tjenesten bruker ikke disse \"informasjonskapslene\" eksplisitt. Imidlertid kan appen bruke tredjepartskode og biblioteker som bruker \"informasjonskapsler\" for å samle inn informasjon og forbedre tjenestene deres. Du har muligheten til å enten godta eller avslå disse informasjonskapslene og vite når en informasjonskapsel sendes til enheten din. Hvis du velger å avslå informasjonskapslene våre, kan det hende du ikke kan bruke enkelte deler av denne tjenesten.\n\nTjenestetilbydere\n\nVi kan ansette tredjepartsselskaper og enkeltpersoner på grunn av følgende årsaker:\n\nFor å lette tjenesten vår;\nFor å tilby tjenesten på våre vegne;\nFor å utføre tjenesterelaterte tjenester; eller\nFor å hjelpe oss med å analysere hvordan tjenesten vår brukes.\nVi ønsker å informere brukere av denne tjenesten om at disse tredjepartene har tilgang til deres personlige opplysninger. Årsaken er å utføre oppgavene som er tildelt dem på våre vegne. De er imidlertid forpliktet til ikke å avsløre eller bruke informasjonen til andre formål.\n\nSikkerhet\n\nVi verdsetter din tillit til å gi oss din personlige informasjon, og derfor streber vi etter å bruke kommersielt akseptable midler for å beskytte den. Men husk at ingen metode for overføring over internett, eller metode for elektronisk lagring er 100 % sikker og pålitelig, og vi kan ikke garantere dens absolutte sikkerhet.\n\nLenker til andre nettsteder\n\nDenne tjenesten kan inneholde lenker til andre nettsteder. Hvis du klikker på en tredjepartslenke, blir du dirigert til dette nettstedet. Merk at disse eksterne sidene ikke drives av oss. Derfor anbefaler vi deg på det sterkeste å lese personvernreglene til disse nettstedene. Vi har ingen kontroll over og påtar oss intet ansvar for innholdet, personvernreglene eller praksisen til tredjeparts nettsteder eller tjenester.\n\nBarns personvern\n\nVi samler ikke bevisst inn personlig identifiserbar informasjon fra barn. Vi oppfordrer alle barn til aldri å sende inn personlig identifiserbar informasjon gjennom applikasjonen og/eller tjenestene. Vi oppfordrer foreldre og foresatte til å overvåke barnas Internett-bruk og hjelpe til med å håndheve disse retningslinjene ved å instruere barna deres til aldri å oppgi personlig identifiserbar informasjon gjennom applikasjonen og/eller tjenestene uten deres tillatelse. Hvis du har grunn til å tro at et barn har gitt oss personlig identifiserbar informasjon gjennom applikasjonen og/eller tjenestene, vennligst kontakt oss. Du må også være minst 16 år for å samtykke til behandling av din personlig identifiserbare informasjon i ditt land (i enkelte land kan vi tillate at foreldre eller foresatte gjør det på dine vegne).\n\nEndringer i denne personvernerklæringen\n\nVi kan oppdatere vår personvernerklæring fra tid til annen. Derfor anbefales det å gå gjennom denne siden med jevne mellomrom for eventuelle endringer. Vi vil varsle deg om eventuelle endringer ved å legge ut den nye personvernerklæringen på denne siden.\n\nDenne policyen trer i kraft fra 2022-08-22\n\nKontakt oss\n\nHvis du har spørsmål eller forslag til våre retningslinjer for personvern, ikke nøl med å kontakte oss på borgerod@hotmail.com.',
    },
    'dyovkwxn': {
      'en': 'Creator',
      'nb': 'Utvikler',
    },
    'q4mnsavs': {
      'en':
          'ProSpector was made by Aleksander Borgerød. If you wish to know more about my work or want to rent my services, click on the icons below. For issues  regarding this app, I refer you to the feedback section. ',
      'nb':
          'ProSpector er laget av Aleksander Borgerød. Hvis du ønsker å vite mer om arbeidet mitt eller ønsker å leie tjenestene mine, klikk på ikonene nedenfor. For problemer angående denne appen, henviser jeg deg til tilbakemeldingsdelen.',
    },
    'cyax9pba': {
      'en': 'Owner\'s Name',
      'nb': 'Eieren\'s Navn',
    },
    'lpnz3qbb': {
      'en': 'Email Address',
      'nb': 'Epost Adresse',
    },
    'yrcrigh3': {
      'en': 'Phone Number',
      'nb': 'TelefonNummer',
    },
    'nrb7ewdg': {
      'en': 'Org number',
      'nb': 'Org Nummer',
    },
    '82b2zj4z': {
      'en': 'Company Name',
      'nb': 'Juridisk Navn',
    },
    '2vcuk8te': {
      'en': 'Aleksander Borgerød',
      'nb': 'Aleksander Borgerød',
    },
    'v8asuq8q': {
      'en': 'Borgerod@hotmail.com',
      'nb': 'Borgerod@hotmail.com',
    },
    'wzlfu94r': {
      'en': '+47 99 33 76 61 ',
      'nb': '+47 99 33 76 61 ',
    },
    'jjk2nn7k': {
      'en': '924 495 685',
      'nb': '924 495 685',
    },
    'w8sc3og2': {
      'en': 'A.Borgerød',
      'nb': 'A.Borgerød',
    },
    'rh5p8v5z': {
      'en':
          'Application made by Aleksander Borgerød,  rights reserved to  (C) 2022 A. Borgerød ENK.',
      'nb':
          'Programvare laget av Aleksander Borgerød, alle rettigheter forbeholdes til  (C) 2022 A. Borgerød ENK.',
    },
    '1x4sofit': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // Settings
  {
    'tppwmwmy': {
      'en': 'Settings',
      'nb': 'Instillinger',
    },
    '7p4179uq': {
      'en': 'Language',
      'nb': 'Språk',
    },
    'zyhkv4uu': {
      'en': 'Password',
      'nb': 'Passord',
    },
    'lymob5pz': {
      'en': 'Change Password',
      'nb': 'Endre Passord',
    },
    'tmwzirro': {
      'en': 'Cancel',
      'nb': 'Abvryt',
    },
    'a4ncm086': {
      'en': 'Save',
      'nb': 'Lagre',
    },
    '9s96gl1k': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // Feedback
  {
    'f86135rs': {
      'en': 'FeedBack',
      'nb': 'Tilbakemelding',
    },
    'jdxfccf5': {
      'en': 'What is your feedback related to?',
      'nb': 'Hva er tilbakemeldingen din knyttet til?',
    },
    '2tnwg56l': {
      'en': 'Issue/Bug',
      'nb': 'Problem/feil',
    },
    'y55lsx8h': {
      'en': 'Missing Feature',
      'nb': 'Manglende funksjon',
    },
    '18b4xxn1': {
      'en': 'User Experience',
      'nb': 'Brukererfaring',
    },
    'komfrau1': {
      'en': 'Legal',
      'nb': 'Juridisk',
    },
    'fyhytso7': {
      'en': 'Other',
      'nb': 'Annet',
    },
    'jv4mmqyf': {
      'en': 'What company do you represent?',
      'nb': 'Hvilket selskap representerer du?',
    },
    '3gpxhhxw': {
      'en': 'ExampleCompany AS',
      'nb': 'EksempelBedrift AS',
    },
    'zewan5yy': {
      'en': 'What is your job position?',
      'nb': 'Hva er arbeidsstillingen din',
    },
    'k8lvq4bg': {
      'en': 'Owner / Administration',
      'nb': 'Eier / Administrasjon',
    },
    'mf0kvfs9': {
      'en': 'IT / Development',
      'nb': 'It / Utvikling',
    },
    'gg4jng8j': {
      'en': 'Employee',
      'nb': 'Ansatt',
    },
    'i5da2rpx': {
      'en': 'Other',
      'nb': 'Annet',
    },
    'z05s1aqw': {
      'en': 'Message',
      'nb': 'Melding',
    },
    'mlhg1hgy': {
      'en': 'Email Address',
      'nb': 'Epostadresse',
    },
    // 'wzputey6': {
    //   'en': '[Some hint text...]',
    //   'nb': '',
    // },
    'c46l6cf6': {
      'en': 'Send',
      'nb': 'Send',
    },
    'laajsjau': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // Login
  {
    '3yvf9h73': {
      'en': 'Not registered?',
      'nb': 'Ikke registrert?',
    },
    '9zbibd94': {
      'en': 'Sign Up',
      'nb': 'Opprett ny Konto',
    },
    'jy7dyfri': {
      'en': 'Email Address',
      'nb': 'Epost Adresse',
    },
    'cqr3lh99': {
      'en': 'Password',
      'nb': 'Passord',
    },
    'argrf05a': {
      'en': 'Remember Me',
      'nb': 'Husk Meg',
    },
    'bbpm2l2x': {
      'en': 'Login',
      'nb': 'Logg Inn',
    },
    '3j5yksm2': {
      'en': 'Forgot your password?',
      'nb': 'Glemt Passordet?',
    },
    'g3asj7so': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // Signup

  {
    'in1c322b': {
      'en': 'Please enter the name of your workplace.',
      'nb': 'Fyll inn arbeidsplass',
    },
    'in1c322s': {
      'en': 'Workplace not filled correctly.',
      'nb': 'Arbeidsplass er ikke fyllt inn riktig',
    },
    'in1c322c': {
      'en': 'Please enter password.',
      'nb': 'Fyll inn passord.',
    },
    'in1c322d': {
      'en': 'Please enter a valid password.',
      'nb': 'Fyll inn en gyldig passord',
    },
    'in1c322a': {
      'en': 'Please enter a valid email.',
      'nb': 'Fyll inn en gyldig epost',
    },
    'ibsc322a': {
      'en': 'Unable to create account',
      'nb': 'Klarte ikke å opprette en konto',
    },
    'ib1c3p2a': {
      'en': 'Form is not properly filled ',
      'nb': 'Skjemaet er ikke riktig fylt inn',
    },
    'ib1c3g2a': {
      'en': 'Workplace not filled correctly.',
      'nb': 'Arbeidsplass er ikke riktig fyllt inn',
    },
    'ib1c322a': {
      'en':
          'Only use lowercase letters,\nDo not use spaces, numbers or special characters.',
      'nb':
          'Bruk bare små bokstaver,\nIkke bruk mellomrom, nummere eller spesielle bokstaver.',
    },
    'ib1c3s2a': {
      'en': 'Please enter a strong password.',
      'nb': 'Fyll inn et sterkere passord.',
    },
    'ib1c3sna': {
      'en':
          'Use atleast \n - one uppercase letter, \n - one lowercase letter, \n - one number\n',
      'nb':
          'Bruk minst \n -en stor bokstav, \n - en liten bokstav, \n - ett nummer\n',
    },
    'ib1c3zui': {
      'en': 'Return To Login',
      'nb': 'Gå tilbake til pålogging',
    },
    'fpke2str': {
      'en': 'Create Account',
      'nb': 'Opprett Ny Konto',
    },
    'chjotsyn': {
      'en': 'Username',
      'nb': 'Brukernavn',
    },
    'b7328u01': {
      'en': 'Workplace',
      'nb': 'Arbeidsplass',
    },
    'zata0tey': {
      'en': 'Email Address',
      'nb': 'Epost Adresse',
    },
    'u1vts5lp': {
      'en': 'Password',
      'nb': 'Passord',
    },
    '4dbf2i4h': {
      'en': 'Sign Up',
      'nb': 'Registrer',
    },
    'xt0gob60': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // AccountCreated
  {
    '3ebfpqcc': {
      'en': 'Your account has been created successfully!',
      'nb': 'Opprett Ny Konto',
    },
    'xzbndtx5': {
      'en': 'GET STARTED',
      'nb': 'KOM I GANG',
    },
    '6bby3gm4': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // LoginErrorMessage
  {
    'ugfxvysw': {
      'en': 'ERROR: Your email  or password was incorrect, \nplease try again.',
      'nb':
          'ERROR: E-postadressen eller passordet ditt var feil, \nprøv igjen.',
    },
    'pshb00rr': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // ResetPassword
  {
    'mkjs1git': {
      'en': 'Password Reset',
      'nb': 'Tilbakestill Passord',
    },
    'b6vxcqkd': {
      'en': 'New Password',
      'nb': 'Nytt Passord',
    },
    'lpsz5j9b': {
      'en': 'Confirm Password',
      'nb': 'Bekreft Passord',
    },
    'weidrreh': {
      'en': 'ERROR: Passwords did not match',
      'nb': 'ERROR: Passordene er forskjellige',
    },
    '973k67jf': {
      'en': 'Reset Password',
      'nb': 'Tilbakestill',
    },
    'yus3tsue': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // ResetPasswordAuthentication
  {
    'pkchmen5': {
      'en': 'Password Recovery',
      'nb': 'Passordgjenoppretting',
    },
    'xrdirw1y': {
      'en': 'To request password reset link, please enter your email',
      'nb':
          'Skriv inn e-postadressen din, for å be om lenke for tilbakestilling av passord',
    },
    'k0qg50zl': {
      'en': 'Email Address',
      'nb': 'Epost Adresse',
    },
    'swysf1rz': {
      'en': 'Recover Password',
      'nb': 'Gjenopprett passord',
    },
    'c56q9stn': {
      'en': 'Home',
      'nb': 'Hjem',
    },
  },
  // LightmodeSwitch
  {
    'x3lg0hnj': {
      'en': 'Switch to Dark Mode',
      'nb': 'Bytt til MørkeModus',
    },
    'k2h24c91': {
      'en': 'Switch to Light Mode',
      'nb': 'Bytt til LysModus',
    },
  },
  // MenuCopy
  {
    'c4xwrvgn': {
      'en': 'Instructions',
      'nb': 'Instruksjoner',
    },
    'dl8jkd4c': {
      'en': 'View Call List',
      'nb': 'Vis RingeListe',
    },
    'pviup14g': {
      'en': 'Renew List',
      'nb': 'Forny RingeListe',
    },
    'mojlgs22': {
      'en': 'Notes',
      'nb': 'Notater',
    },
    'xdz4v725': {
      'en': 'About',
      'nb': 'Om ProSpector',
    },
    'o9mimblc': {
      'en': 'Settings',
      'nb': 'Instillinger',
    },
    'md0rr0g2': {
      'en': 'FeedBack',
      'nb': 'TilbakeMelding',
    },
  },
  // CardSharp
  {
    'dvjziro1': {
      'en': 'Step 1',
      'nb': 'Steg 1',
    },
    'dvjziro2': {
      'en': 'Step 2',
      'nb': 'Steg 2',
    },
    'dvjziro3': {
      'en': 'Step 3',
      'nb': 'Steg 3',
    },
    'dvjziro4': {
      'en': 'Step 4',
      'nb': 'Steg 4',
    },
    'jus2xblm': {
      'en': 'Cancel',
      'nb': 'Avbryt',
    },
    'thndjhfw': {
      'en': 'Save',
      'nb': 'Lagre',
    },
  },
  // Miscellaneous
  {
    'nluytlsa': {
      'en': '',
      'nb': '',
    },
    '3ceip82m': {
      'en': '',
      'nb': '',
    },
    'c8sx0e6y': {
      'en': '',
      'nb': '',
    },
    'l9p6r6si': {
      'en': '',
      'nb': '',
    },
    '2t1fbgnh': {
      'en': '',
      'nb': '',
    },
    '6rk5p9x5': {
      'en': '',
      'nb': '',
    },
    'mb5vn2t3': {
      'en': '',
      'nb': '',
    },
    'v6m47vbu': {
      'en': '',
      'nb': '',
    },
    '0fpw872s': {
      'en': '',
      'nb': '',
    },
    'u24guj8m': {
      'en': '',
      'nb': '',
    },
    'ubj03nhv': {
      'en': '',
      'nb': '',
    },
    'q7n8zkwg': {
      'en': '',
      'nb': '',
    },
    '6o0u8b68': {
      'en': '',
      'nb': '',
    },
    'edm362pg': {
      'en': '',
      'nb': '',
    },
    '31f1h9qv': {
      'en': '',
      'nb': '',
    },
    'goo8tox2': {
      'en': '',
      'nb': '',
    },
    'u1emay7e': {
      'en': '',
      'nb': '',
    },
    'vxbqu86e': {
      'en': '',
      'nb': '',
    },
    'gucetpdq': {
      'en': '',
      'nb': '',
    },
    'htvdt2i1': {
      'en': '',
      'nb': '',
    },
  },
].reduce((a, b) => a..addAll(b));
