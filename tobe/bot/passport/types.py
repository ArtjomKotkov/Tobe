from ..types import BaseType


class PassportData(BaseType):
    """Contains information about Telegram Passport data shared with the bot by the user.

    Parameters
    ----------
    data : Array of EncryptedPassportElement
         Array with information about documents and other Telegram Passport elements that was shared with the bot
    credentials : EncryptedCredentials
         Encrypted credentials required to decrypt the data
    """

    def __init__(self, data,
                 credentials):
        super().__init__()
        self.data = EncryptedPassportElement.parse(data, iterable=True)
        self.credentials = EncryptedCredentials.parse(credentials)


class PassportFile(BaseType):
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    Parameters
    ----------
    file_id : String
         Identifier for this file, which can be used to download or reuse the file
    file_unique_id : String
         Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_size : Integer
         File size
    file_date : Integer
         Unix time when the file was uploaded
    """

    def __init__(self, file_id,
                 file_unique_id,
                 file_size,
                 file_date):
        super().__init__()
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date


class EncryptedPassportElement(BaseType):
    """Contains information about documents or other Telegram Passport elements shared with the bot by the user.

    Parameters
    ----------
    type : String
         Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.
    data : String, optional
         Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials.
    phone_number : String, optional
         User's verified phone number, available only for “phone_number” type
    email : String, optional
         User's verified email address, available only for “email” type
    files : Array of PassportFile, optional
         Array of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    front_side : PassportFile, optional
         Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    reverse_side : PassportFile, optional
         Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    selfie : PassportFile, optional
         Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    translation : Array of PassportFile, optional
         Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    hash : String
         Base64-encoded element hash for using in PassportElementErrorUnspecified
    """

    def __init__(self,
                 type,
                 hash,
                 data=None,
                 phone_number=None,
                 email=None,
                 files=None,
                 front_side=None,
                 reverse_side=None,
                 selfie=None,
                 translation=None):
        super().__init__()
        self.type = type
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = PassportFile.parse(files, iterable=True)
        self.front_side = PassportFile.parse(front_side)
        self.reverse_side = PassportFile.parse(reverse_side)
        self.selfie = PassportFile.parse(selfie)
        self.translation = PassportFile.parse(translation, iterable=True)
        self.hash = hash


class EncryptedCredentials(BaseType):
    """Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.

    Parameters
    ----------
    data : String
         Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
    hash : String
         Base64-encoded data hash for data authentication
    secret : String
         Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
    """

    def __init__(self, data,
                 hash,
                 secret):
        super().__init__()
        self.data = data
        self.hash = hash
        self.secret = secret


class PassportElementErrorDataField(BaseType):
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    Parameters
    ----------
    source : String
         Error source, must be data
    type : String
         The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”
    field_name : String
         Name of the data field which has the error
    data_hash : String
         Base64-encoded data hash
    message : String
         Error message
    """

    def __init__(self, source,
                 type,
                 field_name,
                 data_hash,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message


class PassportElementErrorFrontSide(BaseType):
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    Parameters
    ----------
    source : String
         Error source, must be front_side
    type : String
         The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
    file_hash : String
         Base64-encoded hash of the file with the front side of the document
    message : String
         Error message
    """

    def __init__(self,
                 source,
                 type,
                 file_hash,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorReverseSide(BaseType):
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    Parameters
    ----------
    source : String
         Error source, must be reverse_side
    type : String
         The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”
    file_hash : String
         Base64-encoded hash of the file with the reverse side of the document
    message : String
         Error message
    """

    def __init__(self, source,
                 type,
                 file_hash,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorSelfie(BaseType):
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    Parameters
    ----------
    source : String
         Error source, must be selfie
    type : String
         The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
    file_hash : String
         Base64-encoded hash of the file with the selfie
    message : String
         Error message
    """

    def __init__(self, source,
                 type,
                 file_hash,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorFile(BaseType):
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    Parameters
    ----------
    source : String
         Error source, must be file
    type : String
         The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    file_hash : String
         Base64-encoded file hash
    message : String
         Error message
    """

    def __init__(self, source,
                 type,
                 file_hash,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorFiles(BaseType):
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    Parameters
    ----------
    source : String
         Error source, must be files
    type : String
         The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    file_hashes : Array of String
         List of base64-encoded file hashes
    message : String
         Error message
    """

    def __init__(self, source,
                 type,
                 file_hashes,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message


class PassportElementErrorTranslationFile(BaseType):
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    Parameters
    ----------
    source : String
         Error source, must be translation_file
    type : String
         Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    file_hash : String
         Base64-encoded file hash
    message : String
         Error message
    """

    def __init__(self, source,
                 type,
                 file_hash,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorTranslationFiles(BaseType):
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    Parameters
    ----------
    source : String
         Error source, must be translation_files
    type : String
         Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    file_hashes : Array of String
         List of base64-encoded file hashes
    message : String
         Error message
    """

    def __init__(self, source,
                 type,
                 file_hashes,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message


class PassportElementErrorUnspecified(BaseType):
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    Parameters
    ----------
    source : String
         Error source, must be unspecified
    type : String
         Type of element of the user's Telegram Passport which has the issue
    element_hash : String
         Base64-encoded element hash
    message : String
         Error message
    """

    def __init__(self, source,
                 type,
                 element_hash,
                 message):
        super().__init__()
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message
