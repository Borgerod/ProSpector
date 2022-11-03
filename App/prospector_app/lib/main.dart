import 'package:flutter/material.dart';
import 'dart:io';

import 'package:flutter_acrylic/flutter_acrylic.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:file_picker/file_picker.dart';
import 'package:open_file/open_file.dart';
import 'package:path/path.dart' as p;

import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:prospector_app/flutter_flow/internationalization.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_util.dart';
import 'package:prospector_app/index.dart';
import 'package:prospector_app/pages/loading_page.dart';

Future<void> main() async {
  await runServer();
  WidgetsFlutterBinding.ensureInitialized();
  await Hive.initFlutter();
  await FlutterFlowTheme.initialize();
  await Window.initialize();
  if (Platform.isWindows) {
    await Window.hideWindowControls();
  }
  // initDocs() async {
  //   final appDocsDir = await getApplicationDocumentsDirectory();
  //   Hive.init(appDocsDir.path);
  // }

  WidgetsFlutterBinding.ensureInitialized();
  FFAppState();

  runApp(MyApp());
  if (Platform.isWindows) {
    doWhenWindowReady(() {
      appWindow
        // // ..minSize = Size(640, 360)
        // // ..size = Size(720, 540)
        ..minSize = const Size(954, 580)
        ..size = const Size(954, 580)
        // ..minSize = Size(954, 650)
        // ..size = Size(954, 650)
        ..alignment = Alignment.center
        ..show();
    });
  }
}

Future<void> runServer() async {
  /*
   Runs FastAPI Server when called on startup
  */
  String? filePath = '';
  var absPath = p.absolute('run_server.bat');
  FilePickerResult? result = FilePickerResult([
    PlatformFile(
        path: absPath,
        name: "run_server.bat",
        bytes: null,
        readStream: null,
        size: 0)
  ]);
  filePath = result.files.single.path;
  await OpenFile.open(filePath);
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
      const Duration(seconds: 1),
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
      localizationsDelegates: const [
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
      home: FutureBuilder(
        future: _processingData(),
        builder: (BuildContext context, AsyncSnapshot snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return LoadingScreen();
          } else {
            return const LoginWidget();
          }
        },
      ),
    );
  }

  Future _processingData() {
    // return new Future.delayed(const Duration(seconds: 5), () => 1);
    //> removed unnessasary "new" keyword
    return Future.delayed(const Duration(seconds: 5), () => 1);
  }
}
