from ..types import BaseType


class InlineQuery(BaseType):
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    Parameters
    ----------
    id : String
         Unique identifier for this query
    from : User
         Sender
    location : Location, optional
         Sender location, only for bots that request user location
    query : String
         Text of the query (up to 256 characters)
    offset : String
         Offset of the results to be returned, can be controlled by the bot
    """

    def __init__(self, id,
                 _from,
                 query,
                 offset,
                 location=None):
        super().__init__()
        self.id = id
        self._from = _from
        self.location = location
        self.query = query
        self.offset = offset


class InlineQueryResultArticle(BaseType):
    """Represents a link to an article or web page.

    Parameters
    ----------
    type : String
         Type of the result, must be article
    id : String
         Unique identifier for this result, 1-64 Bytes
    title : String
         Title of the result
    input_message_content : InputMessageContent
         Content of the message to be sent
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    url : String, optional
         URL of the result
    hide_url : Boolean, optional
         Pass True, if you don't want the URL to be shown in the message
    description : String, optional
         Short description of the result
    thumb_url : String, optional
         Url of the thumbnail for the result
    thumb_width : Integer, optional
         Thumbnail width
    thumb_height : Integer, optional
         Thumbnail height
    """

    def __init__(self, type,
                 id,
                 title,
                 input_message_content,
                 reply_markup=None,
                 url=None,
                 hide_url=None,
                 description=None,
                 thumb_url=None,
                 thumb_width=None,
                 thumb_height=None):
        super().__init__()
        self.type = type
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height


class InlineQueryResultPhoto(BaseType):
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    Parameters
    ----------
    type : String
         Type of the result, must be photo
    id : String
         Unique identifier for this result, 1-64 bytes
    photo_url : String
         A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB
    thumb_url : String
         URL of the thumbnail for the photo
    photo_width : Integer, optional
         Width of the photo
    photo_height : Integer, optional
         Height of the photo
    title : String, optional
         Title for the result
    description : String, optional
         Short description of the result
    caption : String, optional
         Caption of the photo to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the photo caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the photo
    """

    def __init__(self, type,
                 id,
                 photo_url,
                 thumb_url,
                 photo_width=None,
                 photo_height=None,
                 title=None,
                 description=None,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.photo_url = photo_url
        self.thumb_url = thumb_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultGif(BaseType):
    """Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Parameters
    ----------
    type : String
         Type of the result, must be gif
    id : String
         Unique identifier for this result, 1-64 bytes
    gif_url : String
         A valid URL for the GIF file. File size must not exceed 1MB
    gif_width : Integer, optional
         Width of the GIF
    gif_height : Integer, optional
         Height of the GIF
    gif_duration : Integer, optional
         Duration of the GIF
    thumb_url : String
         URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    thumb_mime_type : String, optional
         MIME type of the thumbnail, must be one of �image/jpeg�, �image/gif�, or �video/mp4�. Defaults to �image/jpeg�
    title : String, optional
         Title for the result
    caption : String, optional
         Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the GIF animation
    """

    def __init__(self, type,
                 id,
                 thumb_url,
                 gif_url,
                 gif_width=None,
                 gif_height=None,
                 gif_duration=None,
                 thumb_mime_type=None,
                 title=None,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.gif_url = gif_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.thumb_url = thumb_url
        self.thumb_mime_type = thumb_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultMpeg4Gif(BaseType):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Parameters
    ----------
    type : String
         Type of the result, must be mpeg4_gif
    id : String
         Unique identifier for this result, 1-64 bytes
    mpeg4_url : String
         A valid URL for the MP4 file. File size must not exceed 1MB
    mpeg4_width : Integer, optional
         Video width
    mpeg4_height : Integer, optional
         Video height
    mpeg4_duration : Integer, optional
         Video duration
    thumb_url : String
         URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    thumb_mime_type : String, optional
         MIME type of the thumbnail, must be one of �image/jpeg�, �image/gif�, or �video/mp4�. Defaults to �image/jpeg�
    title : String, optional
         Title for the result
    caption : String, optional
         Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the video animation
    """

    def __init__(self, type,
                 id,
                 thumb_url,
                 mpeg4_url,
                 mpeg4_width=None,
                 mpeg4_height=None,
                 mpeg4_duration=None,
                 thumb_mime_type=None,
                 title=None,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.mpeg4_url = mpeg4_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.thumb_url = thumb_url
        self.thumb_mime_type = thumb_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVideo(BaseType):
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    Parameters
    ----------
    type : String
         Type of the result, must be video
    id : String
         Unique identifier for this result, 1-64 bytes
    video_url : String
         A valid URL for the embedded video player or video file
    mime_type : String
         Mime type of the content of video url, �text/html� or �video/mp4�
    thumb_url : String
         URL of the thumbnail (jpeg only) for the video
    title : String
         Title for the result
    caption : String, optional
         Caption of the video to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the video caption. See formatting options for more details.
    video_width : Integer, optional
         Video width
    video_height : Integer, optional
         Video height
    video_duration : Integer, optional
         Video duration in seconds
    description : String, optional
         Short description of the result
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
    """

    def __init__(self, type,
                 id,
                 video_url,
                 mime_type,
                 thumb_url,
                 title,
                 caption=None,
                 parse_mode=None,
                 video_width=None,
                 video_height=None,
                 video_duration=None,
                 description=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumb_url = thumb_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultAudio(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be audio
    id : String
         Unique identifier for this result, 1-64 bytes
    audio_url : String
         A valid URL for the audio file
    title : String
         Title
    caption : String, optional
         Caption, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the audio caption. See formatting options for more details.
    performer : String, optional
         Performer
    audio_duration : Integer, optional
         Audio duration in seconds
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the audio
    """

    def __init__(self, type,
                 id,
                 audio_url,
                 title,
                 caption=None,
                 parse_mode=None,
                 performer=None,
                 audio_duration=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVoice(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be voice
    id : String
         Unique identifier for this result, 1-64 bytes
    voice_url : String
         A valid URL for the voice recording
    title : String
         Recording title
    caption : String, optional
         Caption, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the voice message caption. See formatting options for more details.
    voice_duration : Integer, optional
         Recording duration in seconds
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the voice recording
    """

    def __init__(self, type,
                 id,
                 voice_url,
                 title,
                 caption=None,
                 parse_mode=None,
                 voice_duration=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultDocument(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be document
    id : String
         Unique identifier for this result, 1-64 bytes
    title : String
         Title for the result
    caption : String, optional
         Caption of the document to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the document caption. See formatting options for more details.
    document_url : String
         A valid URL for the file
    mime_type : String
         Mime type of the content of the file, either �application/pdf� or �application/zip�
    description : String, optional
         Short description of the result
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the file
    thumb_url : String, optional
         URL of the thumbnail (jpeg only) for the file
    thumb_width : Integer, optional
         Thumbnail width
    thumb_height : Integer, optional
         Thumbnail height
    """

    def __init__(self, type,
                 id,
                 title,
                 document_url,
                 mime_type,
                 caption=None,
                 parse_mode=None,
                 description=None,
                 reply_markup=None,
                 input_message_content=None,
                 thumb_url=None,
                 thumb_width=None,
                 thumb_height=None):
        super().__init__()
        self.type = type
        self.id = id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.document_url = document_url
        self.mime_type = mime_type
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height


class InlineQueryResultLocation(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be location
    id : String
         Unique identifier for this result, 1-64 Bytes
    latitude : Float number
         Location latitude in degrees
    longitude : Float number
         Location longitude in degrees
    title : String
         Location title
    live_period : Integer, optional
         Period in seconds for which the location can be updated, should be between 60 and 86400.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the location
    thumb_url : String, optional
         Url of the thumbnail for the result
    thumb_width : Integer, optional
         Thumbnail width
    thumb_height : Integer, optional
         Thumbnail height
    """

    def __init__(self, type,
                 id,
                 latitude,
                 longitude,
                 title,
                 live_period=None,
                 reply_markup=None,
                 input_message_content=None,
                 thumb_url=None,
                 thumb_width=None,
                 thumb_height=None):
        super().__init__()
        self.type = type
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.live_period = live_period
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height


class InlineQueryResultVenue(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be venue
    id : String
         Unique identifier for this result, 1-64 Bytes
    latitude : Float
         Latitude of the venue location in degrees
    longitude : Float
         Longitude of the venue location in degrees
    title : String
         Title of the venue
    address : String
         Address of the venue
    foursquare_id : String, optional
         Foursquare identifier of the venue if known
    foursquare_type : String, optional
         Foursquare type of the venue, if known. (For example, �arts_entertainment/default�, �arts_entertainment/aquarium� or �food/icecream�.)
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the venue
    thumb_url : String, optional
         Url of the thumbnail for the result
    thumb_width : Integer, optional
         Thumbnail width
    thumb_height : Integer, optional
         Thumbnail height
    """

    def __init__(self, type,
                 id,
                 latitude,
                 longitude,
                 title,
                 address,
                 foursquare_id=None,
                 foursquare_type=None,
                 reply_markup=None,
                 input_message_content=None,
                 thumb_url=None,
                 thumb_width=None,
                 thumb_height=None):
        super().__init__()
        self.type = type
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height


class InlineQueryResultContact(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be contact
    id : String
         Unique identifier for this result, 1-64 Bytes
    phone_number : String
         Contact's phone number
    first_name : String
         Contact's first name
    last_name : String, optional
         Contact's last name
    vcard : String, optional
         Additional data about the contact in the form of a vCard, 0-2048 bytes
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the contact
    thumb_url : String, optional
         Url of the thumbnail for the result
    thumb_width : Integer, optional
         Thumbnail width
    thumb_height : Integer, optional
         Thumbnail height
    """

    def __init__(self, type,
                 id,
                 phone_number,
                 first_name,
                 last_name=None,
                 vcard=None,
                 reply_markup=None,
                 input_message_content=None,
                 thumb_url=None,
                 thumb_width=None,
                 thumb_height=None):
        super().__init__()
        self.type = type
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height


class InlineQueryResultGame(BaseType):
    """Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

    Parameters
    ----------
    type : String
         Type of the result, must be game
    id : String
         Unique identifier for this result, 1-64 bytes
    game_short_name : String
         Short name of the game
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    """

    def __init__(self, type,
                 id,
                 game_short_name,
                 reply_markup=None):
        super().__init__()
        self.type = type
        self.id = id
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup


class InlineQueryResultCachedPhoto(BaseType):
    """Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    Parameters
    ----------
    type : String
         Type of the result, must be photo
    id : String
         Unique identifier for this result, 1-64 bytes
    photo_file_id : String
         A valid file identifier of the photo
    title : String, optional
         Title for the result
    description : String, optional
         Short description of the result
    caption : String, optional
         Caption of the photo to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the photo caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the photo
    """

    def __init__(self, type,
                 id,
                 photo_file_id,
                 title=None,
                 description=None,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedGif(BaseType):
    """Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    Parameters
    ----------
    type : String
         Type of the result, must be gif
    id : String
         Unique identifier for this result, 1-64 bytes
    gif_file_id : String
         A valid file identifier for the GIF file
    title : String, optional
         Title for the result
    caption : String, optional
         Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the GIF animation
    """

    def __init__(self, type,
                 id,
                 gif_file_id,
                 title=None,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedMpeg4Gif(BaseType):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Parameters
    ----------
    type : String
         Type of the result, must be mpeg4_gif
    id : String
         Unique identifier for this result, 1-64 bytes
    mpeg4_file_id : String
         A valid file identifier for the MP4 file
    title : String, optional
         Title for the result
    caption : String, optional
         Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the video animation
    """

    def __init__(self, type,
                 id,
                 mpeg4_file_id,
                 title=None,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedSticker(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be sticker
    id : String
         Unique identifier for this result, 1-64 bytes
    sticker_file_id : String
         A valid file identifier of the sticker
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the sticker
    """

    def __init__(self, type,
                 id,
                 sticker_file_id,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedDocument(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be document
    id : String
         Unique identifier for this result, 1-64 bytes
    title : String
         Title for the result
    document_file_id : String
         A valid file identifier for the file
    description : String, optional
         Short description of the result
    caption : String, optional
         Caption of the document to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the document caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the file
    """

    def __init__(self, type,
                 id,
                 title,
                 document_file_id,
                 description=None,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVideo(BaseType):
    """Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    Parameters
    ----------
    type : String
         Type of the result, must be video
    id : String
         Unique identifier for this result, 1-64 bytes
    video_file_id : String
         A valid file identifier for the video file
    title : String
         Title for the result
    description : String, optional
         Short description of the result
    caption : String, optional
         Caption of the video to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the video caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the video
    """

    def __init__(self, type,
                 id,
                 video_file_id,
                 title,
                 description=None,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVoice(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be voice
    id : String
         Unique identifier for this result, 1-64 bytes
    voice_file_id : String
         A valid file identifier for the voice message
    title : String
         Voice message title
    caption : String, optional
         Caption, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the voice message caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the voice message
    """

    def __init__(self, type,
                 id,
                 voice_file_id,
                 title,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedAudio(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Parameters
    ----------
    type : String
         Type of the result, must be audio
    id : String
         Unique identifier for this result, 1-64 bytes
    audio_file_id : String
         A valid file identifier for the audio file
    caption : String, optional
         Caption, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the audio caption. See formatting options for more details.
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message
    input_message_content : InputMessageContent, optional
         Content of the message to be sent instead of the audio
    """

    def __init__(self, type,
                 id,
                 audio_file_id,
                 caption=None,
                 parse_mode=None,
                 reply_markup=None,
                 input_message_content=None):
        super().__init__()
        self.type = type
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InputTextMessageContent(BaseType):
    """Represents the content of a text message to be sent as the result of an inline query.

    Parameters
    ----------
    message_text : String
         Text of the message to be sent, 1-4096 characters
    parse_mode : String, optional
         Mode for parsing entities in the message text. See formatting options for more details.
    disable_web_page_preview : Boolean, optional
         Disables link previews for links in the sent message
    """

    def __init__(self, message_text,
                 parse_mode=None,
                 disable_web_page_preview=None):
        super().__init__()
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview


class InputLocationMessageContent(BaseType):
    """Represents the content of a location message to be sent as the result of an inline query.

    Parameters
    ----------
    latitude : Float
         Latitude of the location in degrees
    longitude : Float
         Longitude of the location in degrees
    live_period : Integer, optional
         Period in seconds for which the location can be updated, should be between 60 and 86400.
    """

    def __init__(self, latitude,
                 longitude,
                 live_period=None):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.live_period = live_period


class InputVenueMessageContent(BaseType):
    """Represents the content of a venue message to be sent as the result of an inline query.

    Parameters
    ----------
    latitude : Float
         Latitude of the venue in degrees
    longitude : Float
         Longitude of the venue in degrees
    title : String
         Name of the venue
    address : String
         Address of the venue
    foursquare_id : String, optional
         Foursquare identifier of the venue, if known
    foursquare_type : String, optional
         Foursquare type of the venue, if known. (For example, �arts_entertainment/default�, �arts_entertainment/aquarium� or �food/icecream�.)
    """

    def __init__(self, latitude,
                 longitude,
                 title,
                 address,
                 foursquare_id=None,
                 foursquare_type=None):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type


class InputContactMessageContent(BaseType):
    """Represents the content of a contact message to be sent as the result of an inline query.

    Parameters
    ----------
    phone_number : String
         Contact's phone number
    first_name : String
         Contact's first name
    last_name : String, optional
         Contact's last name
    vcard : String, optional
         Additional data about the contact in the form of a vCard, 0-2048 bytes
    """

    def __init__(self, phone_number,
                 first_name,
                 last_name=None,
                 vcard=None):
        super().__init__()
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard


class ChosenInlineResult(BaseType):
    """Note: It is necessary to enable inline feedback via @Botfather in order to receive these objects in updates.

    Parameters
    ----------
    result_id : String
         The unique identifier for the result that was chosen
    from : User
         The user that chose the result
    location : Location, optional
         Sender location, only for bots that require user location
    inline_message_id : String, optional
         Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
    query : String
         The query that was used to obtain the result
    """

    def __init__(self, result_id,
                 _from,
                 query,
                 location=None,
                 inline_message_id=None):
        super().__init__()
        self.result_id = result_id
        self._from = _from
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query


