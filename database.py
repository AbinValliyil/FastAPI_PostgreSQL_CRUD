from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:123@localhost/my_db",
echo = True

)

Base = declarative_base()

SessionLocal=sessionmaker(bind = engine)