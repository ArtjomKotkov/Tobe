from ..types import BaseType, User


class LabeledPrice(BaseType):
    """This object represents a portion of the price for goods or services.

    Parameters
    ----------
    label : String
         Portion label
    amount : Integer
         Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """

    def __init__(self,
                 label,
                 amount):
        super().__init__()
        self.label = label
        self.amount = amount


class Invoice(BaseType):
    """This object contains basic information about an invoice.

    Parameters
    ----------
    title : String
         Product name
    description : String
         Product description
    start_parameter : String
         Unique bot deep-linking parameter that can be used to generate this invoice
    currency : String
         Three-letter ISO 4217 currency code
    total_amount : Integer
         Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """

    def __init__(self,
                 title,
                 description,
                 start_parameter,
                 currency,
                 total_amount):
        super().__init__()
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = ShippingAddress.parse(total_amount)


class ShippingAddress(BaseType):
    """This object represents a shipping address.

    Parameters
    ----------
    country_code : String
         ISO 3166-1 alpha-2 country code
    state : String
         State, if applicable
    city : String
         City
    street_line1 : String
         First line for the address
    street_line2 : String
         Second line for the address
    post_code : String
         Address post code
    """

    def __init__(self,
                 country_code,
                 state,
                 city,
                 street_line1,
                 street_line2,
                 post_code):
        super().__init__()
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code


class OrderInfo(BaseType):
    """This object represents information about an order.

    Parameters
    ----------
    name : String, optional
         User name
    phone_number : String, optional
         User's phone number
    email : String, optional
         User email
    shipping_address : ShippingAddress, optional
         User shipping address
    """

    def __init__(self,
                 name=None,
                 phone_number=None,
                 email=None,
                 shipping_address=None):
        super().__init__()
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = ShippingAddress.parse(shipping_address)


class ShippingOption(BaseType):
    """This object represents one shipping option.

    Parameters
    ----------
    id : String
         Shipping option identifier
    title : String
         Option title
    prices : Array of LabeledPrice
         List of price portions
    """

    def __init__(self,
                 id,
                 title,
                 prices):
        super().__init__()
        self.id = id
        self.title = title
        self.prices = LabeledPrice.parse(prices)


class SuccessfulPayment(BaseType):
    """This object contains basic information about a successful payment.

    Parameters
    ----------
    currency : String
         Three-letter ISO 4217 currency code
    total_amount : Integer
         Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    invoice_payload : String
         Bot specified invoice payload
    shipping_option_id : String, optional
         Identifier of the shipping option chosen by the user
    order_info : OrderInfo, optional
         Order info provided by the user
    telegram_payment_charge_id : String
         Telegram payment identifier
    provider_payment_charge_id : String
         Provider payment identifier
    """

    def __init__(self, currency,
                 total_amount,
                 invoice_payload,
                 telegram_payment_charge_id,
                 provider_payment_charge_id,
                 shipping_option_id=None,
                 order_info=None):
        super().__init__()
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = OrderInfo.parse(order_info)
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id


class ShippingQuery(BaseType):
    """This object contains information about an incoming shipping query.

    Parameters
    ----------
    id : String
         Unique query identifier
    from : User
         User who sent the query
    invoice_payload : String
         Bot specified invoice payload
    shipping_address : ShippingAddress
         User specified shipping address
    """

    def __init__(self,
                 id,
                 _from,
                 invoice_payload,
                 shipping_address):
        super().__init__()
        self.id = id
        self._from = User.parse(_from)
        self.invoice_payload = invoice_payload
        self.shipping_address = ShippingAddress.parse(shipping_address)


class PreCheckoutQuery(BaseType):
    """This object contains information about an incoming pre-checkout query.

    Parameters
    ----------
    id : String
         Unique query identifier
    from : User
         User who sent the query
    currency : String
         Three-letter ISO 4217 currency code
    total_amount : Integer
         Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    invoice_payload : String
         Bot specified invoice payload
    shipping_option_id : String, optional
         Identifier of the shipping option chosen by the user
    order_info : OrderInfo, optional
         Order info provided by the user
    """

    def __init__(self, id,
                 _from,
                 currency,
                 total_amount,
                 invoice_payload,
                 shipping_option_id=None,
                 order_info=None):
        super().__init__()
        self.id = id
        self._from = User.parse(_from)
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = OrderInfo.parse(order_info)
