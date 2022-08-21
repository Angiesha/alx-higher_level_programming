#!/usr/bin/python3
"""
Unittest for Rectangle class
"""

import unittest
import contextlib
from io import StringIO
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_classBase(self):
        r0 = Rectangle(1, 1)
        self.assertIsInstance(r0, Base)
        self.assertIsInstance(r0, Rectangle)

    def test_class(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(isinstance(r0, Base))

    def test_subclass(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(isinstance(r0, Rectangle))

    def test_nb(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, '_Base__nb_objects'))
        Base._Base__nb_objects = 0

    def test_rectangle_arg(self):
        self.assertRaises(TypeError, Rectangle)
        """
        self.assertRaisesRegex(TypeError,
                              "__init__() missing 2 required positional
                              arguments:
                              'width' and 'height'",
                             Rectangle)
        """
        self.assertRaises(TypeError, Rectangle, 1)
        """
        self.assertRaisesRegex(TypeError,
                              "__init__() missing 1 required
                              positional argument: 'height'",
                             Rectangle, 1)
        """
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, 1, 1, 1)
        """
        self.assertRaisesRegex(TypeError,
                              "__init__() takes from 3 to 6 positional
                              arguments but 7 were given",
                             Rectangle, 1, 1, 1, 1, 1)
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'id'))
        Base._Base__nb_objects = 0

    def test_width(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'width'))
        Base._Base__nb_objects = 0

    def test_width_value(self):
        r0 = Rectangle(1, 1)
        self.assertEqual(r0.width, 1)
        Base._Base__nb_objects = 0

    def test_width_string(self):
        self.assertRaises(TypeError, Rectangle, "string", 1)
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, "string", 1)
        Base._Base__nb_objects = 0

    def test_width_neg(self):
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -1, 1)
        Base._Base__nb_objects = 0

    def test_height(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'height'))
        Base._Base__nb_objects = 0

    def test_height_value(self):
        r0 = Rectangle(1, 1)
        self.assertEqual(r0.height, 1)
        Base._Base__nb_objects = 0

    def test_height_string(self):
        self.assertRaises(TypeError, Rectangle, 1, "string")
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 1, "string")
        Base._Base__nb_objects = 0

    def test_height_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 1, -1)
        Base._Base__nb_objects = 0

    def test_x(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'x'))
        Base._Base__nb_objects = 0

    def test_x_value(self):
        r0 = Rectangle(1, 1, 1)
        self.assertEqual(r0.x, 1)
        Base._Base__nb_objects = 0

    def test_x_string(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, "string")
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 1, 1, "string")
        Base._Base__nb_objects = 0

    def test_x_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Rectangle, 1, 1, -1)
        Base._Base__nb_objects = 0

    def test_y(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'y'))
        Base._Base__nb_objects = 0

    def test_y_value(self):
        r0 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r0.y, 1)
        Base._Base__nb_objects = 0

    def test_y_string(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, "string")
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Rectangle, 1, 1, 1, "string")
        Base._Base__nb_objects = 0

    def test_y_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Rectangle, 1, 1, 1, -1)
        Base._Base__nb_objects = 0

    def test_automatic(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(1, 1)
        self.assertEqual(r4.id, 4)
        r5 = Rectangle(1, 1)
        self.assertEqual(r5.id, 5)
        Base._Base__nb_objects = 0

    def test_manual(self):
        r1 = Rectangle(1, 1, 0, 0, 45)
        self.assertEqual(r1.id, 45)
        r2 = Rectangle(1, 1, 0, 0, 56)
        self.assertEqual(r2.id, 56)
        r3 = Rectangle(1, 1, 0, 0, 67)
        self.assertEqual(r3.id, 67)
        r4 = Rectangle(1, 1, 0, 0, 78)
        self.assertEqual(r4.id, 78)
        r5 = Rectangle(1, 1, 0, 0, 89)
        self.assertEqual(r5.id, 89)
        Base._Base__nb_objects = 0

    def test_mixed(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 1, 0, 0, 56)
        self.assertEqual(r2.id, 56)
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.id, 2)
        r4 = Rectangle(1, 1, 0, 0, 78)
        self.assertEqual(r4.id, 78)
        r5 = Rectangle(1, 1)
        self.assertEqual(r5.id, 3)
        Base._Base__nb_objects = 0

    def test_area(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'area'))
        Base._Base__nb_objects = 0

    def test_area_value(self):
        r0 = Rectangle(1, 1)
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r0.area(), 1)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)
        Base._Base__nb_objects = 0

    def test_display(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'display'))
        Base._Base__nb_objects = 0

    def test_display(self):
        string = "##\n##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            Rectangle(2, 2).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        string = "####\n####\n####\n####\n####\n####"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            Rectangle(4, 6).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_display1(self):
        string = "+\n\n  ##\n  ##\n  ##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("+", end="")
            Rectangle(2, 3, 2, 2).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_display2(self):
        string = "+ ###\n ###"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("+", end="")
            Rectangle(3, 2, 1, 0).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_display_arg(self):
        r1 = Rectangle(1, 1, 1, 1)
        self.assertRaises(TypeError, r1.display, 1)
        """
        self.assertRaisesRegex(TypeError,
                              'display() takes 1 positional
                              argument but 2 were given',
                             r1.display, 1)
        """
        Base._Base__nb_objects = 0

    def test_str(self):
        string = "[Rectangle] (1) 0/0 - 1/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(1, 1, )
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
        string = "[Rectangle] (12) 2/1 - 4/6"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
        string = "[Rectangle] (1) 1/0 - 5/5"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r2 = Rectangle(5, 5, 1)
            print(r2)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_update_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        string = "[Rectangle] (89) 10/10 - 10/10"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2)
        string = "[Rectangle] (89) 10/10 - 2/10"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2, 3)
        string = "[Rectangle] (89) 10/10 - 2/3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2, 3, 4)
        string = "[Rectangle] (89) 4/10 - 2/3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2, 3, 4, 5)
        string = "[Rectangle] (89) 4/5 - 2/3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        string = "[Rectangle] (1) 10/10 - 10/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(width=1, x=2)
        string = "[Rectangle] (1) 2/10 - 1/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(y=1, width=2, x=3, id=89)
        string = "[Rectangle] (89) 3/1 - 2/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(x=1, height=2, y=3, width=4)
        string = "[Rectangle] (89) 1/3 - 4/2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2, 3, 4, 5)
        string = "[Rectangle] (89) 4/5 - 2/3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_uptdate_mixed_args_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        string = "[Rectangle] (1) 10/10 - 10/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(1, 2)
        string = "[Rectangle] (1) 10/10 - 2/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(5, 6, y=1, width=2, x=3, id=89)
        string = "[Rectangle] (5) 10/10 - 6/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(5, 6, 7, 7, y=1, width=2, x=3, id=89)
        string = "[Rectangle] (5) 7/10 - 6/7"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2, 3, 4, 5, id=3)
        string = "[Rectangle] (89) 4/5 - 2/3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        string = "[Rectangle] (1) 1/9 - 10/2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1_dictionary)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(type(r1_dictionary), dict)

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_rectangle_noargs(self):
        self.assertRaises(TypeError, Rectangle)

    def test_rectangle_one_arg(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_rectangle_instance(self):
        obj = Rectangle(1, 1)
        self.assertIsInstance(obj, Rectangle)

    def test_rectangle_inherits_base(self):
        obj = Rectangle(1, 1)
        self.assertIsInstance(obj, Base)

    def test_rectangle_required_attrs_exists(self):
        obj = Rectangle(3, 4)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, '_Rectangle__width'))
        self.assertTrue(hasattr(obj, '_Rectangle__height'))
        self.assertTrue(hasattr(obj, '_Rectangle__x'))
        self.assertTrue(hasattr(obj, '_Rectangle__y'))

    def test_rectangle_getters_setters(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.width = 10
        obj.height = 20
        obj.x = 5
        obj.y = 6
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)

    def test_rectangle_defaults(self):
        obj = Rectangle(1, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_rectangle_type_validation(self):
        with self.assertRaises(TypeError) as context:
            obj = Rectangle('a', 2)
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(2, {})
        self.assertIn('height must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, 1, {'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, 1, 4, [31])
        self.assertIn('y must be an integer', str(context.exception))

    def test_rectangle_value_validation(self):
        with self.assertRaises(ValueError) as context:
            obj = Rectangle(0, 1)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(-20, 1)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 0)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, -69)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 1, -30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 1, 1, -80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_rectangle_area_method(self):
        obj = Rectangle(1, 1)
        self.assertEqual(obj.area(), 1)

        obj = Rectangle(2, 2)
        self.assertEqual(obj.area(), 4)

        obj = Rectangle(123456789, 987654321)
        self.assertEqual(obj.area(), 121932631112635269)

        obj = Rectangle(0xCACA, 0xB0BA)
        self.assertEqual(obj.area(), 2348693188)

        obj = Rectangle(0b01010101010101001, 0b1010000111001001001)
        self.assertEqual(obj.area(), 14475782193)

        obj = Rectangle(0o3542157, 0o775422315)
        self.assertEqual(obj.area(), 129269575248099)

    def test_rectangle_display_without_xy(self):
        out = []
        stdout_data = [io.StringIO() for i in range(6)]
        rectangles = [Rectangle(1, 1),
                      Rectangle(1, 2),
                      Rectangle(2, 1),
                      Rectangle(2, 2),
                      Rectangle(4, 4),
                      Rectangle(4, 6)]
        target = ['#\n',
                  '#\n#\n',
                  '##\n',
                  '##\n##\n',
                  '####\n####\n####\n####\n',
                  '####\n####\n####\n####\n####\n####\n']
        for i in range(6):
            with contextlib.redirect_stdout(stdout_data[i]):
                rectangles[i].display()
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_rectangle_display_str(self):
        out = []
        stdout_data = [io.StringIO() for i in range(7)]
        rectangles = [Rectangle(1, 2, 3, 4),
                      Rectangle(4, 3, 2, 1),
                      Rectangle(1, 1),
                      Rectangle(2, 2, id=666),
                      Rectangle(4, 5, 6, 7, 999),
                      Rectangle(4, 6, 9),
                      Rectangle(9, 8, y=7)]
        target = ['[Rectangle] (1) 3/4 - 1/2\n',
                  '[Rectangle] (2) 2/1 - 4/3\n',
                  '[Rectangle] (3) 0/0 - 1/1\n',
                  '[Rectangle] (666) 0/0 - 2/2\n',
                  '[Rectangle] (999) 6/7 - 4/5\n',
                  '[Rectangle] (4) 9/0 - 4/6\n',
                  '[Rectangle] (5) 0/7 - 9/8\n']
        for i in range(7):
            with contextlib.redirect_stdout(stdout_data[i]):
                print(rectangles[i])
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_rectangle_display_with_xy(self):
        out = []
        stdout_data = [io.StringIO() for i in range(6)]
        rectangles = [Rectangle(1, 1, 2, 2),
                      Rectangle(1, 2, 2, 3),
                      Rectangle(2, 1, 7, 2),
                      Rectangle(2, 3, 2, 2),
                      Rectangle(4, 4, 1, 1),
                      Rectangle(3, 2, 1, 0)]
        target = ['\n\n  #\n',
                  '\n\n\n  #\n  #\n',
                  '\n\n       ##\n',
                  '\n\n  ##\n  ##\n  ##\n',
                  '\n ####\n ####\n ####\n ####\n',
                  ' ###\n ###\n']
        for i in range(6):
            with contextlib.redirect_stdout(stdout_data[i]):
                rectangles[i].display()
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_rectangle_update_valid_args(self):
        obj = Rectangle(1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(111)
        self.assertEqual(obj.id, 111)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(12, 2)
        self.assertEqual(obj.id, 12)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(13, 14, 15)
        self.assertEqual(obj.id, 13)
        self.assertEqual(obj.width, 14)
        self.assertEqual(obj.height, 15)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(100, 200, 300, 400)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 200)
        self.assertEqual(obj.height, 300)
        self.assertEqual(obj.x, 400)
        self.assertEqual(obj.y, 0)
        obj.update(10, 20, 30, 40, 50)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 20)
        self.assertEqual(obj.height, 30)
        self.assertEqual(obj.x, 40)
        self.assertEqual(obj.y, 50)
        obj.update(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_rectangle_update_args_type_validation(self):
        obj = Rectangle(1, 1)

        with self.assertRaises(TypeError) as context:
            obj.update(1, 'b')
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 2, {})
        self.assertIn('height must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 1, 1, {'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 1, 1, 4, [31])
        self.assertIn('y must be an integer', str(context.exception))

    def test_rectangle_update_args_value_validation(self):
        obj = Rectangle(1, 1)

        with self.assertRaises(ValueError) as context:
            obj.update(1, 0)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, -20, 1)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, 1, 0)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, 1, -69)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, 1, 1, -30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, 1, 1, 1, -80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_rectangle_update_valid_kwargs(self):
        obj = Rectangle(1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(id=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(width=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(height=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(x=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 0)
        obj.update(y=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 2)
        obj.update(id=1, width=1, height=1, x=1, y=1)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 1)
        obj.update(y=98, x=98, height=98, width=98, id=98)
        self.assertEqual(obj.id, 98)
        self.assertEqual(obj.width, 98)
        self.assertEqual(obj.height, 98)
        self.assertEqual(obj.x, 98)
        self.assertEqual(obj.y, 98)
        obj.update(y=99, x=99, width=99, id=99)
        self.assertEqual(obj.id, 99)
        self.assertEqual(obj.width, 99)
        self.assertEqual(obj.height, 98)
        self.assertEqual(obj.x, 99)
        self.assertEqual(obj.y, 99)
        obj.update(x=100, width=100, id=100)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 100)
        self.assertEqual(obj.height, 98)
        self.assertEqual(obj.x, 100)
        self.assertEqual(obj.y, 99)
        obj.update(x=101, width=101)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 101)
        self.assertEqual(obj.height, 98)
        self.assertEqual(obj.x, 101)
        self.assertEqual(obj.y, 99)

    def test_rectangle_update_skip_kwargs(self):
        obj = Rectangle(1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, id=4)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, id=13, width=14)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, id=13, width=14, height=15)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, 6, id=13, width=14, height=15, x=16)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, 6, 7, id=13, width=14, height=15, x=16, y=17)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 7)

    def test_rectangle_update_invalid_kwargs(self):
        obj = Rectangle(1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

        with self.assertRaises(TypeError) as context:
            obj.update(width='b')
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(height={})
        self.assertIn('height must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(x={'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(y=[31])
        self.assertIn('y must be an integer', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(width=0)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(width=-20)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(height=0)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(height=-69)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(x=-30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(y=-80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_rectangle_to_dictionary(self):
        obj = Rectangle(1, 1)
        target = {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(obj.to_dictionary(), target)
        obj.update(3, 4, 5, 6, 7)
        target = {'id': 3, 'width': 4, 'height': 5, 'x': 6, 'y': 7}
        self.assertDictEqual(obj.to_dictionary(), target)

    def test_load_from_file_csv_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        target = "[Rectangle] (1) 2/8 - 10/7\n" +\
                 "[Rectangle] (2) 0/0 - 2/4"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            for rect in list_rectangles_output:
                print("{}".format(rect))
            output = temp_stdout.getvalue().strip()
        self.assertEqual(output, target)

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        target = "[Rectangle] (1) 2/8 - 10/7\n" + \
                 "[Rectangle] (2) 0/0 - 2/4"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            for rect in list_rectangles_output:
                print("{}".format(rect))
            output = temp_stdout.getvalue().strip()
        self.assertEqual(output, target)

    def test_create_rect(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

    def test_from_json_string_rect(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("[{}] {}".format(type(list_input), list_input))
            output1 = temp_stdout.getvalue().strip()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("[{}] {}".format(type(list_output), list_output))
            output2 = temp_stdout.getvalue().strip()
        self.assertEqual(output1, output2)

    def test_from_json_string_rect_empty(self):
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("[{}] {}".format(type(list_input), list_input))
            output1 = temp_stdout.getvalue().strip()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("[{}] {}".format(type(list_output), list_output))
            output2 = temp_stdout.getvalue().strip()
        self.assertEqual(output1, output2)

    def test_from_json_string_rect_none(self):
        list_input = None
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        temp_stdout = StringIO()
        output1 = "[<class 'list'>] []"
        with contextlib.redirect_stdout(temp_stdout):
            print("[{}] {}".format(type(list_output), list_output))
            output2 = temp_stdout.getvalue().strip()
        self.assertEqual(output1, output2)

    def test_save_to_file_rect(self):
        r1 = Rectangle(1, 1)
        Rectangle.save_to_file([r1])
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            with open("Rectangle.json", "r") as file:
                print(file.read())
            output = temp_stdout.getvalue().strip()
        self.assertEqual(type(output), str)

    def test_save_to_file_rect_empty(self):
        my_list = None
        Rectangle.save_to_file(my_list)
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            with open("Rectangle.json", "r") as file:
                print(file.read())
            output = temp_stdout.getvalue().strip()
        self.assertEqual(output, "[]")

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str, type(json_dictionary))

    def test_018_dict_representation(self):
        """Tests the to_dictionary() method return
        """
        r1 = Rectangle(7, 7, 0, 0, 100)
        r1_dict = r1.to_dictionary()
        self.assertTrue(type(r1_dict) is dict)
        self.assertEqual(r1_dict['width'], 7)
        self.assertEqual(r1_dict['height'], 7)
        self.assertEqual(r1_dict['x'], 0)
        self.assertEqual(r1_dict['y'], 0)
        self.assertEqual(r1_dict['id'], 100)
        self.assertTrue(len(r1_dict) == 5)
