import json


def test_list_devices(app):
    with app.test_client() as c:
        resp = c.get('/api/device')
        assert resp.status_code == 200
        assert resp.mimetype == 'application/json'
        json_data = json.loads(resp.data.decode())
        assert json_data == {"num_results": 0, "objects": [],
                             "page": 1, "total_pages": 0}
