// source: https://towardsdev.com/in-app-update-in-flutter-desktop-using-github-4b9c6a281510
// https://www.youtube.com/watch?v=XvwX-hmYv0E&ab_channel=RetroPortalStudio
import 'dart:convert';
import 'dart:io';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:path_provider/path_provider.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/internationalization.dart';

class ApplicationConfig {
  static double currentVersion = 1.0;
}

class ShowUpdateDialogue extends StatefulWidget {
  const ShowUpdateDialogue({
    Key? key,
  }) : super(key: key);

  @override
  State<ShowUpdateDialogue> createState() => _ShowUpdateDialogueState();
}

class _ShowUpdateDialogueState extends State<ShowUpdateDialogue> {
  bool isDownloading = false;
  double downloadProgress = 0;
  String downloadedFilePath = "";

  Future<Map<String, dynamic>> loadJsonFromGithub() async {
    final response = await http.read(Uri.parse(
        "https://raw.githubusercontent.com/Borgerod/ProSpector/main/App/prospector/app_version_check/version.json"));
    return jsonDecode(response);
  }

  Future<void> openExeFile(String filePath) async {
    await Process.start(filePath, ["-t", "-l", "1000"]).then((value) {});
  }

  Future<void> openDMGFile(String filePath) async {
    await Process.start(
        "MOUNTDEV=\$(hdiutil mount '$filePath' | awk '/dev.disk/{print\$1}')",
        []).then((value) {
      debugPrint("Value: $value");
    });
  }

  Future downloadNewVersion(String appPath) async {
    final fileName = appPath.split("/").last;
    isDownloading = true;
    setState(() {});

    final dio = Dio();

    downloadedFilePath =
        "${(await getApplicationDocumentsDirectory()).path}/$fileName";
    await dio.download(
      "https://raw.githubusercontent.com/Borgerod/ProSpector/main/App/prospector/app_version_check/$appPath",
      downloadedFilePath,
      onReceiveProgress: (received, total) {
        final progress = (received / total) * 100;
        debugPrint('Rec: $received , Total: $total, $progress%');
        downloadProgress = double.parse(progress.toStringAsFixed(1));
        setState(() {});
      },
    );
    debugPrint("File Downloaded Path: $downloadedFilePath");
    if (Platform.isWindows) {
      await openExeFile(downloadedFilePath);
    }
    isDownloading = false;
    setState(() {});
  }

  showUpdateDialog(Map<String, dynamic> versionJson) {
    final version = versionJson['version'];
    final updates = versionJson['description'] as List;
    return showDialog(
        context: context,
        builder: (context) {
          return SimpleDialog(
            contentPadding: const EdgeInsets.all(10),
            title: Text("Latest Version $version"),
            children: [
              Text("What's new in $version"),
              const SizedBox(
                height: 5,
              ),
              ...updates
                  .map((e) => Row(
                        children: [
                          Container(
                            width: 4,
                            height: 4,
                            decoration: BoxDecoration(
                                color: Colors.grey[400],
                                borderRadius: BorderRadius.circular(20)),
                          ),
                          const SizedBox(
                            width: 10,
                          ),
                          Text(
                            "$e",
                            style: TextStyle(
                              color: Colors.grey[600],
                            ),
                          ),
                        ],
                      ))
                  .toList(),
              const SizedBox(
                height: 10,
              ),
              if (version > ApplicationConfig.currentVersion)
                TextButton.icon(
                    onPressed: () {
                      Navigator.pop(context);
                      if (Platform.isMacOS) {
                        downloadNewVersion(versionJson["macos_file_name"]);
                      }
                      if (Platform.isWindows) {
                        downloadNewVersion(versionJson["windows_file_name"]);
                      }
                    },
                    icon: const Icon(Icons.update),
                    label: const Text("Update")),
            ],
          );
        });
  }

  Future<void> _checkForUpdates() async {
    final jsonVal = await loadJsonFromGithub();
    debugPrint("Response: $jsonVal");
    showUpdateDialog(jsonVal);
    if (jsonVal['version'] > ApplicationConfig.currentVersion) {
      setState(() {
        ApplicationConfig.currentVersion = jsonVal['version'];
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Stack(
        children: [
          if (isDownloading)
            Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              color: Colors.black.withOpacity(0.3),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const CircularProgressIndicator(),
                  Text(downloadProgress.toStringAsFixed(1) + " %")
                ],
              ),
            ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        'Current Version is ${ApplicationConfig.currentVersion}',
                        style: TextStyle(color: Colors.white),
                      ),
                      if (!isDownloading && downloadedFilePath != "")
                        Text("File Downloaded in $downloadedFilePath")
                    ],
                  ),
                ),
                TextButton(
                  style: ButtonStyle(
                    fixedSize: MaterialStateProperty.all(Size(100, 40)),
                    elevation: MaterialStateProperty.all(1.0),
                    backgroundColor:
                        MaterialStateProperty.all(Color(0x3E22282F)),
                  ),
                  onPressed: _checkForUpdates,
                  child: const Icon(Icons.update, color: Colors.white),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
