import 'package:flutter/material.dart';
import 'package:prospector/components/menu_widget.dart';

import 'package:prospector/flutter_flow/flutter_flow_expanded_image_view.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/components/plain_background_widget.dart';
import 'package:prospector/components/home_button_widget.dart';

class InstructionsWidget extends StatefulWidget {
  const InstructionsWidget({Key? key}) : super(key: key);

  @override
  _InstructionsWidgetState createState() => _InstructionsWidgetState();
}

class _InstructionsWidgetState extends State<InstructionsWidget> {
  final scaffoldKey = GlobalKey<ScaffoldState>();
  late String imageOne;
  late String imageTwo;
  late String imageThree;

  @override
  Widget build(BuildContext context) {
    setImages();
    return Scaffold(
      key: scaffoldKey,
      //* __ COLOR __
      backgroundColor: Colors.transparent,
      floatingActionButton: HomeButton(),
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            fit: BoxFit.cover,
            image: Image.asset(
              getImage(context),
            ).image,
          ),
        ),
        child: Padding(
          padding: EdgeInsetsDirectional.fromSTEB(20, 100, 20, 20),
          child: Row(
            mainAxisSize: MainAxisSize.max,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Expanded(
                // flex: 3,
                child: Column(
                  mainAxisSize: MainAxisSize.max,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    //! ___________________ TITLE __________________
                    Padding(
                      padding: EdgeInsetsDirectional.fromSTEB(20, 20, 20, 20),
                      child: Text(
                        FFLocalizations.of(context).getText(
                          'rtlzy4ms' /* Instructions */,
                        ),
                        style: FlutterFlowTheme.of(context).title1.override(
                              fontFamily:
                                  FlutterFlowTheme.of(context).title1Family,
                              fontSize: 30,
                            ),
                      ),
                    ),
                    //! ___________________ CARDS ___________________
                    Expanded(
                      flex: 3,
                      child: Row(
                        mainAxisSize: MainAxisSize.max,
                        mainAxisAlignment: MainAxisAlignment.spaceAround,
                        children: [
                          Expanded(
                            flex: 2,
                            child: Padding(
                              padding: EdgeInsetsDirectional.fromSTEB(
                                  10, 10, 10, 10),
                              child: Material(
                                color: Colors.transparent,
                                elevation: 5,
                                child: Container(
                                  width: MediaQuery.of(context).size.width,
                                  height:
                                      MediaQuery.of(context).size.height * 1,
                                  constraints: BoxConstraints(
                                    maxWidth: MediaQuery.of(context).size.width,
                                    maxHeight:
                                        MediaQuery.of(context).size.height * 1,
                                  ),
                                  decoration: BoxDecoration(
                                    color:
                                        FlutterFlowTheme.of(context).cardColor,
                                    border: Border.all(
                                      color: FlutterFlowTheme.of(context)
                                          .boarderColor,
                                      width: 3,
                                    ),
                                  ),
                                  child: Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        10, 10, 10, 10),
                                    child: Column(
                                      mainAxisSize: MainAxisSize.max,
                                      mainAxisAlignment:
                                          MainAxisAlignment.spaceAround,
                                      crossAxisAlignment:
                                          CrossAxisAlignment.center,
                                      children: [
                                        Expanded(
                                          flex: 1,
                                          child: Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    20, 0, 20, 0),
                                            child: Row(
                                              mainAxisSize: MainAxisSize.max,
                                              mainAxisAlignment:
                                                  MainAxisAlignment
                                                      .spaceBetween,
                                              children: [
                                                Text(
                                                  FFLocalizations.of(context)
                                                      .getText(
                                                    'j9hnq0ql' /* Step 1 */,
                                                  ),
                                                  style: FlutterFlowTheme.of(
                                                          context)
                                                      .subtitle1
                                                      .override(
                                                        fontFamily:
                                                            FlutterFlowTheme.of(
                                                                    context)
                                                                .subtitle1Family,
                                                        fontSize: 20,
                                                      ),
                                                ),
                                                Spacer(),
                                                Spacer(),
                                              ],
                                            ),
                                          ),
                                        ),
                                        Expanded(
                                          flex: 5,
                                          child: Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    20, 20, 20, 20),
                                            child: Row(
                                              mainAxisSize: MainAxisSize.max,
                                              mainAxisAlignment:
                                                  MainAxisAlignment.spaceEvenly,
                                              crossAxisAlignment:
                                                  CrossAxisAlignment.stretch,
                                              children: [
                                                Expanded(
                                                  flex: 1,
                                                  child: Padding(
                                                    padding:
                                                        EdgeInsetsDirectional
                                                            .fromSTEB(
                                                                10, 0, 20, 0),
                                                    child:
                                                        SingleChildScrollView(
                                                      child: Text(
                                                        FFLocalizations.of(
                                                                context)
                                                            .getText(
                                                          'obwwgp74' /* Lorem ipsum dolor sit amet, co... */,
                                                        ),
                                                        style: FlutterFlowTheme
                                                                .of(context)
                                                            .bodyText2
                                                            .override(
                                                                fontFamily:
                                                                    'Poppins',
                                                                fontSize: 12,
                                                                fontWeight:
                                                                    FontWeight
                                                                        .w300),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                                Expanded(
                                                  flex: 1,
                                                  child: Padding(
                                                    padding:
                                                        EdgeInsetsDirectional
                                                            .fromSTEB(
                                                                10, 0, 0, 0),
                                                    child: Material(
                                                      color: Colors.transparent,
                                                      elevation: 5,
                                                      child: Container(
                                                        decoration:
                                                            BoxDecoration(
                                                          color: FlutterFlowTheme
                                                                  .of(context)
                                                              .cardColor,
                                                        ),
                                                        child: Image.asset(
                                                          imageOne,
                                                          //  if (this == InterfaceBrightness.light){

                                                          // },
                                                          // 'assets/images/callList_checkboxes.JPG',
                                                          width: MediaQuery.of(
                                                                  context)
                                                              .size
                                                              .width,
                                                          height: MediaQuery.of(
                                                                      context)
                                                                  .size
                                                                  .height *
                                                              1,
                                                          fit: BoxFit.cover,
                                                        ),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                              ],
                                            ),
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          Expanded(
                            flex: 3,
                            child: Padding(
                              padding: EdgeInsetsDirectional.fromSTEB(
                                  10, 10, 10, 10),
                              child: Material(
                                color: Colors.transparent,
                                elevation: 5,
                                child: Container(
                                  width: MediaQuery.of(context).size.width,
                                  height:
                                      MediaQuery.of(context).size.height * 1,
                                  constraints: BoxConstraints(
                                    maxWidth: MediaQuery.of(context).size.width,
                                    maxHeight:
                                        MediaQuery.of(context).size.height * 1,
                                  ),
                                  decoration: BoxDecoration(
                                    color:
                                        FlutterFlowTheme.of(context).cardColor,
                                    border: Border.all(
                                      color: FlutterFlowTheme.of(context)
                                          .boarderColor,
                                      width: 3,
                                    ),
                                  ),
                                  child: Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        10, 10, 10, 10),
                                    child: Column(
                                      mainAxisSize: MainAxisSize.max,
                                      mainAxisAlignment:
                                          MainAxisAlignment.spaceAround,
                                      crossAxisAlignment:
                                          CrossAxisAlignment.center,
                                      children: [
                                        Expanded(
                                          flex: 1,
                                          child: Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    20, 0, 20, 0),
                                            child: Row(
                                              mainAxisSize: MainAxisSize.max,
                                              mainAxisAlignment:
                                                  MainAxisAlignment
                                                      .spaceBetween,
                                              children: [
                                                Text(
                                                  FFLocalizations.of(context)
                                                      .getText(
                                                    'xnz45xlp' /* Step 2 */,
                                                  ),
                                                  style: FlutterFlowTheme.of(
                                                          context)
                                                      .subtitle1
                                                      .override(
                                                        fontFamily:
                                                            FlutterFlowTheme.of(
                                                                    context)
                                                                .subtitle1Family,
                                                        fontSize: 20,
                                                      ),
                                                ),
                                                Spacer(),
                                                Spacer(),
                                              ],
                                            ),
                                          ),
                                        ),
                                        Expanded(
                                          flex: 5,
                                          child: Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    20, 20, 20, 20),
                                            child: Row(
                                              mainAxisSize: MainAxisSize.max,
                                              mainAxisAlignment:
                                                  MainAxisAlignment.spaceEvenly,
                                              crossAxisAlignment:
                                                  CrossAxisAlignment.stretch,
                                              children: [
                                                Expanded(
                                                  flex: 1,
                                                  child: Padding(
                                                    padding:
                                                        EdgeInsetsDirectional
                                                            .fromSTEB(
                                                                10, 0, 20, 0),
                                                    child:
                                                        SingleChildScrollView(
                                                      child: Text(
                                                        FFLocalizations.of(
                                                                context)
                                                            .getText(
                                                          'rj07qb0g' /* Lorem ipsum dolor sit amet, co... */,
                                                        ),
                                                        style: FlutterFlowTheme
                                                                .of(context)
                                                            .bodyText2
                                                            .override(
                                                                fontFamily:
                                                                    'Poppins',
                                                                fontSize: 12,
                                                                fontWeight:
                                                                    FontWeight
                                                                        .w300),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                                Expanded(
                                                  flex: 2,
                                                  child: Padding(
                                                    padding:
                                                        EdgeInsetsDirectional
                                                            .fromSTEB(
                                                                10, 0, 0, 0),
                                                    child: Material(
                                                      elevation: 5,
                                                      child: Container(
                                                        width: 100,
                                                        height: 100,
                                                        constraints:
                                                            BoxConstraints(
                                                          maxWidth: 100,
                                                          maxHeight: 100,
                                                        ),
                                                        // decoration: BoxDecoration(
                                                        //   boxShadow: [
                                                        //     BoxShadow(
                                                        //       blurRadius: 4,
                                                        //       color: Color(
                                                        //           0x33000000),
                                                        //       offset:
                                                        //           Offset(0, 2),
                                                        //       spreadRadius: 5,
                                                        //     )
                                                        //   ],
                                                        //   color:
                                                        //       FlutterFlowTheme.of(
                                                        //               context)
                                                        //           .cardColor,
                                                        //   shape:
                                                        //       BoxShape.rectangle,
                                                        // ),
                                                        child: InkWell(
                                                          onTap: () async {
                                                            await Navigator
                                                                .push(
                                                              context,
                                                              PageTransition(
                                                                type:
                                                                    PageTransitionType
                                                                        .fade,
                                                                child:
                                                                    FlutterFlowExpandedImageView(
                                                                  image: Image
                                                                      .asset(
                                                                    imageTwo,
                                                                    // 'assets/images/tick_all_prospects.jpg',
                                                                    width: MediaQuery.of(
                                                                            context)
                                                                        .size
                                                                        .width,
                                                                    height: MediaQuery.of(context)
                                                                            .size
                                                                            .height *
                                                                        1,
                                                                    fit: BoxFit
                                                                        .contain,
                                                                  ),
                                                                  allowRotation:
                                                                      false,
                                                                  tag:
                                                                      'instructionImageTag2',
                                                                  useHeroAnimation:
                                                                      true,
                                                                ),
                                                              ),
                                                            );
                                                          },
                                                          child: Hero(
                                                            tag:
                                                                'instructionImageTag2',
                                                            transitionOnUserGestures:
                                                                true,
                                                            child: Image.asset(
                                                              imageTwo,
                                                              // 'assets/images/tick_all_prospects.jpg',
                                                              width:
                                                                  MediaQuery.of(
                                                                          context)
                                                                      .size
                                                                      .width,
                                                              height: MediaQuery.of(
                                                                          context)
                                                                      .size
                                                                      .height *
                                                                  1,
                                                              fit: BoxFit.fill,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                              ],
                                            ),
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                    Expanded(
                      flex: 3,
                      child: Row(
                        mainAxisSize: MainAxisSize.max,
                        mainAxisAlignment: MainAxisAlignment.spaceAround,
                        children: [
                          Expanded(
                            flex: 3,
                            child: Padding(
                              padding: EdgeInsetsDirectional.fromSTEB(
                                  10, 10, 10, 10),
                              child: Material(
                                color: Colors.transparent,
                                elevation: 5,
                                child: Container(
                                  width: MediaQuery.of(context).size.width,
                                  height:
                                      MediaQuery.of(context).size.height * 1,
                                  constraints: BoxConstraints(
                                    maxWidth: MediaQuery.of(context).size.width,
                                    maxHeight:
                                        MediaQuery.of(context).size.height * 1,
                                  ),
                                  decoration: BoxDecoration(
                                    color:
                                        FlutterFlowTheme.of(context).cardColor,
                                    border: Border.all(
                                      color: FlutterFlowTheme.of(context)
                                          .boarderColor,
                                      width: 3,
                                    ),
                                  ),
                                  child: Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        10, 10, 10, 10),
                                    child: Column(
                                      mainAxisSize: MainAxisSize.max,
                                      mainAxisAlignment:
                                          MainAxisAlignment.spaceAround,
                                      crossAxisAlignment:
                                          CrossAxisAlignment.center,
                                      children: [
                                        Expanded(
                                          flex: 1,
                                          child: Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    20, 0, 20, 0),
                                            child: Row(
                                              mainAxisSize: MainAxisSize.max,
                                              mainAxisAlignment:
                                                  MainAxisAlignment
                                                      .spaceBetween,
                                              children: [
                                                Text(
                                                  FFLocalizations.of(context)
                                                      .getText(
                                                    'tsty4p9e' /* Step 3 */,
                                                  ),
                                                  style: FlutterFlowTheme.of(
                                                          context)
                                                      .subtitle1
                                                      .override(
                                                        fontFamily:
                                                            FlutterFlowTheme.of(
                                                                    context)
                                                                .subtitle1Family,
                                                        fontSize: 20,
                                                      ),
                                                ),
                                              ],
                                            ),
                                          ),
                                        ),
                                        Expanded(
                                          flex: 5,
                                          child: Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    20, 20, 20, 20),
                                            child: Row(
                                              mainAxisSize: MainAxisSize.max,
                                              mainAxisAlignment:
                                                  MainAxisAlignment.spaceEvenly,
                                              crossAxisAlignment:
                                                  CrossAxisAlignment.stretch,
                                              children: [
                                                Expanded(
                                                  flex: 2,
                                                  child: Padding(
                                                    padding:
                                                        EdgeInsetsDirectional
                                                            .fromSTEB(
                                                                10, 0, 30, 0),
                                                    child:
                                                        SingleChildScrollView(
                                                      child: Text(
                                                        FFLocalizations.of(
                                                                context)
                                                            .getText(
                                                          'uheh63gf' /* Lorem ipsum dolor sit amet, co... */,
                                                        ),
                                                        style: FlutterFlowTheme
                                                                .of(context)
                                                            .bodyText2
                                                            .override(
                                                                fontFamily:
                                                                    'Poppins',
                                                                fontSize: 12,
                                                                fontWeight:
                                                                    FontWeight
                                                                        .w300),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                                Expanded(
                                                  flex: 5,
                                                  child: Padding(
                                                    padding:
                                                        EdgeInsetsDirectional
                                                            .fromSTEB(
                                                                0, 0, 0, 0),
                                                    child: Material(
                                                      elevation: 5,
                                                      child: Container(
                                                        constraints:
                                                            BoxConstraints.expand(
                                                                width: double
                                                                    .infinity,
                                                                height: double
                                                                    .infinity),
                                                        // decoration:
                                                        //     BoxDecoration(
                                                        //   boxShadow: [
                                                        //     BoxShadow(
                                                        //       blurRadius: 4,
                                                        //       color: Color(
                                                        //           0x33000000),
                                                        //       offset:
                                                        //           Offset(0, 2),
                                                        //       spreadRadius: 5,
                                                        //     )
                                                        //   ],
                                                        //   shape: BoxShape
                                                        //       .rectangle,
                                                        // ),
                                                        child: Image.asset(
                                                          imageThree,
                                                          // 'assets/images/renew_callList.JPG',
                                                          width: MediaQuery.of(
                                                                  context)
                                                              .size
                                                              .width,
                                                          height: MediaQuery.of(
                                                                      context)
                                                                  .size
                                                                  .height *
                                                              1,
                                                          fit: BoxFit.cover,
                                                        ),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                              ],
                                            ),
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          Expanded(
                            flex: 2,
                            child: Padding(
                              padding: EdgeInsetsDirectional.fromSTEB(
                                  10, 10, 10, 10),
                              child: Material(
                                color: Colors.transparent,
                                elevation: 5,
                                child: Container(
                                  width: MediaQuery.of(context).size.width,
                                  height:
                                      MediaQuery.of(context).size.height * 1,
                                  constraints: BoxConstraints(
                                    maxWidth: MediaQuery.of(context).size.width,
                                    maxHeight:
                                        MediaQuery.of(context).size.height * 1,
                                  ),
                                  decoration: BoxDecoration(
                                    color:
                                        FlutterFlowTheme.of(context).cardColor,
                                    border: Border.all(
                                      color: FlutterFlowTheme.of(context)
                                          .boarderColor,
                                      width: 3,
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void setImages() {
    // if (this == InterfaceBrightness.light) {
    // if (InterfaceBrightness.values == light) {
    if (Theme.of(context).brightness == Brightness.light) {
      setState(() {
        imageOne = 'assets/images/callList_checkboxes_light.JPG';
        imageTwo = 'assets/images/tick_all_prospects_light.jpg';
        imageThree = 'assets/images/renew_callList_light.JPG';
      });
    } else {
      setState(() {
        imageOne = 'assets/images/callList_checkboxes.JPG';
        imageTwo = 'assets/images/tick_all_prospects.jpg';
        imageThree = 'assets/images/renew_callList.JPG';
      });
    }
    ;
  }
}
