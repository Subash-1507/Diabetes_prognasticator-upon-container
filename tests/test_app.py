import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_home():
    tester = app.test_client()

    response = tester.get('/')

    assert response.status_code == 200


def test_predict_normal():
    tester = app.test_client()

    response = tester.post(
        '/predict',
        data={
            'pregnancies': '2',
            'glucose': '120',
            'bloodpressure': '70',
            'skinthickness': '20',
            'insulin': '80',
            'bmi': '25',
            'dpf': '0.5',
            'age': '30'
        }
    )

    assert response.status_code == 200


def test_predict_high_glucose():
    tester = app.test_client()

    response = tester.post(
        '/predict',
        data={
            'pregnancies': '5',
            'glucose': '190',
            'bloodpressure': '90',
            'skinthickness': '35',
            'insulin': '150',
            'bmi': '35',
            'dpf': '1.2',
            'age': '45'
        }
    )

    assert response.status_code == 200


def test_predict_low_values():
    tester = app.test_client()

    response = tester.post(
        '/predict',
        data={
            'pregnancies': '0',
            'glucose': '80',
            'bloodpressure': '60',
            'skinthickness': '15',
            'insulin': '50',
            'bmi': '20',
            'dpf': '0.2',
            'age': '22'
        }
    )

    assert response.status_code == 200


def test_predict_boundary():
    tester = app.test_client()

    response = tester.post(
        '/predict',
        data={
            'pregnancies': '10',
            'glucose': '250',
            'bloodpressure': '100',
            'skinthickness': '40',
            'insulin': '300',
            'bmi': '45',
            'dpf': '2.0',
            'age': '60'
        }
    )

    assert response.status_code == 200
