from ..methods import BaseMethod


class answerInlineQuery(BaseMethod):
    """Use this method to send answers to an inline query. On success, True is returned.No more than 50 results per query are allowed.

    Parameters
    ----------
    inline_query_id : String
         Unique identifier for the answered query
    results : Array of InlineQueryResult
         A JSON-serialized array of results for the inline query
    cache_time : Integer, optional
         The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
    is_personal : Boolean, optional
         Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query
    next_offset : String, optional
         Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.
    switch_pm_text : String, optional
         If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter switch_pm_parameter
    switch_pm_parameter : String, optional
         Deep-linking parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed.Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an oauth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.
    """

    def __init__(self, inline_query_id,
                 results,
                 cache_time=None,
                 is_personal=None,
                 next_offset=None,
                 switch_pm_text=None,
                 switch_pm_parameter=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.inline_query_id = inline_query_id
        self.results = results
        self.cache_time = cache_time
        self.is_personal = is_personal
        self.next_offset = next_offset
        self.switch_pm_text = switch_pm_text
        self.switch_pm_parameter = switch_pm_parameter