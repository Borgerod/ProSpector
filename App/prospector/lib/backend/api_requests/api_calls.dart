import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:prospector/globals.dart' as globals;
import 'package:prospector/components/menu_widget.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/popups/login_error_message_widget.dart';

class Login {
  static callback(email, pass, isChecked, box1, context) async {
    String _email = email.text;
    String _pass = pass.text;
    if (_email.isNotEmpty && _pass.isNotEmpty) {
      var request = http.MultipartRequest(
          'POST', Uri.parse('http://127.0.0.1:8000/login/token'));
      request.fields['username'] = _email;
      request.fields['password'] = _pass;
      var response = await request.send();
      final respStr = await response.stream.bytesToString();
      Map tokenMap = json.decode(respStr);
      if (response.statusCode == 200) {
        globals.accsess_token = tokenMap['access_token'];
        globals.token_type = tokenMap['token_type'];
        if (isChecked) {
          box1.put('email', email.text);
          box1.put('pass', pass.text);
        } else {
          // purges box1 if rememberMe is not checked
          box1.put('email', null);
          box1.put('pass', null);
        }
        await Navigator.pushAndRemoveUntil(
          context,
          PageTransition(
            type: PageTransitionType.fade,
            duration: Duration(milliseconds: 0),
            reverseDuration: Duration(milliseconds: 0),
            child: new Scaffold(
                backgroundColor: Colors.transparent, body: MenuWidget()),
          ),
          (r) => false,
        );
      } else {
        print("Login Failed, Incorrect Email or Password");
        await Navigator.push(
          context,
          PageTransition(
            type: PageTransitionType.fade,
            duration: Duration(milliseconds: 0),
            reverseDuration: Duration(milliseconds: 0),
            child: LoginErrorMessageWidget(),
          ),
        );
      }
    } else {
      print("Login Failed, Form is NOT filled");
    }
  }
}
