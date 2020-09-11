from ..methods import BaseMethod


class sendInvoice(BaseMethod):
    """Use this method to send invoices. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer
         Unique identifier for the target private chat
    title : String
         Product name, 1-32 characters
    description : String
         Product description, 1-255 characters
    payload : String
         Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    provider_token : String
         Payments provider token, obtained via Botfather
    start_parameter : String
         Unique deep-linking parameter that can be used to generate this invoice when used as a start parameter
    currency : String
         Three-letter ISO 4217 currency code, see more on currencies
    prices : Array of LabeledPrice
         Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    provider_data : String, optional
         A JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
    photo_url : String, optional
         URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    photo_size : Integer, optional
         Photo size
    photo_width : Integer, optional
         Photo width
    photo_height : Integer, optional
         Photo height
    need_name : Boolean, optional
         Pass True, if you require the user's full name to complete the order
    need_phone_number : Boolean, optional
         Pass True, if you require the user's phone number to complete the order
    need_email : Boolean, optional
         Pass True, if you require the user's email address to complete the order
    need_shipping_address : Boolean, optional
         Pass True, if you require the user's shipping address to complete the order
    send_phone_number_to_provider : Boolean, optional
         Pass True, if user's phone number should be sent to provider
    send_email_to_provider : Boolean, optional
         Pass True, if user's email address should be sent to provider
    is_flexible : Boolean, optional
         Pass True, if the final price depends on the shipping method
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup, optional
         A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button.
    """

    def __init__(self, chat_id,
                 title,
                 description,
                 payload,
                 provider_token,
                 start_parameter,
                 currency,
                 prices,
                 provider_data=None,
                 photo_url=None,
                 photo_size=None,
                 photo_width=None,
                 photo_height=None,
                 need_name=None,
                 need_phone_number=None,
                 need_email=None,
                 need_shipping_address=None,
                 send_phone_number_to_provider=None,
                 send_email_to_provider=None,
                 is_flexible=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_id = chat_id
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.start_parameter = start_parameter
        self.currency = currency
        self.prices = prices
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class answerShippingQuery(BaseMethod):
    """If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.

    Parameters
    ----------
    shipping_query_id : String
         Unique identifier for the query to be answered
    ok : Boolean
         Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
    shipping_options : Array of ShippingOption, optional
         Required if ok is True. A JSON-serialized array of available shipping options.
    error_message : String, optional
         Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.
    """

    def __init__(self, shipping_query_id,
                 ok,
                 shipping_options=None,
                 error_message=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.shipping_query_id = shipping_query_id
        self.ok = ok
        self.shipping_options = shipping_options
        self.error_message = error_message


class answerPreCheckoutQuery(BaseMethod):
    """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

    Parameters
    ----------
    pre_checkout_query_id : String
         Unique identifier for the query to be answered
    ok : Boolean
         Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.
    error_message : String, optional
         Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.
    """

    def __init__(self, pre_checkout_query_id,
                 ok,
                 error_message=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.pre_checkout_query_id = pre_checkout_query_id
        self.ok = ok
        self.error_message = error_message
