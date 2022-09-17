import 'package:flutter/material.dart';
import 'dart:io';

import 'package:flutter_acrylic/flutter_acrylic.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:hive/hive.dart';

import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:prospector/flutter_flow/internationalization.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/pages/login_page_test.dart'; //! TESTING
import 'package:prospector/index.dart';

Future<void> main() async {
  await Hive.initFlutter(); //! TESTING
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
        // ..minSize = Size(640, 360)
        // ..size = Size(720, 540)
        ..minSize = Size(954, 580)
        ..size = Size(954, 580)
        ..alignment = Alignment.center
        ..show();
    });
  }
}

class MyApp extends StatefulWidget {
  // This widget is the root of your application.
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

  void setLocale(String language) =>
      setState(() => _locale = createLocale(language));
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
      home: ResetPasswordAuthenticationWidget(),
      // home: Login_Page(),
      // home: LoginWidget(),
      // home: MenuWidget(),
    );
  }
}
