"""
Program: class_test.py
Author: Andy Volesky
Last date modified: 11/03/2021
The purpose of this program:

Include setUp() and tearDown() methods
Write unit test test_object_created_required_attributes(self)
Test constructor values set to only required attributes for acceptable values
Write unit test test_object_created_all_attributes(self)
Test constructor values set to all attributes for acceptable values
Write unit test test_student_str(self)
Test the str() method
Write unit test test_object_not_created_error_last_name(self) that expect exception raised
Add exception to constructor (not in test!)
Write test_object_not_created_error_first_name(self)
Add exception to constructor (not in test!)
Write test_object_not_created_error_first_name(self)
Add exception to constructor
Write test_object_not_created_error_major(self)
Add exception to constructor
Write test_object_not_created_error_gpa(self)
Add exception to constructor
NOTE: look up how isinstance(gpa, float) works AND check range
Write a main()
Create 2 student objects and print them

"""

import unittest
from Student import Student

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student('Coulier', 'Dave', 'Biology', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Coulier')
        self.assertEqual(self.student.first_name, 'Dave')
        self.assertEqual(self.student.major, 'Biology')

    def test_object_created_all_attributes(self):
        student = Student('Coulier', 'Dave', 'Biology', 4.0)
        assert student.last_name == 'Coulier'
        assert student.first_name == 'Dave'
        assert student.major == 'Biology'
        assert student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Coulier, Dave has major Biology with gpa: 4.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = Student('123', 'Dave', 'Biology')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = Student('Dave', '123', 'Biology')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = Student('Dave', 'Coulier', '495')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = Student('Dave', 'Coulier', 'Biology', 'asdf')

if __name__ == '__main__':
    unittest.main()

