# api-shim
A bit of boilerplate to make rest api wrappers


##  Basic Implementation with Slack

The `APIBase` class is a simple implementation for interacting with API endpoints.

    # slack.py
    from api_shim.base import APIBase
    
    class ChannelHistory(APIBase):
        url = 'https://slack.com/api/'
        endpoint = 'channels.history'
        required_args = ['token','channel']
        optional_args = ['latest', 'oldest']  # could also implement 'inclusive', 'count', 'unreads'
        
       
Using your new API wrapper.

    >>> import slack
    >>> token = 'shhh-be-verwee-verwee-quiet'
    >>> slack.ChannelHistory(token=token, channel='foo')
    <Response [200]>
    

