import 'dart:async';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class PeriodicRequester extends StatelessWidget {
  Stream<http.Response> getRandomNumberFact() async* {
    yield* Stream.periodic(Duration(seconds: 5), (_) {
      return http.get(
          Uri.parse("http://127.0.0.1:8000/ResetPassword/AuthenticationBool"));
    }).asyncMap((event) async => await event);
  }

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<http.Response>(
      stream: getRandomNumberFact(),
      builder: (context, snapshot) => snapshot.hasData
          ? Center(child: Text(snapshot.data!.body))
          : CircularProgressIndicator(),
    );
  }
}
