import 'package:flet/flet.dart';
import "package:mylocalization/mylocalization.dart";

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    default:
      return myLocalization();
  }
};

void ensureInitialized() {
  // nothing to initialize
}
