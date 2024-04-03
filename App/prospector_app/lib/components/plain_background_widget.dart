import 'package:flutter/material.dart';

String getImage(context) {
  if (Theme.of(context).brightness == Brightness.light) {
    return 'assets/images/lightmode_plain.png';
  } else {
    return 'assets/images/darkmode_plain.png';
  }
}
