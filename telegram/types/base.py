from abc import ABC
import json


from ..services import fix_built_ins



class BaseType(ABC):

    status = True

    def serialize(self):
        return json.dumps(self.__dict__)

    @classmethod
    def parse(cls, response, iterable=False):
        """Parse data from response, fix built in names

            Returns:
                Type instance.
        """
        if iterable:
            return [cls(**fix_built_ins(part)) for part in response] if response else None
        else:
            return cls(**fix_built_ins(response)) if response else None


class Error(BaseType):
    """Error type class."""

    status = False

    def __init__(self, ok, error_code, description):
        self.status = ok
        self.error_code = error_code
        self.description = description



class User(BaseType):
    """This object represents a Telegram user or bot.

    Parameters
    ----------
    id : Integer
         Unique identifier for this user or bot
    is_bot : Boolean
         True, if this user is a bot
    first_name : String
         User's or bot's first name
    last_name : String, optional
         User's or bot's last name
    username : String, optional
         User's or bot's username
    language_code : String, optional
         IETF language tag of the user's language
    can_join_groups : Boolean, optional
         True, if the bot can be invited to groups. Returned only in getMe.
    can_read_all_group_messages : Boolean, optional
         True, if privacy mode is disabled for the bot. Returned only in getMe.
    supports_inline_queries : Boolean, optional
         True, if the bot supports inline queries. Returned only in getMe.
    """

    def __init__(self, id,
                 is_bot,
                 first_name,
                 last_name=None,
                 username=None,
                 language_code=None,
                 can_join_groups=None,
                 can_read_all_group_messages=None,
                 supports_inline_queries=None):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries


class Chat(BaseType):
    """This object represents a chat.

    Parameters
    ----------
    id : Integer
         Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    type : String
         Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    title : String, optional
         Title, for supergroups, channels and group chats
    username : String, optional
         Username, for private chats, supergroups and channels if available
    first_name : String, optional
         First name of the other party in a private chat
    last_name : String, optional
         Last name of the other party in a private chat
    photo : ChatPhoto, optional
         Chat photo. Returned only in getChat.
    description : String, optional
         Description, for groups, supergroups and channel chats. Returned only in getChat.
    invite_link : String, optional
         Chat invite link, for groups, supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using exportChatInviteLink. Returned only in getChat.
    pinned_message : Message, optional
         Pinned message, for groups, supergroups and channels. Returned only in getChat.
    permissions : ChatPermissions, optional
         Default chat member permissions, for groups and supergroups. Returned only in getChat.
    slow_mode_delay : Integer, optional
         For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat.
    sticker_set_name : String, optional
         For supergroups, name of group sticker set. Returned only in getChat.
    can_set_sticker_set : Boolean, optional
         True, if the bot can change the group sticker set. Returned only in getChat.
    """

    def __init__(self, id,
                 _type,
                 title=None,
                 username=None,
                 first_name=None,
                 last_name=None,
                 photo=None,
                 description=None,
                 invite_link=None,
                 pinned_message=None,
                 permissions=None,
                 slow_mode_delay=None,
                 sticker_set_name=None,
                 can_set_sticker_set=None):
        self.id = id
        self._type = _type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.photo = ChatPhoto.parse(photo)
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = Message.parse(pinned_message)
        self.permissions = ChatPermissions.parse(permissions)
        self.slow_mode_delay = slow_mode_delay
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set


class Message(BaseType):
    """This object represents a message.

    Parameters
    ----------
    message_id : Integer
         Unique message identifier inside this chat
    _from : User, optional
         Sender, empty for messages sent to channels
    date : Integer
         Date the message was sent in Unix time
    chat : Chat
         Conversation the message belongs to
    forward_from : User, optional
         For forwarded messages, sender of the original message
    forward_from_chat : Chat, optional
         For messages forwarded from channels, information about the original channel
    forward_from_message_id : Integer, optional
         For messages forwarded from channels, identifier of the original message in the channel
    forward_signature : String, optional
         For messages forwarded from channels, signature of the post author if present
    forward_sender_name : String, optional
         Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    forward_date : Integer, optional
         For forwarded messages, date the original message was sent in Unix time
    reply_to_message : Message, optional
         For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    via_bot : User, optional
         Bot through which the message was sent
    edit_date : Integer, optional
         Date the message was last edited in Unix time
    media_group_id : String, optional
         The unique identifier of a media message group this message belongs to
    author_signature : String, optional
         Signature of the post author for messages in channels
    text : String, optional
         For text messages, the actual UTF-8 text of the message, 0-4096 characters
    entities : Array of MessageEntity, optional
         For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    animation : Animation, optional
         Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
    audio : Audio, optional
         Message is an audio file, information about the file
    document : Document, optional
         Message is a general file, information about the file
    photo : Array of PhotoSize, optional
         Message is a photo, available sizes of the photo
    sticker : Sticker, optional
         Message is a sticker, information about the sticker
    video : Video, optional
         Message is a video, information about the video
    video_note : VideoNote, optional
         Message is a video note, information about the video message
    voice : Voice, optional
         Message is a voice message, information about the file
    caption : String, optional
         Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    caption_entities : Array of MessageEntity, optional
         For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    contact : Contact, optional
         Message is a shared contact, information about the contact
    dice : Dice, optional
         Message is a dice with random value from 1 to 6
    game : Game, optional
         Message is a game, information about the game. More about games »
    poll : Poll, optional
         Message is a native poll, information about the poll
    venue : Venue, optional
         Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
    location : Location, optional
         Message is a shared location, information about the location
    new_chat_members : Array of User, optional
         New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    left_chat_member : User, optional
         A member was removed from the group, information about them (this member may be the bot itself)
    new_chat_title : String, optional
         A chat title was changed to this value
    new_chat_photo : Array of PhotoSize, optional
         A chat photo was change to this value
    delete_chat_photo : True, optional
         Service message: the chat photo was deleted
    group_chat_created : True, optional
         Service message: the group has been created
    supergroup_chat_created : True, optional
         Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    channel_chat_created : True, optional
         Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    migrate_to_chat_id : Integer, optional
         The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    migrate_from_chat_id : Integer, optional
         The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    pinned_message : Message, optional
         Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
    invoice : Invoice, optional
         Message is an invoice for a payment, information about the invoice. More about payments »
    successful_payment : SuccessfulPayment, optional
         Message is a service message about a successful payment, information about the payment. More about payments »
    connected_website : String, optional
         The domain name of the website on which the user has logged in. More about Telegram Login »
    passport_data : PassportData, optional
         Telegram Passport data
    reply_markup : InlineKeyboardMarkup, optional
         Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    """

    def __init__(self, message_id,
                 date,
                 chat,
                 _from=None,
                 forward_from=None,
                 forward_from_chat=None,
                 forward_from_message_id=None,
                 forward_signature=None,
                 forward_sender_name=None,
                 forward_date=None,
                 reply_to_message=None,
                 via_bot=None,
                 edit_date=None,
                 media_group_id=None,
                 author_signature=None,
                 text=None,
                 entities=None,
                 animation=None,
                 audio=None,
                 document=None,
                 photo=None,
                 sticker=None,
                 video=None,
                 video_note=None,
                 voice=None,
                 caption=None,
                 caption_entities=None,
                 contact=None,
                 dice=None,
                 game=None,
                 poll=None,
                 venue=None,
                 location=None,
                 new_chat_members=None,
                 left_chat_member=None,
                 new_chat_title=None,
                 new_chat_photo=None,
                 delete_chat_photo=None,
                 group_chat_created=None,
                 supergroup_chat_created=None,
                 channel_chat_created=None,
                 migrate_to_chat_id=None,
                 migrate_from_chat_id=None,
                 pinned_message=None,
                 invoice=None,
                 successful_payment=None,
                 connected_website=None,
                 passport_data=None,
                 reply_markup=None):
        self.message_id = message_id
        self._from = User.parse(_from)
        self.date = date
        self.chat = Chat.parse(chat)
        self.forward_from = User.parse(forward_from)
        self.forward_from_chat = Chat.parse(forward_from_chat)
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.reply_to_message = Message.parse(reply_to_message)
        self.via_bot = User.parse(via_bot)
        self.edit_date = edit_date
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = MessageEntity.parse(entities, iterable=True)
        self.animation = Animation.parse(animation)
        self.audio = Audio.parse(audio)
        self.document = Document.parse(document)
        self.photo = PhotoSize.parse(photo, iterable=True)
        self.sticker = sticker # <-Sticker
        self.video = Video.parse(video)
        self.video_note = MessageEntity.parse(video_note, iterable=True)
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.contact = Contact.parse(contact)
        self.dice = Dice.parse(dice)
        self.game = game # <-Game
        self.poll = Poll.parse(poll)
        self.venue = Venue.parse(venue)
        self.location = Location.parse(location)
        self.new_chat_members = User.parse(new_chat_members, iterable=True)
        self.left_chat_member = User.parse(left_chat_member)
        self.new_chat_title = new_chat_title
        self.new_chat_photo = PhotoSize.parse(new_chat_photo, iterable=True)
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = Message.parse(pinned_message)
        self.invoice = invoice # <- Invoice
        self.successful_payment = successful_payment # <- successful_payment
        self.connected_website = connected_website
        self.passport_data = passport_data # <- passport_data
        self.reply_markup = InlineKeyboardMarkup.parse(reply_markup)


class MessageEntity(BaseType):
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    Parameters
    ----------
    _type : String
         Type of the entity. Can be “mention” (@username), “hashtag” (#hashtag), “cashtag” ($USD), “bot_command” (/start@jobs_bot), “url” (https://telegram.org), “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123), “bold” (bold text), “italic” (italic text), “underline” (underlined text), “strikethrough” (strikethrough text), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames)
    offset : Integer
         Offset in UTF-16 code units to the start of the entity
    length : Integer
         Length of the entity in UTF-16 code units
    url : String, optional
         For “text_link” only, url that will be opened after user taps on the text
    user : User, optional
         For “text_mention” only, the mentioned user
    language : String, optional
         For “pre” only, the programming language of the entity text
    """

    def __init__(self, _type,
                 offset,
                 length,
                 url=None,
                 user=None,
                 language=None):
        self.type = _type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = User.parse(user)
        self.language = language


class PhotoSize(BaseType):
    """This object represents one size of a photo or a file / sticker thumbnail.

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    width : Integer
         Photo width
    height : Integer
         Photo height
    file_size : Integer, optional
         File size
    """

    def __init__(self, file_id,
                 file_unique_id,
                 width,
                 height,
                 file_size=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size


class Animation(BaseType):
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    width : Integer
         Video width as defined by sender
    height : Integer
         Video height as defined by sender
    duration : Integer
         Duration of the video in seconds as defined by sender
    thumb : PhotoSize, optional
         Animation thumbnail as defined by sender
    file_name : String, optional
         Original animation filename as defined by sender
    mime_type : String, optional
         MIME type of the file as defined by sender
    file_size : Integer, optional
         File size
    """

    def __init__(self, file_id,
                 file_unique_id,
                 width,
                 height,
                 duration,
                 thumb=None,
                 file_name=None,
                 mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = PhotoSize.parse(thumb)
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Audio(BaseType):
    """This object represents an audio file to be treated as music by the Telegram clients.

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    duration : Integer
         Duration of the audio in seconds as defined by sender
    performer : String, optional
         Performer of the audio as defined by sender or by audio tags
    title : String, optional
         Title of the audio as defined by sender or by audio tags
    mime_type : String, optional
         MIME type of the file as defined by sender
    file_size : Integer, optional
         File size
    thumb : PhotoSize, optional
         Thumbnail of the album cover to which the music file belongs
    """

    def __init__(self, file_id,
                 file_unique_id,
                 duration,
                 performer=None,
                 title=None,
                 mime_type=None,
                 file_size=None,
                 thumb=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumb = PhotoSize.parse(thumb)


class Document(BaseType):
    """This object represents a general file (as opposed to photos, voice messages and audio files).

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    thumb : PhotoSize, optional
         Document thumbnail as defined by sender
    file_name : String, optional
         Original filename as defined by sender
    mime_type : String, optional
         MIME type of the file as defined by sender
    file_size : Integer, optional
         File size
    """

    def __init__(self, file_id,
                 file_unique_id,
                 thumb=None,
                 file_name=None,
                 mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumb = PhotoSize.parse(thumb)
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Video(BaseType):
    """This object represents a video file.

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    width : Integer
         Video width as defined by sender
    height : Integer
         Video height as defined by sender
    duration : Integer
         Duration of the video in seconds as defined by sender
    thumb : PhotoSize, optional
         Video thumbnail
    mime_type : String, optional
         Mime type of a file as defined by sender
    file_size : Integer, optional
         File size
    """

    def __init__(self, file_id,
                 file_unique_id,
                 width,
                 height,
                 duration,
                 thumb=None,
                 mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = PhotoSize.parse(thumb)
        self.mime_type = mime_type
        self.file_size = file_size


class VideoNote(BaseType):
    """This object represents a video message (available in Telegram apps as of v.4.0).

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    length : Integer
         Video width and height (diameter of the video message) as defined by sender
    duration : Integer
         Duration of the video in seconds as defined by sender
    thumb : PhotoSize, optional
         Video thumbnail
    file_size : Integer, optional
         File size
    """

    def __init__(self, file_id,
                 file_unique_id,
                 length,
                 duration,
                 thumb=None,
                 file_size=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumb = PhotoSize.parse(thumb)
        self.file_size = file_size


class Voice(BaseType):
    """This object represents a voice note.

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    duration : Integer
         Duration of the audio in seconds as defined by sender
    mime_type : String, optional
         MIME type of the file as defined by sender
    file_size : Integer, optional
         File size
    """

    def __init__(self, file_id,
                 file_unique_id,
                 duration,
                 mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size


class Contact(BaseType):
    """This object represents a phone contact.

    Parameters
    ----------
    phone_number : String
         Contact's phone number
    first_name : String
         Contact's first name
    last_name : String, optional
         Contact's last name
    user_id : Integer, optional
         Contact's user identifier in Telegram
    vcard : String, optional
         Additional data about the contact in the form of a vCard
    """

    def __init__(self, phone_number,
                 first_name,
                 last_name=None,
                 user_id=None,
                 vcard=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard


class Dice(BaseType):
    """This object represents an animated emoji that displays a random value.

    Parameters
    ----------
    emoji : String
         Emoji on which the dice throw animation is based
    value : Integer
         Value of the dice, 1-6 for “” and “” base emoji, 1-5 for “” base emoji
    """

    def __init__(self, emoji,
                 value):
        self.emoji = emoji
        self.value = value


class PollOption(BaseType):
    """This object contains information about one answer option in a poll.

    Parameters
    ----------
    text : String
         Option text, 1-100 characters
    voter_count : Integer
         Number of users that voted for this option
    """

    def __init__(self, text,
                 voter_count):
        self.text = text
        self.voter_count = voter_count


class PollAnswer(BaseType):
    """This object represents an answer of a user in a non-anonymous poll.

    Parameters
    ----------
    poll_id : String
         Unique poll identifier
    user : User
         The user, who changed the answer to the poll
    option_ids : Array of Integer
         0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
    """

    def __init__(self, poll_id,
                 user,
                 option_ids):
        self.poll_id = poll_id
        self.user = User.parse(user)
        self.option_ids = option_ids


class Poll(BaseType):
    """This object contains information about a poll.

    Parameters
    ----------
    id : String
         Unique poll identifier
    question : String
         Poll question, 1-255 characters
    options : Array of PollOption
         List of poll options
    total_voter_count : Integer
         Total number of users that voted in the poll
    is_closed : Boolean
         True, if the poll is closed
    is_anonymous : Boolean
         True, if the poll is anonymous
    _type : String
         Poll type, currently can be “regular” or “quiz”
    allows_multiple_answers : Boolean
         True, if the poll allows multiple answers
    correct_option_id : Integer, optional
         0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    explanation : String, optional
         Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    explanation_entities : Array of MessageEntity, optional
         Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    open_period : Integer, optional
         Amount of time in seconds the poll will be active after creation
    close_date : Integer, optional
         Point in time (Unix timestamp) when the poll will be automatically closed
    """

    def __init__(self, id,
                 question,
                 options,
                 total_voter_count,
                 is_closed,
                 is_anonymous,
                 _type,
                 allows_multiple_answers,
                 correct_option_id=None,
                 explanation=None,
                 explanation_entities=None,
                 open_period=None,
                 close_date=None):
        self.id = id
        self.question = question
        self.options = PollOption.parse(options, iterable=True)
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = _type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = MessageEntity.parse(explanation_entities, iterable=True)
        self.open_period = open_period
        self.close_date = close_date


class Location(BaseType):
    """This object represents a point on the map.

    Parameters
    ----------
    longitude : Float
         Longitude as defined by sender
    latitude : Float
         Latitude as defined by sender
    """

    def __init__(self, longitude,
                 latitude):
        self.longitude = longitude
        self.latitude = latitude


class Venue(BaseType):
    """This object represents a venue.

    Parameters
    ----------
    location : Location
         Venue location
    title : String
         Name of the venue
    address : String
         Address of the venue
    foursquare_id : String, optional
         Foursquare identifier of the venue
    foursquare_type : String, optional
         Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    """

    def __init__(self, location,
                 title,
                 address,
                 foursquare_id=None,
                 foursquare_type=None):
        self.location = Location.parse(location)
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type


class UserProfilePhotos(BaseType):
    """This object represent a user's profile pictures.

    Parameters
    ----------
    total_count : Integer
         Total number of profile pictures the target user has
    photos : Array of Array of PhotoSize
         Requested profile pictures (in up to 4 sizes each)
    """

    def __init__(self, total_count,
                 photos):
        self.total_count = total_count
        self.photos = PhotoSize.parse(photos)


class File(BaseType):
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_size : Integer, optional
         File size, if known
    file_path : String, optional
         File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    """

    def __init__(self, file_id,
                 file_unique_id,
                 file_size=None,
                 file_path=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path


class ReplyKeyboardMarkup(BaseType):
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    Parameters
    ----------
    keyboard : Array of Array of KeyboardButton
         Array of button rows, each represented by an Array of KeyboardButton objects
    resize_keyboard : Boolean, optional
         Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    one_time_keyboard : Boolean, optional
         Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
    selective : Boolean, optional
         Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
    """

    def __init__(self, keyboard,
                 resize_keyboard=None,
                 one_time_keyboard=None,
                 selective=None):
        self.keyboard = KeyboardButton.parse(keyboard)
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective


class KeyboardButton(BaseType):
    """Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message.

    Parameters
    ----------
    text : String
         Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
    request_contact : Boolean, optional
         If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
    request_location : Boolean, optional
         If True, the user's current location will be sent when the button is pressed. Available in private chats only
    request_poll : KeyboardButtonPollType, optional
         If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only
    """

    def __init__(self, text,
                 request_contact=None,
                 request_location=None,
                 request_poll=None):
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = KeyboardButtonPollType.parse(request_poll)


class KeyboardButtonPollType(BaseType):
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    Parameters
    ----------
    type : String, optional
         If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    """

    def __init__(self, _type=None):
        self.type = _type


class ReplyKeyboardRemove(BaseType):
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    Parameters
    ----------
    remove_keyboard : True
         Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
    selective : Boolean, optional
         Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    """

    def __init__(self, remove_keyboard=True,
                 selective=None):
        self.remove_keyboard = remove_keyboard
        self.selective = selective


class InlineKeyboardMarkup(BaseType):
    """Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

    Parameters
    ----------
    inline_keyboard : Array of Array of InlineKeyboardButton
         Array of button rows, each represented by an Array of InlineKeyboardButton objects
    """

    def __init__(self, inline_keyboard):
        self.inline_keyboard = self.inline_keyboard_parser(inline_keyboard)

    def inline_keyboard_parser(self, value):
        """Array of button rows, each represented by an Array of InlineKeyboardButton objects."""
        rows = []
        for row in value:
            temp_row = []
            for keyboard_button in row:
                temp_row.append(InlineKeyboardButton.parse(keyboard_button))
        return rows


class InlineKeyboardButton(BaseType):
    """This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    Parameters
    ----------
    text : String
         Label text on the button
    url : String, optional
         HTTP or tg:// url to be opened when button is pressed
    login_url : LoginUrl, optional
         An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
    callback_data : String, optional
         Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    switch_inline_query : String, optional
         If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. Can be empty, in which case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    switch_inline_query_current_chat : String, optional
         If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.
    callback_game : CallbackGame, optional
         Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
    pay : Boolean, optional
         Specify True, to send a Pay button.NOTE: This type of button must always be the first button in the first row.
    """

    def __init__(self, text,
                 url=None,
                 login_url=None,
                 callback_data=None,
                 switch_inline_query=None,
                 switch_inline_query_current_chat=None,
                 callback_game=None,
                 pay=None):
        self.text = text
        self.url = url
        self.login_url = LoginUrl.parse(login_url)
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game # <- callback_game
        self.pay = pay


class LoginUrl(BaseType):
    """Telegram apps support these buttons as of version 5.7.

    Parameters
    ----------
    url : String
         An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
    forward_text : String, optional
         New text of the button in forwarded messages.
    bot_username : String, optional
         Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
    request_write_access : Boolean, optional
         Pass True to request the permission for your bot to send messages to the user.
    """

    def __init__(self, url,
                 forward_text=None,
                 bot_username=None,
                 request_write_access=None):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access


class CallbackQuery(BaseType):
    """This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    Parameters
    ----------
    id : String
         Unique identifier for this query
    from : User
         Sender
    message : Message, optional
         Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
    inline_message_id : String, optional
         Identifier of the message sent via the bot in inline mode, that originated the query.
    chat_instance : String
         Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
    data : String, optional
         Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
    game_short_name : String, optional
         Short name of a Game to be returned, serves as the unique identifier for the game
    """

    def __init__(self, id,
                 _from,
                 chat_instance,
                 message=None,
                 inline_message_id=None,
                 data=None,
                 game_short_name=None):
        self.id = id
        self._from = User.parse(_from)
        self.message = Message.parse(message)
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name


class ForceReply(BaseType):
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Parameters
    ----------
    force_reply : True
         Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
    selective : Boolean, optional
         Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
    """

    def __init__(self, force_reply,
                 selective=None):
        self.force_reply = force_reply
        self.selective = selective


class ChatPhoto(BaseType):
    """This object represents a chat photo.

    Parameters
    ----------
    small_file_id : String
         File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    small_file_unique_id : String
         Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    big_file_id : String
         File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    big_file_unique_id : String
         Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """

    def __init__(self, small_file_id,
                 small_file_unique_id,
                 big_file_id,
                 big_file_unique_id):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id


class ChatMember(BaseType):
    """This object contains information about one member of a chat.

    Parameters
    ----------
    user : User
         Information about the user
    status : String
         The member's status in the chat. Can be “creator”, “administrator”, “member”, “restricted”, “left” or “kicked”
    custom_title : String, optional
         Owner and administrators only. Custom title for this user
    until_date : Integer, optional
         Restricted and kicked only. Date when restrictions will be lifted for this user; unix time
    can_be_edited : Boolean, optional
         Administrators only. True, if the bot is allowed to edit administrator privileges of that user
    can_post_messages : Boolean, optional
         Administrators only. True, if the administrator can post in the channel; channels only
    can_edit_messages : Boolean, optional
         Administrators only. True, if the administrator can edit messages of other users and can pin messages; channels only
    can_delete_messages : Boolean, optional
         Administrators only. True, if the administrator can delete messages of other users
    can_restrict_members : Boolean, optional
         Administrators only. True, if the administrator can restrict, ban or unban chat members
    can_promote_members : Boolean, optional
         Administrators only. True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    can_change_info : Boolean, optional
         Administrators and restricted only. True, if the user is allowed to change the chat title, photo and other settings
    can_invite_users : Boolean, optional
         Administrators and restricted only. True, if the user is allowed to invite new users to the chat
    can_pin_messages : Boolean, optional
         Administrators and restricted only. True, if the user is allowed to pin messages; groups and supergroups only
    is_member : Boolean, optional
         Restricted only. True, if the user is a member of the chat at the moment of the request
    can_send_messages : Boolean, optional
         Restricted only. True, if the user is allowed to send text messages, contacts, locations and venues
    can_send_media_messages : Boolean, optional
         Restricted only. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    can_send_polls : Boolean, optional
         Restricted only. True, if the user is allowed to send polls
    can_send_other_messages : Boolean, optional
         Restricted only. True, if the user is allowed to send animations, games, stickers and use inline bots
    can_add_web_page_previews : Boolean, optional
         Restricted only. True, if the user is allowed to add web page previews to their messages
    """

    def __init__(self, user,
                 status,
                 custom_title=None,
                 until_date=None,
                 can_be_edited=None,
                 can_post_messages=None,
                 can_edit_messages=None,
                 can_delete_messages=None,
                 can_restrict_members=None,
                 can_promote_members=None,
                 can_change_info=None,
                 can_invite_users=None,
                 can_pin_messages=None,
                 is_member=None,
                 can_send_messages=None,
                 can_send_media_messages=None,
                 can_send_polls=None,
                 can_send_other_messages=None,
                 can_add_web_page_previews=None):
        self.user = User.parse(user)
        self.status = status
        self.custom_title = custom_title
        self.until_date = until_date
        self.can_be_edited = can_be_edited
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.is_member = is_member
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews


class ChatPermissions(BaseType):
    """Describes actions that a non-administrator user is allowed to take in a chat.

    Parameters
    ----------
    can_send_messages : Boolean, optional
         True, if the user is allowed to send text messages, contacts, locations and venues
    can_send_media_messages : Boolean, optional
         True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
    can_send_polls : Boolean, optional
         True, if the user is allowed to send polls, implies can_send_messages
    can_send_other_messages : Boolean, optional
         True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
    can_add_web_page_previews : Boolean, optional
         True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
    can_change_info : Boolean, optional
         True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
    can_invite_users : Boolean, optional
         True, if the user is allowed to invite new users to the chat
    can_pin_messages : Boolean, optional
         True, if the user is allowed to pin messages. Ignored in public supergroups
    """

    def __init__(self, can_send_messages=None,
                 can_send_media_messages=None,
                 can_send_polls=None,
                 can_send_other_messages=None,
                 can_add_web_page_previews=None,
                 can_change_info=None,
                 can_invite_users=None,
                 can_pin_messages=None):
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages


class BotCommand(BaseType):
    """This object represents a bot command.

    Parameters
    ----------
    command : String
         Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    description : String
         Description of the command, 3-256 characters.
    """

    def __init__(self, command,
                 description):
        self.command = command
        self.description = description


class Parameters(BaseType):
    """Contains information about why a request was unsuccessful.

    Parameters
    ----------
    migrate_to_chat_id : Integer, optional
         The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    retry_after : Integer, optional
         In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    """

    def __init__(self, migrate_to_chat_id=None,
                 retry_after=None):
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after


class InputMediaPhoto(BaseType):
    """Represents a photo to be sent.

    Parameters
    ----------
    type : String
         Type of the result, must be photo
    media : String
         File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    caption : String, optional
         Caption of the photo to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the photo caption. See formatting options for more details.
    """

    def __init__(self, type,
                 media,
                 caption=None,
                 parse_mode=None):
        self.type = type # <- input file or str
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode


class InputMediaVideo(BaseType):
    """Represents a video to be sent.

    Parameters
    ----------
    type : String
         Type of the result, must be video
    media : String
         File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    caption : String, optional
         Caption of the video to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the video caption. See formatting options for more details.
    width : Integer, optional
         Video width
    height : Integer, optional
         Video height
    duration : Integer, optional
         Video duration
    supports_streaming : Boolean, optional
         Pass True, if the uploaded video is suitable for streaming
    """

    def __init__(self, type,
                 media,
                 thumb=None,
                 caption=None,
                 parse_mode=None,
                 width=None,
                 height=None,
                 duration=None,
                 supports_streaming=None):
        self.type = type
        self.media = media
        self.thumb = thumb # <- input file or str
        self.caption = caption
        self.parse_mode = parse_mode
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming


class InputMediaAnimation(BaseType):
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    Parameters
    ----------
    type : String
         Type of the result, must be animation
    media : String
         File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    caption : String, optional
         Caption of the animation to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the animation caption. See formatting options for more details.
    width : Integer, optional
         Animation width
    height : Integer, optional
         Animation height
    duration : Integer, optional
         Animation duration
    """

    def __init__(self, type,
                 media,
                 thumb=None,
                 caption=None,
                 parse_mode=None,
                 width=None,
                 height=None,
                 duration=None):
        self.type = type
        self.media = media
        self.thumb = thumb # <- input file or str
        self.caption = caption
        self.parse_mode = parse_mode
        self.width = width
        self.height = height
        self.duration = duration


class InputMediaAudio(BaseType):
    """Represents an audio file to be treated as music to be sent.

    Parameters
    ----------
    type : String
         Type of the result, must be audio
    media : String
         File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    caption : String, optional
         Caption of the audio to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the audio caption. See formatting options for more details.
    duration : Integer, optional
         Duration of the audio in seconds
    performer : String, optional
         Performer of the audio
    title : String, optional
         Title of the audio
    """

    def __init__(self, type,
                 media,
                 thumb=None,
                 caption=None,
                 parse_mode=None,
                 duration=None,
                 performer=None,
                 title=None):
        self.type = type
        self.media = media
        self.thumb = thumb # <- input file or str
        self.caption = caption
        self.parse_mode = parse_mode
        self.duration = duration
        self.performer = performer
        self.title = title


class InputMediaDocument(BaseType):
    """Represents a general file to be sent.

    Parameters
    ----------
    type : String
         Type of the result, must be document
    media : String
         File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    thumb : InputFile or String, optional
         Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    caption : String, optional
         Caption of the document to be sent, 0-1024 characters after entities parsing
    parse_mode : String, optional
         Mode for parsing entities in the document caption. See formatting options for more details.
    """

    def __init__(self, type,
                 media,
                 thumb=None,
                 caption=None,
                 parse_mode=None):
        self.type = type
        self.media = media
        self.thumb = thumb # <- input file or str
        self.caption = caption
        self.parse_mode = parse_mode
