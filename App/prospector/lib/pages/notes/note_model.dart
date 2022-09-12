import 'package:flutter/cupertino.dart';
import 'package:flutter_quill/flutter_quill.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';

// ignore: must_be_immutable
class Notepad extends StatelessWidget {
  QuillController _controller = QuillController.basic();
  @override
  Widget build(BuildContext context) {
    return Container(
      color: FlutterFlowTheme.of(context).cardColor,
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: QuillEditor.basic(
          controller: _controller,
          readOnly: false, // true for view only mode
        ),
      ),
    );
  }
}
