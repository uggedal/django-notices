from django.test import TestCase
from django.http import QueryDict
from urlparse import urlsplit

class NoticesTestCase(TestCase):

    def _get_with_redirect(self, location):
        request = self.client.get(location)
        scheme, netloc, path, query, fragment = urlsplit(request['Location'])
        redirected_request = self.client.get(path, QueryDict(query))
        return (request, redirected_request)

    def test_should_display_notices(self):
        r1, r2 = self._get_with_redirect('/redirect_with_notice/')
        self.assertContains(r2, '<ul class="notices">')
