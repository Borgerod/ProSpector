import 'package:flutter/material.dart';

String getImage(context) {
  if (Theme.of(context).brightness == Brightness.light) {
    return 'assets/images/lightmode_plain.png';
  } else {
    return 'assets/images/darkmode_plain.png';
  }
}

class PlainBackgroundWidget extends StatefulWidget {
  const PlainBackgroundWidget({Key? key}) : super(key: key);

  @override
  _PlainBackgroundWidgetState createState() => _PlainBackgroundWidgetState();
}

class _PlainBackgroundWidgetState extends State<PlainBackgroundWidget> {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.amber,
    );
  }
}
