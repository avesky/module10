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

