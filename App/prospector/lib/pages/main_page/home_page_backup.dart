import 'package:prospector/components/home_button_widget.dart';
import 'package:prospector/components/menu_widget.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:flutter_acrylic/flutter_acrylic.dart';
import 'package:flutter/material.dart';
import 'dart:io';

class HomePageWidget extends StatefulWidget {
  const HomePageWidget({Key? key}) : super(key: key);

  @override
  _HomePageWidgetState createState() => _HomePageWidgetState();
}

class _HomePageWidgetState extends State<HomePageWidget> {
  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.transparent,
      key: scaffoldKey,
      // backgroundColor: FlutterFlowTheme.of(context).tertiaryColor,
      floatingActionButton: HomeButton(),
      body: Row(
        children: const [MenuWidget(), RightSide()],
      ),

      // Row(
      //   mainAxisSize: MainAxisSize.max,
      //   children: [
      //     MenuWidget(),
      //     Expanded(
      //       child: UIbackGroundWidget(),
      //     ),
      //   ],
      // ),
      // ),
    );
  }
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

//
//
//
//
//
//
//
//
//
//
//

//  ____________________________________________ RIGHT SIDE
//
//
//
//
//
//
//
//
//
//
//
//
//

class RightSide extends StatefulWidget {
  const RightSide({Key? key}) : super(key: key);

  // }
  @override
  RightSideState createState() => RightSideState();
}

class RightSideState extends State<RightSide> {
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
      color = Platform.isWindows ? Color(0x22DDDDDD) : Colors.transparent;
    }
    this.setWindowEffect(this.effect);
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Expanded(
        child: Container(
          // decoration: const BoxDecoration(
          //   color: ,
          //   // gradient: LinearGradient(
          //   //     begin: Alignment.topCenter,
          //   //     end: Alignment.bottomCenter,
          //   //     colors: [backgroundStartColor, backgroundEndColor],
          //   //     stops: [0.0, 1.0]),
          // ),
          child: Stack(
            alignment: AlignmentDirectional.topStart,
            children: [
              Stack(
                children: [
                  Image.asset(
                    'assets/images/dark3.png',
                    width: MediaQuery.of(context).size.width,
                    height: MediaQuery.of(context).size.height * 1,
                    fit: BoxFit.cover,
                  ),
                  if (Theme.of(context).brightness == Brightness.light)
                    Image.asset(
                      'assets/images/light2.png',
                      width: MediaQuery.of(context).size.width,
                      height: MediaQuery.of(context).size.height * 1,
                      fit: BoxFit.cover,
                    ),
                ],
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
    );
  }
}

// ______________________________________________ WINDOWS BUTTONS ______________

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
            // Theme.of(context).brightness == Brightness.light
            //     ? Colors.black
            //     : Colors.white,
            iconMouseOver: Colors.white,
            // Theme.of(context).brightness == Brightness.light
            //     ? Colors.black
            //     : Colors.white,
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
