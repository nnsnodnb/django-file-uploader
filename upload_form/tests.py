from django.test import TestCase
from upload_form.models import FileNameModel

# Create your tests here.

class FileNameModelTest(TestCase):
	def test_is_empty(self):
		saved_file_name = FileNameModel.objects.all()
		self.assertEqual(saved_file_name.count(), 0)
