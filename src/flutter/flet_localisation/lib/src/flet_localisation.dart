import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:mylocalization/mylocalization.dart';

class FletLocalisationControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const FletLocalisationControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    String text =
        control.attrString("value", MyLocalization().getDeviceLocale()) ?? "";

    return Text(text); // only string as widget
  }
}
