# EXECUTE TO CREATE THE NECESSARY FILE
from redis import Redis

# configuration
DATABASE_HOST="onu1.s2.chalmers.se"
DATABASE_PORT=6380
DATABASE_DB=46
DATABASE_PASSWORD="6a580447-cc21-422e-8d74-66f93bdee3ab"

# connecting
db: Redis = Redis(
    host=DATABASE_HOST,
    port=DATABASE_PORT,
    db=DATABASE_DB,
    password=DATABASE_PASSWORD
)
db.ping()
db.delete("dataset")
