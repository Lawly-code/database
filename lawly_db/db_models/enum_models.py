from enum import Enum


class DocumentStatusEnum(str, Enum):
    STARTED = "started"
    COMPLETED = "completed"
    ERROR = "error"
    PROCESSING = "processing"


class ChatTypeEnum(str, Enum):
    AI = "ai"
    LAWYER = "lawyer"


class MessageSenderTypeEnum(str, Enum):
    USER = "user"
    AI = "ai"
    LAWYER = "lawyer"


class MessageStatusEnum(str, Enum):
    SENT = "sent"
    ERROR = "error"
    READ = "read"


class PaymentStatusEnum(str, Enum):
    PAID = "paid"


class LawyerRequestStatusEnum(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"


class DocumentReviewStatusEnum(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
