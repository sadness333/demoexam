from database.connection import Base, engine
from database.init_db_data import insert_data, materials_data, products_type_data, products_data, partner_data, \
    orders_data
from database.models.MaterialModel import MaterialModel
from database.models.OrderModel import OrderModel
from database.models.PartnerModel import PartnerModel
from database.models.ProductModel import ProductModel
from database.models.ProductTypeModel import ProductTypeModel

Base.metadata.create_all(engine)

