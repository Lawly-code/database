from enum import Enum


class DocumentStatusEnum(str, Enum):
    ACTIVE = "active"


class ChatTypeEnum(str, Enum):
    TYPE = "type"


class MessageSenderTypeEnum(str, Enum):
    SENDER_TYPE = "sender_type"


class MessageStatusEnum(str, Enum):
    SENT = "sent"


class PaymentStatusEnum(str, Enum):
    PAID = "paid"


class FieldTypeENum(str, Enum):
    TYPE = "type"

class LawyerRequestStatusEnum(str, Enum):
    PENDING = "pending"

class DocumentReviewStatusEnum(str, Enum):
    PENDING = "pending"
