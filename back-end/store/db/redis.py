from redis_om import get_redis_connection
from dotenv import load_dotenv
import os

load_dotenv()

redis = get_redis_connection(
    host=os.getenv("host"),
    port=int(os.getenv("port")),
    password=os.getenv("password"),
    decode_responses=True,
)
