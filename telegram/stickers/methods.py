from ..methods import BaseMethod


class sendSticker(BaseMethod):
    """Use this method to send static .WEBP or animated .TGS stickers. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer or String
         Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    sticker : InputFile or String
         Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files �
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, optional
         Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    def __init__(self, chat_id,
                 sticker,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None):
        super().__init__()
        self.chat_id = chat_id
        self.sticker = sticker
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class getStickerSet(BaseMethod):
    """Use this method to get a sticker set. On success, a StickerSet object is returned.

    Parameters
    ----------
    name : String
         Name of the sticker set
    """

    def __init__(self, name):
        super().__init__()
        self.name = name


class uploadStickerFile(BaseMethod):
    """Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success.

    Parameters
    ----------
    user_id : Integer
         User identifier of sticker file owner
    png_sticker : InputFile
         PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. More info on Sending Files �
    """

    def __init__(self, user_id,
                 png_sticker):
        super().__init__()
        self.user_id = user_id
        self.png_sticker = png_sticker


class createNewStickerSet(BaseMethod):
    """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker or tgs_sticker. Returns True on success.

    Parameters
    ----------
    user_id : Integer
         User identifier of created sticker set owner
    name : String
         Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only english letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in �_by_<bot username>�. <bot_username> is case insensitive. 1-64 characters.
    title : String
         Sticker set title, 1-64 characters
    png_sticker : InputFile or String, optional
         PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files �
    tgs_sticker : InputFile, optional
         TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
    emojis : String
         One or more emoji corresponding to the sticker
    contains_masks : Boolean, optional
         Pass True, if a set of mask stickers should be created
    mask_position : MaskPosition, optional
         A JSON-serialized object for position where the mask should be placed on faces
    """

    def __init__(self, user_id,
                 name,
                 title,
                 emojis,
                 png_sticker=None,
                 tgs_sticker=None,
                 contains_masks=None,
                 mask_position=None):
        super().__init__()
        self.user_id = user_id
        self.name = name
        self.title = title
        self.png_sticker = png_sticker
        self.tgs_sticker = tgs_sticker
        self.emojis = emojis
        self.contains_masks = contains_masks
        self.mask_position = mask_position


class addStickerToSet(BaseMethod):
    """Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker or tgs_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success.

    Parameters
    ----------
    user_id : Integer
         User identifier of sticker set owner
    name : String
         Sticker set name
    png_sticker : InputFile or String, optional
         PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files �
    tgs_sticker : InputFile, optional
         TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
    emojis : String
         One or more emoji corresponding to the sticker
    mask_position : MaskPosition, optional
         A JSON-serialized object for position where the mask should be placed on faces
    """

    def __init__(self, user_id,
                 name,
                 emojis,
                 png_sticker=None,
                 tgs_sticker=None,
                 mask_position=None):
        super().__init__()
        self.user_id = user_id
        self.name = name
        self.png_sticker = png_sticker
        self.tgs_sticker = tgs_sticker
        self.emojis = emojis
        self.mask_position = mask_position


class setStickerPositionInSet(BaseMethod):
    """Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.

    Parameters
    ----------
    sticker : String
         File identifier of the sticker
    position : Integer
         New sticker position in the set, zero-based
    """

    def __init__(self, sticker,
                 position):
        super().__init__()
        self.sticker = sticker
        self.position = position


class deleteStickerFromSet(BaseMethod):
    """Use this method to delete a sticker from a set created by the bot. Returns True on success.

    Parameters
    ----------
    sticker : String
         File identifier of the sticker
    """

    def __init__(self, sticker):
        super().__init__()
        self.sticker = sticker


class setStickerSetThumb(BaseMethod):
    """Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Returns True on success.

    Parameters
    ----------
    name : String
         Sticker set name
    user_id : Integer
         User identifier of the sticker set owner
    thumb : InputFile or String, optional
         A PNG image with the thumbnail, must be up to 128 kilobytes in size and have width and height exactly 100px, or a TGS animation with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/animated_stickers#technical-requirements for animated sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files �. Animated sticker set thumbnail can't be uploaded via HTTP URL.
    """

    def __init__(self, name,
                 user_id,
                 thumb=None):
        super().__init__()
        self.name = name
        self.user_id = user_id
        self.thumb = thumb