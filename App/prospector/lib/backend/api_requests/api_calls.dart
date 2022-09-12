// import 'package:prospector/../flutter_flow/flutter_flow_util.dart';

import 'api_manager.dart';

export 'api_manager.dart' show ApiCallResponse;

class LoginCallCall {
  static Future<ApiCallResponse> call({
    String? emailAddress = '',
    String? password = '',
  }) {
    return ApiManager.instance.makeApiCall(
      callName: 'LoginCall',
      apiUrl: 'http://127.0.0.1:8000/login/token',
      callType: ApiCallType.GET,
      headers: {
        'accept': 'application/json, Content-Type: multipart/form-data',
      },
      params: {
        'emailAddress': emailAddress,
        'password': password,
      },
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
      },
      params: {},
      returnBody: true,
    );
  }
}
