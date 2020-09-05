from .base import BaseMethod
from ..types import User, Message


class getMe(BaseMethod):

    response_type = User

    def __init__(self):
        super().__init__()


class sendMessage(BaseMethod):
    """Use this method to send text messages. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    text : String
         Text of the message to be sent, 1-4096 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the message text. See formatting options for more details.
    disable_web_page_preview : Boolean, optional
         Disables link previews for links in this message
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    response_type = Message

    def __init__(self, chat_id,
                 text,
                 parse_mode=None,
                 disable_web_page_preview=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.text = text
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class forwardMessage(BaseMethod):
    """Use this method to forward messages of any kind. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    from_chat_id : Integer or String
         Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    message_id : Integer
         Message identifier in the chat specified in from_chat_id
    """

    response_type = Message

    def __init__(self, chat_id,
                 from_chat_id,
                 message_id,
                 disable_notification=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.from_chat_id = from_chat_id
        self.disable_notification = disable_notification
        self.message_id = message_id


class sendPhoto(BaseMethod):
    """Use this method to send photos. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    photo : InputFile or String
         Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. More info on Sending Files �
    caption : String, optional
         Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the photo caption. See formatting options for more details.
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    response_type = Message

    def __init__(self, chat_id,
                 photo,
                 caption=None,
                 parse_mode=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.photo = photo
        self.caption = caption
        self.parse_mode = parse_mode
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendAudio(BaseMethod):
    """For sending voice messages, use the sendVoice method instead.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    audio : InputFile or String
         Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files �
    caption : String, optional
         Audio caption, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the audio caption. See formatting options for more details.
    duration : Integer, optional
         Duration of the audio in seconds
    performer : String, optional
         Performer
    title : String, optional
         Track name
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass �attach://<file_attach_name>� if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files �
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    response_type = Message

    def __init__(self, chat_id,
                 audio,
                 caption=None,
                 parse_mode=None,
                 duration=None,
                 performer=None,
                 title=None,
                 thumb=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.audio = audio
        self.caption = caption
        self.parse_mode = parse_mode
        self.duration = duration
        self.performer = performer
        self.title = title
        self.thumb = thumb
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendDocument(BaseMethod):
    """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    document : InputFile or String
         File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files �
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass �attach://<file_attach_name>� if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files �
    caption : String, optional
         Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the document caption. See formatting options for more details.
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    response_type = Message

    def __init__(self, chat_id,
                 document,
                 thumb=None,
                 caption=None,
                 parse_mode=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.document = document
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendVideo(BaseMethod):
    """Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    video : InputFile or String
         Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More info on Sending Files �
    duration : Integer, optional
         Duration of sent video in seconds
    width : Integer, optional
         Video width
    height : Integer, optional
         Video height
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass �attach://<file_attach_name>� if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files �
    caption : String, optional
         Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the video caption. See formatting options for more details.
    supports_streaming : Boolean, optional
         Pass True, if the uploaded video is suitable for streaming
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 video,
                 duration=None,
                 width=None,
                 height=None,
                 thumb=None,
                 caption=None,
                 parse_mode=None,
                 supports_streaming=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.video = video
        self.duration = duration
        self.width = width
        self.height = height
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.supports_streaming = supports_streaming
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendAnimation(BaseMethod):
    """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    animation : InputFile or String
         Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More info on Sending Files �
    duration : Integer, optional
         Duration of sent animation in seconds
    width : Integer, optional
         Animation width
    height : Integer, optional
         Animation height
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass �attach://<file_attach_name>� if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files �
    caption : String, optional
         Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the animation caption. See formatting options for more details.
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 animation,
                 duration=None,
                 width=None,
                 height=None,
                 thumb=None,
                 caption=None,
                 parse_mode=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.animation = animation
        self.duration = duration
        self.width = width
        self.height = height
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendVoice(BaseMethod):
    """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    voice : InputFile or String
         Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files �
    caption : String, optional
         Voice message caption, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the voice message caption. See formatting options for more details.
    duration : Integer, optional
         Duration of the voice message in seconds
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 voice,
                 caption=None,
                 parse_mode=None,
                 duration=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.voice = voice
        self.caption = caption
        self.parse_mode = parse_mode
        self.duration = duration
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendVideoNote(BaseMethod):
    """As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    video_note : InputFile or String
         Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More info on Sending Files �. Sending video notes by a URL is currently unsupported
    duration : Integer, optional
         Duration of sent video in seconds
    length : Integer, optional
         Video width and height, i.e. diameter of the video message
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass �attach://<file_attach_name>� if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files �
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 video_note,
                 duration=None,
                 length=None,
                 thumb=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.video_note = video_note
        self.duration = duration
        self.length = length
        self.thumb = thumb
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendMediaGroup(BaseMethod):
    """Use this method to send a group of photos or videos as an album. On success, an array of the sent Messages is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    media : Array of InputMediaPhoto and InputMediaVideo
         A JSON-serialized array describing photos and videos to be sent, must include 2-10 items
    disable_notification : Boolean, optional
         Sends the messages silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the messages are a reply, ID of the original message
    """

    def __init__(self, chat_id,
                 media,
                 disable_notification=None,
                 reply_to_message_id=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.media = media
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id


class sendLocation(BaseMethod):
    """Use this method to send point on the map. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    latitude : Float number
         Latitude of the location
    longitude : Float number
         Longitude of the location
    live_period : Integer, optional
         Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400.
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 latitude,
                 longitude,
                 live_period=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.latitude = latitude
        self.longitude = longitude
        self.live_period = live_period
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class editMessageLiveLocation(BaseMethod):
    """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message was sent by the bot, the edited Message is returned, otherwise True is returned.

    Parameters
    ----------
    chat_id : Integer or String, optional
         Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    message_id : Integer, optional
         Required if inline_message_id is not specified. Identifier of the message to edit
    inline_message_id : String, optional
         Required if chat_id and message_id are not specified. Identifier of the inline message
    latitude : Float number
         Latitude of new location
    longitude : Float number
         Longitude of new location
    reply_markup : InlineKeyboardMarkup, optional
         A JSON-serialized object for a new inline keyboard.
    """

    def __init__(self,
                 latitude,
                 longitude,
                 chat_id=None,
                 message_id=None,
                 inline_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.latitude = latitude
        self.longitude = longitude
        self.reply_markup = reply_markup


class stopMessageLiveLocation(BaseMethod):
    """Use this method to stop updating a live location message before live_period expires. On success, if the message was sent by the bot, the sent Message is returned, otherwise True is returned.

    Parameters
    ----------
    chat_id : Integer or String, optional
         Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    message_id : Integer, optional
         Required if inline_message_id is not specified. Identifier of the message with live location to stop
    inline_message_id : String, optional
         Required if chat_id and message_id are not specified. Identifier of the inline message
    reply_markup : InlineKeyboardMarkup, optional
         A JSON-serialized object for a new inline keyboard.
    """

    def __init__(self, chat_id=None,
                 message_id=None,
                 inline_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.reply_markup = reply_markup


class sendVenue(BaseMethod):
    """Use this method to send information about a venue. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    latitude : Float number
         Latitude of the venue
    longitude : Float number
         Longitude of the venue
    title : String
         Name of the venue
    address : String
         Address of the venue
    foursquare_id : String, optional
         Foursquare identifier of the venue
    foursquare_type : String, optional
         Foursquare type of the venue, if known. (For example, �arts_entertainment/default�, �arts_entertainment/aquarium� or �food/icecream�.)
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 latitude,
                 longitude,
                 title,
                 address,
                 foursquare_id=None,
                 foursquare_type=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendContact(BaseMethod):
    """Use this method to send phone contacts. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    phone_number : String
         Contact's phone number
    first_name : String
         Contact's first name
    last_name : String, optional
         Contact's last name
    vcard : String, optional
         Additional data about the contact in the form of a vCard, 0-2048 bytes
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 phone_number,
                 first_name,
                 last_name=None,
                 vcard=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendPoll(BaseMethod):
    """Use this method to send a native poll. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    question : String
         Poll question, 1-255 characters
    options : Array of String
         A JSON-serialized list of answer options, 2-10 strings 1-100 characters each
    is_anonymous : Boolean, optional
         True, if the poll needs to be anonymous, defaults to True
    type : String, optional
         Poll type, �quiz� or �regular�, defaults to �regular�
    allows_multiple_answers : Boolean, optional
         True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
    correct_option_id : Integer, optional
         0-based identifier of the correct answer option, required for polls in quiz mode
    explanation : String, optional
         Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
    explanation_parse_mode : String, optional
         Mode for parsing entities in the explanation. See formatting options for more details.
    open_period : Integer, optional
         Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
    close_date : Integer, optional
         Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period.
    is_closed : Boolean, optional
         Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 question,
                 options,
                 is_anonymous=None,
                 type=None,
                 allows_multiple_answers=None,
                 correct_option_id=None,
                 explanation=None,
                 explanation_parse_mode=None,
                 open_period=None,
                 close_date=None,
                 is_closed=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.question = question
        self.options = options
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_parse_mode = explanation_parse_mode
        self.open_period = open_period
        self.close_date = close_date
        self.is_closed = is_closed
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendDice(BaseMethod):
    """Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    emoji : String, optional
         Emoji on which the dice throw animation is based. Currently, must be one of ��, ��, or ��. Dice can have values 1-6 for �� and ��, and values 1-5 for ��. Defaults to ��
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 emoji=None,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.emoji = emoji
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class sendChatAction(BaseMethod):
    """We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    action : String
         Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_audio or upload_audio for audio files, upload_document for general files, find_location for location data, record_video_note or upload_video_note for video notes.
    """

    def __init__(self, chat_id,
                 action,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.action = action


class getUserProfilePhotos(BaseMethod):
    """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

    Parameters
    ----------
    user_id : Integer
         Unique identifier of the target user
    offset : Integer, optional
         Sequential number of the first photo to be returned. By default, all photos are returned.
    limit : Integer, optional
         Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.
    """

    def __init__(self, user_id,
                 offset=None,
                 limit=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.user_id = user_id
        self.offset = offset
        self.limit = limit


class getFile(BaseMethod):
    """Note: This function may not preserve the original file name and MIME type. You should save the file's MIME type and name (if available) when the File object is received.

    Parameters
    ----------
    file_id : String
         File identifier to get info about
    """

    def __init__(self, file_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.file_id = file_id


class kickChatMember(BaseMethod):
    """Use this method to kick a user from a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
    user_id : Integer
         Unique identifier of the target user
    until_date : Integer, optional
         Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever
    """

    def __init__(self, chat_id,
                 user_id,
                 until_date=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.user_id = user_id
        self.until_date = until_date


class unbanChatMember(BaseMethod):
    """Use this method to unban a previously kicked user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target group or username of the target supergroup or channel (in the format @username)
    user_id : Integer
         Unique identifier of the target user
    """

    def __init__(self, chat_id,
                 user_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.user_id = user_id


class restrictChatMember(BaseMethod):
    """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate admin rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    user_id : Integer
         Unique identifier of the target user
    permissions : ChatPermissions
         A JSON-serialized object for new user permissions
    until_date : Integer, optional
         Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
    """

    def __init__(self, chat_id,
                 user_id,
                 permissions,
                 until_date=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.user_id = user_id
        self.permissions = permissions
        self.until_date = until_date


class promoteChatMember(BaseMethod):
    """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Pass False for all boolean parameters to demote a user. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    user_id : Integer
         Unique identifier of the target user
    can_change_info : Boolean, optional
         Pass True, if the administrator can change chat title, photo and other settings
    can_post_messages : Boolean, optional
         Pass True, if the administrator can create channel posts, channels only
    can_edit_messages : Boolean, optional
         Pass True, if the administrator can edit messages of other users and can pin messages, channels only
    can_delete_messages : Boolean, optional
         Pass True, if the administrator can delete messages of other users
    can_invite_users : Boolean, optional
         Pass True, if the administrator can invite new users to the chat
    can_restrict_members : Boolean, optional
         Pass True, if the administrator can restrict, ban or unban chat members
    can_pin_messages : Boolean, optional
         Pass True, if the administrator can pin messages, supergroups only
    can_promote_members : Boolean, optional
         Pass True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him)
    """

    def __init__(self, chat_id,
                 user_id,
                 can_change_info=None,
                 can_post_messages=None,
                 can_edit_messages=None,
                 can_delete_messages=None,
                 can_invite_users=None,
                 can_restrict_members=None,
                 can_pin_messages=None,
                 can_promote_members=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.user_id = user_id
        self.can_change_info = can_change_info
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_invite_users = can_invite_users
        self.can_restrict_members = can_restrict_members
        self.can_pin_messages = can_pin_messages
        self.can_promote_members = can_promote_members

class setChatAdministratorCustomTitle(BaseMethod):
    """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    user_id : Integer
         Unique identifier of the target user
    custom_title : String
         New custom title for the administrator; 0-16 characters, emoji are not allowed
    """

    def __init__(self, chat_id,
                 user_id,
                 custom_title,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.user_id = user_id
        self.custom_title = custom_title


class setChatPermissions(BaseMethod):
    """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members admin rights. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    permissions : ChatPermissions
         New default chat permissions
    """

    def __init__(self, chat_id,
                 permissions,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.permissions = permissions


class exportChatInviteLink(BaseMethod):
    """Use this method to generate a new invite link for a chat; any previously generated link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns the new invite link as String on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    """

    def __init__(self, chat_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id


class setChatPhoto(BaseMethod):
    """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    photo : InputFile
         New chat photo, uploaded using multipart/form-data
    """

    def __init__(self, chat_id,
                 photo,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.photo = photo


class deleteChatPhoto(BaseMethod):
    """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    """

    def __init__(self, chat_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id


class setChatTitle(BaseMethod):
    """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    title : String
         New chat title, 1-255 characters
    """

    def __init__(self, chat_id,
                 title,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.title = title


class setChatDescription(BaseMethod):
    """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    description : String, optional
         New chat description, 0-255 characters
    """

    def __init__(self, chat_id,
                 description=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.description = description


class pinChatMessage(BaseMethod):
    """Use this method to pin a message in a group, a supergroup, or a channel. The bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' admin right in the supergroup or 'can_edit_messages' admin right in the channel. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    message_id : Integer
         Identifier of a message to pin
    disable_notification : Boolean, optional
         Pass True, if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels.
    """

    def __init__(self, chat_id,
                 message_id,
                 disable_notification=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.message_id = message_id
        self.disable_notification = disable_notification


class unpinChatMessage(BaseMethod):
    """Use this method to unpin a message in a group, a supergroup, or a channel. The bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' admin right in the supergroup or 'can_edit_messages' admin right in the channel. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    """

    def __init__(self, chat_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id


class leaveChat(BaseMethod):
    """Use this method for your bot to leave a group, supergroup or channel. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
    """

    def __init__(self, chat_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id


class getChat(BaseMethod):
    """Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
    """

    def __init__(self, chat_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id


class getChatAdministrators(BaseMethod):
    """Use this method to get a list of administrators in a chat. On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
    """

    def __init__(self, chat_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id


class getChatMembersCount(BaseMethod):
    """Use this method to get the number of members in a chat. Returns Int on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
    """

    def __init__(self, chat_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id


class getChatMember(BaseMethod):
    """Use this method to get information about a member of a chat. Returns a ChatMember object on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
    user_id : Integer
         Unique identifier of the target user
    """

    def __init__(self, chat_id,
                 user_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.user_id = user_id


class setChatStickerSet(BaseMethod):
    """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    sticker_set_name : String
         Name of the sticker set to be set as the group sticker set
    """

    def __init__(self, chat_id,
                 sticker_set_name,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id
        self.sticker_set_name = sticker_set_name


class deleteChatStickerSet(BaseMethod):
    """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    """

    def __init__(self, chat_id,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.chat_id = chat_id


class answerCallbackQuery(BaseMethod):
    """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.

    Parameters
    ----------
    callback_query_id : String
         Unique identifier for the query to be answered
    text : String, optional
         Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
    show_alert : Boolean, optional
         If true, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
    url : String, optional
         URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game � note that this will only work if the query comes from a callback_game button.Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.
    cache_time : Integer, optional
         The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.
    """

    def __init__(self, callback_query_id,
                 text=None,
                 show_alert=None,
                 url=None,
                 cache_time=None,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.callback_query_id = callback_query_id
        self.text = text
        self.show_alert = show_alert
        self.url = url
        self.cache_time = cache_time


class setMyCommands(BaseMethod):
    """Use this method to change the list of the bot's commands. Returns True on success.

    Parameters
    ----------
    commands : Array of BotCommand
         A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.
    """

    def __init__(self, commands,
                 propagate_values:bool=False):
        super().__init__(propagate_values=propagate_values)
        self.commands = commands
