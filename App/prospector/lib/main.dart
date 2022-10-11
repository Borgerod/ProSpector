import 'package:flutter/material.dart';
import 'dart:io';

import 'package:flutter_acrylic/flutter_acrylic.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:hive_flutter/hive_flutter.dart';

import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:prospector/flutter_flow/internationalization.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/pages/loading_page.dart';
import 'package:prospector/index.dart';
import 'package:prospector/components/update_widget.dart';

Future<void> main() async {
  await Hive.initFlutter();
  await FlutterFlowTheme.initialize();
  await Window.initialize();
  if (Platform.isWindows) {
    await Window.hideWindowControls();
  }

  WidgetsFlutterBinding.ensureInitialized();
  FFAppState();

  runApp(MyApp());
  if (Platform.isWindows) {
    doWhenWindowReady(() {
      appWindow
        // // ..minSize = Size(640, 360)
        // // ..size = Size(720, 540)
        ..minSize = Size(954, 580)
        ..size = Size(954, 580)
        // ..minSize = Size(954, 650)
        // ..size = Size(954, 650)
        ..alignment = Alignment.center
        ..show();
    });
  }
}

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();

  static _MyAppState of(BuildContext context) =>
      context.findAncestorStateOfType<_MyAppState>()!;
}

class _MyAppState extends State<MyApp> {
  Locale? _locale;

  ThemeMode _themeMode = FlutterFlowTheme.themeMode;

  bool displaySplashImage = true;

  @override
  void initState() {
    super.initState();
    Future.delayed(
      Duration(seconds: 1),
      () => setState(() => displaySplashImage = false),
    );
  }

  void setLocale(String language) {
    return setState(() => _locale = createLocale(language));
  }

  void setThemeMode(ThemeMode mode) => setState(() {
        _themeMode = mode;
        FlutterFlowTheme.saveThemeMode(mode);
      });

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Prospector',
      localizationsDelegates: [
        FFLocalizationsDelegate(),
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      locale: _locale,
      supportedLocales: const [
        Locale('en'),
        Locale('nb'),
      ],
      theme: ThemeData(brightness: Brightness.light),
      darkTheme: ThemeData(brightness: Brightness.dark),
      themeMode: _themeMode,
      //! TEMP - remove later
      // home: LoginWidget(),

      //! KEEP THIS
      home: FutureBuilder(
        future: _processingData(),
        builder: (BuildContext context, AsyncSnapshot snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            // if (UpdateWidget.) {}
            return LoadingScreen();
          } else {
            return const LoginWidget();
          }
        },
      ),
    );
  }

  Future _processingData() {
    return new Future.delayed(const Duration(seconds: 5), () => 1);
  }
}
