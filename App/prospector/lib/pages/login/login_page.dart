// import 'package:prospector/pages/home_page/main_page.dart';

import 'dart:convert';

import 'package:prospector/backend/api_requests/api_calls.dart';
import 'package:prospector/components/menu_widget.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/pages/main_page/main_page.dart';
// import 'package:prospector/home_page/home_page_widget.dart';
import 'package:prospector/popups/login_error_message/login_error_message_widget.dart';
import 'package:http/http.dart' as http;

import 'package:prospector/pages/signup/signup_page.dart';
// import 'dart:ui';
import 'package:flutter/material.dart';
// import 'package:google_fonts/google_fonts.dart';
// import 'package:flutter_acrylic/flutter_acrylic.dart';
// import 'package:bitsdojo_window/bitsdojo_window.dart';

class LoginWidget extends StatefulWidget {
  const LoginWidget({Key? key}) : super(key: key);

  @override
  _LoginWidgetState createState() => _LoginWidgetState();
}

class _LoginWidgetState extends State<LoginWidget> {
  ApiCallResponse? loginResponse;
  bool? checkboxListTileValue;
  TextEditingController? emailController;
  TextEditingController? passwordController;
  late bool passwordVisibility;
  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    emailController = TextEditingController();
    passwordController = TextEditingController();
    passwordVisibility = false;
  }

  @override
  Widget build(BuildContext context) {
    final bodyHeight =
        MediaQuery.of(context).size.height - MediaQuery.of(context).padding.top;

    final bodyWidth = MediaQuery.of(context).size.width -
        MediaQuery.of(context).padding.right;

    return Scaffold(
      backgroundColor: Colors.transparent,
      body: GestureDetector(
        onTap: () => FocusScope.of(context).unfocus(),
        child: Container(
          height: bodyHeight * 1,
          width: bodyWidth * 1,
          decoration: BoxDecoration(
            color: FlutterFlowTheme.of(context).cardColor,
            image: DecorationImage(
              fit: BoxFit.cover,
              image: Image.asset(
                'assets/images/dante_s_view_by_chateaugrief_de1tex5-fullview.jpg',
              ).image,
            ),
          ),
          child: Align(
            alignment: Alignment.centerRight,
            child: Container(
              width: 954,
              height: 580,
              child: Row(
                mainAxisSize: MainAxisSize.max,
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Expanded(
                    flex: 3,
                    child: Column(
                      mainAxisSize: MainAxisSize.max,
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        Padding(
                          padding:
                              EdgeInsetsDirectional.fromSTEB(60, 20, 20, 0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            mainAxisAlignment: MainAxisAlignment.spaceAround,
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              ElevatedButton(
                                  style: ButtonStyle(
                                    fixedSize: MaterialStateProperty.all(
                                        Size(150, 40)),
                                    backgroundColor: MaterialStateProperty.all(
                                        Color(0x3E22282F)),
                                  ),
                                  onPressed: () async {
                                    await Navigator.of(context).pushReplacement(
                                        MaterialPageRoute(
                                            builder: (BuildContext context) =>
                                                MenuWidget()));
                                    // MainPageWidget()));
                                  },
                                  child: Text("temp login bypass")),
                              Expanded(
                                flex: 2,
                                child: Padding(
                                  padding: EdgeInsetsDirectional.fromSTEB(
                                      30, 25, 10, 50),
                                  child: Text(
                                    FFLocalizations.of(context).getText(
                                      '3yvf9h73' /* Not registered? */,
                                    ),
                                    textAlign: TextAlign.end,
                                    style: FlutterFlowTheme.of(context)
                                        .bodyText1
                                        .override(
                                            fontFamily: 'Poppins',
                                            color: Color(0xFFD6D8DA),
                                            fontSize: 14,
                                            fontWeight: FontWeight.w300),
                                  ),
                                ),
                              ),
                              Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                    10, 15, 10, 100),
                                child: TextButton(
                                  style: ButtonStyle(
                                    fixedSize: MaterialStateProperty.all(
                                        Size(100, 40)),
                                    elevation: MaterialStateProperty.all(1.0),
                                    backgroundColor: MaterialStateProperty.all(
                                        Color(0x3E22282F)),
                                  ),
                                  onPressed: () async {
                                    await Navigator.push(
                                      context,
                                      PageTransition(
                                        type: PageTransitionType.fade,
                                        duration: Duration(milliseconds: 0),
                                        reverseDuration:
                                            Duration(milliseconds: 0),
                                        child: SignupWidget(),
                                      ),
                                    );
                                  },
                                  child: Text(
                                    FFLocalizations.of(context).getText(
                                      '9zbibd94' /* Sign Up */,
                                    ),
                                    style: FlutterFlowTheme.of(context)
                                        .bodyText1
                                        .override(
                                          fontFamily:
                                              FlutterFlowTheme.of(context)
                                                  .bodyText1Family,
                                          color: FlutterFlowTheme.of(context)
                                              .primaryBtnText,
                                        ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                        Spacer(flex: 10),
                        Container(
                          child: Column(
                            mainAxisSize: MainAxisSize.min,
                            mainAxisAlignment: MainAxisAlignment.start,
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: [
                              Row(
                                mainAxisSize: MainAxisSize.max,
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Spacer(flex: 2),
                                  Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        10, 0, 20, 0),
                                    child: Icon(
                                      Icons.person_sharp,
                                      color: Color(0xFFD6D8DA),
                                      size: 18,
                                    ),
                                  ),
                                  Expanded(
                                    flex: 3,
                                    child: Padding(
                                      padding: EdgeInsetsDirectional.fromSTEB(
                                          0, 0, 0, 10),
                                      child: TextFormField(
                                        controller: emailController,
                                        onFieldSubmitted: (_) async {
                                          setState(() =>
                                              FFAppState().emailAdress =
                                                  passwordController!.text);
                                        },
                                        obscureText: false,
                                        decoration: InputDecoration(
                                          labelText: FFLocalizations.of(context)
                                              .getText(
                                            'jy7dyfri' /* Email Address */,
                                          ),
                                          labelStyle:
                                              FlutterFlowTheme.of(context)
                                                  .bodyText1
                                                  .override(
                                                    fontFamily: 'Lexend Deca',
                                                    color: Color(0xFFD6D8DA),
                                                    fontSize: 12,
                                                    fontWeight:
                                                        FontWeight.normal,
                                                  ),
                                          enabledBorder: UnderlineInputBorder(
                                            borderSide: BorderSide(
                                              color: Color(0xFF95A1AC),
                                              width: 2,
                                            ),
                                            borderRadius:
                                                const BorderRadius.only(
                                              topLeft: Radius.circular(4.0),
                                              topRight: Radius.circular(4.0),
                                            ),
                                          ),
                                          focusedBorder: UnderlineInputBorder(
                                            borderSide: BorderSide(
                                              color: Color(0xFF95A1AC),
                                              width: 2,
                                            ),
                                            borderRadius:
                                                const BorderRadius.only(
                                              topLeft: Radius.circular(4.0),
                                              topRight: Radius.circular(4.0),
                                            ),
                                          ),
                                        ),
                                        style: FlutterFlowTheme.of(context)
                                            .bodyText1
                                            .override(
                                              fontFamily: 'Lexend Deca',
                                              color: Color(0xFFD6D8DA),
                                              fontSize: 12,
                                              fontWeight: FontWeight.normal,
                                            ),
                                        keyboardType:
                                            TextInputType.emailAddress,
                                      ),
                                    ),
                                  ),
                                  Spacer(flex: 2),
                                ],
                              ),
                              Row(
                                mainAxisSize: MainAxisSize.max,
                                children: [
                                  Spacer(flex: 2),
                                  Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        10, 0, 20, 0),
                                    child: Icon(
                                      Icons.lock_sharp,
                                      color: Color(0xFFD6D8DA),
                                      size: 18,
                                    ),
                                  ),
                                  Expanded(
                                    flex: 3,
                                    child: Padding(
                                      padding: EdgeInsetsDirectional.fromSTEB(
                                          0, 0, 0, 10),
                                      child: TextFormField(
                                        controller: passwordController,
                                        onFieldSubmitted: (_) async {
                                          setState(() =>
                                              FFAppState().emailAdress =
                                                  passwordController!.text);
                                        },
                                        obscureText: !passwordVisibility,
                                        decoration: InputDecoration(
                                          labelText: 'Password',
                                          labelStyle:
                                              FlutterFlowTheme.of(context)
                                                  .bodyText1
                                                  .override(
                                                    fontFamily: 'Lexend Deca',
                                                    color: Color(0xFFD6D8DA),
                                                    fontSize: 12,
                                                    fontWeight:
                                                        FontWeight.normal,
                                                  ),
                                          enabledBorder: UnderlineInputBorder(
                                            borderSide: BorderSide(
                                              color: Color(0xFF95A1AC),
                                              width: 2,
                                            ),
                                            borderRadius:
                                                const BorderRadius.only(
                                              topLeft: Radius.circular(4.0),
                                              topRight: Radius.circular(4.0),
                                            ),
                                          ),
                                          focusedBorder: UnderlineInputBorder(
                                            borderSide: BorderSide(
                                              color: Color(0xFF95A1AC),
                                              width: 2,
                                            ),
                                            borderRadius:
                                                const BorderRadius.only(
                                              topLeft: Radius.circular(4.0),
                                              topRight: Radius.circular(4.0),
                                            ),
                                          ),
                                          suffixIcon: InkWell(
                                            onTap: () => setState(
                                              () => passwordVisibility =
                                                  !passwordVisibility,
                                            ),
                                            focusNode:
                                                FocusNode(skipTraversal: true),
                                            child: Icon(
                                              passwordVisibility
                                                  ? Icons.visibility_outlined
                                                  : Icons
                                                      .visibility_off_outlined,
                                              color: Color(0xFF95A1AC),
                                              size: 22,
                                            ),
                                          ),
                                        ),
                                        style: FlutterFlowTheme.of(context)
                                            .bodyText1
                                            .override(
                                              fontFamily: 'Lexend Deca',
                                              color: Color(0xFFD6D8DA),
                                              fontSize: 12,
                                              fontWeight: FontWeight.normal,
                                            ),
                                      ),
                                    ),
                                  ),
                                  Spacer(flex: 2),
                                ],
                              ),
                              Row(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceEvenly,
                                crossAxisAlignment: CrossAxisAlignment.center,
                                children: [
                                  Spacer(flex: 6),
                                  Container(
                                    width: 130,
                                    height: 100,
                                    decoration: BoxDecoration(),
                                    child: Theme(
                                      data: ThemeData(
                                        unselectedWidgetColor:
                                            Color(0xFFD6D8DA),
                                      ),
                                      child: Row(
                                        children: [
                                          Transform.scale(
                                            scale: .7,
                                            child: Checkbox(
                                              value: checkboxListTileValue ??=
                                                  false,
                                              onChanged: (newValue) => setState(
                                                  () => checkboxListTileValue =
                                                      newValue!),
                                              activeColor:
                                                  FlutterFlowTheme.of(context)
                                                      .primaryColor,
                                            ),
                                          ),
                                          Text(
                                            FFLocalizations.of(context).getText(
                                              'argrf05a' /* Remember Me */,
                                            ),
                                            style: FlutterFlowTheme.of(context)
                                                .title3
                                                .override(
                                                  fontFamily: 'Poppins',
                                                  color: Color(0xFFD6D8DA),
                                                  fontSize: 12,
                                                  fontWeight: FontWeight.w500,
                                                ),
                                          ),
                                        ],
                                      ),
                                    ),
                                  ),
                                  Spacer(flex: 2),
                                  Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        0, 0, 0, 0),
                                    child: FutureBuilder<ApiCallResponse>(
                                      future: LoginCallCall.call(
                                        password: passwordController!.text,
                                        emailAddress: emailController!.text,
                                      ),
                                      builder: (context, snapshot) {
                                        if (!snapshot.hasData) {
                                          return Center(
                                            child: SizedBox(
                                              width: 50,
                                              height: 50,
                                              child: CircularProgressIndicator(
                                                color: Color(0xFF418D75),
                                              ),
                                            ),
                                          );
                                        }
                                        final mainButtonLoginCallResponse =
                                            snapshot.data!;
                                        return InkWell(
                                          onTap: () async {
                                            if (checkboxListTileValue!) {
                                              setState(() =>
                                                  FFAppState().emailAdress =
                                                      emailController!.text);
                                              setState(() =>
                                                  FFAppState().password =
                                                      passwordController!.text);
                                            }

                                            Map data = {
                                              'username': emailController!.text,
                                              'password':
                                                  passwordController!.text,
                                            };
                                            print(data);
                                            var body = json.encode(data);
                                            loginResponse =
                                                await LoginCallCall.call(
                                              emailAddress:
                                                  emailController!.text,
                                              password:
                                                  passwordController!.text,
                                            );
                                            var response = await http.post(
                                                Uri.parse(
                                                    'http://127.0.0.1:8000/login/token/'),
                                                headers: {
                                                  // "Content-Type":
                                                  //     "application/x-www-form-urlencoded",
                                                  'accept': 'application/json',
                                                },
                                                body: body);
                                            print(response);
                                            print(response.statusCode);

                                            // if (mainButtonLoginCallResponse
                                            //     .succeeded) {
                                            if (response.statusCode == 307) {
                                              await Navigator
                                                  .pushAndRemoveUntil(
                                                context,
                                                PageTransition(
                                                  type: PageTransitionType.fade,
                                                  duration:
                                                      Duration(milliseconds: 0),
                                                  reverseDuration:
                                                      Duration(milliseconds: 0),

                                                  child: new Scaffold(
                                                      backgroundColor:
                                                          Colors.transparent,
                                                      body: MenuWidget()),

                                                  // child: MainPageWidget(),
                                                ),
                                                (r) => false,
                                              );
                                            } else {
                                              await Navigator.push(
                                                context,
                                                PageTransition(
                                                  type: PageTransitionType.fade,
                                                  duration:
                                                      Duration(milliseconds: 0),
                                                  reverseDuration:
                                                      Duration(milliseconds: 0),
                                                  child:
                                                      LoginErrorMessageWidget(),
                                                ),
                                              );
                                            }

                                            setState(() {});
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
                                                alignment:
                                                    AlignmentDirectional(0, 0),
                                                child: Text(
                                                  FFLocalizations.of(context)
                                                      .getText(
                                                    'bbpm2l2x' /* Login */,
                                                  ),
                                                  textAlign: TextAlign.center,
                                                  style: FlutterFlowTheme.of(
                                                          context)
                                                      .bodyText1
                                                      .override(
                                                        fontFamily:
                                                            FlutterFlowTheme.of(
                                                                    context)
                                                                .bodyText1Family,
                                                        color:
                                                            FlutterFlowTheme.of(
                                                                    context)
                                                                .primaryBtnText,
                                                      ),
                                                ),
                                              ),
                                            ),
                                          ),
                                        );
                                      },
                                    ),
                                  ),
                                  Spacer(flex: 5),
                                ],
                              ),
                              Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                    0, 30, 0, 30),
                                child: Row(
                                  mainAxisSize: MainAxisSize.max,
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      FFLocalizations.of(context).getText(
                                        '3j5yksm2' /* Forgot your password? */,
                                      ),
                                      style: FlutterFlowTheme.of(context)
                                          .bodyText1
                                          .override(
                                            fontFamily: 'Poppins',
                                            color: Color(0xFFD6D8DA),
                                            fontWeight: FontWeight.w300,
                                          ),
                                    ),
                                  ],
                                ),
                              ),
                            ],
                          ),
                        ),
                        Spacer(
                          flex: 1,
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
    );
  }
}
