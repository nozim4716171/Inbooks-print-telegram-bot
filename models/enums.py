import enum



class BookFormatsEnum(enum.Enum):
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    A6 = "A6"
    B4 = "B4"
    B5 = "B5"
    B6 = "B6"
    C5 = "C5"

class PrintTypesEnum(enum.Enum):
    BLACK_AND_WHITE = "Black and White"
    COLOR = "Color"

class BindingTypesEnum(enum.Enum):
    SPIRAL = "Spiral"
    GLUE = "Glue"
    HARDCOVER = "Hardcover"
    METAL_BINDING = "Metal Binding"

class DeliveryTypesEnum(enum.Enum):
    PICKUP = "pickup"
    DELIVERY = "delivery"

class OrderStatusEnum(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class PaymentMethodEnum(enum.Enum):
    CARD = "card"
    CASH = "cash"

class PaymentStatusEnum(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"
