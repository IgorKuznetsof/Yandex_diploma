import requests
import configuration
import data

# задаем функцию создания заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)
#задаем функцию, которая записывает номер трека нового заказа
def track_id():
    new_order = post_new_order()
    track_id = new_order.json()["track"]
    return track_id



# задаем функцию запроса на получение заказа по номеру трека
def get_order_by_track_id(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, params={'t': track_id})

