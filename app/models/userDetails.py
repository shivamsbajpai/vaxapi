import uuid
from ..data.database import Base
from sqlalchemy import Column, String,Integer
from sqlalchemy.dialects.postgresql import UUID

class UserDetails(Base):
    __tablename__ = 'UserDetails'
    user_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String)
    dose_number = Column(Integer)
    district_code = Column(Integer)
    age = Column(Integer)
    whatsappNumber = Column(String)