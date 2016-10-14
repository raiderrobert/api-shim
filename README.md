# api-shim
A bit of boilerplate to make rest api wrappers


##  Basic Implementation

The `APIBase` class is a simple implementation for interacting with API endpoints.


    from api_shim.base import APIBase
    
    class SlackAPI(APIBase):
    
        sercret= 'ab12-0000000-000000000-000000000000-abc1234567890'
    
        def token_exchange(self):
            pass
