
#!/usr/bin/python3
"""
Unittest for Square class
"""

import unittest
import contextlib
from io import StringIO
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_classBase(self):
        s0 = Square(1)
        self.assertIsInstance(s0, Base)
        self.assertIsInstance(s0, Rectangle)
        self.assertIsInstance(s0, Square)

    def test_nb(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, '_Base__nb_objects'))
        Base._Base__nb_objects = 0

    def test_Square_arg(self):
        self.assertRaises(TypeError, Square)
        """
        self.assertRaisesRegex(TypeError,
                              "__init__() missing 2 required positional
                              arguments: 'width' and 'height'",
                             Square)
        """
        self.assertRaises(TypeError, Square, 1, 1, 1, 1, 1, 1)
        """
        self.assertRaisesRegex(TypeError,
                              "__init__() takes from 2 to 5 positional
                              arguments but 7 were given",
                             Square, 1, 1, 1, 1, 1)
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'id'))
        Base._Base__nb_objects = 0

    def test_size(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'size'))
        Base._Base__nb_objects = 0

    def test_size_value(self):
        s0 = Square(1)
        self.assertEqual(s0.size, 1)
        Base._Base__nb_objects = 0

    def test_size_string(self):
        self.assertRaises(TypeError, Square, "string")
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, "string")
        Base._Base__nb_objects = 0

    def test_size_neg(self):
        self.assertRaises(ValueError, Square, -1)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, -1)
        Base._Base__nb_objects = 0

    def test_height(self):
        s0 = Square(1, 1)
        self.assertTrue(hasattr(s0, 'height'))
        Base._Base__nb_objects = 0

    def test_height_value(self):
        s0 = Square(1)
        self.assertEqual(s0.height, 1)
        Base._Base__nb_objects = 0

    def test_width(self):
        s0 = Square(1, 1)
        self.assertTrue(hasattr(s0, 'width'))
        Base._Base__nb_objects = 0

    def test_width_value(self):
        s0 = Square(1)
        self.assertEqual(s0.width, 1)
        Base._Base__nb_objects = 0

    def test_x(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'x'))
        Base._Base__nb_objects = 0

    def test_x_value(self):
        s0 = Square(1, 1, 1)
        self.assertEqual(s0.x, 1)
        Base._Base__nb_objects = 0

    def test_x_string(self):
        self.assertRaises(TypeError, Square, 1, "string")
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 1, "string")
        Base._Base__nb_objects = 0

    def test_x_neg(self):
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Square, 1, -1)
        Base._Base__nb_objects = 0

    def test_y(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'y'))
        Base._Base__nb_objects = 0

    def test_y_value(self):
        s0 = Square(1, 1, 1)
        self.assertEqual(s0.y, 1)
        Base._Base__nb_objects = 0

    def test_y_string(self):
        self.assertRaises(TypeError, Square, 1, 1, "string")
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Square, 1, 1, "string")
        Base._Base__nb_objects = 0

    def test_y_neg(self):
        self.assertRaises(ValueError, Square, 1, 1, -1)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Square, 1, 1, -1)
        Base._Base__nb_objects = 0

    def test_automatic(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        s2 = Square(1)
        self.assertEqual(s2.id, 2)
        s3 = Square(1)
        self.assertEqual(s3.id, 3)
        s4 = Square(1)
        self.assertEqual(s4.id, 4)
[O        s5 = Square(1)
        self.assertEqual(s5.id, 5)
        Base._Base__nb_objects = 0

    def test_manual(self):
        s1 = Square(1, 0, 0, 45)
        self.assertEqual(s1.id, 45)
        s2 = Square(1, 0, 0, 56)
        self.assertEqual(s2.id, 56)
        s3 = Square(1, 0, 0, 67)
        self.assertEqual(s3.id, 67)
        s4 = Square(1, 0, 0, 78)
        self.assertEqual(s4.id, 78)
        s5 = Square(1, 0, 0, 89)
        self.assertEqual(s5.id, 89)
        Base._Base__nb_objects = 0

    def test_mixed(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        s2 = Square(1, 0, 0, 56)
        self.assertEqual(s2.id, 56)
        s3 = Square(1)
        self.assertEqual(s3.id, 2)
        s4 = Square(1, 0, 0, 78)
        self.assertEqual(s4.id, 78)
        s5 = Square(1)
        self.assertEqual(s5.id, 3)
        Base._Base__nb_objects = 0

    def test_area(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'area'))
        Base._Base__nb_objects = 0

    def test_area_value(self):
        s0 = Square(1)
        s1 = Square(3)
        s2 = Square(2)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s0.area(), 1)
        self.assertEqual(s1.area(), 9)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 64)
        Base._Base__nb_objects = 0

    def test_display(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'display'))
        Base._Base__nb_objects = 0

    def test_display_d(self):
        string = "##\n##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            Square(2).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        string = "####\n####\n####\n####"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            Square(4).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_display1(self):
        string = "+\n\n  ##\n  ##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("+", end="")
            Square(2, 2, 2).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_display2(self):
        string = "+ ##\n ##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("+", end="")
            Square(2, 1, 0).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_display_arg(self):
        s1 = Square(1, 1, 1)
        self.assertRaises(TypeError, s1.display, 1)
        """
        self.assertRaisesRegex(TypeError,
                              'display() takes 1 positional
                              argument but 2 were given',
                             s1.display, 1)
        """
        Base._Base__nb_objects = 0

    def test_str(self):
        string = "[Square] (1) 0/0 - 1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(1)
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
        string = "[Square] (12) 2/1 - 4"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(4, 2, 1, 12)
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
        string = "[Square] (1) 1/0 - 5"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s2 = Square(5, 1)
            print(s2)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_update_args(self):
        s1 = Square(10, 10, 10)
        s1.update(89)
        string = "[Square] (89) 10/10 - 10"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89)
        string = "[Square] (89) 10/10 - 10"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 2)
        string = "[Square] (89) 10/10 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 2, 4)
        string = "[Square] (89) 4/10 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 2, 4, 5)
        string = "[Square] (89) 4/5 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_update_kwargs(self):
        s1 = Square(10, 10, 10)
        s1.update(size=1)
        string = "[Square] (1) 10/10 - 1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(size=3, x=2)
        string = "[Square] (1) 2/10 - 3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(y=1, size=2, x=3, id=89)
        string = "[Square] (89) 3/1 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(x=1, size=4, y=3)
        string = "[Square] (89) 1/3 - 4"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 2, 4, 5)
        string = "[Square] (89) 4/5 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_update_mixed_args_kwargs(self):
        s1 = Square(10, 10, 10)
        s1.update(size=1)
        string = "[Square] (1) 10/10 - 1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(2)
        string = "[Square] (2) 10/10 - 1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(5, y=1, size=2, x=3, id=89)
        string = "[Square] (5) 10/10 - 1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(5, 7, 7, y=1, width=2, x=3, id=89)
        string = "[Square] (5) 7/10 - 7"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 3, 4, 5, id=3)
        string = "[Square] (89) 4/5 - 3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_square_instance(self):
        obj = Square(1)
        self.assertIsInstance(obj, Square)

    def test_square_inherits_rectangle(self):
        obj = Square(1)
        self.assertIsInstance(obj, Rectangle)

    def test_square_noargs(self):
        self.assertRaises(TypeError, Square)

    def test_square_required_attrs_exists(self):
        obj = Square(1)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'width'))
        self.assertTrue(hasattr(obj, 'height'))
        self.assertTrue(hasattr(obj, 'size'))
        self.assertTrue(hasattr(obj, 'x'))
        self.assertTrue(hasattr(obj, 'y'))

    def test_square_getters_setters(self):
        obj = Square(1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.size = 4
        obj.x = 5
        obj.y = 6
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)

    def test_square_defaults(self):
        obj = Square(1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_square_update_valid_args(self):
        obj = Square(1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(111)
        self.assertEqual(obj.id, 111)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(12, 2)
        self.assertEqual(obj.id, 12)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(13, 14, 15)
        self.assertEqual(obj.id, 13)
        self.assertEqual(obj.size, 14)
        self.assertEqual(obj.x, 15)
        self.assertEqual(obj.y, 0)
        obj.update(100, 200, 300, 400)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.size, 200)
        self.assertEqual(obj.x, 300)
        self.assertEqual(obj.y, 400)
        obj.update(10, 20, 30, 40, 50)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.size, 20)
        self.assertEqual(obj.x, 30)
        self.assertEqual(obj.y, 40)
        obj.update(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_rectangle_update_args_type_validation(self):
        obj = Square(1)

        with self.assertRaises(TypeError) as context:
            obj.update(1, 'b')
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 2, {})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 1, 1, {'a': 1})
        self.assertIn('y must be an integer', str(context.exception))

    def test_square_display(self):
        out = []
        stdout_data = [io.StringIO() for i in range(6)]
        squares = [Square(1),
                   Square(1, 2),
                   Square(2, 2, 2),
                   Square(3, 3, 3, 3),
                   Square(4, 4),
                   Square(4, 6, 2, 3)]
        target = ['#\n',
                  '  #\n',
                  '\n\n  ##\n  ##\n',
                  '\n\n\n   ###\n   ###\n   ###\n',
                  '    ####\n    ####\n    ####\n    ####\n',
                  '\n\n      ####\n      ####\n      ####\n      ####\n']
        for i in range(6):
            with contextlib.redirect_stdout(stdout_data[i]):
                squares[i].display()
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_square_display_str(self):
        out = []
        stdout_data = [io.StringIO() for i in range(7)]
        squares = [Square(1, 2, 3, 4),
                   Square(4, 3, 2, 1),
                   Square(1, 1),
                   Square(2, 2, id=666),
                   Square(4, 5, 6, 999),
                   Square(4, 6, 9),
                   Square(9, 8, y=7)]
        target = ['[Square] (4) 2/3 - 1\n',
                  '[Square] (1) 3/2 - 4\n',
                  '[Square] (1) 1/0 - 1\n',
                  '[Square] (666) 2/0 - 2\n',
                  '[Square] (999) 5/6 - 4\n',
                  '[Square] (2) 6/9 - 4\n',
                  '[Square] (3) 8/7 - 9\n']
        for i in range(7):
            with contextlib.redirect_stdout(stdout_data[i]):
                print(squares[i])
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_square_update_valid_kwargs(self):
        obj = Square(1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(id=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(size=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(x=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 0)
        obj.update(y=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 2)
        obj.update(id=1, size=1, x=1, y=1)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 1)
        obj.update(y=98, x=98, size=98, id=98)
        self.assertEqual(obj.id, 98)
        self.assertEqual(obj.size, 98)
        self.assertEqual(obj.x, 98)
        self.assertEqual(obj.y, 98)
        obj.update(y=99, x=99, size=99, id=99)
        self.assertEqual(obj.id, 99)
        self.assertEqual(obj.size, 99)
        self.assertEqual(obj.x, 99)
        self.assertEqual(obj.y, 99)
        obj.update(x=100, size=100, id=100)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.size, 100)
        self.assertEqual(obj.x, 100)
        self.assertEqual(obj.y, 99)
        obj.update(x=101, size=101)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.size, 101)
        self.assertEqual(obj.x, 101)
        self.assertEqual(obj.y, 99)

    def test_rectangle_update_invalid_kwargs(self):
        obj = Square(1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

        with self.assertRaises(TypeError) as context:
            obj.update(size='3')
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(x={'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(y=[31])
        self.assertIn('y must be an integer', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(size=0)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(size=-20)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(x=-30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(y=-80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_rectangle_update_skip_kwargs(self):
        obj = Square(1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, id=4)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, id=13, size=14)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, id=13, size=14, x=15)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, 6, id=13, size=14, x=15, y=16)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)
        obj.update(3, 4, 5, 6, 7, id=13, width=14, height=15, x=16, y=17)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)

    def test_square_to_dictionary(self):
        obj = Square(1)
        target = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(obj.to_dictionary(), target)
        obj.update(3, 4, 5, 6)
        target = {'id': 3, 'size': 4, 'x': 5, 'y': 6}
        self.assertDictEqual(obj.to_dictionary(), target)

    def test_load_from_file_csv_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        target = "[Square] (1) 0/0 - 5\n" + \
                 "[Square] (2) 9/1 - 7"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            for sqr in list_squares_output:
                print("{}".format(sqr))
            output = temp_stdout.getvalue().strip()
        self.assertEqual(output, target)
        Base._Base__nb_objects = 0

    def test_load_from_file_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        target = "[Square] (1) 0/0 - 5" + "\n" + "[Square] (2) 9/1 - 7"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            for sqr in list_squares_output:
                print(sqr)
            output = temp_stdout.getvalue().strip()
        self.assertEqual(output, target)
        Base._Base__nb_objects = 0

    def test_create_sqr(self):
        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 == s2)
        self.assertFalse(s1 is s2)

    def test_from_json_string_sqr(self):
        list_input = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("[{}] {}".format(type(list_input), list_input))
            output1 = temp_stdout.getvalue().strip()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("[{}] {}".format(type(list_output), list_output))
            output2 = temp_stdout.getvalue().strip()
        self.assertEqual(output1, output2)
