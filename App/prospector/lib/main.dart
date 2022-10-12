import 'package:flutter/material.dart';
import 'dart:io';

import 'package:flutter_acrylic/flutter_acrylic.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:file_picker/file_picker.dart';
import 'package:open_file/open_file.dart';
import 'package:path/path.dart' as p;
import 'package:process_run/shell_run.dart';
import 'package:workmanager/workmanager.dart';

import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:prospector/flutter_flow/internationalization.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/pages/loading_page.dart';
import 'package:prospector/index.dart';

Future<void> main() async {
  // await shell.run(
  //     'cd build/windows/runner/Release/api_server/server_backend/fast_api_server/backend');

  await runServer();
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

// Future<void> runServer() async {
//   var shell = Shell();
//   await shell.run(
//       'cd build/windows/runner/Release/api_server/server_backend/fast_api_server/backend && uvicorn main:app --reload');
// }

Future<void> runServer() async {
  /*
   Runs FastAPI Server when called on startup
  */
  String? filePath = '';
  // build\windows\runner\Release','run_server.bat

// C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\

  var absPath =
      // p.absolute('build', 'windows', 'runner', 'Release', 'run_server.bat');
      p.absolute('run_server.bat');
  // p.absolute('build', 'windows', 'runner', 'Release', 'launch.vbs');
  // p.absolute('launch.vbs');
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
