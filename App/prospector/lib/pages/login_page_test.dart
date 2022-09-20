import 'dart:convert';
import 'package:flutter/material.dart';

import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:flutter/services.dart';
import 'package:prospector/backend/api_requests/api_calls.dart';
import 'package:prospector/components/menu_widget.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/flutter_flow/internationalization.dart';
import 'package:prospector/pages/main_page/home_page_backup.dart';
import 'package:prospector/popups/login_error_message_widget.dart';
import 'package:velocity_x/velocity_x.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:hive/hive.dart';
import 'package:http/http.dart' as http;
import 'package:prospector/globals.dart' as globals;

import 'package:prospector/pages/signup_page.dart';

class Login_Page extends StatefulWidget {
  const Login_Page({Key? key}) : super(key: key);
  @override
  _Login_PageState createState() => _Login_PageState();
}

class _Login_PageState extends State<Login_Page> {
  // // _____ VARIABLES ______
  bool isChecked = false; //* rememberMe checkbox
  TextEditingController email = TextEditingController(); //* email-controller
  TextEditingController pass = TextEditingController(); //*  pass-controller

  // late Box box1 = '' as Box;
  late Box box1;
  // Box? box1;
  // _____ STATES ______
  @override
  void initState() {
    super.initState();
    // ! This is where the data will be stored
    createBox();
  }

  void createBox() async {
    // creating the Hive-database
    // 'login_data' is what we call the database
    box1 = await Hive.openBox('login_data');
    // we use async to open the box as fast as possible upon laoding the page
    // ! this is the function that gets the remembered login data and fills the forms upon page load
    getData();
  }

  void getData() async {
    // the job of this method is to get the "data" from "box1" [ from createBox() ]
    // first we need to check if box1 has data
    //
    // it gets the "email"-key and checks if it is not null
    if (box1.get('email') != null) {
      // if true:
      //      then the email-textcontroller is now: = 'email' value in box1
      email.text = box1.get('email');
      isChecked = true;
      setState(() {});
    }
    // then does the same for "pass"
    if (box1.get('pass') != null) {
      pass.text = box1.get('pass');
      isChecked = true;
      setState(() {});
    }
  }

  // _______ USER INTERFACE ________
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey,
      resizeToAvoidBottomInset: false,
      body: SafeArea(
        child: Column(
          children: [
            Container(
              child: WindowTitleBarBox(child: MoveWindow()),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 40, 20, 0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  // _________________  USERNAME _______________________________
                  Padding(
                    padding: const EdgeInsets.fromLTRB(30, 0, 30, 0),
                    child: TextField(
                      controller: email, //* <--- email-controller
                      decoration: InputDecoration(
                        hintText: 'Email',
                        hintStyle: const TextStyle(color: Colors.white),
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10.0),
                          borderSide: const BorderSide(color: Colors.white),
                        ),
                        focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(10.0),
                            borderSide: const BorderSide(color: Colors.blue)),
                        isDense: true,
                        // Added this
                        contentPadding:
                            const EdgeInsets.fromLTRB(10, 20, 10, 10),
                      ),
                      cursorColor: Colors.white,
                      style: const TextStyle(color: Colors.white),
                    ),
                  ),
                  // ___________________________________________________________
                  const HeightBox(20),
                  // _________________  PASSWORD _______________________________
                  Padding(
                    padding: const EdgeInsets.fromLTRB(30, 0, 30, 0),
                    child: TextFormField(
                      controller: pass, //* <--- password-controller
                      onFieldSubmitted: (value) {
                        print("Login Event; Pressed Enter-key");
                        Login.callback(email, pass, isChecked, box1, context);
                      },
                      obscureText: true,
                      decoration: InputDecoration(
                        hintText: 'Password',
                        hintStyle: const TextStyle(color: Colors.white),
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10.0),
                          borderSide: const BorderSide(color: Colors.white),
                        ),
                        focusedBorder: OutlineInputBorder(
                            borderRadius: new BorderRadius.circular(10.0),
                            borderSide: const BorderSide(color: Colors.blue)),
                        isDense: true,
                        contentPadding:
                            const EdgeInsets.fromLTRB(10, 20, 10, 10),
                      ),
                      cursorColor: Colors.white,
                      style: const TextStyle(color: Colors.white),
                    ),
                  ),
                  // ___________________________________________________________
                  const HeightBox(20),
                  // _________________  REMEMBER ME ____________________________
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        FFLocalizations.of(context).getText(
                          'argrf05a' /* Remember me */,
                        ),
                        textAlign: TextAlign.center,
                        style: FlutterFlowTheme.of(context).bodyText1.override(
                              fontFamily:
                                  FlutterFlowTheme.of(context).bodyText1Family,
                              color:
                                  FlutterFlowTheme.of(context).primaryBtnText,
                            ),
                      ),
                      Checkbox(
                        value: //  The checkbox value is initially the basevalue
                            isChecked, // of isChecked (bool isChecked = false;)
                        onChanged: (value) {
                          // when checkbox is checked/unchecked;
                          // the value (isChecked) is changed to "!isChecked"
                          // meaning isChecked is now -> "not" isChecked
                          // [ "!" means: "not" / "opposite" / "not equal" ]
                          // [    foo = !0  --> foo is: "not 0"            ]
                          // [    foo =! 0  --> is foo "not 0"?            ]
                          isChecked = !isChecked;
                          //* Our task:
                          //*   When the user presses "Login" buton:
                          //*       if (isChecked == true) => Then we are going
                          //*                                 to save the data
                          setState(() {});
                        },
                      ),
                      GestureDetector(
                        onTap: () {},
                        child: const Text(
                          "Forgot Password ? Reset Now",
                          style: TextStyle(color: Colors.white),
                        ),
                      ),
                    ],
                  ),
                  // ___________________________________________________________
                  HeightBox(10),
                  // _________________  LOGIN BUTTON ___________________________
                  InkWell(
                    onTap: () {
                      print("Button Click => Login Event");
                      Login.callback(email, pass, isChecked, box1, context);
                    },
                    child: Material(
                      color: Colors.transparent,
                      elevation: 5,
                      child: Container(
                        width: 150,
                        height: 30,
                        decoration: BoxDecoration(
                          color: Color(0xFF5D8387),
                        ),
                        child: Align(
                          alignment: AlignmentDirectional(0, 0),
                          child: Text(
                            FFLocalizations.of(context).getText(
                              'bbpm2l2x' /* Login */,
                            ),
                            textAlign: TextAlign.center,
                            style:
                                FlutterFlowTheme.of(context).bodyText1.override(
                                      fontFamily: FlutterFlowTheme.of(context)
                                          .bodyText1Family,
                                      color: FlutterFlowTheme.of(context)
                                          .primaryBtnText,
                                    ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  // ___________________________________________________________
                  const HeightBox(20),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
