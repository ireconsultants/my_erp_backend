from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# This creates a local SQLite database file called erp.db
engine = create_engine("sqlite:///erp.db", echo=False)
Base = declarative_base()

# Define the Account table
class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False) # asset, liability, income, etc.
    subtype = Column(String, nullable=True) # cash, loan_long, etc.
    balance = Column(Float, default=0.0)

    def __repr__(self):
        return f"<Account(name={self.name}, type={self.type}, balance={self.balance})>"

# Create the table in the database
Base.metadata.create_all(engine)
print("✅ Database and 'accounts' table created successfully!")
