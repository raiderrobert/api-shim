# api-shim
A bit of boilerplate to make rest api wrappers

!!! WARNING IN PRE-ALPHA: LOTS OF STUFF IS BROKEN !!!

##  Basic Implementation with Slack

The `APIBase` class is a simple implementation for interacting with API endpoints. (Slack docs: https://api.slack.com/methods/channels.history)

    # slack.py
    from api_shim import APIBase
    
    class ChannelHistory(APIBase):
        url = 'https://slack.com/api/'
        endpoint = 'channels.history'
        params = ['token','channel']
        
       
Using your new API wrapper.

    >>> import slack
    >>> token = 'shhh-be-verwee-verwee-quiet'
    >>> slack.ChannelHistory(token=token, channel='foo')
    <Response [200]>
    


##  Advanced Implementation with Slack

The more advanced `API` implementation permits nested resources.

    # slack.py
    from api_shim import API, APIBase
    
    class Slack(API):
        url = 'https://slack.com/api/'
        resources = [Channels]
        params = ['token']
        
    class Channels(API):
        resources = [History, Info, List]
    
    class History(APIBase):
        endpoint = 'channels.history'
        params = ['channel']
        
    class Info(APIBase):
        endpoint = 'channels.info'
        params = ['channel']
     
    class List(APIBase):
        endpoint = 'channels.list'
        
Using your new API wrapper.

    >>> import slack
    >>> token = 'shhh-be-verwee-verwee-quiet'
    >>> slack.Channels.History(token=token, channel='foo')
    <Response [200]>
