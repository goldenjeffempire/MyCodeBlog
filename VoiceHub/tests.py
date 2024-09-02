# VoiceHub/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostViewTests(TestCase):
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'VoiceHub/post_list.html')

    def test_post_detail_view(self):
        post = Post.objects.create(title='Test Post', content='Content')
        response = self.client.get(reverse('post_detail', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'VoiceHub/post_detail.html')

