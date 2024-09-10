from models.bill import Bill 
from models.enums import DbOpStatus 

def create_bill(db, bill: Bill): 
    try:
        db.add(bill)
        db.commit()
        db.refresh(bill)
        return DbOpStatus.SUCCESS, bill
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)
    
def read_bill_by_status(): 
    pass 

def read_bill_by_user_id(): 
    pass 