from enum import Enum

class BillStatus(Enum):
    UNVERIFY="UNVERYFY"
    VERIFY  = "VERIFY"
    PHONE_CONFIRM = "PHONE_CONFIRM"
    SHIPPING = "SHIPPING"
    SHIPPED = "SHIPPED"