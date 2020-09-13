from io import IOBase

from tobe.bot.methods import BaseMethod
from .types import Update, WebhookInfo


class getUpdates(BaseMethod):
    """Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

    Parameters
    ----------
    offset : Integer, optional
         Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.
    limit : Integer, optional
         Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
    timeout : Integer, optional
         Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.
    allowed_updates : Array of String, optional
         A JSON-serialized list of the update types you want your bot to receive. For example, specify [�message�, �edited_channel_post�, �callback_query�] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all updates regardless of type (default). If not specified, the previous setting will be used.Please note that this parameter doesn't affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time.
    """

    response_type = [Update]

    def __init__(self, offset: int = None,
                 limit: int = None,
                 timeout: int = None,
                 allowed_updates=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
        self.timeout = timeout
        self.allowed_updates = allowed_updates


class setWebhook(BaseMethod):
    """If you'd like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. https://www.example.com/<token>. Since nobody else knows your bot's token, you can be pretty sure it's us.

    Parameters
    ----------
    url : String
         HTTPS url to send updates to. Use an empty string to remove webhook integration
    certificate : InputFile, optional
         Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.
    max_connections : Integer, optional
         Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput.
    allowed_updates : Array of String, optional
         A JSON-serialized list of the update types you want your bot to receive. For example, specify [�message�, �edited_channel_post�, �callback_query�] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all updates regardless of type (default). If not specified, the previous setting will be used.Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.
    """

    def __init__(self,
                 url: str,
                 certificate: IOBase = None,
                 max_connections: int = None,
                 allowed_updates=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.certificate = certificate
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates


class deleteWebhook(BaseMethod):
    """
    Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success. Requires no parameters.
    """

    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)


class getWebhookInfo(BaseMethod):
    """
    Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.
    """
    response_type = WebhookInfo

    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
