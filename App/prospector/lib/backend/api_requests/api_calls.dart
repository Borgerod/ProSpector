import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:prospector/globals.dart' as globals;
import 'package:prospector/components/menu_widget.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/popups/login_error_message_widget.dart';
import 'package:prospector/backend/api_requests/api_manager.dart';
export 'package:prospector/backend/api_requests/api_manager.dart'
    show ApiCallResponse;

class Login {
  static callback(email, pass, isChecked, box1, context) async {
    String _email = email.text;
    String _pass = pass.text;
    //*  Doing the task:
    //*  When the user presses "Login" buton:
    //*        if (isChecked == true) => Then we are going
    //*                                  to save the data

    // First checks if email and password form is filled,
    // only continues if they are.
    if (_email.isNotEmpty && _pass.isNotEmpty) {
      // print("Form is filled");
      var request = http.MultipartRequest(
          'POST', Uri.parse('http://127.0.0.1:8000/login/token'));
      request.fields['username'] = _email;
      request.fields['password'] = _pass;
      var response = await request.send();
      final respStr = await response.stream.bytesToString();
      Map token_map = json.decode(respStr);
      // checking if isChecked == true
      if (response.statusCode == 200) {
        globals.accsess_token = token_map['access_token'];
        globals.token_type = token_map['token_type'];
        if (isChecked) {
          // if so: it puts the 'key' and 'value' of email and password in our box.
          box1.put('email', email.text);
          box1.put('pass', pass.text);
          // print("Login Succsessfull");
          // print("do remember me");
          // the key can be named whatever but its best to use the same names
          // the value comes from the textcontrollers
        } else {
          // purges box1 if rememberMe is not checked
          box1.put('email', null);
          box1.put('pass', null);
          // print("Login Succsessfull");
          // print("do NOT remember me");
        }
        await Navigator.pushAndRemoveUntil(
          context,
          PageTransition(
            type: PageTransitionType.fade,
            duration: Duration(milliseconds: 0),
            reverseDuration: Duration(milliseconds: 0),
            child: new Scaffold(
                backgroundColor: Colors.transparent, body: MenuWidget()),
            // child: MainPageWidget(),
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

// ! CURRENTLY NOT IN USE
class GetCurrentCallListCall {
  static Future<ApiCallResponse> call() {
    return ApiManager.instance.makeApiCall(
      callName: 'GetCurrentCallList',
      apiUrl: 'http://127.0.0.1:8000/currentcallList',
      callType: ApiCallType.GET,
      headers: {
        'accept': 'application/json',
        'Authorization': globals.accsess_token,
      },
      params: {},
      returnBody: true,
    );
  }
}
