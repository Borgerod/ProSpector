import 'package:flutter/material.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';

import 'package:flutter_acrylic/flutter_acrylic.dart';

import 'dart:io';

import 'package:quiver/iterables.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(
        title: '',
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final String title;

  const MyHomePage({Key? key, required this.title}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // final routes = List.generate(20, (i) => 'test $i');
  final routes = [
    'ScreenOne',
    'ScreenTwo',
  ];

  final navigatorKey = GlobalKey<NavigatorState>();

  bool isMenuFixed(BuildContext context) {
    return MediaQuery.of(context).size.width > 500;
  }
  // String nav = settings.name.toString();

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    final List<Icon> listIcons = [
      Icon(
        Icons.menu_book_sharp,
        size: 15,
      ),
      Icon(
        Icons.table_rows_sharp,
        size: 15,
      ),
      Icon(
        Icons.playlist_add_sharp,
        size: 15,
      ),
      Icon(
        Icons.sticky_note_2_sharp,
        size: 15,
      ),
      Icon(
        Icons.info_sharp,
        size: 15,
      ),
      Icon(
        Icons.settings,
        size: 15,
      ),
      Icon(
        Icons.feedback_sharp,
        size: 15,
      ),
    ];
    final menu = Container(
        color: theme.canvasColor,
        child: SafeArea(
            right: false,
            child: Drawer(
                elevation: 0,

                //       SizedBox(
                // width: 250,
                // width: 300,
                child: Column(
                  children: [
                    WindowTitleBarBox(child: MoveWindow()),
                    Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      mainAxisSize: MainAxisSize.max,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        if (Theme.of(context).brightness == Brightness.dark)
                          Padding(
                            padding:
                                EdgeInsetsDirectional.fromSTEB(30, 0, 20, 20),
                            child: Container(
                              width: MediaQuery.of(context).size.width,
                              height: MediaQuery.of(context).size.height * 0.1,
                              decoration: BoxDecoration(),
                              child: Visibility(
                                visible: Theme.of(context).brightness ==
                                    Brightness.dark,
                                child: InkWell(
                                    onTap: () async {
                                      Navigator.pop(context);
                                    },
                                    child: Container(
                                      child: Text("I AM LOGO "),
                                    )),
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
                                  ),
                                  onTap: () {
                                    // Using navigator key, because the widget is above nested navigator
                                    navigatorKey.currentState
                                        ?.pushNamedAndRemoveUntil(
                                            pair[1].toString(), (r) => false);
                                  },
                                )
                            ],
                          ),
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
                          Container(
                            child: Text('I AM DARKMODE SWITCH '),
                          )
                        ],
                      ),
                    ),
                  ],
                ))));

    // final menu = Container(
    //     color: theme.canvasColor,
    //     child: SafeArea(
    //         right: false,
    //         child: Drawer(
    //           elevation: 0,
    //           child: ListView(
    //             children: <Widget>[
    //               for (final s in routes)
    //                 ListTile(
    //                   title: Text(s),
    //                   onTap: () {
    //                     // Using navigator key, because the widget is above nested navigator
    //                     navigatorKey.currentState
    //                         ?.pushNamedAndRemoveUntil(s, (r) => false);

    //                     // navigatorKey.currentState.pushNamed(s);
    //                   },
    //                 ),
    //             ],
    //           ),
    //         )));

    return Row(
      children: <Widget>[
        if (isMenuFixed(context)) menu,
        Expanded(
          child: Navigator(
            key: navigatorKey,
            initialRoute: '/',
            onGenerateRoute: (settings) {
              return MaterialPageRoute(
                  builder: (context) {
                    return Scaffold(
                      body: SafeArea(
                          child: _getBodyWidget(settings.name.toString())

                          // Text(settings.name.toString()),
                          ),
                      drawer: isMenuFixed(context) ? null : menu,
                    );
                  },
                  settings: settings);
            },
          ),
        ),
      ],
    );
  }

  _getBodyWidget(name) {
    switch (name) {
      case 'ScreenOne':
        return ScreenOne();
      case 'ScreenTwo':
        return ScreenTwo();
      default:
        return HomeView();
    }
  }
}

class HomeView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Expanded(
        child: Container(
      color: Colors.white,
      child: Text('HOME'),
    ));
  }
}

class ScreenOne extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Expanded(
        child: Container(
      color: Colors.amberAccent,
    ));
  }
}

class ScreenTwo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Expanded(
        child: Container(
      color: Colors.blueAccent,
    ));
  }
}

class WindowTitleBar extends StatelessWidget {
  // final InterfaceBrightness brightness;
  // const WindowTitleBar({Key? key, required this.brightness}) : super(key: key);

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
