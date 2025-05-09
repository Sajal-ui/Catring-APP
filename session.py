from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import inspect

class CustomSession(Session):
    def delete(self, instance):
        if hasattr(instance, 'deleted_at'):
            instance.deleted_at = datetime.now()
            self.add(instance)  # mark as dirty instead of deleting
        else:
            super().delete(instance)

    def commit(self):
        for obj in self.new:
            if hasattr(obj, 'created_at'):
                obj.created_at = datetime.now()
            if hasattr(obj, 'updated_at'):
                obj.updated_at = datetime.now()
        for obj in self.dirty:
            state = inspect(obj)
            if hasattr(obj, 'updated_at') and state.attrs.updated_at.history.has_changes() is False:
                obj.updated_at = datetime.now()
        super().commit()
