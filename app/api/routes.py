from fastapi import APIRouter, HTTPException
from app.schemas.notification import NotificationCreate
from app.services.notifier import NotifierService

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("")
async def create_notification(payload: NotificationCreate):
    try:
        msg = NotifierService.add_notification(payload.id_usuario, payload.mensaje)
        return {"message": "Notificación registrada con éxito", "data": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user/{id_usuario}")
async def get_user_notifications(id_usuario: int, limit: int = 5):
    if id_usuario <= 0:
        raise HTTPException(status_code=400, detail="ID de usuario inválido")
    
    alertas = NotifierService.get_notifications(id_usuario, limit)
    return {
        "id_usuario": id_usuario,
        "total": len(alertas),
        "notificaciones": alertas
    }