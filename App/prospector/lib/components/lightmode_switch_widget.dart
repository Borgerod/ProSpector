import 'package:prospector/flutter_flow/flutter_flow_animations.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:flutter/material.dart';

class LightmodeSwitchWidget extends StatefulWidget {
  const LightmodeSwitchWidget({
    Key? key,
    this.color,
  }) : super(key: key);

  final Color? color;

  @override
  _LightmodeSwitchWidgetState createState() => _LightmodeSwitchWidgetState();
}

class _LightmodeSwitchWidgetState extends State<LightmodeSwitchWidget>
    with TickerProviderStateMixin {
  final animationsMap = {
    'containerOnActionTriggerAnimation1': AnimationInfo(
      trigger: AnimationTrigger.onActionTrigger,
      duration: 600,
      hideBeforeAnimating: false,
      initialState: AnimationState(
        offset: Offset(0, 0),
        scale: 1,
        opacity: 0,
      ),
      finalState: AnimationState(
        offset: Offset(20, 0),
        scale: 1,
        opacity: 1,
      ),
    ),
    'containerOnActionTriggerAnimation2': AnimationInfo(
      trigger: AnimationTrigger.onActionTrigger,
      duration: 600,
      hideBeforeAnimating: false,
      initialState: AnimationState(
        offset: Offset(0, 0),
        scale: 1,
        opacity: 0,
      ),
      finalState: AnimationState(
        offset: Offset(-20, 0),
        scale: 1,
        opacity: 1,
      ),
    ),
  };

  @override
  void initState() {
    super.initState();
    setupTriggerAnimations(
      animationsMap.values
          .where((anim) => anim.trigger == AnimationTrigger.onActionTrigger),
      this,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.max,
      mainAxisAlignment: MainAxisAlignment.start,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        InkWell(
          onTap: () async {
            setDarkModeSetting(context, ThemeMode.dark);
            if (animationsMap['containerOnActionTriggerAnimation2'] == null) {
              return;
            }
            await (animationsMap['containerOnActionTriggerAnimation2']!
                    .curvedAnimation
                    .parent as AnimationController)
                .forward(from: 0.0);
          },
          child: Material(
            color: Colors.transparent,
            elevation: 5,
            child: Container(
              width: MediaQuery.of(context).size.width,
              decoration: BoxDecoration(
                color: Colors.transparent,
                border: Border.all(
                  color: Color(0x0E000000),
                  width: 5,
                ),
              ),
              child: Padding(
                padding: EdgeInsetsDirectional.fromSTEB(24, 12, 12, 12),
                child: Row(
                  mainAxisSize: MainAxisSize.max,
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Column(
                      mainAxisSize: MainAxisSize.max,
                      children: [
                        if (Theme.of(context).brightness == Brightness.light)
                          Text(
                              FFLocalizations.of(context).getText(
                                'x3lg0hnj' /* Switch to Dark Mode */,
                              ),
                              style: FlutterFlowTheme.of(context).bodyText1),
                        if (Theme.of(context).brightness == Brightness.dark)
                          Text(
                              FFLocalizations.of(context).getText(
                                'k2h24c91' /* Switch to Light Mode */,
                              ),
                              style: FlutterFlowTheme.of(context).bodyText1),
                      ],
                    ),
                    Container(
                      decoration: BoxDecoration(
                        color: Color(0x00E2E2E5),
                      ),
                      child: Column(
                        mainAxisSize: MainAxisSize.max,
                        children: [
                          if (Theme.of(context).brightness == Brightness.dark)
                            InkWell(
                              onTap: () async {
                                if (animationsMap[
                                        'containerOnActionTriggerAnimation1'] ==
                                    null) {
                                  return;
                                }
                                await (animationsMap[
                                            'containerOnActionTriggerAnimation1']!
                                        .curvedAnimation
                                        .parent as AnimationController)
                                    .forward(from: 0.0);

                                setDarkModeSetting(context, ThemeMode.light);
                              },
                              child: Container(
                                width: 40,
                                height: 20,
                                decoration: BoxDecoration(
                                  color: FlutterFlowTheme.of(context)
                                      .secondaryBackground,
                                  borderRadius: BorderRadius.circular(20),
                                ),
                                child: Stack(
                                  children: [
                                    Row(
                                      mainAxisSize: MainAxisSize.max,
                                      mainAxisAlignment:
                                          MainAxisAlignment.spaceAround,
                                      crossAxisAlignment:
                                          CrossAxisAlignment.stretch,
                                      children: [
                                        Icon(
                                          Icons.nights_stay,
                                          color: FlutterFlowTheme.of(context)
                                              .primaryBtnText,
                                          size: 15,
                                        ),
                                        Icon(
                                          Icons.wb_sunny_rounded,
                                          color: FlutterFlowTheme.of(context)
                                              .primaryBtnText,
                                          size: 15,
                                        ),
                                      ],
                                    ),
                                    Row(
                                      mainAxisSize: MainAxisSize.max,
                                      mainAxisAlignment:
                                          MainAxisAlignment.start,
                                      children: [
                                        Material(
                                          color: Colors.transparent,
                                          elevation: 5,
                                          shape: RoundedRectangleBorder(
                                            borderRadius:
                                                BorderRadius.circular(20),
                                          ),
                                          child: Container(
                                            width: 20,
                                            height: 20,
                                            decoration: BoxDecoration(
                                              color:
                                                  FlutterFlowTheme.of(context)
                                                      .tertiaryColor,
                                              borderRadius:
                                                  BorderRadius.circular(20),
                                            ),
                                          ),
                                        ).animated([
                                          animationsMap[
                                              'containerOnActionTriggerAnimation1']!
                                        ]),
                                      ],
                                    ),
                                  ],
                                ),
                                // ),
                              ),
                            ),
                          if (Theme.of(context).brightness == Brightness.light)
                            InkWell(
                              onTap: () async {
                                if (animationsMap[
                                        'containerOnActionTriggerAnimation2'] ==
                                    null) {
                                  return;
                                }
                                await (animationsMap[
                                            'containerOnActionTriggerAnimation2']!
                                        .curvedAnimation
                                        .parent as AnimationController)
                                    .forward(from: 0.0);

                                setDarkModeSetting(context, ThemeMode.dark);
                              },
                              child: Container(
                                width: 40,
                                height: 20,
                                decoration: BoxDecoration(
                                  color:
                                      FlutterFlowTheme.of(context).handleColor,
                                  borderRadius: BorderRadius.circular(20),
                                ),
                                child: Stack(
                                  children: [
                                    Row(
                                      mainAxisSize: MainAxisSize.max,
                                      mainAxisAlignment:
                                          MainAxisAlignment.spaceAround,
                                      crossAxisAlignment:
                                          CrossAxisAlignment.stretch,
                                      children: [
                                        Icon(
                                          Icons.nights_stay_sharp,
                                          color: FlutterFlowTheme.of(context)
                                              .primaryBtnText,
                                          size: 14,
                                        ),
                                        Icon(
                                          Icons.wb_sunny_rounded,
                                          color: FlutterFlowTheme.of(context)
                                              .primaryBtnText,
                                          size: 14,
                                        ),
                                      ],
                                    ),
                                    Padding(
                                      padding: EdgeInsetsDirectional.fromSTEB(
                                          0, 0, 10, 0),
                                      child: Row(
                                        children: [
                                          Container(
                                            width: 20,
                                            height: 20,
                                            decoration: BoxDecoration(
                                              color: Color(0x00353E49),
                                            ),
                                          ),
                                          Container(
                                            width: 20,
                                            height: 20,
                                            decoration: BoxDecoration(
                                              color:
                                                  FlutterFlowTheme.of(context)
                                                      .primaryBtnText,
                                              borderRadius:
                                                  BorderRadius.circular(20),
                                              border: Border.all(
                                                color:
                                                    FlutterFlowTheme.of(context)
                                                        .boarderColor,
                                              ),
                                            ),
                                          ).animated([
                                            animationsMap[
                                                'containerOnActionTriggerAnimation2']!
                                          ]),
                                        ],
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          // ),
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
    );
  }
}
