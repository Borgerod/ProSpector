import 'package:prospector/components/plain_background_widget.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/components/home_button_widget.dart';
import 'package:flutter/material.dart';
import 'package:prospector/globals.dart' as globals;

class NotesWidget extends StatefulWidget {
  const NotesWidget({Key? key}) : super(key: key);

  @override
  _NotesWidgetState createState() => _NotesWidgetState();
}

class _NotesWidgetState extends State<NotesWidget> {
  TextEditingController textController = TextEditingController();
  final scaffoldKey = GlobalKey<ScaffoldState>();
  late String valueFromTextField;
  @override
  void initState() {
    super.initState();
    textController = TextEditingController();
    String note_text = globals.note_text;
    textController.text = "$note_text";
  }

  void textChange(TextEditingController textController) {
    this.textController = textController;
    globals.note_text = this.textController.text;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      backgroundColor: Color(0x00F9FDFF),
      floatingActionButton: HomeButton(),
      body: GestureDetector(
        onTap: () => FocusScope.of(context).unfocus(),
        child: Container(
          child: Expanded(
            child: Stack(
              children: [
                PlainBackgroundWidget(),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(10, 100, 10, 10),
                  child: Column(
                    children: [
                      Row(
                        mainAxisSize: MainAxisSize.max,
                        children: [
                          Padding(
                            padding:
                                EdgeInsetsDirectional.fromSTEB(20, 0, 0, 0),
                            child: Text(
                              FFLocalizations.of(context).getText(
                                '8mdtm5jj' /* Notes */,
                              ),
                              style:
                                  FlutterFlowTheme.of(context).title1.override(
                                        fontFamily: 'Poppins',
                                        fontSize: 30,
                                      ),
                            ),
                          ),
                        ],
                      ),
                      Expanded(
                        child: Padding(
                          padding:
                              EdgeInsetsDirectional.fromSTEB(20, 20, 20, 20),
                          child: Container(
                            color: FlutterFlowTheme.of(context).cardColor,
                            child: Container(
                              width: MediaQuery.of(context).size.width,
                              decoration: BoxDecoration(
                                // color: FlutterFlowTheme.of(context)
                                //     .secondaryBackground,
                                color: FlutterFlowTheme.of(context)
                                    .primaryBackground,
                                border: Border.all(
                                  color:
                                      FlutterFlowTheme.of(context).boarderColor,
                                  width: 5,
                                ),
                              ),
                              child: new ConstrainedBox(
                                constraints: BoxConstraints(),
                                child: new Scrollbar(
                                  child: new SingleChildScrollView(
                                    scrollDirection: Axis.vertical,
                                    reverse: true,
                                    child: Padding(
                                      padding:
                                          const EdgeInsetsDirectional.fromSTEB(
                                              10, 0, 10, 0),
                                      child: SizedBox(
                                        child: new TextField(
                                          onChanged: (value) =>
                                              textChange(textController),
                                          controller: textController,
                                          maxLines: 100,
                                          decoration: new InputDecoration(
                                            border: InputBorder.none,
                                          ),
                                        ),
                                      ),
                                    ),
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
              ],
            ),
          ),
        ),
      ),
    );
  }
}
