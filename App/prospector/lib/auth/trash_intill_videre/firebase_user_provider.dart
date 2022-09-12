// import 'package:firebase_auth/firebase_auth.dart';
// import 'package:rxdart/rxdart.dart';

// class ProspectorFirebaseUser {
//   ProspectorFirebaseUser(this.user);
//   User? user;
//   bool get loggedIn => user != null;
// }

// ProspectorFirebaseUser? currentUser;
// bool get loggedIn => currentUser?.loggedIn ?? false;
// Stream<ProspectorFirebaseUser> prospectorFirebaseUserStream() =>
//     FirebaseAuth.instance
//         .authStateChanges()
//         .debounce((user) => user == null && !loggedIn
//             ? TimerStream(true, const Duration(seconds: 1))
//             : Stream.value(user))
//         .map<ProspectorFirebaseUser>(
//             (user) => currentUser = ProspectorFirebaseUser(user));
