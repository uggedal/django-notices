from django.test import TestCase
from django.http import QueryDict
from urlparse import urlsplit

class NoticesTestCase(TestCase):

    def test_should_display_notices(self):
        r1 = self.client.get('/redirect_with_notice/')
        scheme, netloc, path, query, fragment = urlsplit(r1['Location'])
        r2 = self.client.get(path, QueryDict(query))
        self.assertContains(r2, '<ul class="notices">')
