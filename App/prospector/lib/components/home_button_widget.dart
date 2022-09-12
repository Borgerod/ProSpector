import 'package:flutter/material.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';

class HomeButton extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return FloatingActionButton(
      onPressed: () {
        print('FloatingHomeButton pressed ...');
      },
      mini: true,
      backgroundColor: FlutterFlowTheme.of(context).primaryColor,
      elevation: 8,
      child: InkWell(
        onTap: () async {
          Navigator.pop(context);
          // TODO write if statement:
          // if current page == homepage, then do nothing
        },
        child: Icon(
          Icons.home,
          color: FlutterFlowTheme.of(context).primaryBtnText,
          size: 24,
        ),
      ),
    );
  }
}
