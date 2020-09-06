from ..types import BaseType, Message, Poll, PollAnswer, CallbackQuery
from ..inline.types import InlineQuery, ChosenInlineResult


class Update(BaseType):
    """This object represents an incoming update.At most one of the optional parameters can be present in any given update.

    Parameters
    ----------
    update_id : Integer
         The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    message : Message, optional
         New incoming message of any kind � text, photo, sticker, etc.
    edited_message : Message, optional
         New version of a message that is known to the bot and was edited
    channel_post : Message, optional
         New incoming channel post of any kind � text, photo, sticker, etc.
    edited_channel_post : Message, optional
         New version of a channel post that is known to the bot and was edited
    inline_query : InlineQuery, optional
         New incoming inline query
    chosen_inline_result : ChosenInlineResult, optional
         The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
    callback_query : CallbackQuery, optional
         New incoming callback query
    shipping_query : ShippingQuery, optional
         New incoming shipping query. Only for invoices with flexible price
    pre_checkout_query : PreCheckoutQuery, optional
         New incoming pre-checkout query. Contains full information about checkout
    poll : Poll, optional
         New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
    poll_answer : PollAnswer, optional
         A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
    """

    def __init__(self,
                 update_id,
                 message=None,
                 edited_message=None,
                 channel_post=None,
                 edited_channel_post=None,
                 inline_query=None,
                 chosen_inline_result=None,
                 callback_query=None,
                 shipping_query=None,
                 pre_checkout_query=None,
                 poll=None,
                 poll_answer=None):
        super().__init__()
        self.update_id = update_id
        self.message = Message.parse(message)
        self.edited_message = Message.parse(edited_message)
        self.channel_post = Message.parse(channel_post)
        self.edited_channel_post = Message.parse(edited_channel_post)
        self.inline_query = InlineQuery.parse(inline_query)
        self.chosen_inline_result = ChosenInlineResult.parse(chosen_inline_result)
        self.callback_query = CallbackQuery.parse(callback_query)
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.poll = Poll.parse(poll)
        self.poll_answer = PollAnswer.parse(poll_answer)

    def get_offset(self):
        return self.update_id


class WebhookInfo(BaseType):
    """Contains information about the current status of a webhook. """

    def __init__(self,
                 url: str,
                 has_custom_certificate: bool,
                 pending_update_count: int,
                 last_error_date: int = None,
                 last_error_message: str = None,
                 max_connections: int = None,
                 allowed_updates=None):
        super().__init__()
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates