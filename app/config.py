from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    kafka_brokers: str = "localhost:9092"
    redis_url: str = "redis://localhost:6379/0"
    group_id: str = "event-stream"


settings = Settings()
# check perf here
# check perf here
# left a note for myself
