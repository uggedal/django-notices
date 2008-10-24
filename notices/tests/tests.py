from django.test import TestCase
from django.http import QueryDict
from django.conf import settings
from urlparse import urlsplit

class NoticesTestHelper(TestCase):
    notice_identifier = '<ul class="notices">'

    def assert_contains_notices(self, request):
        self.assertContains(request, self.notice_identifier)

    def assert_not_contains_notices(self, request):
        self.assertNotContains(request, self.notice_identifier)

    def get_with_redirect(self, location):
        request = self.client.get(location)
        scheme, netloc, path, query, fragment = urlsplit(request['Location'])
        redirected_request = self.client.get(path, QueryDict(query))
        return (request, redirected_request)

class NoticesTestCase(NoticesTestHelper):

    def test_should_display_notices(self):
        r1, r2 = self.get_with_redirect('/redirect_with_notice/')
        self.assert_contains_notices(r2)

    def test_should_not_display_unsupported_notice_types(self):
        settings.NOTICE_TYPES = ('soletype')
        r1, r2 = self.get_with_redirect('/redirect_with_notice/')
        self.assert_not_contains_notices(r2)
        settings.NOTICE_TYPES = None
