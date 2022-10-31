import 'package:flutter/material.dart';

import 'package:prospector_app/flutter_flow/flutter_flow_theme.dart';

class LoadingScreen extends StatelessWidget {
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
                'assets/images/loading_screen.png',
              ).image,
            ),
          ),
          child: Align(
            alignment: Alignment.bottomCenter,
            child: Padding(
              padding: EdgeInsetsDirectional.fromSTEB(50, 50, 50, 50),
              child: Container(),
            ),
          ),
        ),
      ),
    );
  }
}
