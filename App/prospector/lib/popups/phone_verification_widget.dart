import 'dart:convert';
import 'dart:convert' show utf8;

import 'package:flutter/material.dart';
import 'dart:ui';
import 'package:http/http.dart' as http;

import 'package:prospector/flutter_flow/flutter_flow_widgets.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/pages/login_page.dart';
import 'package:prospector/popups/account_created_widget.dart';

class PhoneVerificationWidget extends StatefulWidget {
  const PhoneVerificationWidget({Key? key}) : super(key: key);

  @override
  _PhoneVerificationWidgetState createState() =>
      _PhoneVerificationWidgetState();
}

class _PhoneVerificationWidgetState extends State<PhoneVerificationWidget> {
  TextEditingController? verifyCodeController;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    verifyCodeController = TextEditingController();
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
            //> BLURRY BACKGROUND
            Align(
              alignment: Alignment.center,
              child: ClipRect(
                child: BackdropFilter(
                  filter: ImageFilter.blur(
                    sigmaX: 10,
                    sigmaY: 10,
                  ),
                  child: InkWell(
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

            //> CONTENT CONTAINER
            Align(
              alignment: Alignment.center,
              child: Material(
                color: Colors.transparent,
                elevation: 10,

                // ____ content container start ____

                child: Container(
                  width: 500,
                  height: 350,
                  decoration: BoxDecoration(
                    color: FlutterFlowTheme.of(context).tertiaryColor,
                  ),

                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      // ICON ____________________________________________
                      Padding(
                        padding: EdgeInsetsDirectional.fromSTEB(0, 30, 0, 0),
                        child: Row(
                          mainAxisSize: MainAxisSize.max,
                          children: [
                            Expanded(
                              child: Icon(
                                Icons.phone_iphone,
                                color:
                                    FlutterFlowTheme.of(context).primaryColor,
                                size: 60,
                              ),
                            ),
                          ],
                        ),
                      ),

                      // TITLE ___________________________________________
                      Padding(
                        padding:
                            // EdgeInsetsDirectional.fromSTEB(0, 30, 0, 20),
                            EdgeInsetsDirectional.fromSTEB(0, 10, 0, 10),
                        child: Row(
                          mainAxisSize: MainAxisSize.max,
                          mainAxisAlignment: MainAxisAlignment.center,
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: [
                            Text(
                              FFLocalizations.of(context).getText(
                                '3ebfpqc1' /* Verify phone number */,
                              ),
                              textAlign: TextAlign.center,
                              style: FlutterFlowTheme.of(context)
                                  .subtitle1
                                  .override(
                                    fontFamily: FlutterFlowTheme.of(context)
                                        .subtitle1Family,
                                    color: FlutterFlowTheme.of(context)
                                        .primaryText,
                                  ),
                            ),
                          ],
                        ),
                      ),

                      // CONTAINER: [BODY TEXT & INPUT FIELD] ____________
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          Column(
                            children: [
                              // BODY TEXT _______________________________________
                              Padding(
                                padding:
                                    EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                                // EdgeInsetsDirectional.fromSTEB(0, 10, 0, 10),
                                // EdgeInsetsDirectional.fromSTEB(0, 30, 0, 20),
                                child: Text(
                                  FFLocalizations.of(context).getText(
                                    '3ebfpqc2' /* Please, enter the verification code... */,
                                  ),
                                  textAlign: TextAlign.center,
                                  style: FlutterFlowTheme.of(context)
                                      .bodyText1
                                      .override(
                                        fontFamily: 'Poppins',
                                        color: Color(0xFFD6D8DA),
                                        fontSize: 12,
                                        fontWeight: FontWeight.w300,
                                      ),
                                ),
                              ),

                              // INPUT FIELD _____________________________________
                              Padding(
                                padding:
                                    EdgeInsetsDirectional.fromSTEB(0, 0, 55, 0),
                                child: Row(
                                  children: [
                                    // // SPACER ****
                                    // Spacer(flex: 2),

                                    // ICON ****
                                    Padding(
                                      padding: EdgeInsetsDirectional.fromSTEB(
                                          10, 0, 20, 0),
                                      child: Icon(
                                        Icons.verified_user_sharp,
                                        color: Color(0xFFD6D8DA),
                                        size: 24,
                                      ),
                                    ),

                                    // TEXT FORM FIELD ****
                                    Container(
                                      // width: 80,
                                      width: 110,
                                      child: TextFormField(
                                        textAlign: TextAlign.center,
                                        cursorColor: Color(0xFFD6D8DA),
                                        controller: verifyCodeController,
                                        obscureText: false,
                                        decoration: InputDecoration(
                                          hintText: FFLocalizations.of(context)
                                              .getText(
                                            '3ebfpqc3' /* CODE */,
                                          ),
                                          hintStyle:
                                              FlutterFlowTheme.of(context)
                                                  .bodyText1
                                                  .override(
                                                    fontFamily: 'Poppins',
                                                    color: Color(0xFFD6D8DA),
                                                    fontSize: 12,
                                                    fontWeight: FontWeight.w300,
                                                  ),
                                          focusedBorder: UnderlineInputBorder(
                                            borderSide: BorderSide(
                                              color: Color(0xFF95A1AC),
                                              width: 2,
                                            ),
                                          ),
                                        ),
                                        style: FlutterFlowTheme.of(context)
                                            .bodyText1
                                            .override(
                                              fontFamily: 'Poppins',
                                              color: Color(0xFFD6D8DA),
                                              fontSize: 16,
                                              fontWeight: FontWeight.normal,
                                              letterSpacing: 5,
                                            ),
                                      ),
                                    ),

                                    // // SPACER ****
                                    // Spacer(flex: 2),
                                  ],
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),

                      // VERIFY BUTTON ___________________________________
                      Padding(
                        padding: EdgeInsetsDirectional.fromSTEB(0, 20, 0, 20),
                        child: Row(
                          mainAxisSize: MainAxisSize.max,
                          mainAxisAlignment: MainAxisAlignment.center,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            FFButtonWidget(
                              // BUTTON TEXT
                              text: FFLocalizations.of(context).getText(
                                '3ebfpqc4' /* VERIFY */,
                              ),

                              // BUTTON APPEARANCE
                              options: FFButtonOptions(
                                width: 200,
                                height: 40,
                                color:
                                    FlutterFlowTheme.of(context).primaryColor,
                                textStyle: FlutterFlowTheme.of(context)
                                    .subtitle2
                                    .override(
                                      fontFamily: 'Poppins',
                                      color: FlutterFlowTheme.of(context)
                                          .primaryBtnText,
                                      fontWeight: FontWeight.w500,
                                      fontSize: 14,
                                    ),
                                borderSide: BorderSide(
                                  color: Colors.transparent,
                                  width: 1,
                                ),
                                borderRadius: BorderRadius.circular(8),
                              ),

                              //> BUTTON ACTION
                              onPressed: () async {
                                // var body = json.encode({
                                //   'phone_number': FFAppState().phoneNumber,
                                //   'otp_code': verifyCodeController!.text,
                                // });
                                // print(body);

                                postVerification(verifyCodeController, context);

                                // await Navigator.pushAndRemoveUntil(
                                //   context,
                                //   MaterialPageRoute(
                                //     builder: (context) => LoginWidget(),
                                //   ),
                                //   (r) => false,
                                // );
                              },
                            ),
                          ],
                        ),
                      ),

                      //
                    ],
                  ),

                  // ____ content container end ____
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

stripSpecialChar(phone_number) {
  if (phone_number.contains('+')) {
    return phone_number.replaceAll(new RegExp(r'[^\w\s]+'), '');
  }
  ;
}

postVerification(verifyCodeController, BuildContext context) async {
  String phone_number = FFAppState().phoneNumber;
  String otp_code = verifyCodeController!.text;
  var phone_number_stripped = stripSpecialChar(phone_number);
  String link =
      'http://127.0.0.1:8000/users/verification/phone/recieve_code?phone_number=%2B$phone_number_stripped&otp_code=$otp_code';
  print(link);
  var response = await http.get(
    Uri.parse(
        'http://127.0.0.1:8000/users/verification/phone/recieve_code?phone_number=%2B$phone_number_stripped&otp_code=$otp_code'),
    headers: {
      "accept": "application/json",
    },
  );
  if (response.statusCode == 200) {
    await Navigator.push(
      context,
      PageTransition(
          type: PageTransitionType.fade,
          duration: Duration(milliseconds: 0),
          reverseDuration: Duration(milliseconds: 0),
          child: AccountCreatedWidget()),
    );
  } else {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          contentTextStyle: FlutterFlowTheme.of(context).bodyText1,
          title: Text(
            FFLocalizations.of(context).getText('3ebfpqc5' /* Invalid Code */
                ),
            textAlign: TextAlign.center,
          ),
          content: Text(
            FFLocalizations.of(context)
                .getText('3ebfpqc6' /* please try again */
                    ),
            textAlign: TextAlign.center,
            style: FlutterFlowTheme.of(context).bodyText1.override(
                fontFamily: FlutterFlowTheme.of(context).bodyText1Family,
                fontSize: 12,
                fontWeight: FontWeight.w300),
          ),
        );
      },
    );
  }
}
