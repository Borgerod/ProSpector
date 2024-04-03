import 'package:flutter/material.dart';

import 'package:prospector_app/components/plain_background_widget.dart';
import 'package:prospector_app/components/home_button_widget.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_util.dart';
import 'package:prospector_app/globals.dart' as globals;

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
    String noteText = globals.note_text;
    textController.text = "$noteText";
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
          padding: EdgeInsetsDirectional.fromSTEB(10, 100, 10, 10),
          child: Column(
            children: [
              Row(
                mainAxisSize: MainAxisSize.max,
                children: [
                  Padding(
                    padding: EdgeInsetsDirectional.fromSTEB(20, 0, 0, 0),
                    child: Text(
                      FFLocalizations.of(context).getText(
                        '8mdtm5jj' /* Notes */,
                      ),
                      style: FlutterFlowTheme.of(context).title1.override(
                            fontFamily: 'Poppins',
                            fontSize: 30,
                          ),
                    ),
                  ),
                ],
              ),
              Expanded(
                child: Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(20, 20, 20, 20),
                  child: Container(
                    color: FlutterFlowTheme.of(context).cardColor,
                    child: Container(
                      width: MediaQuery.of(context).size.width,
                      decoration: BoxDecoration(
                        color: FlutterFlowTheme.of(context).primaryBackground,
                        border: Border.all(
                          color: FlutterFlowTheme.of(context).boarderColor,
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
                              padding: const EdgeInsetsDirectional.fromSTEB(
                                  10, 0, 10, 0),
                              child: SizedBox(
                                child: new TextField(
                                  cursorColor:
                                      FlutterFlowTheme.of(context).primaryColor,
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
      ),
    );
  }
}
