"""
Base API Interface
"""

try:
    from urllib.parse import urlparse, urlencode, urljoin
except ImportError:
    from urlparse import urlparse, urljoin
    from urllib import urlencode

import requests


class APIBase(object):
    """
    Base implementation to connect to an API endpoint
    """
    url = None
    endpoint = None
    POST_headers = {"Content-Type": "Application/json"}

    def join(self, query):
        absolute_url = '/'.join([self.url, self.endpoint, query])
        return absolute_url

    def post(self, data, query=None, headers=None):
        query = query if query else ''
        headers = self.POST_headers if not headers else headers
        absolute_url = self.join(query)
        return self._post(absolute_url, data=data, headers=headers)

    def _post(self, absolute_url, data, headers):
        return requests.post(absolute_url, data=data, headers=headers)

    def get(self, query):
        absolute_url = self.join(query)
        return self._get(absolute_url)

    def _get(self, absolute_url):
        return requests.get(absolute_url)


class SessionAPIBase(APIBase):
    """
    Added in session based stuff, so username and password can be used.
    """
    session = None

    def setup_session(self, session=None, username=None, password=None):
        if not session:
            self.session = requests.Session()
            self.session.auth = (username, password)
        else:
            self.session = session
        return session

    def _post(self, absolute_url, data, headers):
        return self.session.post(absolute_url, data=data, headers=headers)

    def _get(self, absolute_url):
        return self.session.get(absolute_url)

