import 'package:flutter/material.dart';

class HomeView extends StatefulWidget {
  const HomeView({Key? key}) : super(key: key);
  @override
  HomeViewState createState() => HomeViewState();
}

class HomeViewState extends State<HomeView> {
  final scaffoldKey = GlobalKey<ScaffoldState>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      //* __ COLOR __
      backgroundColor: Colors.transparent,
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            fit: BoxFit.cover,
            image: Image.asset(
              getImage(context),
            ).image,
          ),
        ),
      ),
    );
  }
}

String getImage(context) {
  if (Theme.of(context).brightness == Brightness.light) {
    return 'assets/images/light2.png';
  } else {
    return 'assets/images/dark3.png';
  }
}
