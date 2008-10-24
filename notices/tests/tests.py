from django.test import TestCase
from django.http import QueryDict
from django.conf import settings
from urlparse import urlsplit
from notices import pack

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

    def test_should_display_notices_for_supported_types(self):
        r1, r2 = self.get_with_redirect('/redirect_with_notice/')
        self.assert_contains_notices(r2)

    def test_should_not_display_unsupported_notice_types(self):
        backup = settings.NOTICE_TYPES
        settings.NOTICE_TYPES = ('soletype')
        r1, r2 = self.get_with_redirect('/redirect_with_notice/')
        self.assert_not_contains_notices(r2)
        settings.NOTICE_TYPES = backup

    def test_should_raise_error_if_secret_key_is_empty(self):
        backup = settings.SECRET_KEY
        settings.SECRET_KEY = ""
        self.assertRaises(ValueError,
                          self.get_with_redirect,
                          '/redirect_with_notice/')
        settings.SECRET_KEY = backup

    def test_should_not_display_shorted_notice(self):
        str = pack('Perfectly legal notice')
        print str[:-2]
        r = self.client.get('/', QueryDict('_notice=' + str[:-2]))
        self.assert_not_contains_notices(r)

    def test_should_not_display_tampered_notice(self):
        str = pack('Perfectly legal notice')
        r = self.client.get('/', QueryDict('_notice=' + str[:-1] + 'x'))
        self.assert_not_contains_notices(r)
