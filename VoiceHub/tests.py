from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from VoiceHub.models import Post

class PostViewTests(TestCase):
    def setUp(self):
        # Create a user to associate with posts
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'VoiceHub/post_list.html')

    def test_post_detail_view(self):
        # Create a post with the user as author
        post = Post.objects.create(title='Test Post', content='Content', author=self.user)
        response = self.client.get(reverse('post_detail', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'VoiceHub/post_detail.html')
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Content')
