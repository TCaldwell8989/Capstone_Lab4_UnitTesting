import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloTyler', camelcase.camel_case('Hello Tyler'))
        self.assertEqual('helloTyler', camelcase.camel_case('   Hello   Tyler   '))
        self.assertEqual('123456789', camelcase.camel_case('1 2 3 4 5 6 7 8 9'))
        self.assertEqual('!@#$$', camelcase.camel_case('!@# $ $'))
        self.assertEqual('tyler', camelcase.camel_case('    TYLER'))

    def test_camelcase_for_input(self):

        with self.assertRaises(ValueError):
            camelcase.camel_case('')