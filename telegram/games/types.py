from ..types import BaseType, PhotoSize, MessageEntity, Animation, User


class Game(BaseType):
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Parameters
    ----------
    title : String
         Title of the game
    description : String
         Description of the game
    photo : Array of PhotoSize
         Photo that will be displayed in the game message in chats.
    text : String, optional
         Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    text_entities : Array of MessageEntity, optional
         Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    animation : Animation, optional
         Animation that will be displayed in the game message in chats. Upload via BotFather
    """

    def __init__(self, title,
                 description,
                 photo,
                 text=None,
                 text_entities=None,
                 animation=None):
        super().__init__()
        self.title = title
        self.description = description
        self.photo = PhotoSize.parse(photo, iterable=True)
        self.text = text
        self.text_entities = MessageEntity.parse(text_entities, iterable=True)
        self.animation = Animation.parse(animation, iterable=True)


class GameHighScore(BaseType):
    """This object represents one row of the high scores table for a game.

    Parameters
    ----------
    position : Integer
         Position in high score table for the game
    user : User
         User
    score : Integer
         Score
    """

    def __init__(self, position,
                 user,
                 score):
        super().__init__()
        self.position = position
        self.user = User.parse(user)
        self.score = score
