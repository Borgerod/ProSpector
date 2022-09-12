// import 'package:firebase_auth/firebase_auth.dart';
// import 'package:flutter/material.dart';
// export 'email_auth.dart';

// String? _currentJwtToken = '';
// String get currentJwtToken => _currentJwtToken ?? '';

// /// Tries to sign in or create an account using Firebase Auth.
// /// Returns the User object if sign in was successful.
// Future<User?> signInOrCreateAccount(
//     BuildContext context, Future<UserCredential?> Function() signInFunc) async {
//   try {
//     final userCredential = await signInFunc();
//     return userCredential?.user;
//   } on FirebaseAuthException catch (e) {
//     ScaffoldMessenger.of(context).hideCurrentSnackBar();
//     ScaffoldMessenger.of(context).showSnackBar(
//       SnackBar(content: Text('Error: ${e.message!}')),
//     );
//     return null;
//   }
// }

// Future signOut() {
//   _currentJwtToken = '';
//   return FirebaseAuth.instance.signOut();
// }

// Future resetPassword(
//     {required String email, required BuildContext context}) async {
//   try {
//     await FirebaseAuth.instance.sendPasswordResetEmail(email: email);
//   } on FirebaseAuthException catch (e) {
//     ScaffoldMessenger.of(context).hideCurrentSnackBar();
//     ScaffoldMessenger.of(context).showSnackBar(
//       SnackBar(content: Text('Error: ${e.message!}')),
//     );
//     return null;
//   }
//   ScaffoldMessenger.of(context).showSnackBar(
//     SnackBar(content: Text('Password reset email sent')),
//   );
// }



// //// * Kan være nyttig i fremtiden 

// // import 'package:prospector/flutter_flow/flutter_flow_util.dart';
// // import 'package:flutter/foundation.dart' show kIsWeb;

// // String get currentUserEmail => currentUser?.user?.email ?? '';
// // String get currentUserUid => currentUser?.user?.uid ?? '';
// // String get currentUserDisplayName => currentUser?.user?.displayName ?? '';
// // String get currentUserPhoto => currentUser?.user?.photoURL ?? '';
// // String get currentPhoneNumber => currentUser?.user?.phoneNumber ?? '';
// // bool get currentUserEmailVerified => currentUser?.user?.emailVerified ?? false;


// // Future deleteUser(BuildContext context) async {
// //   try {
// //     if (currentUser?.user == null) {
// //       print('Error: delete user attempted with no logged in user!');
// //       return;
// //     }
// //     await currentUser?.user?.delete();
// //   } on FirebaseAuthException catch (e) {
// //     if (e.code == 'requires-recent-login') {
// //       ScaffoldMessenger.of(context).hideCurrentSnackBar();
// //       ScaffoldMessenger.of(context).showSnackBar(
// //         SnackBar(
// //             content: Text(
// //                 'Too long since most recent sign in. Sign in again before deleting your account.')),
// //       );
// //     }
// //   }
// // }


// // Future sendEmailVerification() async =>
// //     currentUser?.user?.sendEmailVerification();
