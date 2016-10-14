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

The `APIBase` class is a simple implementation for interacting with API endpoints. (Slack docs: https://api.slack.com/methods/channels.history)

    # slack.py
    from api_shim import API, APIBase
    
    class Slack(API):
        url = 'https://slack.com/api/'
        resources = [Channels]
        args = ['token']
        
    class Channels(API):
        resources = [ChannelsHistory, ChannelsList]
    
    class ChannelsHistory(APIBase):
        endpoint = 'channels.history'
        args = ['channel']
     
    class ChannelsList(APIBase):
        endpoint = 'channels.list'
        
