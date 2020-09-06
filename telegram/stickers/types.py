from ..types import BaseType, PhotoSize


class Sticker(BaseType):
    """This object represents a sticker.

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    width : Integer
         Sticker width
    height : Integer
         Sticker height
    is_animated : Boolean
         True, if the sticker is animated
    thumb : PhotoSize, optional
         Sticker thumbnail in the .WEBP or .JPG format
    emoji : String, optional
         Emoji associated with the sticker
    set_name : String, optional
         Name of the sticker set to which the sticker belongs
    mask_position : MaskPosition, optional
         For mask stickers, the position where the mask should be placed
    file_size : Integer, optional
         File size
    """

    def __init__(self, file_id,
                 file_unique_id,
                 width,
                 height,
                 is_animated,
                 thumb=None,
                 emoji=None,
                 set_name=None,
                 mask_position=None,
                 file_size=None):
        super().__init__()
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.thumb = PhotoSize.parse(thumb)
        self.emoji = emoji
        self.set_name = set_name
        self.mask_position = MaskPosition.parse(mask_position)
        self.file_size = file_size


class StickerSet(BaseType):
    """This object represents a sticker set.

    Parameters
    ----------
    name : String
         Sticker set name
    title : String
         Sticker set title
    is_animated : Boolean
         True, if the sticker set contains animated stickers
    contains_masks : Boolean
         True, if the sticker set contains masks
    stickers : Array of Sticker
         List of all set stickers
    thumb : PhotoSize, optional
         Sticker set thumbnail in the .WEBP or .TGS format
    """

    def __init__(self, name,
                 title,
                 is_animated,
                 contains_masks,
                 stickers,
                 thumb=None):
        super().__init__()
        self.name = name
        self.title = title
        self.is_animated = is_animated
        self.contains_masks = contains_masks
        self.stickers = Sticker.parse(stickers, iterable=True)
        self.thumb = PhotoSize.parse(thumb)


class MaskPosition(BaseType):
    """This object describes the position on faces where a mask should be placed by default.

    Parameters
    ----------
    point : String
         The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
    x_shift : Float number
         Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    y_shift : Float number
         Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    scale : Float number
         Mask scaling coefficient. For example, 2.0 means double size.
    """

    def __init__(self, point,
                 x_shift,
                 y_shift,
                 scale):
        super().__init__()
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale