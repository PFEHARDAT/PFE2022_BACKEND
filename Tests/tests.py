from django.test import TestCase

# Create your tests here.

class TestHelloWorld(TestCase):
   def test_hello_world(self):
       self.assertEqual("hello world", "hello world")
