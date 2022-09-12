import 'package:font_awesome_flutter/font_awesome_flutter.dart';
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

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 250,
        // width: 300,
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
                    padding: EdgeInsetsDirectional.fromSTEB(30, 0, 20, 20),

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
                    padding: EdgeInsetsDirectional.fromSTEB(30, 0, 20, 20),
                    child: Container(
                      width: MediaQuery.of(context).size.width,
                      height: MediaQuery.of(context).size.height * 0.1,
                      decoration: BoxDecoration(),
                      child: Visibility(
                        visible:
                            Theme.of(context).brightness == Brightness.dark,
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

                Column(
                  children: [
                    TextButton(
                      onPressed: () async {
                        setBrightness(
                          brightness == InterfaceBrightness.dark
                              ? InterfaceBrightness.dark
                              : InterfaceBrightness.light,
                        );
                        await Navigator.push(
                          context,
                          PageTransition(
                            type: PageTransitionType.fade,
                            duration: Duration(milliseconds: 0),
                            reverseDuration: Duration(milliseconds: 0),
                            child: InstructionsWidget(),
                          ),
                        );
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(
                            Colors.transparent),
                      ),
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(20, 10, 0, 0),
                        child: Row(
                          children: [
                            FaIcon(
                              FontAwesomeIcons.bookReader,
                              size: 15,
                              color: FlutterFlowTheme.of(context).primaryText,
                            ),
                            SizedBox(width: 20),
                            Text(
                              FFLocalizations.of(context)
                                  .getText('c4xwrvgn' /* Instructions*/),
                              style: FlutterFlowTheme.of(context)
                                  .subtitle1
                                  .override(
                                    fontFamily: FlutterFlowTheme.of(context)
                                        .subtitle1Family,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w300,
                                  ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    TextButton(
                      onPressed: () async {
                        await Navigator.push(
                          context,
                          PageTransition(
                            type: PageTransitionType.fade,
                            duration: Duration(milliseconds: 0),
                            reverseDuration: Duration(milliseconds: 0),
                            child: CallListWidget(),
                          ),
                        );
                      },
                      style: ButtonStyle(
                          backgroundColor: MaterialStateProperty.all<Color>(
                              Colors.transparent)),
                      // MaterialStateProperty.all<Color>(
                      // Colors.transparent),
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(20, 10, 0, 0),
                        child: Row(
                          children: [
                            FaIcon(
                              Icons.table_rows_sharp,
                              size: 15,
                              color: FlutterFlowTheme.of(context).primaryText,
                            ),
                            SizedBox(width: 20),
                            Text(
                              FFLocalizations.of(context).getText(
                                'dl8jkd4c' /* View Call List*/,
                              ),
                              style: FlutterFlowTheme.of(context)
                                  .subtitle1
                                  .override(
                                    fontFamily: FlutterFlowTheme.of(context)
                                        .subtitle1Family,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w300,
                                  ),
                            ),
                          ],
                        ),
                      ),
                    ),

                    TextButton(
                      onPressed: () async {
                        await Navigator.push(
                          context,
                          PageTransition(
                            type: PageTransitionType.fade,
                            duration: Duration(milliseconds: 0),
                            reverseDuration: Duration(milliseconds: 0),
                            child: RenewListWidget(),
                          ),
                        );
                      },
                      style: ButtonStyle(
                          backgroundColor: MaterialStateProperty.all<Color>(
                              Colors.transparent)),
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(20, 10, 0, 0),
                        child: Row(
                          children: [
                            FaIcon(
                              Icons.playlist_add_sharp,
                              size: 15,
                              color: FlutterFlowTheme.of(context).primaryText,
                            ),
                            SizedBox(width: 20),
                            Text(
                              FFLocalizations.of(context)
                                  .getText('pviup14g' /* Renew List */),
                              style: FlutterFlowTheme.of(context)
                                  .subtitle1
                                  .override(
                                    fontFamily: FlutterFlowTheme.of(context)
                                        .subtitle1Family,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w300,
                                  ),
                            ),
                          ],
                        ),
                      ),
                    ),

                    TextButton(
                      onPressed: () async {
                        await Navigator.push(
                          context,
                          PageTransition(
                            type: PageTransitionType.fade,
                            duration: Duration(milliseconds: 0),
                            reverseDuration: Duration(milliseconds: 0),
                            child: NotesWidget(),
                          ),
                        );
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(
                            Colors.transparent),
                      ),
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(20, 10, 0, 0),
                        child: Row(
                          children: [
                            Icon(
                              Icons.sticky_note_2_sharp,
                              size: 15,
                              color: FlutterFlowTheme.of(context).primaryText,
                            ),
                            SizedBox(width: 20),
                            Text(
                              FFLocalizations.of(context)
                                  .getText('mojlgs22' /* Notes*/),
                              style: FlutterFlowTheme.of(context)
                                  .subtitle1
                                  .override(
                                    fontFamily: FlutterFlowTheme.of(context)
                                        .subtitle1Family,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w300,
                                  ),
                            ),
                          ],
                        ),
                      ),
                    ),

                    TextButton(
                      onPressed: () async {
                        await Navigator.push(
                          context,
                          PageTransition(
                            type: PageTransitionType.fade,
                            duration: Duration(milliseconds: 0),
                            reverseDuration: Duration(milliseconds: 0),
                            child: AboutWidget(),
                          ),
                        );
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(
                            Colors.transparent),
                      ),
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(20, 10, 0, 0),
                        child: Row(
                          children: [
                            Icon(
                              Icons.info_sharp,
                              size: 15,
                              color: FlutterFlowTheme.of(context).primaryText,
                            ),
                            SizedBox(width: 20),
                            Text(
                              FFLocalizations.of(context)
                                  .getText('xdz4v725' /* About*/),
                              style: FlutterFlowTheme.of(context)
                                  .subtitle1
                                  .override(
                                    fontFamily: FlutterFlowTheme.of(context)
                                        .subtitle1Family,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w300,
                                  ),
                            ),
                          ],
                        ),
                      ),
                    ),

                    TextButton(
                      onPressed: () async {
                        await Navigator.push(
                          context,
                          PageTransition(
                            type: PageTransitionType.fade,
                            duration: Duration(milliseconds: 300),
                            reverseDuration: Duration(milliseconds: 300),
                            child: SettingsWidget(),
                          ),
                        );
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(
                            Colors.transparent),
                      ),
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(20, 10, 0, 0),
                        child: Row(
                          children: [
                            Icon(
                              Icons.settings,
                              size: 15,
                              color: FlutterFlowTheme.of(context).primaryText,
                            ),
                            SizedBox(width: 20),
                            Text(
                              FFLocalizations.of(context)
                                  .getText('o9mimblc' /* Settings*/),
                              style: FlutterFlowTheme.of(context)
                                  .subtitle1
                                  .override(
                                    fontFamily: FlutterFlowTheme.of(context)
                                        .subtitle1Family,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w300,
                                  ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    // FEEDBACK
                    TextButton(
                      onPressed: () async {
                        await Navigator.push(
                          context,
                          PageTransition(
                            type: PageTransitionType.fade,
                            duration: Duration(milliseconds: 0),
                            reverseDuration: Duration(milliseconds: 0),
                            child: FeedbackWidget(),
                          ),
                        );
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(
                            Colors.transparent),
                      ),
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(20, 10, 0, 0),
                        child: Row(
                          children: [
                            Icon(
                              Icons.feedback_sharp,
                              size: 15,
                              color: FlutterFlowTheme.of(context).primaryText,
                            ),
                            SizedBox(width: 20),
                            Text(
                              FFLocalizations.of(context)
                                  .getText('md0rr0g2' /* FeedBack */),
                              style: FlutterFlowTheme.of(context)
                                  .subtitle1
                                  .override(
                                    fontFamily: FlutterFlowTheme.of(context)
                                        .subtitle1Family,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w300,
                                  ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
            Spacer(),
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
                            setDarkModeSetting(context, ThemeMode.light);
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
        ));
  }
}
