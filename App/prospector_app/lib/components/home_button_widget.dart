import 'package:prospector_app/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_util.dart';
import 'package:prospector_app/pages/home_page.dart';
import 'package:flutter/material.dart';

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
          Navigator.of(context).pushReplacement(
            PageTransition(
                type: PageTransitionType.fade,
                duration: Duration(milliseconds: 0),
                reverseDuration: Duration(milliseconds: 0),
                child: HomeView()),
          );
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
