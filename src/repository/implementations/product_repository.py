from core.dto.product import SimpleProduct
from repository.interfaces.sqlalchemy_repository import SQLAlchemyRepository
from repository.models import Product


class ProductRepository(SQLAlchemyRepository[SimpleProduct]):
    model = Product
    dto_model = SimpleProduct
    lookup_field = 'slug'
