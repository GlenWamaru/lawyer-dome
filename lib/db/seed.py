# seed.py
from db.models import Lawyer, Case, Client
from db.models import session
from helpers import validate_email, validate_phone_number

def seed():
    # Example seeding logic to create initial data
    lawyer1 = Lawyer(name="John Doe", speciality="Criminal Defense")
    lawyer2 = Lawyer(name="Jane Smith", speciality="Family Law")
    
    case1 = Case(title="Criminal Case", description="Defending client in criminal trial", lawyer=lawyer1)
    case2 = Case(title="Divorce Case", description="Handling divorce proceedings for client", lawyer=lawyer2)

    client1 = Client(name="Alice Johnson", email="alice@example.com", phone_number="1234567890", lawyer=lawyer1)
    client2 = Client(name="Bob Smith", email="bob@example.com", phone_number="9876543210", lawyer=lawyer2)

    session.add_all([lawyer1, lawyer2, case1, case2, client1, client2])
    session.commit()

if __name__ == "__main__":
    seed()
