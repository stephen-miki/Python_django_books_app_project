from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='steph', email='steph123@gmail.com', password='testpassword123')
        self.assertEqual(user.username, 'steph')
        self.assertEqual(user.email, 'steph123@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user(self):
        User = get_user_model()
        admin_user =User.objects.create_superuser(username='superadmin', email='superadmin@email.com', password='testpassword123')
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
