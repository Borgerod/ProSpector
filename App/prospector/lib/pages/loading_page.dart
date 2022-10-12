import 'package:flutter/material.dart';
import 'dart:async';

import 'package:prospector/flutter_flow/flutter_flow_theme.dart';

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
              child: Container(
                  // child: ProgressBarCall(),
                  ),
            ),
          ),
        ),
      ),
    );
  }
}

// class ProgressBarCall extends StatefulWidget {
//   const ProgressBarCall({Key? key}) : super(key: key);

//   @override
//   _ProgressBarCallState createState() => _ProgressBarCallState();
// }

// class _ProgressBarCallState extends State<ProgressBarCall> {
//   double _value = 0;
//   @override
//   Widget build(BuildContext context) {
//     // checkIndicator();
//     return LinearProgressIndicator(
//       backgroundColor: Colors.grey,
//       color: Color(0xFF5D8387),
//       minHeight: 5,
//       value: _value,
//     );
//   }

//   void setStateIfMounted(timer) {
//     if (!mounted)
//       setState(
//         () {
//           if (_value == 1) {
//             timer.cancel();
//           } else {
//             _value += 1;
//           }
//         },
//       );
//   }

  // void checkIndicator({delay = 5}) {
  //   new Timer.periodic(Duration(milliseconds: delay * 500), (Timer timer) {
  //     setState(() {
  //       if (_value == 1) {
  //         timer.cancel();
  //         setStateIfMounted(timer);
  //       } else {
  //         _value = _value + 0.1;
  //       }
  //     });
  //   });
  // }
// }
