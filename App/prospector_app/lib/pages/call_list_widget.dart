// ignore_for_file: use_function_type_syntax_for_parameters

import 'package:flutter/material.dart';
import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';
import 'package:syncfusion_flutter_datagrid/datagrid.dart';
import 'package:http/http.dart' as http;

import 'package:prospector_app/components/plain_background_widget.dart';
import 'package:prospector_app/components/home_button_widget.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector_app/flutter_flow/flutter_flow_util.dart';
import 'package:prospector_app/globals.dart' as globals;
import 'package:url_launcher/url_launcher.dart';

class CallListWidget extends StatefulWidget {
  const CallListWidget({Key? key}) : super(key: key);

  @override
  _CallListWidgetState createState() => _CallListWidgetState();
}

// todo [ ] replace message string with: FFLocalizations.of(context).getText('nhdfcp17' /* something */,),

//* ______ TABLE CONTAINER _____________________________________________________

class _CallListWidgetState extends State<CallListWidget> {
  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
          padding: const EdgeInsetsDirectional.fromSTEB(30, 100, 30, 30),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Padding(
                padding: const EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                child: Row(
                  children: [
                    Padding(
                      padding:
                          const EdgeInsetsDirectional.fromSTEB(10, 0, 0, 10),
                      child: Text(
                        FFLocalizations.of(context).getText(
                          'nhdfcp17' /* Call List */,
                        ),
                        style: FlutterFlowTheme.of(context).title1.override(
                              fontFamily: 'Poppins',
                              fontSize: 30,
                            ),
                      ),
                    ),
                  ],
                ),
              ),
              Expanded(
                child: Padding(
                  padding: const EdgeInsetsDirectional.fromSTEB(10, 0, 10, 0),
                  child: Container(
                      color: FlutterFlowTheme.of(context).cardColor,
                      child: JsonDataGrid()),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
//* ____________________________________________________________________________

class JsonDataGrid extends StatefulWidget {
  @override
  _JsonDataGridState createState() => _JsonDataGridState();
}

class _JsonDataGridState extends State<JsonDataGrid> {
  late _JsonDataGridSource jsonDataGridSource;
  List<_Product> productlist = [];
  String accsess_token = globals.accsess_token;
  Future generateProductList() async {
    Uri url = Uri.parse('http://127.0.0.1:8000/currentcallList');
    var response = await http
        .get(url, headers: {'Cookie': 'access_token=Bearer $accsess_token'});

    var list = json
        .decode(utf8.decode(response.bodyBytes))
        .cast<Map<String, dynamic>>();
    productlist =
        await list.map<_Product>((json) => _Product.fromJson(json)).toList();

    jsonDataGridSource = _JsonDataGridSource(productlist);

    return productlist;
  }

//* ______ COLUMN NAMES ________________________________________________________
  List<GridColumn> getColumns() {
    List<GridColumn> columns;
    columns = ([
      GridColumn(
          width: 120,
          columnName: 'Org Num.',
          label: Container(
              padding: const EdgeInsets.symmetric(horizontal: 10.0),
              alignment: Alignment.center,
              child: Tooltip(
                message: 'virksomhetens organisasjons nummer',
                child: Text(
                  'Org Num.',
                  style: Theme.of(context).textTheme.bodyText1,
                ),
              ))),
      GridColumn(
          columnName: 'name',
          label: Container(
              padding: const EdgeInsets.symmetric(horizontal: 10.0),
              alignment: Alignment.center,
              child: Tooltip(
                  message: 'Virksomhetens juridiske name',
                  child: Align(
                    alignment: Alignment.centerLeft,
                    child: Text(
                      'name',
                      style: Theme.of(context).textTheme.bodyText1,
                    ),
                  )))),
      GridColumn(
          columnName: 'Google Profil',
          width: 120,
          label: Container(
              padding: const EdgeInsets.symmetric(horizontal: 10.0),
              alignment: Alignment.center,
              child: Tooltip(
                  message:
                      'Viser om virksomheten har en googleprofil eller ikke; True: den har en profil, False: den har IKKE en profil, Usikkert: det dukker opp en profil når virksomheten søkes, men programmet er usikker på om den hører til virksomheten som undersøkes eller en annen, konsulenten oppfordres til å bekrefte/avkrefte dette selv',
                  child: Text('Google Profil',
                      style: Theme.of(context).textTheme.bodyText1)))),
      GridColumn(
          width: 120,
          columnName: 'Eier Bekreftet',
          label: Container(
              padding: const EdgeInsets.symmetric(horizontal: 10.0),
              alignment: Alignment.center,
              child: Tooltip(
                  message:
                      'Viser om virksomheten står som eier av google profilen; True: Bekreftet, False: Ikke bekreftet',
                  child: Text(
                    'Eier Bekreftet',
                    style: Theme.of(context).textTheme.bodyText1,
                  )))),
      GridColumn(
          width: 120,
          columnName: 'Komplett Profil',
          label: Container(
              padding: const EdgeInsets.symmetric(horizontal: 10.0),
              alignment: Alignment.center,
              child: Tooltip(
                  message:
                      'Viser om profilen er fullstendig eller om den har mangler; True: profilen er komplett og har INGEN mangler, False: profilen er ufullstendig og HAR mangler.',
                  child: Text(
                    'Komplett Profil',
                    style: Theme.of(context).textTheme.bodyText1,
                  )))),

      GridColumn(
          width: 120,
          columnName: 'Ringestatus',
          label: Container(
            padding: const EdgeInsets.symmetric(horizontal: 10.0),
            alignment: Alignment.center,
            child: Tooltip(
                message: FFLocalizations.of(context).getText(
                  'nydqnbi1' /* Ringestatus description */,
                ),
                child: Text(
                  FFLocalizations.of(context).getText(
                    'nydqnbi2' /* Ringestatus title */,
                  ),
                  // 'Ringestatus',
                  style: Theme.of(context).textTheme.bodyText1,
                )),
          )),
      //> _____ NEW: URL BUTTON ____________________________________________

      GridColumn(
          width: 120,
          columnName: 'Profile Link',
          label: Container(
            padding: const EdgeInsets.symmetric(horizontal: 10.0),
            alignment: Alignment.center,
            child: Tooltip(
                message: FFLocalizations.of(context).getText(
                  'nydqnbi3' /* Profile Link description */,
                ),

                // 'En sjekkliste på om virksomheten har blitt ringt eller ikke, NB: Du kan ikke oppdatere listen før alle virksomhetene har blitt ringt.',
                child: Text(
                  FFLocalizations.of(context).getText(
                    'nydqnbi4' /* Profile Link title */,
                  ),
                  style: Theme.of(context).textTheme.bodyText1,
                )),
          )),
      //> __________________________________________________________________
    ]);
    return columns;
  }
//* ____________________________________________________________________________

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: generateProductList(),
      builder: (BuildContext context, AsyncSnapshot<dynamic> snapshot) {
        return snapshot.hasData
            ? SfDataGrid(
                isScrollbarAlwaysShown: true,
                columnWidthMode: ColumnWidthMode.fill,
                allowEditing: true,
                source: jsonDataGridSource,
                columns: getColumns())
            : const Center(
                child: CircularProgressIndicator(
                  strokeWidth: 3,
                ),
              );
      },
    );
  }
}

//* ______ ROW DATA FACTORY ____________________________________________________
class _Product {
  factory _Product.fromJson(Map<String, dynamic> json) {
    return _Product(
      orgNum: json['org_num'],
      name: json['name'],
      googleProfil: json['google_profil'],
      eierBekreftet: json['eier_bekreftet'],
      komplettProfil: json['komplett_profil'],
      ringeStatus: json['ringe_status'],
      liste_id: json['liste_id'],
      link_til_profil: json['link_til_profil'], //> NEW
    );
  }
  _Product({
    this.orgNum,
    this.name,
    this.googleProfil,
    this.eierBekreftet,
    this.komplettProfil,
    this.ringeStatus,
    this.liste_id,
    this.link_til_profil, //> NEW
  });

  int? orgNum;
  String? name;
  String? googleProfil;
  bool? eierBekreftet;
  bool? komplettProfil;
  bool? ringeStatus;
  // int? liste_id;
  double? liste_id;
  String? link_til_profil; //> NEW
}
//* ____________________________________________________________________________

//* ______ ROW DATA  ___________________________________________________________

class _JsonDataGridSource extends DataGridSource {
  // BuildContext context;
  // late BuildContext context;
  // = context;
  // var context;

  _JsonDataGridSource(this.productlist) {
    buildDataGridRow();
  }

  List<DataGridRow> dataGridRows = [];
  List<_Product> productlist = [];

  void buildDataGridRow() {
    dataGridRows = productlist.map<DataGridRow>(
      (dataGridRow) {
        return DataGridRow(
          cells: [
            DataGridCell<int>(
                columnName: 'Org Num.', value: dataGridRow.orgNum),
            DataGridCell<String>(columnName: 'name', value: dataGridRow.name),
            DataGridCell<String>(
                columnName: 'Google Profil', value: dataGridRow.googleProfil),
            DataGridCell<bool>(
                columnName: 'Eier Bekreftet', value: dataGridRow.eierBekreftet),
            DataGridCell<bool>(
                columnName: 'Komplett Profil',
                value: dataGridRow.komplettProfil),

            DataGridCell(
                columnName: 'Ringestatus', value: dataGridRow.ringeStatus),
            DataGridCell(
                columnName: 'Profile Link', //> NEW
                // value: dataGridRow.link_til_profil), //> NEW
                value: dataGridRow.link_til_profil), // TEMP
          ],
        );
      },
    ).toList(growable: false);
  }

  @override
  List<DataGridRow> get rows => dataGridRows;

  @override
  DataGridRowAdapter buildRow(DataGridRow row) {
    return DataGridRowAdapter(
      cells: [
        Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[0].value.toString()),
        ),
        Container(
          alignment: Alignment.centerLeft,
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[1].value),
        ),
        Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[2].value.toString()),
        ),
        Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[3].value.toString()),
        ),
        Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[4].value.toString()),
        ),

        Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: Checkbox(
            activeColor: const Color.fromRGBO(30, 167, 169, 1),
            // activeColor: Color(0xFF48B892),
            value: row.getCells()[5].value,
            onChanged: (value) {
              http.put(Uri.parse(
                  "http://127.0.0.1:8000/callList/ringe_status?org_num=${row.getCells()[0].value}"));
              final index = dataGridRows.indexOf(row);
              productlist[index].ringeStatus = value!;
              row.getCells()[5] =
                  DataGridCell(value: value, columnName: 'Ringestatus');
              notifyDataSourceListeners(
                  rowColumnIndex: RowColumnIndex(index, 5));
            },
          ),
        ),
        //> _____ NEW: URL BUTTON CONTAINER ____________________________________
        Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: OutlinedButton(
            onPressed: () async {
              // String url = row.getCells()[0].value; //> might use this
              // Opens url to the company's google profile, url will vary.
              String link_til_profil = row.getCells()[6].value;
              // "https://www.google.com/search?q=mediavest+AS+maps&ei=gOZgY-mZCoqHxc8Poaij4AY&ved=0ahUKEwjp2aSp1Yz7AhWKQ_EDHSHUCGwQ4dUDCA8&uact=5&oq=mediavest+AS+maps&gs_lp=Egxnd3Mtd2l6LXNlcnC4AQP4AQFIlglQ_ANY4gdwAXgAyAEAkAEAmAGBAaABxQKqAQMyLjHiAwQgQRgB4gMEIEYYAIgGAQ&sclient=gws-wiz-serp";
              // row.getCells()[6].value.toString();

              http.put(Uri.parse(link_til_profil));

              if (!await launchUrl(Uri.parse(link_til_profil))) {
                if (link_til_profil.isEmpty) {
                  // noUrlErrorMessage(context);
                  throw 'Error: ${row.getCells()[1].value} has no Url assinged to it.';
                }
                // couldNotLaunchErrorMessage(context);
                throw 'Error: Could not launch $link_til_profil'; //todo replace with getText
              }
            },
            child: Text(
              "Link",
              // style: TextStyle(color: Color.fromRGBO(30, 167, 169, 1)),
            ),
          ),
        ),

        //> __________________________________________________________________
      ],
    );
  }
//* ____________________________________________________________________________

//> NEW:  ERROR MESSAGES
  // void noUrlErrorMessage(context) {
  //   showDialog(
  //       context: context,
  //       builder: (BuildContext context) {
  //         return AlertDialog(
  //           backgroundColor: Color(0x00353E49),
  //           title: Text(
  //             FFLocalizations.of(context).getText(
  //               'ib1c3p2a' /* No url  */,
  //             ),
  // style: FlutterFlowTheme.of(context).bodyText1.override(
  //       fontFamily: FlutterFlowTheme.of(context).bodyText1Family,
  //       color: Colors.white,
  //     ),
  //           ),
  //         );
  //       },
  //   );
  // }
  // void couldNotLaunchErrorMessage(context) {
  //   showDialog(
  //       context: context,
  //       builder: (BuildContext context) {
  //         return AlertDialog(
  //           backgroundColor: Color(0x00353E49),
  //           title: "Error!",
  //           : Text(
  //             FFLocalizations.of(context).getText(
  //               'ib1c3p22' /* Could not Launch  */,
  //             ),
  //             style: FlutterFlowTheme.of(context).bodyText1.override(
  //                   fontFamily: FlutterFlowTheme.of(context).bodyText1Family,
  //                   color: Colors.white,
  //                 ),
  //           ),
  //         );
  //       },
  //   );
  // }
}

class SwitchWidget extends StatefulWidget {
  const SwitchWidget({super.key});

  @override
  SwitchWidgetState createState() => SwitchWidgetState();
}

class SwitchWidgetState extends State<SwitchWidget> {
  bool switchControl = false;

  Future<bool> saveSwitchState(bool value) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setBool("switchState", value);
    return prefs.setBool("switchState", value);
  }

  Future<bool> getSwitchState() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    bool isSwitchedFT = prefs.getBool("switchState") ?? false;
    return isSwitchedFT;
  }

  Future<void> toggleSwitch(bool value) async {
    if (switchControl == false) {
      setState(() {
        saveSwitchState(value);
        switchControl = true;
      });
    } else {
      setState(() {
        saveSwitchState(value);
        switchControl = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Switch(
      onChanged: toggleSwitch,
      value: switchControl,
      activeColor: FlutterFlowTheme.of(context).primaryColor,
      // activeColor: Colors.greenAccent,
      activeTrackColor: Colors.grey[400],
      inactiveThumbColor: Colors.grey[200],
      inactiveTrackColor: Colors.grey,
    );
  }
}
