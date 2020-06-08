from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import home_page
from blog.models import Item

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class BlogPageTest(TestCase):

    def test_blog_page_returns_correct_html(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

class CVPageTest(TestCase):

    def test_cv_page_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'blog/cv_display.html')

    def test_cv_edit_page_returns_correct_html(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

    def test_cv_edit_add_page_returns_correct_html(self):
        response = self.client.get('/cv/edit/add')
        self.assertTemplateUsed(response, 'blog/cv_add.html')

    def test_cv_edit_del_page_returns_correct_html(self):
        response = self.client.get('/cv/edit/delete')
        self.assertTemplateUsed(response, 'blog/cv_delete.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

    def test_can_save_a_POST_request(self):
        self.client.post('/cv/edit/add', data={'item_text': 'A new list item', 'item_category': 'skills'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/edit/add', data={'item_text': 'A new list item', 'item_category': 'skills'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/edit/add')

    #def test_only_saves_items_when_necessary(self):
    #    self.client.get('/')
    #    self.assertEqual(Item.objects.count(), 0)

    #def test_displays_all_list_items(self):
    #    Item.objects.create(text='itemey 1')
    #    Item.objects.create(text='itemey 2')

    #    response = self.client.get('/')

    #    self.assertIn('itemey 1', response.content.decode())
    #    self.assertIn('itemey 2', response.content.decode())