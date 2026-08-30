from enum import Enum

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    OWNER = "OWNER"
    MANAGER = "MANAGER"
    STAFF = "STAFF"

class StockMovementType(str, Enum):
    PURCHASE = "PURCHASE"
    SALE = "SALE"
    ADJUSTMENT = "ADJUSTMENT"
    RETURN = "RETURN"

class TransactionType(str, Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class AlertSeverity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

class AlertType(str, Enum):
    LOW_STOCK = "LOW_STOCK"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    HIGH_EXPENSE = "HIGH_EXPENSE"
    SALES_DROP = "SALES_DROP"
    PAYMENT_DUE = "PAYMENT_DUE"
