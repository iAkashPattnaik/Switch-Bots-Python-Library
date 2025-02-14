import enum


class EventType(enum.Enum):
    """Represents the type of a event."""

    # Chat
    MESSAGE = "MESSAGE"
    COMMAND = "COMMAND"
    CALLBACK_QUERY = "CALLBACK_QUERY"
    INLINE_QUERY = "INLINE_QUERY"

    # Community
    COMMUNITY_CHANNEL_CREATE = "COMMUNITY_CHANNEL_CREATE"
    COMMUNITY_CHANNEL_UPDATE = "COMMUNITY_CHANNEL_UPDATE"
    COMMUNITY_CHANNEL_DELETE = "COMMUNITY_CHANNEL_DELETE"
    COMMUNITY_GROUP_CREATE = "COMMUNITY_GROUP_CREATE"
    COMMUNITY_GROUP_UPDATE = "COMMUNITY_GROUP_UPDATE"
    COMMUNITY_GROUP_DELETE = "COMMUNITY_GROUP_DELETE"
    COMMUNITY_USER_BAN = "COMMUNITY_USER_BAN"
    COMMUNITY_USER_UNBAN = "COMMUNITY_USER_UNBAN"
    COMMUNITY_MEMBER_JOIN = "COMMUNITY_MEMBER_JOIN"
    COMMUNITY_MEMBER_LEAVE = "COMMUNITY_MEMBER_LEAVE"
    COMMUNITY_UPDATE = "COMMUNITY_UPDATE"
    COMMUNITY_DELETE = "COMMUNITY_DELETE"

    COMMUNITY_UNRESTRICT_USER = "COMMUNITY_UN_RESTRICT_USER"
    COMMUNITY_RESTRICT_USER = "COMMUNITY_RESTRICT_USER"


class MediaType(enum.Enum):
    IMAGE = 1
    VIDEO = 2
    AUDIO = 3
    DOCUMENT = 7
    STICKER = 200


def GetMediaType(media_type: int):
    try:
        return {
            1: "IMAGE",
            2: "VIDEO",
            3: "AUDIO",
            4: "EMBED",
            7: "FILE",
            200: "STATIC_STICKER",
            201: "ANIMATED_STICKER",
            202: "VIDEO_STICKER",
        }[media_type]
    except KeyError:
        return None
