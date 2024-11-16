import 'package:flet/flet.dart';
import 'package:flutter/widgets.dart';
import 'package:mylocalization/mylocalization.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    default:
      var mylocale = Text(MyLocalization().toString());
      return mylocale;
  }
};
var mylocale = Text(MyLocalization().toString());
void ensureInitialized() {
  // nothing to initialize
}
