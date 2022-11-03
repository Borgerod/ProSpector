import 'package:flutter/material.dart';
import 'dart:io';

import 'package:open_file/open_file.dart';
import 'package:path/path.dart' as p;

Future<void> main() async {
  await runServer();
}

Future<void> runServer() async {
  /*
   Runs FastAPI Server when called on startup
  */
  String? filePath = '';
  var absPath = p.absolute('python_installer/run_server.bat');
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
