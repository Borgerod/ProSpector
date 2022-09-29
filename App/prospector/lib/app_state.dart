// ignore_for_file: non_constant_identifier_names

import 'package:shared_preferences/shared_preferences.dart';

class FFAppState {
  static final FFAppState _instance = FFAppState._internal();

  factory FFAppState() {
    return _instance;
  }

  FFAppState._internal() {
    initializePersistedState();
  }

  Future initializePersistedState() async {
    prefs = await SharedPreferences.getInstance();
    _apiKey = prefs.getString('ff_apiKey') ?? _apiKey;
    _Language = prefs.getString('ff_Language') ?? _Language;
    _rememberME = prefs.getBool('ff_rememberME') ?? _rememberME;
    _userName = prefs.getString('ff_userName') ?? _userName;
    _LocalPasswordHash =
        prefs.getString('ff_LocalPasswordHash') ?? _LocalPasswordHash;
    _listeID = prefs.getInt('ff_listeID') ?? _listeID;
    _listeLimit = prefs.getInt('ff_listeLimit') ?? _listeLimit;
    _listeStart = prefs.getInt('ff_listeStart') ?? _listeStart;
    _erLedig = prefs.getBool('ff_erLedig') ?? _erLedig;
    _erFerdig = prefs.getBool('ff_erFerdig') ?? _erFerdig;
    _callStatusList =
        prefs.getStringList('ff_callStatusList') ?? _callStatusList;
    _completedListIDs =
        prefs.getStringList('ff_completedListIDs')?.map(int.parse).toList() ??
            _completedListIDs;
  }

  late SharedPreferences prefs;

  String _apiKey = '';
  String get apiKey => _apiKey;
  set apiKey(String _value) {
    _apiKey = _value;
    prefs.setString('ff_apiKey', _value);
  }

  String companyName = '';

  String contactReason = '';

  String jobPosition = '';

  String emailAdress = '';

  String _Language = '';
  String get Language => _Language;
  set Language(String _value) {
    _Language = _value;
    prefs.setString('ff_Language', _value);
  }

  bool _rememberME = false;
  bool get rememberME => _rememberME;
  set rememberME(bool _value) {
    _rememberME = _value;
    prefs.setBool('ff_rememberME', _value);
  }

  String password = '';

  String _userName = '';
  String get userName => _userName;
  set userName(String _value) {
    _userName = _value;
    prefs.setString('ff_userName', _value);
  }

  String _LocalPasswordHash = '';
  String get LocalPasswordHash => _LocalPasswordHash;
  set LocalPasswordHash(String _value) {
    _LocalPasswordHash = _value;
    prefs.setString('ff_LocalPasswordHash', _value);
  }

  bool darkMode = false;

  int userID = 0;

  int _listeID = 0;
  int get listeID => _listeID;
  set listeID(int _value) {
    _listeID = _value;
    prefs.setInt('ff_listeID', _value);
  }

  int _listeLimit = 0;
  int get listeLimit => _listeLimit;
  set listeLimit(int _value) {
    _listeLimit = _value;
    prefs.setInt('ff_listeLimit', _value);
  }

  int _listeStart = 0;
  int get listeStart => _listeStart;
  set listeStart(int _value) {
    _listeStart = _value;
    prefs.setInt('ff_listeStart', _value);
  }

  bool _erLedig = false;
  bool get erLedig => _erLedig;
  set erLedig(bool _value) {
    _erLedig = _value;
    prefs.setBool('ff_erLedig', _value);
  }

  bool _erFerdig = false;
  bool get erFerdig => _erFerdig;
  set erFerdig(bool _value) {
    _erFerdig = _value;
    prefs.setBool('ff_erFerdig', _value);
  }

  List<String> _callStatusList = [];
  List<String> get callStatusList => _callStatusList;
  set callStatusList(List<String> _value) {
    _callStatusList = _value;
    prefs.setStringList('ff_callStatusList', _value);
  }

  void addToCallStatusList(String _value) {
    _callStatusList.add(_value);
    prefs.setStringList('ff_callStatusList', _callStatusList);
  }

  void removeFromCallStatusList(String _value) {
    _callStatusList.remove(_value);
    prefs.setStringList('ff_callStatusList', _callStatusList);
  }

  List<int> _completedListIDs = [];
  List<int> get completedListIDs => _completedListIDs;
  set completedListIDs(List<int> _value) {
    _completedListIDs = _value;
    prefs.setStringList(
        'ff_completedListIDs', _value.map((x) => x.toString()).toList());
  }

  void addToCompletedListIDs(int _value) {
    _completedListIDs.add(_value);
    prefs.setStringList('ff_completedListIDs',
        _completedListIDs.map((x) => x.toString()).toList());
  }

  void removeFromCompletedListIDs(int _value) {
    _completedListIDs.remove(_value);
    prefs.setStringList('ff_completedListIDs',
        _completedListIDs.map((x) => x.toString()).toList());
  }
}
