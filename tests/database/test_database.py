import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_addres_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders [0][0] == 1
    assert orders [0][1] == 'Sergii'
    assert orders [0][2] == 'солодка вода'
    assert orders [0][3] == 'з цукром'


@pytest.mark.database
def test_customer_insert():
    db = Database()
    db.insert_new_customer(13, 'Viktoria', 'Peremogy 98', 'Warsaw', '02-485', 'Poland')
    customer = db.get_customer_by_id(13)
    #db.delete_customer_by_id(13)

    assert customer[0] == (13, 'Viktoria', 'Peremogy 98', 'Warsaw', '02-485', 'Poland')


@pytest.mark.database
def test_customer_delete():
    db = Database()
    db.delete_customer_by_id(13)
    customer = db.get_customer_by_id(13)

    assert len(customer) == 0


@pytest.mark.database
def test_update_customer_address():
    db = Database()
    db.insert_new_customer(13, 'Viktoria', 'Peremogy 98', 'Warsaw', '02-485', 'Poland')
    db.update_customer_address_by_id('Shevchenka 23', 13)
    address = db.get_customer_address_by_id(13)

    assert address [0][0] == 'Shevchenka 23'