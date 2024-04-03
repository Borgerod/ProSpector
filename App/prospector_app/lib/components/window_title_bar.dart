import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:flutter/material.dart';
import 'package:prospector_app/components/menu_widget.dart';

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
