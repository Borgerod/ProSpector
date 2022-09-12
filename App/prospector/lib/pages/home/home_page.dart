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
    );
  }
}
