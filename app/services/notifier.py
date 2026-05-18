import redis
from app.core.config import settings

r = redis.Redis(
    host=settings.REDIS_HOST, 
    port=settings.REDIS_PORT, 
    db=settings.REDIS_DB, 
    decode_responses=True 
)

class NotifierService:
    @staticmethod
    def add_notification(id_usuario: int, mensaje: str) -> str:
        key = f"notificaciones:{id_usuario}"
                
        r.lpush(key, mensaje)
        
        r.ltrim(key, 0, 19)
        
        return mensaje

    @staticmethod
    def get_notifications(id_usuario: int, limit: int = 5) -> list:
        key = f"notificaciones:{id_usuario}"
        
        return r.lrange(key, 0, limit - 1)