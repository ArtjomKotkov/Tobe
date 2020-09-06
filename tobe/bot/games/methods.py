from ..methods import BaseMethod


class sendGame(BaseMethod):
    """Use this method to send a game. On success, the sent Message is returned.

    Parameters
    ----------
    chat_id : Integer
         Unique identifier for the target chat
    game_short_name : String
         Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather.
    disable_notification : Boolean, optional
         Sends the message silently. Users will receive a notification with no sound.
    reply_to_message_id : Integer, optional
         If the message is a reply, ID of the original message
    reply_markup : InlineKeyboardMarkup, optional
         A JSON-serialized object for an inline keyboard. If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game.
    """

    def __init__(self, chat_id,
                 game_short_name,
                 disable_notification=None,
                 reply_to_message_id=None,
                 reply_markup=None,
                 propagate_values: bool = False,
                 propagate_fields: dict = None):
        super().__init__(propagate_values=propagate_values, propagate_fields=propagate_fields)
        self.chat_id = chat_id
        self.game_short_name = game_short_name
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup


class setGameScore(BaseMethod):
    """Use this method to set the score of the specified user in a game. On success, if the message was sent by the bot, returns the edited Message, otherwise returns True. Returns an error, if the new score is not greater than the user's current score in the chat and force is False.

    Parameters
    ----------
    user_id : Integer
         User identifier
    score : Integer
         New score, must be non-negative
    force : Boolean, optional
         Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters
    disable_edit_message : Boolean, optional
         Pass True, if the game message should not be automatically edited to include the current scoreboard
    chat_id : Integer, optional
         Required if inline_message_id is not specified. Unique identifier for the target chat
    message_id : Integer, optional
         Required if inline_message_id is not specified. Identifier of the sent message
    inline_message_id : String, optional
         Required if chat_id and message_id are not specified. Identifier of the inline message
    """

    def __init__(self, user_id,
                 score,
                 force=None,
                 disable_edit_message=None,
                 chat_id=None,
                 message_id=None,
                 inline_message_id=None,
                 propagate_values: bool = False,
                 propagate_fields: dict = None):
        super().__init__(propagate_values=propagate_values, propagate_fields=propagate_fields)
        self.user_id = user_id
        self.score = score
        self.force = force
        self.disable_edit_message = disable_edit_message
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id


class getGameHighScores(BaseMethod):
    """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an Array of GameHighScore objects.

    Parameters
    ----------
    user_id : Integer
         Target user id
    chat_id : Integer, optional
         Required if inline_message_id is not specified. Unique identifier for the target chat
    message_id : Integer, optional
         Required if inline_message_id is not specified. Identifier of the sent message
    inline_message_id : String, optional
         Required if chat_id and message_id are not specified. Identifier of the inline message
    """

    def __init__(self, user_id,
                 chat_id=None,
                 message_id=None,
                 inline_message_id=None,
                 propagate_values: bool = False,
                 propagate_fields: dict = None):
        super().__init__(propagate_values=propagate_values, propagate_fields=propagate_fields)
        self.user_id = user_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id

