from database.connection import session

from database.models.MaterialModel import MaterialModel
from database.models.ProductTypeModel import ProductTypeModel
from database.models.PartnerModel import PartnerModel
from database.models.ProductModel import ProductModel
from database.models.OrderModel import OrderModel

# Инициализация материалов
def insert_data(model, data):
    records = [model(**item) for item in data]
    session.add_all(records)
    session.commit()  

# Пример данных
materials_data = [
    {"type": "Тип материала 1", "percentage_of_defective_material": 0.10},
    {"type": "Тип материала 2", "percentage_of_defective_material": 0.95},
    {"type": "Тип материала 3", "percentage_of_defective_material": 0.28},
    {"type": "Тип материала 4", "percentage_of_defective_material": 0.55},
    {"type": "Тип материала 5", "percentage_of_defective_material": 0.34},
]

partner_data = [
    {
        "type": "ЗАО","company_name": "База Строитель","boss_name": "Иванова Александра Ивановна","mail": "aleksandraivanova@ml.ru","phone_number": "493 123 45 67",
        "address": "652050, Кемеровская область, город Юрга, ул. Лесная, 15", "inn": 2222455179,"rank": 7,
    },
    {
        "type": "ООО","company_name": "Паркет 29","boss_name": "Петров Василий Петрович","mail": "vppetrov@vl.ru","phone_number": "987 123 56 78",
        "address": "164500, Архангельская область, город Северодвинск, ул. Строителей, 18","inn": 2222455179,"rank": 7,
    },
    {
        "type": "ПАО","company_name": "Стройсервис","boss_name": "Соловьев Андрей Николаевич","mail": "ansolovev@st.ru","phone_number": "812 223 32 00",
        "address": "188910, Ленинградская область, город Приморск, ул. Парковая, 21","inn": 4440391035 ,"rank": 7,
    },
    {
        "type": "ОАО","company_name": "Ремонт и отделка","boss_name": "ПВоробьева Екатерина Валерьевна","mail": "ekaterina.vorobeva@ml.ru","phone_number": "444 222 33 11",
        "address": "143960, Московская область, город Реутов, ул. Свободы, 51","inn": 1111520857,"rank": 5,
    },
    {
        "type": "ЗАО","company_name": "Монтаж ПРО","boss_name": "Степанов Степан Сергеевич","mail": "stepanov@stepan.ru","phone_number": "912 888 33 33",
        "address": "309500, Белгородская область, город Старый Оскол, ул. Рабочая, 122","inn": 5552431140,"rank": 10,
    },
]

products_type_data = [
    {"type": "Ламинат", "coefficient_of_product_type": 2.35},
    {"type": "Массивная доска", "coefficient_of_product_type": 5.15},
    {"type": "Паркетная доска", "coefficient_of_product_type": 4.34},
    {"type": "Пробковое покрытие", "coefficient_of_product_type": 1.5},

]

products_data = [
    {"article": "8758385", "name": "Паркетная доска Ясень темный однополосная 14 мм", "min_cost": "4456.9", "fk_type": "3"},
    {"article": "8858958", "name": "Инженерная доска Дуб Французская елка однополосная 12 мм", "min_cost": "7330.99", "fk_type": "3"},
    {"article": "7750282", "name": "Ламинат Дуб дымчато-белый 33 класс 12 мм", "min_cost": "1799.33", "fk_type": "1"},
    {"article": "7028748", "name": "Ламинат Дуб серый 32 класс 8 мм с фаской", "min_cost": "3890.41", "fk_type": "1"},
    {"article": "5012543", "name": "Пробковое напольное клеевое покрытие 32 класс 4 мм", "min_cost": "5450.59", "fk_type": "4"},
]

orders_data = [
    {"fk_product_id": "1", "fk_company_id": "1", "quantity_of_products": "15500", "date_of_create": "2023-03-23"},
    {"fk_product_id": "2", "fk_company_id": "1", "quantity_of_products": "12350", "date_of_create": "2023-12-18"},
    {"fk_product_id": "4", "fk_company_id": "1", "quantity_of_products": "37400", "date_of_create": "2024-06-07"},
    {"fk_product_id": "2", "fk_company_id": "2", "quantity_of_products": "1250", "date_of_create": "2022-12-02"},
    {"fk_product_id": "5", "fk_company_id": "2", "quantity_of_products": "15500", "date_of_create": "2023-05-17"},
    {"fk_product_id": "3", "fk_company_id": "2", "quantity_of_products": "15500", "date_of_create": "2024-06-07"},
    {"fk_product_id": "1", "fk_company_id": "2", "quantity_of_products": "7550", "date_of_create": "2024-07-01"},
    {"fk_product_id": "2", "fk_company_id": "3", "quantity_of_products": "15500", "date_of_create": "2023-01-22"},
    {"fk_product_id": "1", "fk_company_id": "3", "quantity_of_products": "7250", "date_of_create": "2024-07-05"},
    {"fk_product_id": "4", "fk_company_id": "4", "quantity_of_products": "59050", "date_of_create": "2023-03-20"},
    {"fk_product_id": "1", "fk_company_id": "4", "quantity_of_products": "15500", "date_of_create": "2024-03-12"},
    {"fk_product_id": "5", "fk_company_id": "4", "quantity_of_products": "4500", "date_of_create": "2024-05-14"},
    {"fk_product_id": "3", "fk_company_id": "5", "quantity_of_products": "50000", "date_of_create": "2023-09-19"},
    {"fk_product_id": "4", "fk_company_id": "5", "quantity_of_products": "670000", "date_of_create": "2023-11-10"},
    {"fk_product_id": "1", "fk_company_id": "5", "quantity_of_products": "35000", "date_of_create": "2024-04-15"},
    {"fk_product_id": "5", "fk_company_id": "5", "quantity_of_products": "25000", "date_of_create": "2024-06-12"},
]
# Добавление данных в таблицу
insert_data(MaterialModel, materials_data)
insert_data(ProductTypeModel, products_type_data)
insert_data(ProductModel, products_data),
insert_data(PartnerModel, partner_data)
insert_data(OrderModel, orders_data)