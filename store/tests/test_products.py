from rest_framework import status
import pytest
from model_bakery import baker


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product

@pytest.fixture
def retrieve_product(api_client):
    def do_retrieve_product(product_id):
        return api_client.get(f'/store/products/{product_id}/')
    return do_retrieve_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        # Arrange

        # Act
        response = create_product({'title': 'a', 'slug': 'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_returns_403(self, authenticate, create_product):
            # Arrange
            authenticate(is_staff=False)

            # Act
            response = create_product({'title': 'a', 'slug': 'a'})

            # Assert
            assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_invalid_returns_400(self, authenticate, create_product):
                # Arrange
                authenticate(is_staff=True)
        
                # Act
                response = create_product({'title': '', 'slug': ''})
        
                # Assert
                assert response.status_code == status.HTTP_400_BAD_REQUEST
                assert response.data['title'] is not None


    def test_if_data_is_valid_returns_201(self, authenticate, create_product):
                    # Arrange
                    authenticate(is_staff=True)
            
                    # Act
                    response = create_product({'title': 'a', 'unit_price': 10, 'slug': 'a', 'inventory': 10, 'collection': baker.make('store.Collection').id})
            
                    # Assert
                    assert response.status_code == status.HTTP_201_CREATED
                    assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_returns_200(self, retrieve_product):
        # Arrange
        product = baker.make('store.Product')

        # Act
        response = retrieve_product(product.id)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] > 0


    def test_if_product_does_not_exist_returns_404(self, retrieve_product):
            # Arrange
            product_id = 999

            # Act
            response = retrieve_product(product_id)

            # Assert
            assert response.status_code == status.HTTP_404_NOT_FOUND