import sender_stand_request

def test_find_order_info():
    response = sender_stand_request.get_order_info()
    assert response.status_code == 200