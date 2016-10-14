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

The `APIBase` class is a simple implementation for interacting with API endpoints.

    # slack.py
    from api_shim import API, APIBase
    
    class Slack(API):
        url = 'https://slack.com/api/'
        resources = [Channels]
        args = ['token']
        
    class Channels(API):
        resources = [ChannelsHistory, ChannelsInfo, ChannelsList]
    
    class ChannelsHistory(APIBase):
        """
        Docs: https://api.slack.com/methods/channels.history
        """
        endpoint = 'channels.history'
        args = ['channel']
        
    class ChannelsInfo(APIBase):
        """
        Docs: https://api.slack.com/methods/channels.info
        """
        endpoint = 'channels.info'
        args = ['channel']
     
    class ChannelsList(APIBase):
        """
        Docs: https://api.slack.com/methods/channels.list
        """
        endpoint = 'channels.list'
        
