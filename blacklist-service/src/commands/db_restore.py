from .base_command import BaseCommannd
from ..models.model import db
from ..errors.errors import DataDeleted
##Pte Link de esta funcion con blueprint users/reset
class db_restore(BaseCommannd):
    def execute():
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print('Deleted table = {}'.format(table))
            db.session.execute(table.delete())
        db.session.commit()
        raise DataDeleted
        