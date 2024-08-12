from uuid import uuid4

from slugify import slugify
from sqlalchemy import func


def unique_slug_generator(session, instance, slug_field, slug_value=None):
    if slug_value is not None:
        slug = slug_value
    else:
        slug = slugify(getattr(instance, slug_field))

    Klass = instance.__class__
    query = session.query(Klass).filter(func.lower(getattr(Klass, slug_field)) == slug.lower())

    if session.query(query.exists()).scalar():
        new_slug = f'{slug}-{str(uuid4())[:8]}'
        return unique_slug_generator(session, instance, slug_field, new_slug)

    return slug