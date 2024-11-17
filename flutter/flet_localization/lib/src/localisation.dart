import 'dart:async';
import 'dart:convert';
import 'package:mylocalization/mylocalization.dart';
import 'package:flet/flet.dart';
import 'package:collection/collection.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';

class FletLocalization extends StatefulWidget {
  final Control? parent;
  final Control control;
  final Widget? nextChild;
  final FletControlBackend backend;

  const FletLocalization(
      {super.key,
      required this.parent,
      required this.control,
      required this.backend,
      required this.nextChild});
  @override
  State<FletLocalization> createState() => _FletLocalization();
}

class _FletLocalization extends State<FletLocalization> with FletStoreMixin {
  MyLocalization? locale;
}
