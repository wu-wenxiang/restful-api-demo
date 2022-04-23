from rest_demo.model import Session


def create(instance):
    Session.add(instance)
    return instance


def get(model, id):
    query = Session.query(model)
    return query.filter_by(id=id).one()


def list(model):
    query = Session.query(model)
    return query.all()
