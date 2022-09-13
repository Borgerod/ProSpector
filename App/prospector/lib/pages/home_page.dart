import 'package:flutter/material.dart';

class HomeView extends StatefulWidget {
  const HomeView({Key? key}) : super(key: key);
  @override
  HomeViewState createState() => HomeViewState();
}

class HomeViewState extends State<HomeView> {
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Container(
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
          child: Image.asset(
            'assets/images/dark3.png',
            width: MediaQuery.of(context).size.width,
            height: MediaQuery.of(context).size.height * 1,
            fit: BoxFit.cover,
          ),
        ),
        if (Theme.of(context).brightness == Brightness.light)
          Container(
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
            child: Image.asset(
              'assets/images/light2.png',
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height * 1,
              fit: BoxFit.cover,
            ),
          ),
      ],
    );
  }
}
