// ignore_for_file: unused_element

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:ui';

import 'package:prospector_app/popups/reset_password_authentication_widget.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_icon_button.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_widgets.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_util.dart';

class ResetPasswordWidget extends StatefulWidget {
  const ResetPasswordWidget({Key? key, required this.email}) : super(key: key);
  final Email email;
  @override
  _ResetPasswordWidgetState createState() => _ResetPasswordWidgetState(email);
}

class _ResetPasswordWidgetState extends State<ResetPasswordWidget> {
  _ResetPasswordWidgetState(this.email, {Key? key});
  TextEditingController? confirmPasswordController;
  TextEditingController? newPasswordController;
  final Email email;
  final scaffoldKey = GlobalKey<ScaffoldState>();
  late bool confirmPasswordVisibility;
  late bool newPasswordVisibility;
  late Color colorState = FlutterFlowTheme.of(context).thirdTextColor;
  late Color labelColorState = FlutterFlowTheme.of(context).thirdTextColor;
  late String labelState = FFLocalizations.of(context).getText(
    'lpsz5j9b' /* Confirm Password */,
  );

  @override
  void initState() {
    super.initState();

    confirmPasswordController = TextEditingController();
    confirmPasswordVisibility = false;
    newPasswordController = TextEditingController();
    newPasswordVisibility = false;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      backgroundColor: Colors.transparent,
      body: GestureDetector(
        onTap: () => FocusScope.of(context).unfocus(),
        child: Stack(
          children: [
            Align(
              alignment: AlignmentDirectional(0.02, -0.08),
              child: ClipRect(
                child: BackdropFilter(
                  filter: ImageFilter.blur(
                    sigmaX: 10,
                    sigmaY: 10,
                  ),
                  child: InkWell(
                    hoverColor: Colors.transparent,
                    focusColor: Colors.transparent,
                    highlightColor: Colors.transparent,
                    splashColor: Colors.transparent,
                    splashFactory: NoSplash.splashFactory,
                    onTap: () async {
                      Navigator.pop(context);
                    },
                    child: Container(
                      width: MediaQuery.of(context).size.width,
                      height: MediaQuery.of(context).size.height * 1,
                      decoration: BoxDecoration(
                        color: Colors.transparent,
                      ),
                    ),
                  ),
                ),
              ),
            ),
            Align(
              alignment: AlignmentDirectional(0, 0),
              child: Material(
                color: Colors.transparent,
                elevation: 10,
                child: Container(
                  width: 600,
                  height: 270,
                  decoration: BoxDecoration(
                    color: FlutterFlowTheme.of(context).tertiaryColor,
                  ),
                  child: Padding(
                    padding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 30),
                    child: Column(
                      mainAxisSize: MainAxisSize.max,
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                    30, 15, 20, 0),
                                child: Text(
                                  FFLocalizations.of(context).getText(
                                    'mkjs1git' /* Password Reset */,
                                  ),
                                  style: FlutterFlowTheme.of(context)
                                      .title1
                                      .override(
                                        fontFamily: FlutterFlowTheme.of(context)
                                            .title1Family,
                                        fontSize: 25,
                                      ),
                                ),
                              ),
                              FlutterFlowIconButton(
                                borderColor: Colors.transparent,
                                borderRadius: 30,
                                borderWidth: 1,
                                buttonSize: 60,
                                icon: Icon(
                                  Icons.close,
                                  color:
                                      FlutterFlowTheme.of(context).primaryText,
                                  size: 20,
                                ),
                                onPressed: () async {
                                  Navigator.pop(context);
                                },
                              ),
                            ],
                          ),
                        ),
                        Expanded(
                          child: Padding(
                            padding:
                                EdgeInsetsDirectional.fromSTEB(30, 20, 30, 0),
                            child: Row(
                              mainAxisSize: MainAxisSize.max,
                              children: [
                                // PASSWORD ________________________________________________
                                Expanded(
                                  flex: 3,
                                  child: Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        0, 0, 0, 20),
                                    child: TextFormField(
                                      controller: newPasswordController,
                                      onFieldSubmitted: (_) async {
                                        setState(() =>
                                            FFAppState().emailAdress =
                                                newPasswordController!.text);
                                      },
                                      obscureText: !newPasswordVisibility,
                                      decoration: InputDecoration(
                                        labelText:
                                            FFLocalizations.of(context).getText(
                                          'b6vxcqkd' /* New Password */,
                                        ),
                                        labelStyle: TextStyle(
                                          color: Color(0xFFD6D8DA),
                                        ),
                                        enabledBorder: UnderlineInputBorder(
                                          borderSide: BorderSide(
                                            color: Color(0xFF95A1AC),
                                            width: 2,
                                          ),
                                          borderRadius: const BorderRadius.only(
                                            topLeft: Radius.circular(4.0),
                                            topRight: Radius.circular(4.0),
                                          ),
                                        ),
                                        focusedBorder: UnderlineInputBorder(
                                          borderSide: BorderSide(
                                            color: Color(0xFF95A1AC),
                                            width: 2,
                                          ),
                                          borderRadius: const BorderRadius.only(
                                            topLeft: Radius.circular(4.0),
                                            topRight: Radius.circular(4.0),
                                          ),
                                        ),
                                        suffixIcon: InkWell(
                                          onTap: () => setState(
                                            () => newPasswordVisibility =
                                                !newPasswordVisibility,
                                          ),
                                          focusNode:
                                              FocusNode(skipTraversal: true),
                                          child: Icon(
                                            newPasswordVisibility
                                                ? Icons.visibility_outlined
                                                : Icons.visibility_off_outlined,
                                            color: Color(0xFF95A1AC),
                                            size: 15,
                                          ),
                                        ),
                                      ),
                                      style: FlutterFlowTheme.of(context)
                                          .bodyText1
                                          .override(
                                            fontFamily: 'Poppins',
                                            color: Color(0xFFD6D8DA),
                                            fontSize: 12,
                                            fontWeight: FontWeight.normal,
                                          ),
                                    ),
                                  ),
                                ),
                                //  __________________________________________________________
                              ],
                            ),
                          ),
                        ),
                        Expanded(
                          child: Padding(
                            padding:
                                EdgeInsetsDirectional.fromSTEB(30, 0, 30, 20),
                            child: Row(
                              mainAxisSize: MainAxisSize.max,
                              children: [
                                Expanded(
                                  flex: 3,
                                  child: Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        0, 0, 0, 20),
                                    child: TextFormField(
                                      controller: confirmPasswordController,
                                      onFieldSubmitted: (_) async {
                                        setState(() => FFAppState()
                                                .emailAdress =
                                            confirmPasswordController!.text);
                                      },
                                      obscureText: !confirmPasswordVisibility,
                                      decoration: InputDecoration(
                                        labelText: labelState,
                                        labelStyle:
                                            TextStyle(color: labelColorState),
                                        enabledBorder: UnderlineInputBorder(
                                          borderSide: BorderSide(
                                            color: Color(0xFF95A1AC),
                                            width: 2,
                                          ),
                                          borderRadius: const BorderRadius.only(
                                            topLeft: Radius.circular(4.0),
                                            topRight: Radius.circular(4.0),
                                          ),
                                        ),
                                        focusedBorder: UnderlineInputBorder(
                                          borderSide: BorderSide(
                                            color: Color(0xFF95A1AC),
                                            width: 2,
                                          ),
                                          borderRadius: const BorderRadius.only(
                                            topLeft: Radius.circular(4.0),
                                            topRight: Radius.circular(4.0),
                                          ),
                                        ),
                                        suffixIcon: InkWell(
                                          onTap: () => setState(
                                            () => confirmPasswordVisibility =
                                                !confirmPasswordVisibility,
                                          ),
                                          focusNode:
                                              FocusNode(skipTraversal: true),
                                          child: Icon(
                                            confirmPasswordVisibility
                                                ? Icons.visibility_outlined
                                                : Icons.visibility_off_outlined,
                                            color: Color(0xFF95A1AC),
                                            size: 15,
                                          ),
                                        ),
                                      ),
                                      style: FlutterFlowTheme.of(context)
                                          .bodyText1
                                          .override(
                                            fontFamily: 'Poppins',
                                            color: colorState,
                                            fontSize: 12,
                                            fontWeight: FontWeight.normal,
                                          ),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(30, 0, 30, 0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: [
                              FFButtonWidget(
                                onPressed: () async {
                                  print(newPasswordController!.text);
                                  print(confirmPasswordController!.text);
                                  print(newPasswordController!.text ==
                                      confirmPasswordController!.text);
                                  if (newPasswordController!.text ==
                                      confirmPasswordController!.text) {
                                    String newPass =
                                        newPasswordController!.text;
                                    String emailStr = email.email;
                                    print(emailStr);
                                    await http.get(
                                      Uri.parse(
                                          'http://127.0.0.1:8000/ResetPassword?new_password=$newPass&email=$emailStr'),
                                    );
                                    Navigator.pop(context);
                                  } else {
                                    setState(() {
                                      colorState = Colors.red;
                                      labelState =
                                          "INCORRECT VERIFICATION NUMBER.";
                                      labelColorState = Colors.red;
                                    });
                                  }
                                },
                                text: FFLocalizations.of(context).getText(
                                  '973k67jf' /* Reset Password */,
                                ),
                                options: FFButtonOptions(
                                  width: 150,
                                  height: 30,
                                  color:
                                      FlutterFlowTheme.of(context).primaryColor,
                                  textStyle: FlutterFlowTheme.of(context)
                                      .subtitle2
                                      .override(
                                        fontFamily: 'Poppins',
                                        color: FlutterFlowTheme.of(context)
                                            .primaryBtnText,
                                        fontSize: 12,
                                        fontWeight: FontWeight.w500,
                                      ),
                                  elevation: 3,
                                  borderSide: BorderSide(
                                    color: Colors.transparent,
                                    width: 1,
                                  ),
                                  borderRadius: BorderRadius.circular(0),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
