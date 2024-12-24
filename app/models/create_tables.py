from app.backend.db import Base, engine
from app.models import User, Task

Base.metadata.create_all(engine)