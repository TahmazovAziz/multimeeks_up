from django.test import TestCase
from cinema.models import *
from django.urls import reverse


class TestCinema(TestCase): 
    def create_media(self,name='s', year='2020', discription='discription' ,direct_by='sss', country='ru', poster='//',slug='s',category=None):
        if category == None:
            c = Category.objects.create(name='s' , slug='ed') 
        return Media.objects.create(name=name,year=year,discription=discription,direct_by=direct_by,country=country,poster=poster,slug=slug,category=c)
    
    def test_media_creation(self):
        m = self.create_media()
        self.assertTrue(isinstance(m,Media))
        self.assertEqual(str(m),m.name)
        
    def test_view(self):
        w = self.create_media()
        url = reverse('player' , args=[w.pk, w.slug, w.slug])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)
        self.assertIn(w.name.encode(), resp.content)
    
    def create_category(self, name='s',slug='d'):
        return Category.objects.create(name=name, slug=slug)
    
    def test_category_create(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(str(c), c.name)
    
    def create_message(self, message_text='sd', chatid='None', niknaimid='None'):
        if chatid == 'None' or niknaimid == 'None':
            ch = ComentName.objects.create(room_name='ss')
            ni = Niknaim.objects.create(name='sss')

        return Message.objects.create(message_text=message_text, chatid=ch, niknaimid=ni)
    
    def test_mess(self):
        mes = self.create_message() 
        self.assertTrue(isinstance(mes, Message))
        self.assertEqual(str(mes), mes.message_text)