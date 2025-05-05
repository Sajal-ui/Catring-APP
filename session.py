from datetime import datetime
from sqlachemy.orm import Session

class DBSession(Session):
    def delete(self, instance):
        if hasattr(instance, 'deleted_at'):
            instance.deleted_at = datetime.now()
            self.add(obj)  # mark as dirty instead of deleting
        else:
            super().delete(obj)

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
