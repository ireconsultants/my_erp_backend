from sqlalchemy.orm import sessionmaker
from models import engine, Account

# Connect to the database
Session = sessionmaker(bind=engine)
session = Session()

# 1. Create a new account (Cash in Hand with 10,000 balance)
cash_account = Account(
    name="Cash in Hand", 
    type="asset", 
    subtype="cash", 
    balance=10000.0
)

# 2. Add it to the database and save
session.add(cash_account)
session.commit()

# 3. Fetch all accounts from the database and print them
print("\n--- Accounts in Database ---")
accounts = session.query(Account).all()
for acc in accounts:
    print(acc)

session.close()
