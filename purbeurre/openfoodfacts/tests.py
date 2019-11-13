from unittest import mock
import json

from django.test import TestCase, tag

from openfoodfacts.openfoodfacts_api import OpenFoodFactsAPI, OpenFoodFactsException


class TestOpenFoodFactsAPI(TestCase):

    def setUp(self) -> None:
        self.response_content_cat = json.dumps({
            "tags": [
                {
                    "name": "Charcuterie"
                },
                {
                    "name": "Boissons"
                }

            ]
        })
        self.response_content_prod = json.dumps({
            "products": [
                {
                    "code": 12345,
                    "product_name_fr": "Saucisson sec",
                    "image_url": "http://www.saucissonsec.com",
                    "nutrition_score_debug": "FR at the end of the string -- fr 10",
                    "nutriscore_grade": "a",
                    "category": "Charcuterie",
                    "countries_lc": "fr",
                    "categories_lc": "fr",
                    "labels_lc": "fr",
                    "selected_images": {
                        "ingredients": {
                            "display": {
                                'fr': "http://www.image.com"
                            }
                        }
                    }
                }
            ]
        })
        patcher = mock.patch("openfoodfacts.openfoodfacts_api.requests.get")
        self.addCleanup(patcher.stop)
        self.mock_requests = patcher.start()
        self.mock_requests.return_value = self.mock_response = mock.Mock()

    # _get_categories()
    def test_get_categories_len(self):
        self.mock_response.status_code = 200
        self.mock_response.content = self.response_content_cat

        api = OpenFoodFactsAPI(2, 2)
        self.assertEqual(2, len(api.categories))
        self.assertIn("Boissons", api.categories)
        self.assertIn("Charcuterie", api.categories)

    def test_get_categories_no_content(self):
        self.mock_response.content = ""
        self.mock_response.status_code = 200

        with self.assertRaises(OpenFoodFactsException, msg="No content doesn't raises Exception"):
            OpenFoodFactsAPI(1, 1)

    def test_get_categories_status_code_not_200(self):
        self.mock_response.content = self.response_content_cat
        self.mock_response.status_code = 404

        with self.assertRaises(OpenFoodFactsException,
                               msg="Status code != 200 doesn't raises Exception"):
            OpenFoodFactsAPI(1, 1)

    def test_get_categories_bad_response_content(self):
        self.mock_response.content = "Bad response"

        with self.assertRaises(OpenFoodFactsException,
                               msg="Status code != 200 doesn't raises Exception"):
            OpenFoodFactsAPI(1, 1)

    # get_products()
    @mock.patch("openfoodfacts.openfoodfacts_api.OpenFoodFactsAPI._check_product_is_fr",
                return_value=True)
    def test_get_products_proper_yield(self, mock_is_fr):
        self.mock_response.content = self.response_content_prod
        self.mock_response.status_code = 200

        api = OpenFoodFactsAPI(1, 1, ['Boissons'])

        for product in api.get_products():
            self.assertEqual(json.loads(self.response_content_prod)['products'][0]['code'],
                             product['code'])

    def test_get_products_status_code_not_200(self):
        self.mock_response.content = self.response_content_prod
        self.mock_response.status_code = 404

        api = OpenFoodFactsAPI(1, 1, ["Boissons"])

        with self.assertRaises(OpenFoodFactsException,
                               msg="Don't raise Exception when Status Code != 200"):
            next(api.get_products())

    def test_get_products_no_response_content(self):
        self.mock_response.content = ""
        self.mock_response.status_code = 200

        api = OpenFoodFactsAPI(1, 1, ["Boissons"])

        with self.assertRaises(OpenFoodFactsException,
                               msg="Don't raise Exception when Status Code != 200"):
            next(api.get_products())
