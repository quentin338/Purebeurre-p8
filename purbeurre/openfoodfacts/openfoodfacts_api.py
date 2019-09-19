import json

import requests


class OpenFoodFactsException(Exception):
    pass


class OpenFoodFactsAPI:
    _OFF_URL = "https://fr.openfoodfacts.org/"
    _PRODUCTS_URL = "https://fr.openfoodfacts.org/category/{}/{}.json"
    _PRODUCTS_BY_PAGE = 20

    def __init__(self, number_categories, number_products_by_category):
        self._number_categories = number_categories
        self._number_products_by_category = number_products_by_category
        self.categories = self._get_categories()

    def _get_categories(self) -> list:
        """
        Get self.number_categories categories from OFF

        :return: list of categories names

        """
        params = {
            "json": "true"
        }

        response = requests.get(self._OFF_URL + "categories", params=params)

        if not response.content or response.status_code != 200:
            raise OpenFoodFactsException(f"Error when retrieving categories : Status code - {response.status_code}, "
                                         f"response.content - {response.content}")

        try:
            response_json = json.loads(response.content)
            categories = response_json['tags'][:self._number_categories]
        except (TypeError, KeyError):
            raise OpenFoodFactsException(f"Error when retrieving categories : response.content = {response.content}")

        list_categories = []
        for category in categories:
            list_categories.append(category['name'])

        return list_categories

    def get_products(self) -> dict:
        """
        Get generator of products dictionary with name/category/image/nutriscore/ingredients_image/code

        :return: product dict

        """
        # Only 20 are returned by page so we need to calculate how many of them we need to go through
        # number_of_pages = math.ceil(self._number_products_by_category / self._PRODUCTS_BY_PAGE)

        for category in self.categories:
            products_added = 0
            page_number = 1

            while products_added < self._number_products_by_category:
                response = requests.get(self._PRODUCTS_URL.format(category, page_number))

                if not response.content or response.status_code != 200:
                    raise OpenFoodFactsException(f"Error when retrieving products from category : {category}, "
                                                 f"status_code - {response.status_code}")

                try:
                    response_json = json.loads(response.content)
                    products = response_json['products']
                except (TypeError, KeyError):
                    raise OpenFoodFactsException(f"Error when retrieving products from category : {category}, "
                                                 f"response.content - {response.content}")

                for product in products:
                    if not self._check_product_is_fr(product):
                        continue

                    try:
                        product_dict = {
                            'name': product['product_name_fr'],
                            'category': category,
                            'image_url': product['image_url'],
                            'nutriscore': product['nutrition_score_debug'],
                            'ingredients_image': product['selected_images']['ingredients']['display']['fr'],
                            'code': product['code']
                        }
                    except KeyError:
                        continue

                    # One value is missing or we don't have the french nutriscore
                    product_values = set(product_dict.values())
                    if "" in product_values or "-- fr" not in product_dict['nutriscore']:
                        continue

                    # Notes are on the form X | -X | XX at the end of the string - FR note always at the end
                    nutriscore = product_dict['nutriscore']
                    nutriscore = nutriscore[-2:].strip()
                    try:
                        product_dict['nutriscore'] = int(nutriscore)
                    except ValueError:
                        continue

                    yield product_dict

                    # To stop if we reach the number of products required
                    products_added += 1
                    if products_added == self._number_products_by_category:
                        break

                # We don't reach the target number of products so we go to the next page
                page_number += 1

    @staticmethod
    def _check_product_is_fr(product: dict) -> bool:
        """
        Return True if product is French

        :param product: dict of the product
        :return: bool - is French
        """
        keys_to_check = ['countries_lc', 'categories_lc', 'labels_lc']

        for key in keys_to_check:
            if "fr" not in product.get(key, ""):
                return False

        return True


if __name__ == "__main__":
    api = OpenFoodFactsAPI(number_categories=10, number_products_by_category=2)

    for prod in api.get_products():
        print(prod)
