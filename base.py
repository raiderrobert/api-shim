"""
Base API Interface
"""

import requests


class APIBase(object):
    """
    Base implementation to connect to an API endpoint
    """
    url = None
    session = None
    endpoint = None
    POST_headers = {"Content-Type": "Application/json"}

    def setup_session(self, session=None, username=None, password=None):
        if not session:
            self.session = requests.Session()
            self.session.auth = (username, password)
        else:
            self.session = session
        return session

    def post(self, data, query=None, headers=None, endpoint=None):
        query = query if query else ''
        headers = self.POST_headers if not headers else headers
        endpoint = self.endpoint if not endpoint else endpoint

        return self.session.post(self.url + endpoint + query, data=data, headers=headers)

    def get(self, query, endpoint=None):
        endpoint = self.endpoint if not endpoint else endpoint
        return self.session.get(self.url + endpoint + query)
