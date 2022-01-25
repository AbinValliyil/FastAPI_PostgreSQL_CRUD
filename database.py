from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
'''

engine = create_engine("postgresql://postgres:paa@localhost/my_db",
echo = True
)
'''
engine=create_engine("postgres://jdloegvnvlmzzs:7e869dd6f782952e46ac9673eb84d55a54dfbb3953203372c827087ce08e779e@ec2-3-227-154-49.compute-1.amazonaws.com:5432/d9089slsnpa3re",
                     echo=True
)

Base = declarative_base()

SessionLocal=sessionmaker(bind = engine)
