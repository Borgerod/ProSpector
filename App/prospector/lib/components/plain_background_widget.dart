import 'package:flutter/material.dart';

class PlainBackgroundWidget extends StatefulWidget {
  const PlainBackgroundWidget({Key? key}) : super(key: key);

  @override
  _PlainBackgroundWidgetState createState() => _PlainBackgroundWidgetState();
}

class _PlainBackgroundWidgetState extends State<PlainBackgroundWidget> {
  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      elevation: 50,
      child: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height * 1,
        decoration: BoxDecoration(
          color: Color(0xFF0C0C0A),
          boxShadow: [
            BoxShadow(
              blurRadius: 10,
              color: Color(0x33000000),
              offset: Offset(-10, 0),
            )
          ],
        ),
        child: Stack(
          children: [
            Image.asset(
              'assets/images/darkmode_plain.png',
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height * 1,
              fit: BoxFit.cover,
            ),
            if (Theme.of(context).brightness == Brightness.light)
              Image.asset(
                'assets/images/lightmode_plain.png',
                width: MediaQuery.of(context).size.width,
                height: MediaQuery.of(context).size.height * 1,
                fit: BoxFit.cover,
              ),
          ],
        ),
      ),
    );
  }
}
