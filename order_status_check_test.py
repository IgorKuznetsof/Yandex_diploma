# Кузнецов Игорь, 10-ая когорта, Финальный проект, Инженер по тестированию плюс.
import sender_stand_request

# Тест. Проверка создания заказа и получения заказа по номеру его трека
def test_order_status_check():
    response = sender_stand_request.get_order_by_track_id(sender_stand_request.track_id())
    # Проверяем, что код ответа равен 200
    assert response.status_code == 200
# Запускаем тест
test_order_status_check()