from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment


class PostDetailTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            blog_title='Test Post',
            slug='test-post',
            blog_author=self.user,
            blog_content='This is a test post content',
            status=1
        )
        self.comment = Comment.objects.create(
            blog_post=self.post,
            user=self.user,
            message='Test comment',
            approved=True
        )

    def test_get_post_detail(self):
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        # self.assertEqual(response.context['post'], self.post)
        print(response.context['comments'].count())
        self.assertEqual(response.context['comments'].count(), 1)

    def test_post_comment(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_detail', args=['test-post']), {
        'message': 'New test comment',
        })
        self.assertEqual(response.context['commented'], True)
        self.assertEqual(response.context['comments'].count(), 1)  # 1 because the recent comment is not approved yet
    
    def test_like_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_like', args=['test-post']))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(self.post.likes.count(), 1)
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())

    def test_delete_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_delete', args=['test-post']))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertFalse(Post.objects.filter(slug='test-post').exists())

    def test_remove_comment(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('remove-comment', args=['test-post']))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())
