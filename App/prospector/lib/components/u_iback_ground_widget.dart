import 'package:flutter/material.dart';

class UIbackGroundWidget extends StatefulWidget {
  const UIbackGroundWidget({Key? key}) : super(key: key);

  @override
  _UIbackGroundWidgetState createState() => _UIbackGroundWidgetState();
}

class _UIbackGroundWidgetState extends State<UIbackGroundWidget> {
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
      ),
    );
  }
}
