from django.test import TestCase, Client

# Create your tests here.
from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='sunwie',
            sex=1,
            email='dd@qq.com',
            profession='ops',
            qq='33',
            phone='222'
        )
        Student.objects.create(
            name='sunwie',
            sex=1,
            email='dd@qq.com',
            profession='ops',
            qq='33',
            phone='222'
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='mufeng',
            sex=1,
            email='dd@qq.com',
            profession='ops',
            qq='33',
            phone='222'
        )
        print(student.get_sex_display())
        self.assertEqual(student.get_sex_display(),'boy','性别和展示不一致')

    def test_filter(self):
        Student.objects.create(
            name='mufeng',
            sex=1,
            email='dd@qq.com',
            profession='ops',
            qq='33',
            phone='222'
        )
        name = 'mufeng'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,'应该只存在名称为 {} 的记录'.format(name))

# view部分测试
    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='2@qq.com',
            profession='程序员',
            qq='33',
            phone='3222'
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertTrue(
            b'test_for_post' in response.content,
            'response must contain `test_for_post`'
        )
