import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:prospector/pages/home/home_page.dart';
import 'package:prospector/pages/main_page/main_page.dart';
import 'package:prospector/popups/about/about_widget.dart';
import 'package:prospector/pages/call_list/call_list_widget.dart';
import 'package:prospector/popups/feedback/feedback_widget.dart';
import 'package:prospector/pages/instructions/instructions_page.dart';
import 'package:prospector/pages/notes/notes_page.dart';
import 'package:prospector/popups/renew_list/renew_list_widget.dart';
import 'package:prospector/popups/settings/settings_widget.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:flutter_acrylic/flutter_acrylic.dart';
import 'package:flutter_neumorphic/flutter_neumorphic.dart';
import 'dart:io';
import 'package:quiver/iterables.dart';

//! ISSUE DESCRIPTION -- HOME-BUTTON:
// darkmode switch: fungerer som den skal
// home button: når du trykker på homebutton så blir acrylic sin mode i menyen resettet tilbake til darkmode,
//              mens alt det andre beholder moden sin.
// potensielle grunner:
//    - det er en state i homepage som overrider staten
//    - staten blir ikke passet fra hvor den ble endret.
//    - homebutton pusher en replacement, istedenfor å navigere tilbake til homepage.
//        selvom det ikke burde ha en effekt på menu, siden menu er (skal være) konstant.

class MenuWidget extends StatefulWidget {
  const MenuWidget({Key? key}) : super(key: key);

  @override
  MenuWidgetState createState() => MenuWidgetState();
}

enum InterfaceBrightness {
  light,
  dark,
  auto,
}

extension InterfaceBrightnessExtension on InterfaceBrightness {
  bool getIsDark(BuildContext? context) {
    if (this == InterfaceBrightness.light) return false;
    if (this == InterfaceBrightness.auto) {
      if (context == null) return true;
      return MediaQuery.of(context).platformBrightness == Brightness.dark;
    }

    return true;
  }

  Color getForegroundColor(BuildContext? context) {
    return getIsDark(context) ? Colors.white : Colors.black;
  }
}

class MenuWidgetState extends State<MenuWidget> {
  bool toggle = false;
  WindowEffect effect = WindowEffect.aero;
  Color color = Platform.isWindows ? Color(0xCC222222) : Colors.transparent;

  InterfaceBrightness brightness =
      Platform.isMacOS ? InterfaceBrightness.auto : InterfaceBrightness.dark;
  @override
  void initState() {
    super.initState();
    this.setWindowEffect(this.effect);
  }

  void setWindowEffect(WindowEffect? value) {
    Window.setEffect(
      effect: value!,
      color: this.color,
      dark: brightness == InterfaceBrightness.dark,
    );
    if (Platform.isMacOS) {
      if (brightness != InterfaceBrightness.auto) {
        Window.overrideMacOSBrightness(
            dark: brightness == InterfaceBrightness.dark);
      }
    }
    this.setState(() => this.effect = value);
  }

  void setBrightness(InterfaceBrightness brightness) {
    this.brightness = brightness;
    if (this.brightness == InterfaceBrightness.dark) {
      color = Platform.isWindows ? Color(0xCC222222) : Colors.transparent;
    } else {
      // color = Platform.isWindows ? Color(0x22DDDDDD) : Colors.transparent;
      color = Platform.isWindows
          ? Color.fromARGB(120, 255, 255, 255)
          : Colors.transparent;
    }
    this.setWindowEffect(this.effect);
  }

  final routes = [
    'Instructions',
    'View Call List',
    'Renew List',
    'Notes',
    'About',
    'Settings',
    'Feedback',
  ];

  final navigatorKey = GlobalKey<NavigatorState>();

  bool isMenuFixed(BuildContext context) {
    return MediaQuery.of(context).size.width > 250;
  }

  @override
  Widget build(BuildContext context) {
    final List<Icon> listIcons = [
      Icon(
        FontAwesomeIcons.bookReader,
        size: 15,
        color: FlutterFlowTheme.of(context).primaryText,
      ),
      Icon(
        Icons.table_rows_sharp,
        size: 15,
        color: FlutterFlowTheme.of(context).primaryText,
      ),
      Icon(
        Icons.playlist_add_sharp,
        size: 15,
        color: FlutterFlowTheme.of(context).primaryText,
      ),
      Icon(
        Icons.sticky_note_2_sharp,
        size: 15,
        color: FlutterFlowTheme.of(context).primaryText,
      ),
      Icon(
        Icons.info_sharp,
        size: 15,
        color: FlutterFlowTheme.of(context).primaryText,
      ),
      Icon(
        Icons.settings,
        size: 15,
        color: FlutterFlowTheme.of(context).primaryText,
      ),
      Icon(
        Icons.feedback_sharp,
        size: 15,
        color: FlutterFlowTheme.of(context).primaryText,
      ),
    ];

    final menu = Container(
        color: Colors.transparent,
        child: SafeArea(
            right: false,
            child: Drawer(
                backgroundColor: Colors.transparent,
                elevation: 0,
                child: Column(
                  children: [
                    WindowTitleBarBox(child: MoveWindow()),
                    Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      mainAxisSize: MainAxisSize.max,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
//
//
//
//
// ______________________ ProSpector Logo [LIGHTMODE] __________________
                        // TODO MERGE LGIHTMODE AND DARKMODE ICONS
                        if (Theme.of(context).brightness == Brightness.light)
                          Padding(
                            // padding: EdgeInsetsDirectional.fromSTEB(30, 0, 20, 0),
                            padding:
                                EdgeInsetsDirectional.fromSTEB(30, 0, 20, 20),

                            child: Container(
                              width: MediaQuery.of(context).size.width,
                              height: MediaQuery.of(context).size.height * 0.1,
                              decoration: BoxDecoration(),
                              child: InkWell(
                                //
                                //
                                onTap: () async {
                                  Navigator.pop(context);
                                  // TODO write if statement:
                                  // todo if current page == homepage, then do nothing

                                  // setState(() {
                                  //   setBrightness(InterfaceBrightness.light);
                                  // });

                                  // await Navigator.of(context).pushReplacement(
                                  //   PageTransition(
                                  //     type: PageTransitionType.fade,
                                  //     duration: Duration(milliseconds: 0),
                                  //     reverseDuration: Duration(milliseconds: 0),
                                  //     child: HomePageWidget(),
                                  //   ),
                                  // );
                                },
                                //
                                //
                                child: Image.asset(
                                  'assets/images/prospector_title_light_[lightmode].png',
                                  width: MediaQuery.of(context).size.width,
                                  height: 300,
                                  fit: BoxFit.contain,
                                ),
                              ),
                            ),
                          ),
// ____________________________________________________________________
//
//
//
// ______________________ ProSpector Logo [DARKMODE] __________________
                        if (Theme.of(context).brightness == Brightness.dark)
                          Padding(
                            // padding: EdgeInsetsDirectional.fromSTEB(30, 0, 20, 0),
                            padding:
                                EdgeInsetsDirectional.fromSTEB(30, 0, 20, 20),
                            child: Container(
                              width: MediaQuery.of(context).size.width,
                              height: MediaQuery.of(context).size.height * 0.1,
                              decoration: BoxDecoration(),
                              child: Visibility(
                                visible: Theme.of(context).brightness ==
                                    Brightness.dark,
                                child: InkWell(
                                  //
                                  //
                                  onTap: () async {
                                    Navigator.pop(context);
                                    // setState(() {
                                    //   setBrightness(InterfaceBrightness.dark);
                                    // });

                                    // await Navigator.of(context).pushReplacement(
                                    //   PageTransition(
                                    //     type: PageTransitionType.fade,
                                    //     duration: Duration(milliseconds: 0),
                                    //     reverseDuration: Duration(milliseconds: 0),
                                    //     child: HomePageWidget(),
                                    //   ),
                                    // );
                                  },
                                  //
                                  //
                                  child: Image.asset(
                                    'assets/images/prospector_title_light_[darkmode].png',
                                    width: MediaQuery.of(context).size.width,
                                    height: 300,
                                    fit: BoxFit.contain,
                                  ),
                                ),
                              ),
                            ),
                          ),
// ____________________________________________________________________
//
//
//
//

                        Padding(
                          padding: EdgeInsets.fromLTRB(20, 0, 0, 0),
                          child: Column(
                            children: <Widget>[
                              for (final pair in zip([listIcons, routes]))
                                ListTile(
                                  horizontalTitleGap: 0,
                                  minVerticalPadding: 0,
                                  dense: true,
                                  leading: pair[0] as Icon,
                                  title: Text(
                                    pair[1].toString(),
                                    style: FlutterFlowTheme.of(context)
                                        .subtitle1
                                        .override(
                                          fontFamily:
                                              FlutterFlowTheme.of(context)
                                                  .subtitle1Family,
                                          fontSize: 14,
                                          fontWeight: FontWeight.w300,
                                        ),
                                  ),
                                  onTap: () {
                                    navigatorKey.currentState
                                        ?.pushNamedAndRemoveUntil(
                                            pair[1].toString(), (r) => false);
                                  },
                                )
                            ],
                          ),
                        ),
                      ],
                    ),
                    Spacer(),
                    // Padding(
                    //   padding: const EdgeInsets.all(8.0),
                    //   child: Container(
                    //     child: ElevatedButton(
                    //         onPressed: () => Navigator.of(context).push(
                    //             PageRouteBuilder(
                    //                 opaque: false,
                    //                 pageBuilder:
                    //                     (BuildContext context, _, __) =>
                    //                         AboutWidget())),
                    //         child: Text("try me bitch")),
                    //   ),
                    // ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),
                      child: Divider(
                          // color: FlutterFlowTheme.of(context).primaryText,
                          ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(10, 5, 10, 10),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          Text(
                            'switch to ${(() {
                              switch (brightness) {
                                case InterfaceBrightness.light:
                                  return 'lightmode';
                                case InterfaceBrightness.dark:
                                  return 'darkmode';
                                default:
                                  return 'auto';
                              }
                            })()}',
                            style:
                                FlutterFlowTheme.of(context).subtitle1.override(
                                      fontFamily: FlutterFlowTheme.of(context)
                                          .subtitle1Family,
                                      fontSize: 13,
                                      fontWeight: FontWeight.w300,
                                    ),
                          ),
                          Neumorphic(
                            style: NeumorphicStyle(
                                shape: NeumorphicShape.convex,
                                boxShape: NeumorphicBoxShape.roundRect(
                                    BorderRadius.circular(30)),
                                depth: 1,
                                lightSource: LightSource.topLeft,
                                color: Colors.transparent),
                            child: SizedBox(
                              height: 35,
                              width: 35,
                              child: IconButton(
                                padding: EdgeInsets.zero,
                                iconSize: 20,
                                visualDensity: VisualDensity(),
                                splashRadius: 1,
                                icon: toggle
                                    ? Icon(
                                        Icons.dark_mode_sharp,
                                      )
                                    : Icon(
                                        Icons.light_mode_sharp,
                                      ),
                                onPressed: () => setState(() {
                                  toggle = !toggle;
                                  if (Theme.of(context).brightness ==
                                      Brightness.light) {
                                    setDarkModeSetting(context, ThemeMode.dark);
                                  } else {
                                    setDarkModeSetting(
                                        context, ThemeMode.light);
                                  }

                                  setBrightness(
                                    brightness == InterfaceBrightness.dark
                                        ? InterfaceBrightness.light
                                        : InterfaceBrightness.dark,
                                  );
                                }),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ))));
    return Row(
      children: <Widget>[
        if (isMenuFixed(context)) menu,
        Expanded(
          child: Container(
            child: Stack(
              alignment: AlignmentDirectional.topStart,
              children: [
                Expanded(
                  child: Navigator(
                    key: navigatorKey,
                    initialRoute: '/',
                    onGenerateRoute: (settings) {
                      return PageRouteBuilder(
                        opaque: false,
                        pageBuilder: (BuildContext context,
                            Animation<double> animation,
                            Animation<double> secondaryAnimation) {
                          return Scaffold(
                            body: SafeArea(
                                child:
                                    _getBodyWidget(settings.name.toString())),
                            drawer: isMenuFixed(context) ? null : menu,
                          );
                        },
                        fullscreenDialog: true,
                        transitionDuration: const Duration(milliseconds: 0),
                        settings: settings,
                      );
                    },
                  ),
                ),
                Stack(
                  children: [
                    WindowTitleBarBox(
                      child: Row(
                        // mainAxisAlignment: MainAxisAlignment.start,
                        children: [
                          Expanded(child: MoveWindow()),
                          WindowTitleBar(brightness: brightness)
                        ],
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
// // Container(
// //   child:

// //   Expanded(
// //     child: Container(
// //       child: Stack(
// //         alignment: AlignmentDirectional.topStart,
// //         children: [
// //           Expanded(
// //             child: Navigator(
// //               // key: navigatorKey,
// //               initialRoute: '/',
// //               onGenerateRoute: (settings) {
// //                 return MaterialPageRoute(
// //                     builder: (context) {
// //                       return
// //                           // Scaffold(
// //                           //   body:
// //                           SafeArea(
// //                               child:
// //                                   _getBodyWidget(settings.name.toString())
// //                               // ),
// //                               // drawer: isMenuFixed(context) ? null : menu,
// //                               );
// //                     },
// //                     settings: settings);
// //               },
// //             ),
// //           ),
// //           Stack(
// //             children: [
// //               WindowTitleBarBox(
// //                 child: Row(
// //                   // mainAxisAlignment: MainAxisAlignment.start,
// //                   children: [
// //                     Expanded(child: MoveWindow()),
// //                     WindowTitleBar(brightness: brightness)
// //                   ],
// //                 ),
// //               ),
// //             ],
// //           ),
// //         ],
// //       ),
// //     ),
// //   ),
// // );
//   }
// }

class RedeemConfirmationScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white.withOpacity(0.5),
    );
  }
}

_getBodyWidget(name) {
  switch (name) {
    case 'Instructions':
      return InstructionsWidget();
    case 'View Call List':
      return CallListWidget();
    case 'Renew List':
      return RenewListWidget();
    case 'Notes':
      return NotesWidget();
    case 'About':
      return AboutWidget();
    case 'Settings':
      return SettingsWidget();
    case 'Feedback':
      return FeedbackWidget();
    default:
      return HomeView();
  }
}

class WindowTitleBar extends StatelessWidget {
  final InterfaceBrightness brightness;
  const WindowTitleBar({Key? key, required this.brightness}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    if (Theme.of(context).brightness == Brightness.light) {}
    return Row(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        MinimizeWindowButton(
          colors: WindowButtonColors(
            iconNormal: Theme.of(context).brightness == Brightness.light
                ? Colors.black
                : Colors.white,
            iconMouseDown: Theme.of(context).brightness == Brightness.light
                ? Colors.black
                : Colors.white,
            iconMouseOver: Theme.of(context).brightness == Brightness.light
                ? Colors.black
                : Colors.white,
            normal: Colors.transparent,
            mouseOver: Theme.of(context).brightness == Brightness.light
                ? Color.fromARGB(70, 222, 222, 222)
                : Color.fromARGB(45, 134, 134, 134),
            mouseDown: Theme.of(context).brightness == Brightness.light
                ? Color.fromARGB(45, 134, 134, 134)
                : Color.fromARGB(140, 134, 134, 134),
          ),
        ),
        MaximizeWindowButton(
          colors: WindowButtonColors(
            iconNormal: Theme.of(context).brightness == Brightness.light
                ? Colors.black
                : Colors.white,
            iconMouseDown: Theme.of(context).brightness == Brightness.light
                ? Colors.black
                : Colors.white,
            iconMouseOver: Theme.of(context).brightness == Brightness.light
                ? Colors.black
                : Colors.white,
            normal: Colors.transparent,
            mouseOver: Theme.of(context).brightness == Brightness.light
                ? Color.fromARGB(70, 222, 222, 222)
                : Color.fromARGB(45, 134, 134, 134),
            mouseDown: Theme.of(context).brightness == Brightness.light
                ? Color.fromARGB(45, 134, 134, 134)
                : Color.fromARGB(140, 134, 134, 134),
          ),
        ),
        CloseWindowButton(
          onPressed: () {
            appWindow.close();
          },
          colors: WindowButtonColors(
            iconNormal: Theme.of(context).brightness == Brightness.light
                ? Colors.black
                : Colors.white,
            iconMouseDown: Colors.white,
            iconMouseOver: Colors.white,
            normal: Colors.transparent,
            mouseOver: Theme.of(context).brightness == Brightness.light
                ? Color.fromARGB(200, 211, 47, 47)
                : Color.fromARGB(200, 255, 57, 57),
            mouseDown: Theme.of(context).brightness == Brightness.light
                ? Color.fromARGB(255, 211, 47, 47)
                : Color.fromARGB(255, 255, 57, 57),
          ),
        ),
      ],
    );
  }
}
