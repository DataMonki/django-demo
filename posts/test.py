from unittest.case import expectedFailure
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just in case')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just in case')



class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self) -> None:
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
