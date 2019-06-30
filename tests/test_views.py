

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'


def test_book_views_get(client):
    response = client.get('/book')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
