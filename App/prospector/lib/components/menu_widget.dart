// ignore_for_file: deprecated_member_use

import 'dart:io';
import 'package:quiver/iterables.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:flutter_acrylic/flutter_acrylic.dart';
import 'package:flutter_neumorphic/flutter_neumorphic.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/components/window_title_bar.dart';
import 'package:prospector/popups/renew_list_widget.dart';
import 'package:prospector/popups/settings_widget.dart';
import 'package:prospector/popups/feedback_widget.dart';
import 'package:prospector/popups/about_widget.dart';
import 'package:prospector/pages/instructions_page.dart';
import 'package:prospector/pages/call_list_widget.dart';
import 'package:prospector/pages/notes_page.dart';
import 'package:prospector/pages/home_page.dart';

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
  Color color = Color(0xCC222222);
  InterfaceBrightness brightness = InterfaceBrightness.dark;

  @override
  void initState() {
    super.initState();
    setBrightness(brightness);
    this.setWindowEffect(this.effect);
    if (Platform.isWindows) {
      doWhenWindowReady(() {
        appWindow
          ..minSize = Size(1050, 650)
          ..size = Size(1450, 750)
          ..alignment = Alignment.center
          ..show();
      });
    }
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
    final theme = FlutterFlowTheme.themeMode;
    if (theme == ThemeMode.dark) {
      brightness = InterfaceBrightness.dark;
      color = Color(0xCC222222);
    } else {
      color = Platform.isWindows
          ? color = Color.fromARGB(120, 255, 255, 255)
          : Colors.transparent;

      brightness = InterfaceBrightness.light;
    }
    this.setWindowEffect(this.effect);
  }

  final routes = [
    'Instructions',
    'View Call List',
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
                  if (Theme.of(context).brightness == Brightness.light)
                    Padding(
                      padding: EdgeInsetsDirectional.fromSTEB(30, 0, 20, 20),
                      child: Container(
                        width: MediaQuery.of(context).size.width,
                        height: MediaQuery.of(context).size.height * 0.1,
                        decoration: BoxDecoration(),
                        child: Image.asset(
                          'assets/images/logo_text_small[lightmode].png',
                          width: MediaQuery.of(context).size.width,
                          height: 300,
                          fit: BoxFit.contain,
                        ),
                      ),
                    ),
                  if (Theme.of(context).brightness == Brightness.dark)
                    Padding(
                      padding: EdgeInsetsDirectional.fromSTEB(30, 0, 20, 20),
                      child: Container(
                        width: MediaQuery.of(context).size.width,
                        height: MediaQuery.of(context).size.height * 0.1,
                        decoration: BoxDecoration(),
                        child: Visibility(
                          visible:
                              Theme.of(context).brightness == Brightness.dark,
                          child: Image.asset(
                            'assets/images/logo_text_small[darkmode].png',
                            width: MediaQuery.of(context).size.width,
                            height: 300,
                            fit: BoxFit.contain,
                          ),
                        ),
                      ),
                    ),
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
                                    fontFamily: FlutterFlowTheme.of(context)
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
                          ),
                        ListTile(
                          horizontalTitleGap: 0,
                          minVerticalPadding: 0,
                          dense: true,
                          leading: Icon(
                            Icons.playlist_add_sharp,
                            size: 15,
                            color: FlutterFlowTheme.of(context).primaryText,
                          ),
                          title: Text(
                            'Renew List',
                            style:
                                FlutterFlowTheme.of(context).subtitle1.override(
                                      fontFamily: FlutterFlowTheme.of(context)
                                          .subtitle1Family,
                                      fontSize: 14,
                                      fontWeight: FontWeight.w300,
                                    ),
                          ),
                          onTap: () {
                            Navigator.of(context).push(PageRouteBuilder(
                                opaque: false,
                                pageBuilder: (BuildContext context, _, __) =>
                                    RenewListWidget()));
                          },
                        ),
                        ListTile(
                          horizontalTitleGap: 0,
                          minVerticalPadding: 0,
                          dense: true,
                          leading: Icon(
                            Icons.sticky_note_2_sharp,
                            size: 15,
                            color: FlutterFlowTheme.of(context).primaryText,
                          ),
                          title: Text(
                            'Notes',
                            style:
                                FlutterFlowTheme.of(context).subtitle1.override(
                                      fontFamily: FlutterFlowTheme.of(context)
                                          .subtitle1Family,
                                      fontSize: 14,
                                      fontWeight: FontWeight.w300,
                                    ),
                          ),
                          onTap: () {
                            navigatorKey.currentState?.pushNamedAndRemoveUntil(
                                'Notes'.toString(), (r) => false);
                          },
                        ),
                        ListTile(
                          horizontalTitleGap: 0,
                          minVerticalPadding: 0,
                          dense: true,
                          leading: Icon(
                            Icons.info_sharp,
                            size: 15,
                            color: FlutterFlowTheme.of(context).primaryText,
                          ),
                          title: Text(
                            'About',
                            style:
                                FlutterFlowTheme.of(context).subtitle1.override(
                                      fontFamily: FlutterFlowTheme.of(context)
                                          .subtitle1Family,
                                      fontSize: 14,
                                      fontWeight: FontWeight.w300,
                                    ),
                          ),
                          onTap: () {
                            Navigator.of(context).push(
                              PageRouteBuilder(
                                opaque: false,
                                pageBuilder: (BuildContext context, _, __) =>
                                    AboutWidget(),
                              ),
                            );
                          },
                        ),
                        ListTile(
                          horizontalTitleGap: 0,
                          minVerticalPadding: 0,
                          dense: true,
                          leading: Icon(
                            Icons.settings,
                            size: 15,
                            color: FlutterFlowTheme.of(context).primaryText,
                          ),
                          title: Text(
                            'settings',
                            style:
                                FlutterFlowTheme.of(context).subtitle1.override(
                                      fontFamily: FlutterFlowTheme.of(context)
                                          .subtitle1Family,
                                      fontSize: 14,
                                      fontWeight: FontWeight.w300,
                                    ),
                          ),
                          onTap: () {
                            Navigator.of(context).push(
                              PageRouteBuilder(
                                opaque: false,
                                pageBuilder: (BuildContext context, _, __) =>
                                    SettingsWidget(),
                              ),
                            );
                          },
                        ),
                        ListTile(
                          horizontalTitleGap: 0,
                          minVerticalPadding: 0,
                          dense: true,
                          leading: Icon(
                            Icons.feedback_sharp,
                            size: 15,
                            color: FlutterFlowTheme.of(context).primaryText,
                          ),
                          title: Text(
                            'Feedback',
                            style:
                                FlutterFlowTheme.of(context).subtitle1.override(
                                      fontFamily: FlutterFlowTheme.of(context)
                                          .subtitle1Family,
                                      fontSize: 14,
                                      fontWeight: FontWeight.w300,
                                    ),
                          ),
                          onTap: () {
                            Navigator.of(context).push(
                              PageRouteBuilder(
                                opaque: false,
                                pageBuilder: (BuildContext context, _, __) =>
                                    FeedbackWidget(),
                              ),
                            );
                          },
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              Spacer(),
              Padding(
                padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),
                child: Divider(),
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
                      style: FlutterFlowTheme.of(context).subtitle1.override(
                            fontFamily:
                                FlutterFlowTheme.of(context).subtitle1Family,
                            fontSize: 13,
                            fontWeight: FontWeight.w300,
                          ),
                    ),
                    Neumorphic(
                      style: NeumorphicStyle(
                          shape: NeumorphicShape.convex,
                          boxShape: NeumorphicBoxShape.roundRect(
                            BorderRadius.circular(30),
                          ),
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
                          onPressed: () => setState(
                            () {
                              toggle = !toggle;
                              if (Theme.of(context).brightness ==
                                  Brightness.light) {
                                setDarkModeSetting(context, ThemeMode.dark);
                              } else {
                                setDarkModeSetting(context, ThemeMode.light);
                              }
                              sleep(Duration(milliseconds: 200));
                              setBrightness(
                                brightness == InterfaceBrightness.dark
                                    ? InterfaceBrightness.light
                                    : InterfaceBrightness.dark,
                              );
                            },
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
    return Row(
      children: <Widget>[
        if (isMenuFixed(context)) menu,
        Expanded(
          child: Container(
            decoration: BoxDecoration(
              boxShadow: [
                BoxShadow(
                  blurRadius: 10,
                  color: Color(0x33000000),
                  offset: Offset(-10, 0),
                )
              ],
              image: DecorationImage(
                fit: BoxFit.cover,
                image: Image.asset(
                  getImage(context),
                ).image,
              ),
            ),
            child: Column(
              children: [
                WindowTitleBarBox(
                  child: Row(
                    children: [
                      Expanded(
                        child: MoveWindow(),
                      ),
                      WindowTitleBar(brightness: brightness)
                    ],
                  ),
                ),
                Container(
                  width: MediaQuery.of(context).size.width,
                  height: MediaQuery.of(context).size.height * 0.95,
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
                              child: _getBodyWidget(
                                settings.name.toString(),
                              ),
                            ),
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
              ],
            ),
          ),
        ),
      ],
    );
  }

  String getImage(context) {
    if (Theme.of(context).brightness == Brightness.light) {
      return 'assets/images/light2.png';
    } else {
      return 'assets/images/dark3.png';
    }
  }
}

_getBodyWidget(name) {
  switch (name) {
    case 'Instructions':
      return InstructionsWidget();
    case 'View Call List':
      return CallListWidget();
    case 'Notes':
      return NotesWidget();
    case 'HomeView':
      return HomeView();
    default:
      return HomeView();
  }
}
