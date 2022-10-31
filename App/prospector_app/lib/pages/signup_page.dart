import 'package:flutter/material.dart';
import 'dart:convert';
import 'dart:ui';

import 'package:email_validator/email_validator.dart';
import 'package:http/http.dart' as http;

import 'package:prospector_app/popups/account_created_widget.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_util.dart';

class SignupWidget extends StatefulWidget {
  const SignupWidget({Key? key}) : super(key: key);

  @override
  _SignupWidgetState createState() => _SignupWidgetState();
}

class _SignupWidgetState extends State<SignupWidget> {
  TextEditingController? usernameController;
  TextEditingController? workplaceController;
  TextEditingController? emailController;
  TextEditingController? phoneNumberController;
  TextEditingController? countryCodeController;
  TextEditingController? passwordController;

  late bool passwordVisibility;
  final scaffoldKey = GlobalKey<ScaffoldState>();

  //* NEW STUFF
  late Color colorState = Color(0xFFD6D8DA);
  late TextStyle labelColorState =
      FlutterFlowTheme.of(context).bodyText1.override(
            fontFamily: 'Poppins',
            color: Color(0xFFD6D8DA),
            fontSize: 12,
            fontWeight: FontWeight.w300,
          );
  late String passwordlabelState = FFLocalizations.of(context).getText(
    'u1vts5lp' /* Password */,
  );

  @override
  void initState() {
    super.initState();
    usernameController = TextEditingController();
    workplaceController = TextEditingController();
    emailController = TextEditingController();
    phoneNumberController = TextEditingController();
    // countryCodeController = TextEditingController();
    final countryCodeController = TextEditingController(text: "+47");
    passwordController = TextEditingController();
    passwordVisibility = false;
  }

  bool req_200 = false;
  bool isEmail(String input) => EmailValidator.validate(input);
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
                  decoration: BoxDecoration(
                    color: FlutterFlowTheme.of(context).cardColor,
                    image: DecorationImage(
                      fit: BoxFit.cover,
                      image: Image.asset(
                        'assets/images/dante_s_view_by_chateaugrief_de1tex5-fullview.jpg',
                      ).image,
                    ),
                  ),
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
                                padding: EdgeInsetsDirectional.fromSTEB(
                                    10, 20, 20, 0),
                                child: TextButton(
                                  onPressed: () async {
                                    Navigator.pop(context);
                                  },
                                  child: Row(
                                    children: [
                                      Icon(
                                        Icons.chevron_left_outlined,
                                        size: 25,
                                        color: Color(0xFFD6D8DA),
                                      ),
                                      SizedBox(width: 10),
                                      Text(
                                        FFLocalizations.of(context).getText(
                                          'ib1c3zui' /* Return To Login */,
                                        ),
                                        style: FlutterFlowTheme.of(context)
                                            .subtitle2
                                            .override(
                                              fontFamily: 'Poppins',
                                              color: Color(0xFFD6D8DA),
                                            ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                              Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                    0, 50, 0, 100),
                                child: Row(
                                  mainAxisSize: MainAxisSize.max,
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  crossAxisAlignment: CrossAxisAlignment.center,
                                  children: [
                                    Text(
                                      FFLocalizations.of(context).getText(
                                        'fpke2str' /* Create Account */,
                                      ),
                                      textAlign: TextAlign.center,
                                      style: FlutterFlowTheme.of(context)
                                          .subtitle1
                                          .override(
                                            fontFamily:
                                                FlutterFlowTheme.of(context)
                                                    .subtitle1Family,
                                            color: Color(0xFFD6D8DA),
                                          ),
                                    ),
                                  ],
                                ),
                              ),
                              Expanded(
                                  child: Padding(
                                      padding: EdgeInsetsDirectional.fromSTEB(
                                          0, 0, 0, 100),
                                      child: Container(
                                          width: 100,
                                          height: 100,
                                          decoration: BoxDecoration(),
                                          child: Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    20, 0, 20, 20),
                                            child: Column(
                                                mainAxisSize: MainAxisSize.min,
                                                mainAxisAlignment:
                                                    MainAxisAlignment.start,
                                                crossAxisAlignment:
                                                    CrossAxisAlignment.center,
                                                children: [
                                                  // USERNAME ________________________________________________
                                                  //Expanded(
                                                  // child:
                                                  Row(
                                                    mainAxisSize:
                                                        MainAxisSize.max,
                                                    mainAxisAlignment:
                                                        MainAxisAlignment
                                                            .center,
                                                    children: [
                                                      Spacer(flex: 2),
                                                      Padding(
                                                        padding:
                                                            EdgeInsetsDirectional
                                                                .fromSTEB(10, 0,
                                                                    20, 0),
                                                        child: Icon(
                                                          Icons.person_sharp,
                                                          color:
                                                              Color(0xFFD6D8DA),
                                                          size: 24,
                                                        ),
                                                      ),
                                                      Expanded(
                                                        flex: 3,
                                                        child: Padding(
                                                          padding:
                                                              EdgeInsetsDirectional
                                                                  .fromSTEB(0,
                                                                      0, 0, 10),
                                                          child: TextFormField(
                                                            cursorColor: Color(
                                                                0xFFD6D8DA),
                                                            controller:
                                                                usernameController,
                                                            obscureText: false,
                                                            decoration:
                                                                InputDecoration(
                                                              hintText:
                                                                  FFLocalizations.of(
                                                                          context)
                                                                      .getText(
                                                                '4dbf2i422' /* Username */,
                                                              ),
                                                              hintStyle:
                                                                  FlutterFlowTheme.of(
                                                                          context)
                                                                      .bodyText1
                                                                      .override(
                                                                        fontFamily:
                                                                            'Poppins',
                                                                        color: Color(
                                                                            0xFFD6D8DA),
                                                                        fontSize:
                                                                            12,
                                                                        fontWeight:
                                                                            FontWeight.w300,
                                                                      ),
                                                              enabledBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                              focusedBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                            ),
                                                            style: FlutterFlowTheme
                                                                    .of(context)
                                                                .bodyText1
                                                                .override(
                                                                  fontFamily:
                                                                      'Poppins',
                                                                  color: Color(
                                                                      0xFFD6D8DA),
                                                                  fontSize: 14,
                                                                  fontWeight:
                                                                      FontWeight
                                                                          .normal,
                                                                ),
                                                            keyboardType:
                                                                TextInputType
                                                                    .emailAddress,
                                                          ),
                                                        ),
                                                      ),
                                                      Spacer(flex: 2),
                                                    ],
                                                  ),
                                                  // ),
                                                  // WORKPLACE ________________________________________________
                                                  //Expanded(
                                                  // child:
                                                  Row(
                                                    mainAxisSize:
                                                        MainAxisSize.max,
                                                    mainAxisAlignment:
                                                        MainAxisAlignment
                                                            .center,
                                                    children: [
                                                      Spacer(flex: 2),
                                                      Padding(
                                                        padding:
                                                            EdgeInsetsDirectional
                                                                .fromSTEB(10, 0,
                                                                    20, 0),
                                                        child: Tooltip(
                                                          message:
                                                              FFLocalizations.of(
                                                                      context)
                                                                  .getText(
                                                            'ib1c322a' /* Only use lowercase letters */,
                                                          ),
                                                          child: Icon(
                                                            Icons
                                                                .home_work_sharp,
                                                            color: Color(
                                                                0xFFD6D8DA),
                                                            size: 24,
                                                          ),
                                                        ),
                                                      ),
                                                      Expanded(
                                                        flex: 3,
                                                        child: Padding(
                                                          padding:
                                                              EdgeInsetsDirectional
                                                                  .fromSTEB(0,
                                                                      0, 0, 10),
                                                          child: TextFormField(
                                                            cursorColor: Color(
                                                                0xFFD6D8DA),
                                                            autovalidateMode:
                                                                AutovalidateMode
                                                                    .onUserInteraction,
                                                            validator: (value) {
                                                              if (validateWorkplace(
                                                                      value!) !=
                                                                  null) {
                                                                return FFLocalizations.of(
                                                                        context)
                                                                    .getText(
                                                                  'ib1c3g2a' /* Workplace not filled correctly */,
                                                                );
                                                              }
                                                              return null;
                                                            },
                                                            controller:
                                                                workplaceController,
                                                            onFieldSubmitted:
                                                                (_) async {
                                                              setState(() => FFAppState()
                                                                      .companyName =
                                                                  workplaceController!
                                                                      .text);
                                                            },
                                                            obscureText: false,
                                                            decoration:
                                                                InputDecoration(
                                                              hintText:
                                                                  FFLocalizations.of(
                                                                          context)
                                                                      .getText(
                                                                'b7328u01' /* Workplace */,
                                                              ),
                                                              hintStyle:
                                                                  FlutterFlowTheme.of(
                                                                          context)
                                                                      .bodyText1
                                                                      .override(
                                                                        fontFamily:
                                                                            'Poppins',
                                                                        color: Color(
                                                                            0xFFD6D8DA),
                                                                        fontSize:
                                                                            12,
                                                                        fontWeight:
                                                                            FontWeight.w300,
                                                                      ),
                                                              enabledBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                              focusedBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                            ),
                                                            style: FlutterFlowTheme
                                                                    .of(context)
                                                                .bodyText1
                                                                .override(
                                                                  fontFamily:
                                                                      'Poppins',
                                                                  color: Color(
                                                                      0xFFD6D8DA),
                                                                  fontSize: 14,
                                                                  fontWeight:
                                                                      FontWeight
                                                                          .normal,
                                                                ),
                                                            keyboardType:
                                                                TextInputType
                                                                    .emailAddress,
                                                          ),
                                                        ),
                                                      ),
                                                      Spacer(flex: 2),
                                                    ],
                                                  ),
                                                  // ),
                                                  //Expanded(
                                                  // child:
                                                  // EMAIL ________________________________________________
                                                  Row(
                                                    mainAxisSize:
                                                        MainAxisSize.max,
                                                    mainAxisAlignment:
                                                        MainAxisAlignment
                                                            .center,
                                                    children: [
                                                      Spacer(flex: 2),
                                                      Padding(
                                                        padding:
                                                            EdgeInsetsDirectional
                                                                .fromSTEB(10, 0,
                                                                    20, 0),
                                                        child: Icon(
                                                          Icons.email_sharp,
                                                          color:
                                                              Color(0xFFD6D8DA),
                                                          size: 24,
                                                        ),
                                                      ),
                                                      Expanded(
                                                        flex: 3,
                                                        child: Padding(
                                                          padding:
                                                              EdgeInsetsDirectional
                                                                  .fromSTEB(0,
                                                                      0, 0, 10),
                                                          child: Form(
                                                            child:
                                                                TextFormField(
                                                              cursorColor: Color(
                                                                  0xFFD6D8DA),
                                                              validator:
                                                                  (value) {
                                                                if (!isEmail(
                                                                    value!)) {
                                                                  return FFLocalizations.of(
                                                                          context)
                                                                      .getText(
                                                                          'in1c322a' /* Please enter a valid email. */
                                                                          );
                                                                }
                                                                return null;
                                                              },
                                                              autovalidateMode:
                                                                  AutovalidateMode
                                                                      .onUserInteraction,
                                                              controller:
                                                                  emailController,
                                                              onFieldSubmitted:
                                                                  (_) async {
                                                                setState(() => FFAppState()
                                                                        .emailAdress =
                                                                    passwordController!
                                                                        .text);
                                                              },
                                                              obscureText:
                                                                  false,
                                                              decoration:
                                                                  InputDecoration(
                                                                hintText:
                                                                    FFLocalizations.of(
                                                                            context)
                                                                        .getText(
                                                                  'zata0tey' /* Email Address */,
                                                                ),
                                                                hintStyle: FlutterFlowTheme.of(
                                                                        context)
                                                                    .bodyText1
                                                                    .override(
                                                                      fontFamily:
                                                                          'Poppins',
                                                                      color: Color(
                                                                          0xFFD6D8DA),
                                                                      fontSize:
                                                                          12,
                                                                      fontWeight:
                                                                          FontWeight
                                                                              .w300,
                                                                    ),
                                                                enabledBorder:
                                                                    UnderlineInputBorder(
                                                                  borderSide:
                                                                      BorderSide(
                                                                    color: Color(
                                                                        0xFF95A1AC),
                                                                    width: 2,
                                                                  ),
                                                                  borderRadius:
                                                                      const BorderRadius
                                                                          .only(
                                                                    topLeft: Radius
                                                                        .circular(
                                                                            4.0),
                                                                    topRight: Radius
                                                                        .circular(
                                                                            4.0),
                                                                  ),
                                                                ),
                                                                focusedBorder:
                                                                    UnderlineInputBorder(
                                                                  borderSide:
                                                                      BorderSide(
                                                                    color: Color(
                                                                        0xFF95A1AC),
                                                                    width: 2,
                                                                  ),
                                                                  borderRadius:
                                                                      const BorderRadius
                                                                          .only(
                                                                    topLeft: Radius
                                                                        .circular(
                                                                            4.0),
                                                                    topRight: Radius
                                                                        .circular(
                                                                            4.0),
                                                                  ),
                                                                ),
                                                              ),
                                                              style: FlutterFlowTheme
                                                                      .of(context)
                                                                  .bodyText1
                                                                  .override(
                                                                    fontFamily:
                                                                        'Poppins',
                                                                    color: Color(
                                                                        0xFFD6D8DA),
                                                                    fontSize:
                                                                        14,
                                                                    fontWeight:
                                                                        FontWeight
                                                                            .normal,
                                                                  ),
                                                              keyboardType:
                                                                  TextInputType
                                                                      .emailAddress,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Spacer(flex: 2),
                                                    ],
                                                  ),
                                                  // ),
                                                  //
                                                  //
                                                  //
                                                  // PHONE NUMBER ________________________________________________
                                                  //Expanded(
                                                  // child:
                                                  Row(
                                                    mainAxisSize:
                                                        MainAxisSize.max,
                                                    mainAxisAlignment:
                                                        MainAxisAlignment
                                                            .center,
                                                    children: [
                                                      Spacer(flex: 8),
                                                      Padding(
                                                        padding:
                                                            EdgeInsetsDirectional
                                                                .fromSTEB(10, 0,
                                                                    20, 0),
                                                        child: Tooltip(
                                                          message:
                                                              FFLocalizations.of(
                                                                      context)
                                                                  .getText(
                                                            'ib1c32na' /* phone tooltip */,
                                                          ),
                                                          child: Icon(
                                                            Icons.phone,
                                                            color: Color(
                                                                0xFFD6D8DA),
                                                            size: 24,
                                                          ),
                                                        ),
                                                      ),
                                                      // country code field****
                                                      Expanded(
                                                        flex: 1,
                                                        child: Padding(
                                                          padding:
                                                              EdgeInsetsDirectional
                                                                  .fromSTEB(0,
                                                                      0, 0, 10),
                                                          child: TextFormField(
                                                            // initialValue: '+47',
                                                            initialValue:
                                                                countryCodeController
                                                                    ?.text,
                                                            cursorColor: Color(
                                                                0xFFD6D8DA),
                                                            controller:
                                                                countryCodeController,
                                                            obscureText: false,
                                                            decoration:
                                                                InputDecoration(
                                                              hintText: '+47',
                                                              // countryCodeController
                                                              // ?.text,
                                                              // hintText:
                                                              //     countryCodeController
                                                              //         ?.text,
                                                              // hintText:
                                                              //     FFLocalizations.of(
                                                              //             context)
                                                              //         .getText(
                                                              //   'cjdsadsl' /* phone number */,
                                                              // ),
                                                              hintStyle:
                                                                  FlutterFlowTheme.of(
                                                                          context)
                                                                      .bodyText1
                                                                      .override(
                                                                        fontFamily:
                                                                            'Poppins',
                                                                        color: Color(
                                                                            0xFFD6D8DA),
                                                                        fontSize:
                                                                            12,
                                                                        fontWeight:
                                                                            FontWeight.w300,
                                                                      ),
                                                              enabledBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                              focusedBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                            ),
                                                            style: FlutterFlowTheme
                                                                    .of(context)
                                                                .bodyText1
                                                                .override(
                                                                  fontFamily:
                                                                      'Poppins',
                                                                  color: Color(
                                                                      0xFFD6D8DA),
                                                                  fontSize: 14,
                                                                  fontWeight:
                                                                      FontWeight
                                                                          .normal,
                                                                ),
                                                            keyboardType:
                                                                TextInputType
                                                                    .emailAddress,
                                                          ),
                                                        ),
                                                      ),

                                                      // number field *****
                                                      Expanded(
                                                        flex: 11,
                                                        child: Padding(
                                                          padding:
                                                              EdgeInsetsDirectional
                                                                  .fromSTEB(0,
                                                                      0, 0, 10),
                                                          child: TextFormField(
                                                            cursorColor: Color(
                                                                0xFFD6D8DA),
                                                            controller:
                                                                phoneNumberController,
                                                            obscureText: false,
                                                            decoration:
                                                                InputDecoration(
                                                              hintText:
                                                                  FFLocalizations.of(
                                                                          context)
                                                                      .getText(
                                                                'cjdsadsl' /* phone number */,
                                                              ),
                                                              hintStyle:
                                                                  FlutterFlowTheme.of(
                                                                          context)
                                                                      .bodyText1
                                                                      .override(
                                                                        fontFamily:
                                                                            'Poppins',
                                                                        color: Color(
                                                                            0xFFD6D8DA),
                                                                        fontSize:
                                                                            12,
                                                                        fontWeight:
                                                                            FontWeight.w300,
                                                                      ),
                                                              enabledBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                              focusedBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                            ),
                                                            style: FlutterFlowTheme
                                                                    .of(context)
                                                                .bodyText1
                                                                .override(
                                                                  fontFamily:
                                                                      'Poppins',
                                                                  color: Color(
                                                                      0xFFD6D8DA),
                                                                  fontSize: 14,
                                                                  fontWeight:
                                                                      FontWeight
                                                                          .normal,
                                                                ),
                                                            keyboardType:
                                                                TextInputType
                                                                    .emailAddress,
                                                          ),
                                                        ),
                                                      ),
                                                      Spacer(flex: 8),
                                                    ],
                                                  ),
                                                  // ), //
                                                  //
                                                  // PASSWORD ________________________________________________
                                                  //Expanded(
                                                  // child:
                                                  Row(
                                                    mainAxisSize:
                                                        MainAxisSize.max,
                                                    children: [
                                                      Spacer(flex: 2),
                                                      Padding(
                                                        padding:
                                                            EdgeInsetsDirectional
                                                                .fromSTEB(10, 0,
                                                                    20, 0),
                                                        child: Tooltip(
                                                          message:
                                                              FFLocalizations.of(
                                                                      context)
                                                                  .getText(
                                                            'ib1c3sna' /* password tooltip */,
                                                          ),
                                                          child: Icon(
                                                            Icons.lock_sharp,
                                                            color: Color(
                                                                0xFFD6D8DA),
                                                            size: 24,
                                                          ),
                                                        ),
                                                      ),
                                                      Expanded(
                                                        flex: 3,
                                                        child: Padding(
                                                          padding:
                                                              EdgeInsetsDirectional
                                                                  .fromSTEB(0,
                                                                      0, 0, 10),
                                                          child: TextFormField(
                                                            cursorColor: Color(
                                                                0xFFD6D8DA),
                                                            validator: (value) {
                                                              if (validatePassword(
                                                                      value!) !=
                                                                  null) {
                                                                return FFLocalizations.of(
                                                                        context)
                                                                    .getText(
                                                                  'ib1c3s2a' /* Please enter a strong password. */,
                                                                );
                                                              }

                                                              return null;
                                                            },
                                                            autovalidateMode:
                                                                AutovalidateMode
                                                                    .onUserInteraction,
                                                            controller:
                                                                passwordController,
                                                            onFieldSubmitted:
                                                                (_) async {
                                                              setState(() => FFAppState()
                                                                      .emailAdress =
                                                                  passwordController!
                                                                      .text);
                                                            },
                                                            obscureText:
                                                                !passwordVisibility,
                                                            decoration:
                                                                InputDecoration(
                                                              hintText:
                                                                  passwordlabelState,
                                                              hintStyle:
                                                                  labelColorState,
                                                              enabledBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                              focusedBorder:
                                                                  UnderlineInputBorder(
                                                                borderSide:
                                                                    BorderSide(
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  width: 2,
                                                                ),
                                                                borderRadius:
                                                                    const BorderRadius
                                                                        .only(
                                                                  topLeft: Radius
                                                                      .circular(
                                                                          4.0),
                                                                  topRight: Radius
                                                                      .circular(
                                                                          4.0),
                                                                ),
                                                              ),
                                                              suffixIcon:
                                                                  InkWell(
                                                                onTap: () =>
                                                                    setState(
                                                                  () => passwordVisibility =
                                                                      !passwordVisibility,
                                                                ),
                                                                focusNode: FocusNode(
                                                                    skipTraversal:
                                                                        true),
                                                                child: Icon(
                                                                  passwordVisibility
                                                                      ? Icons
                                                                          .visibility_outlined
                                                                      : Icons
                                                                          .visibility_off_outlined,
                                                                  color: Color(
                                                                      0xFF95A1AC),
                                                                  size: 22,
                                                                ),
                                                              ),
                                                            ),
                                                            style: FlutterFlowTheme
                                                                    .of(context)
                                                                .bodyText1
                                                                .override(
                                                                  fontFamily:
                                                                      'Poppins',
                                                                  color:
                                                                      colorState,
                                                                  fontSize: 14,
                                                                  fontWeight:
                                                                      FontWeight
                                                                          .normal,
                                                                ),
                                                          ),
                                                        ),
                                                      ),
                                                      Spacer(flex: 2),
                                                    ],
                                                  ),
                                                  // ),
                                                  // SIGNUP BUTTON ________________________________________________
                                                  //Expanded(
                                                  // child:
                                                  Container(
                                                    width:
                                                        MediaQuery.of(context)
                                                            .size
                                                            .width,
                                                    height: 100,
                                                    decoration: BoxDecoration(
                                                      color: Color(0x00353E49),
                                                    ),
                                                    child: Padding(
                                                      padding:
                                                          EdgeInsetsDirectional
                                                              .fromSTEB(
                                                                  0, 10, 0, 0),
                                                      child: Row(
                                                        mainAxisSize:
                                                            MainAxisSize.max,
                                                        mainAxisAlignment:
                                                            MainAxisAlignment
                                                                .spaceAround,
                                                        crossAxisAlignment:
                                                            CrossAxisAlignment
                                                                .end,
                                                        children: [
                                                          Spacer(flex: 5),
                                                          Expanded(
                                                            flex: 4,
                                                            child: Container(
                                                              width: 100,
                                                              height: 100,
                                                              decoration:
                                                                  BoxDecoration(),
                                                            ),
                                                          ),
                                                          Spacer(flex: 2),
                                                          Padding(
                                                            padding:
                                                                EdgeInsetsDirectional
                                                                    .fromSTEB(
                                                                        10,
                                                                        0,
                                                                        10,
                                                                        0),
                                                            child: Container(
                                                              width: 150,
                                                              height: 30,
                                                              child: InkWell(
                                                                onTap:
                                                                    () async {
                                                                  if (emailController?.text == "" ||
                                                                      workplaceController!
                                                                              .text ==
                                                                          "" ||
                                                                      usernameController!
                                                                              .text ==
                                                                          "" ||
                                                                      passwordController!
                                                                              .text ==
                                                                          "" ||
                                                                      phoneNumberController!
                                                                              .text ==
                                                                          "") {
                                                                    showDialog(
                                                                        context:
                                                                            context,
                                                                        builder:
                                                                            (BuildContext
                                                                                context) {
                                                                          return AlertDialog(
                                                                            backgroundColor:
                                                                                Color(0x00353E49),
                                                                            title:
                                                                                Text(
                                                                              FFLocalizations.of(context).getText(
                                                                                'ib1c3p2a' /* Form is not properly filled  */,
                                                                              ),
                                                                              style: FlutterFlowTheme.of(context).bodyText1.override(
                                                                                    fontFamily: FlutterFlowTheme.of(context).bodyText1Family,
                                                                                    color: Colors.white,
                                                                                  ),
                                                                            ),
                                                                          );
                                                                        });
                                                                  } else {
                                                                    String
                                                                        email =
                                                                        emailController!
                                                                            .text;
                                                                    String
                                                                        username =
                                                                        usernameController!
                                                                            .text;
                                                                    String
                                                                        password =
                                                                        passwordController!
                                                                            .text;
                                                                    String
                                                                        workplace =
                                                                        workplaceController!
                                                                            .text;
                                                                    String
                                                                        phone_number =
                                                                        countryCodeController!.text +
                                                                            phoneNumberController!.text;
                                                                    Map data = {
                                                                      'brukernavn':
                                                                          username,
                                                                      'epost':
                                                                          email,
                                                                      'passord':
                                                                          password,
                                                                      'organisasjon':
                                                                          workplace,
                                                                      'telefon_nummer':
                                                                          phone_number,
                                                                    };
                                                                    var body = json
                                                                        .encode(
                                                                            data);

                                                                    var response = await http.post(
                                                                        Uri.parse(
                                                                            'http://127.0.0.1:8000/users/'),
                                                                        headers: {
                                                                          "Content-Type":
                                                                              "application/json",
                                                                          "accept":
                                                                              "application/json",
                                                                        },
                                                                        body:
                                                                            body);

                                                                    if (response
                                                                            .statusCode ==
                                                                        200) {
                                                                      await Navigator
                                                                          .push(
                                                                        context,
                                                                        PageTransition(
                                                                            type:
                                                                                PageTransitionType.fade,
                                                                            duration: Duration(milliseconds: 0),
                                                                            reverseDuration: Duration(milliseconds: 0),
                                                                            child: AccountCreatedWidget()),
                                                                      );
                                                                    } else {
                                                                      showDialog(
                                                                        context:
                                                                            context,
                                                                        builder:
                                                                            (BuildContext
                                                                                context) {
                                                                          return AlertDialog(
                                                                            contentTextStyle:
                                                                                FlutterFlowTheme.of(context).bodyText1,
                                                                            title:
                                                                                Text("Error!"),
                                                                            content:
                                                                                Text(
                                                                              FFLocalizations.of(context).getText('ibsc322a' /* Unable to create account */
                                                                                  ),
                                                                              style: FlutterFlowTheme.of(context).bodyText1.override(fontFamily: FlutterFlowTheme.of(context).bodyText1Family, fontSize: 14, fontWeight: FontWeight.w300),
                                                                            ),
                                                                          );
                                                                        },
                                                                      );
                                                                    }
                                                                  }

                                                                  setState(() => FFAppState()
                                                                          .emailAdress =
                                                                      emailController!
                                                                          .text);
                                                                  setState(() => FFAppState()
                                                                          .companyName =
                                                                      workplaceController!
                                                                          .text);
                                                                  setState(() => FFAppState()
                                                                          .userName =
                                                                      usernameController!
                                                                          .text);
                                                                },
                                                                child: Material(
                                                                  color: Colors
                                                                      .transparent,
                                                                  elevation: 5,
                                                                  child:
                                                                      Container(
                                                                    width: 150,
                                                                    height: 30,
                                                                    decoration:
                                                                        BoxDecoration(
                                                                      color: FlutterFlowTheme.of(
                                                                              context)
                                                                          .primaryColor,
                                                                      // color: Color(
                                                                      //     0xFF5D8387),
                                                                    ),
                                                                    child:
                                                                        Align(
                                                                      alignment:
                                                                          AlignmentDirectional(
                                                                              0,
                                                                              0),
                                                                      child:
                                                                          Text(
                                                                        FFLocalizations.of(context)
                                                                            .getText(
                                                                          '4dbf2i4h' /* Sign Up */,
                                                                        ),
                                                                        style: FlutterFlowTheme.of(context)
                                                                            .bodyText1
                                                                            .override(
                                                                              fontFamily: FlutterFlowTheme.of(context).bodyText1Family,
                                                                              color: Colors.white,
                                                                            ),
                                                                      ),
                                                                    ),
                                                                  ),
                                                                ),
                                                              ),
                                                            ),
                                                          ),
                                                          Spacer(flex: 5),
                                                        ],
                                                      ),
                                                    ),
                                                  ),
                                                ]),
                                          ))))
                            ],
                          ),
                        ),
                      ]),
                ),
              ),
            )
          ],
        ),
      ),
      // ],
      // ),
      // ),
      // ),
      // ),
      // ],
      // ),
      // ),
    );
  }

  String? validateWorkplace(String value) {
    RegExp regex = new RegExp(r'^[a-z]+$');
    if (value.isEmpty) {
      return
          // Text(
          //   FFLocalizations.of(context)
          //       .getText('in1c322b' /* Please enter the name of your workplace */),
          //   style: TextStyle(fontSize: 30),
          // );
          FFLocalizations.of(context).getText(
              'in1c322b' /* Please enter the name of your workplace */);
    } else {
      if (!regex.hasMatch(value)) {
        return FFLocalizations.of(context)
            .getText('in1c322s' /* Workplace not filled correctly */);
      } else {
        return null;
      }
    }
  }

  String? validatePassword(String value) {
    RegExp regex = RegExp(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$');
    if (value.isEmpty) {
      return FFLocalizations.of(context)
          .getText('in1c322c' /* Please enter password */);
    } else {
      if (!regex.hasMatch(value)) {
        return FFLocalizations.of(context)
            .getText('in1c322d' /* Enter valid password */);
      } else {
        return null;
      }
    }
  }
}
