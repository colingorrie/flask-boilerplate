from flask.ext.security import Security
from flask.ext.security.datastore import Datastore, UserDatastore
from flask.ext.security.utils import get_identity_attributes
from .util import autoreconnect
from .models import db, User, Role


class AutoReconnectDatastore(Datastore):
    @autoreconnect
    def put(self, model):
        model.save()
        return model

    @autoreconnect
    def delete(self, model):
        model.delete()


class AutoReconnectUserDatastore(AutoReconnectDatastore, UserDatastore):
    def __init__(self, db, user_model, role_model):
        AutoReconnectDatastore.__init__(self, db)
        UserDatastore.__init__(self, user_model, role_model)

    @autoreconnect
    def get_user(self, identifier):
        from mongoengine import ValidationError
        try:
            return self.user_model.objects(id=identifier).first()
        except ValidationError:
            pass
        for attr in get_identity_attributes():
            query_key = '%s__iexact' % attr
            query = {query_key: identifier}
            rv = self.user_model.objects(**query).first()
            if rv is not None:
                return rv

    @autoreconnect
    def find_user(self, **kwargs):
        try:
            from mongoengine.queryset import Q, QCombination
        except ImportError:
            from mongoengine.queryset.visitor import Q, QCombination
        from mongoengine.errors import ValidationError

        queries = map(lambda i: Q(**{i[0]: i[1]}), kwargs.items())
        query = QCombination(QCombination.AND, queries)
        try:
            return self.user_model.objects(query).first()
        except ValidationError:  # pragma: no cover
            return None

    @autoreconnect
    def find_role(self, role):
        return self.role_model.objects(name=role).first()


user_datastore = AutoReconnectUserDatastore(db, User, Role)
security = Security()
