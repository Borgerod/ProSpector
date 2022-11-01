import 'package:flutter/material.dart';
import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';
import 'package:syncfusion_flutter_datagrid/datagrid.dart';
import 'package:http/http.dart' as http;

import 'package:prospector/components/plain_background_widget.dart';
import 'package:prospector/components/home_button_widget.dart';
import 'package:prospector/flutter_flow/flutter_flow_theme.dart';
import 'package:prospector/flutter_flow/flutter_flow_util.dart';
import 'package:prospector/globals.dart' as globals;

class CallListWidget extends StatefulWidget {
  const CallListWidget({Key? key}) : super(key: key);

  @override
  _CallListWidgetState createState() => _CallListWidgetState();
}

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
          padding: EdgeInsetsDirectional.fromSTEB(30, 100, 30, 30),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                child: Row(
                  children: [
                    Padding(
                      padding: EdgeInsetsDirectional.fromSTEB(10, 0, 0, 10),
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
                  padding: EdgeInsetsDirectional.fromSTEB(10, 0, 10, 0),
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

class JsonDataGrid extends StatefulWidget {
  @override
  _JsonDataGridState createState() => _JsonDataGridState();
}

class _JsonDataGridState extends State<JsonDataGrid> {
  late _JsonDataGridSource jsonDataGridSource;
  List<_Product> productlist = [];
  String accsess_token = globals.accsess_token;
  Future generateProductList() async {
    Uri _url = Uri.parse('http://127.0.0.1:8000/currentcallList');
    var response = await http
        .get(_url, headers: {'Cookie': 'access_token=Bearer $accsess_token'});
    var list = json
        .decode(utf8.decode(response.bodyBytes))
        .cast<Map<String, dynamic>>();
    productlist =
        await list.map<_Product>((json) => _Product.fromJson(json)).toList();
    jsonDataGridSource = _JsonDataGridSource(productlist);
    return productlist;
  }

  List<GridColumn> getColumns() {
    List<GridColumn> columns;
    columns = ([
      GridColumn(
          width: 120,
          columnName: 'Org Num.',
          label: Container(
              padding: EdgeInsets.symmetric(horizontal: 10.0),
              alignment: Alignment.center,
              child: Tooltip(
                message: 'virksomhetens organisasjons nummer',
                child: Text(
                  'Org Num.',
                  style: Theme.of(context).textTheme.bodyText1,
                ),
              ))),
      GridColumn(
          columnName: 'Navn',
          label: Container(
              padding: EdgeInsets.symmetric(horizontal: 10.0),
              alignment: Alignment.center,
              child: Tooltip(
                  message: 'Virksomhetens juridiske navn',
                  child: Align(
                    alignment: Alignment.centerLeft,
                    child: Text(
                      'Navn',
                      style: Theme.of(context).textTheme.bodyText1,
                    ),
                  )))),
      GridColumn(
          columnName: 'Google Profil',
          width: 120,
          label: Container(
              padding: EdgeInsets.symmetric(horizontal: 10.0),
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
              padding: EdgeInsets.symmetric(horizontal: 10.0),
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
              padding: EdgeInsets.symmetric(horizontal: 10.0),
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
            padding: EdgeInsets.symmetric(horizontal: 10.0),
            alignment: Alignment.center,
            child: Tooltip(
                message:
                    'En sjekkliste på om virksomheten har blitt ringt eller ikke, NB: Du kan ikke oppdatere listen før alle virksomhetene har blitt ringt.',
                child: Text(
                  'Ringestatus',
                  style: Theme.of(context).textTheme.bodyText1,
                )),
          )),
    ]);
    return columns;
  }

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

class _Product {
  factory _Product.fromJson(Map<String, dynamic> json) {
    return _Product(
        orgNum: json['org_num'],
        navn: json['navn'],
        googleProfil: json['google_profil'],
        eierBekreftet: json['eier_bekreftet'],
        komplettProfil: json['komplett_profil'],
        ringeStatus: json['ringe_status'],
        liste_id: json['liste_id']);
  }
  _Product({
    this.orgNum,
    this.navn,
    this.googleProfil,
    this.eierBekreftet,
    this.komplettProfil,
    this.ringeStatus,
    this.liste_id,
  });

  int? orgNum;
  String? navn;
  String? googleProfil;
  bool? eierBekreftet;
  bool? komplettProfil;
  bool? ringeStatus;
  int? liste_id;
}

class _JsonDataGridSource extends DataGridSource {
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
            DataGridCell<String>(columnName: 'Navn', value: dataGridRow.navn),
            DataGridCell<String>(
                columnName: 'Google Profil', value: dataGridRow.googleProfil),
            DataGridCell<bool>(
                columnName: 'Eier Bekreftet', value: dataGridRow.eierBekreftet),
            DataGridCell<bool>(
                columnName: 'Komplett Profil',
                value: dataGridRow.komplettProfil),
            DataGridCell(
                columnName: 'Ringestatus', value: dataGridRow.ringeStatus),
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
          padding: EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[0].value.toString()),
        ),
        Container(
          alignment: Alignment.centerLeft,
          padding: EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[1].value),
        ),
        Container(
          alignment: Alignment.center,
          padding: EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[2].value.toString()),
        ),
        Container(
          alignment: Alignment.center,
          padding: EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[3].value.toString()),
        ),
        Container(
          alignment: Alignment.center,
          padding: EdgeInsets.symmetric(horizontal: 10),
          child: Text(row.getCells()[4].value.toString()),
        ),
        Container(
          alignment: Alignment.center,
          padding: EdgeInsets.symmetric(horizontal: 10),
          child: Checkbox(
            activeColor: Color.fromRGBO(30, 167, 169, 1),
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
        )
      ],
    );
  }
}

class SwitchWidget extends StatefulWidget {
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
