import 'package:flutter_test/flutter_test.dart';
import 'package:flet_localization/flet_localization.dart';
import 'package:mylocalization/mylocalization.dart';
import 'package:flet_localization/src/create_control.dart';

void main() {
  test('adds one to input values', () {
    final locale = mylocale;
    expect(locale, mylocale);
    print(locale);
  });
}
