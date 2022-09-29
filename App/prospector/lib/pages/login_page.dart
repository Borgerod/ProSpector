import 'package:flutter/material.dart';

import 'package:hive_flutter/hive_flutter.dart';
import 'package:hive/hive.dart';

import 'package:prospector/popups/reset_password_authentication_widget.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/backend/api_requests/api_calls.dart';
import 'package:prospector/pages/signup_page.dart';

class LoginWidget extends StatefulWidget {
  const LoginWidget({Key? key}) : super(key: key);

  @override
  _LoginWidgetState createState() => _LoginWidgetState();
}

class _LoginWidgetState extends State<LoginWidget> {
  late bool passwordVisibility;
  final scaffoldKey = GlobalKey<ScaffoldState>();

  // * NEW VARIABLES
  TextEditingController email = TextEditingController(); //* email-controller
  TextEditingController pass = TextEditingController(); //*  pass-controller
  bool isChecked = false; //*                                rememberMe
  late Box box1;

  @override
  void initState() {
    super.initState();
    passwordVisibility = false;
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

  // _______________________________________________ USER INTERFACE ______________________________________________________
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
                              // _________________  EMAIL ADDRESS __________________________
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
                                        controller:
                                            email, //* <--- email-controller
                                        keyboardType:
                                            TextInputType.emailAddress,
                                        obscureText: false,
                                        cursorColor: Color(0xFFD6D8DA),
                                        style: FlutterFlowTheme.of(context)
                                            .bodyText1
                                            .override(
                                              fontFamily: 'Poppins',
                                              color: Color(0xFFD6D8DA),
                                              fontSize: 12,
                                              fontWeight: FontWeight.normal,
                                            ),
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
                                        //? ______ TEMPORARLY DISABLED ______
                                        // onFieldSubmitted: (_) async {
                                        //   setState(() =>
                                        //       FFAppState().emailAdress =
                                        //           passwordController!.text);
                                        // },
                                        //? _________________________________
                                      ),
                                    ),
                                  ),
                                  Spacer(flex: 2),
                                ],
                              ),
                              // ___________________________________________________________
                              // _________________  PASSWORD _______________________________
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
                                        controller: pass,
                                        keyboardType:
                                            TextInputType.visiblePassword,
                                        obscureText: !passwordVisibility,
                                        cursorColor: Color(0xFFD6D8DA),
                                        style: FlutterFlowTheme.of(context)
                                            .bodyText1
                                            .override(
                                              fontFamily: 'Lexend Deca',
                                              color: Color(0xFFD6D8DA),
                                              fontSize: 12,
                                              fontWeight: FontWeight.normal,
                                            ),
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
                                        onFieldSubmitted: (value) async {
                                          Login.callback(email, pass, isChecked,
                                              box1, context);
                                        },
                                      ),
                                    ),
                                  ),
                                  Spacer(flex: 2),
                                ],
                              ),
                              // ___________________________________________________________
                              // _________________  LOGIN & REMEMBER ME ____________________
                              Row(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceEvenly,
                                crossAxisAlignment: CrossAxisAlignment.center,
                                children: [
                                  Spacer(flex: 6),
                                  // _________________  REMEMBER ME ________________________
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
                                              value: //  The checkbox value is initially the basevalue
                                                  isChecked, // of isChecked (bool isChecked = false;)
                                              activeColor:
                                                  FlutterFlowTheme.of(context)
                                                      .primaryColor,
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
                                  // _______________________________________________________

                                  Spacer(flex: 2),
                                  // _________________  LOGIN BUTTON ME ____________________
                                  Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        0, 0, 0, 0),
                                    child: InkWell(
                                      onTap: () {
                                        Login.callback(email, pass, isChecked,
                                            box1, context);
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
                                              style:
                                                  FlutterFlowTheme.of(context)
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
                                    ),
                                  ),
                                  //________________________________________________________
                                  Spacer(flex: 5),
                                ],
                              ),

                              // _________________  FORGOT PASSWORD ________________________
                              Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                    0, 30, 0, 30),
                                child: Row(
                                  mainAxisSize: MainAxisSize.max,
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    InkWell(
                                      child: Text(
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
                                      onTap: () async {
                                        await Navigator.push(
                                          context,
                                          PageTransition(
                                            type: PageTransitionType.fade,
                                            duration: Duration(milliseconds: 0),
                                            reverseDuration:
                                                Duration(milliseconds: 0),
                                            child:
                                                ResetPasswordAuthenticationWidget(),
                                          ),
                                        );
                                      },
                                    ),
                                  ],
                                ),
                              ),
                              // ___________________________________________________________
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
