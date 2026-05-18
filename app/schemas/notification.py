from pydantic import BaseModel
from typing import Optional

class NotificationCreate(BaseModel):
    id_usuario: int
    mensaje: str
    tipo: Optional[str] = "sistema"