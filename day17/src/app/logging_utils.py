from app.models import RagLog


def create_log(db, data):
    log = RagLog(**data)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
