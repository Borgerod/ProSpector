// import 'package:prospector/../flutter_flow/flutter_flow_util.dart';

import 'dart:convert';

import 'api_manager.dart';

export 'api_manager.dart' show ApiCallResponse;
import 'package:prospector/globals.dart' as globals;

class LoginCallCall {
  static Future<ApiCallResponse> call({
    String? emailAddress = '',
    String? password = '',
  }) {
    Map data = {
      // 'emailAddress': emailAddress,
      'username': emailAddress,
      'password': password,
    };
    var body = json.encode(data);
    return ApiManager.instance.makeApiCall(
      callName: 'LoginCall',
      apiUrl: 'http://127.0.0.1:8000/login/token',
      callType: ApiCallType.POST,
      headers: {
        'accept': 'application/json, Content-Type: multipart/form-data',
      },
      body: body,
      returnBody: true,
    );
  }
}

class GetCurrentCallListCall {
  static Future<ApiCallResponse> call() {
    return ApiManager.instance.makeApiCall(
      callName: 'GetCurrentCallList',
      apiUrl: 'http://127.0.0.1:8000/currentcallList',
      callType: ApiCallType.GET,
      headers: {
        'accept': 'application/json',
        'Authorization': globals.accsess_token,
      },
      params: {},
      returnBody: true,
    );
  }
}
