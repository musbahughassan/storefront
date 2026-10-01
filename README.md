# Storefront — E-commerce REST API

A backend e-commerce application built with **Django REST Framework** and **PostgreSQL**, with asynchronous task processing, caching, background workers, automated testing, Docker support, and deployment configuration.

The project was developed to explore the architecture and engineering practices involved in building a real-world e-commerce backend.

## Features

* Product and collection management
* Product search, filtering, ordering, and pagination
* Shopping carts and cart items
* Customer management
* Order creation and management
* Order items
* Product reviews
* Product promotions and discounts
* Authentication and permissions
* PostgreSQL database
* Redis integration
* Celery background tasks
* Email-related background processing
* API performance monitoring
* Automated tests with Pytest
* Load testing with Locust
* Docker and Docker Compose support
* Gunicorn deployment configuration
* Heroku deployment configuration

## Tech Stack

| Technology            | Purpose                       |
| --------------------- | ----------------------------- |
| Python                | Backend programming language  |
| Django                | Web framework                 |
| Django REST Framework | REST API development          |
| PostgreSQL            | Relational database           |
| Redis                 | Caching and message broker    |
| Celery                | Asynchronous/background tasks |
| Docker                | Containerization              |
| Docker Compose        | Multi-container development   |
| Gunicorn              | WSGI application server       |
| Pytest                | Automated testing             |
| Locust                | Load testing                  |
| Git                   | Version control               |
| Heroku                | Deployment                    |

## Architecture

The application follows a modular Django architecture with separate applications responsible for different areas of the system.

```text
                    ┌─────────────────────┐
                    │       Client        │
                    │ Web / Mobile / API  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Django REST API  │
                    │                     │
                    │  Views / Serializers│
                    │  Permissions        │
                    │  Filtering           │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
        ┌──────────────┐ ┌────────────┐ ┌──────────────┐
        │ PostgreSQL   │ │   Redis    │ │    Celery    │
        │   Database   │ │ Cache/Broker│ │   Workers    │
        └──────────────┘ └────────────┘ └──────────────┘
                                               │
                                               ▼
                                      Background Tasks
```

## Project Structure

```text
storefront/
├── core/                 # Shared application functionality
├── store/                # Products, carts, orders, reviews, etc.
├── likes/                # Like-related functionality
├── tags/                 # Tag functionality
├── playground/           # Development/experimentation app
├── storefront/           # Django project configuration
├── locustfiles/          # Load-testing scenarios
├── Dockerfile
├── docker-compose.yml
├── docker-entrypoint.sh
├── Pipfile
├── Pipfile.lock
├── Procfile
├── manage.py
└── pytest.ini
```

## API Capabilities

The REST API exposes resources for common e-commerce operations, including:

* Products
* Collections
* Carts
* Cart items
* Customers
* Orders
* Order items
* Reviews
* Promotions

The API supports features such as:

* Pagination
* Filtering
* Searching
* Ordering
* Authentication
* Permission-based access
* Resource relationships

Example API request:

```http
GET /store/products/?ordering=unit_price
```

Example response:

```json
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}
```

## Background Processing

Celery and Redis are used to support asynchronous/background processing.

The architecture separates work that does not need to block an API request from the main request-response cycle.

```text
Django API
    │
    │ enqueue task
    ▼
 Redis
    │
    ▼
Celery Worker
    │
    ▼
Background Task
```

This provides a foundation for operations such as email processing and other tasks that can be executed asynchronously.

## Database

The application uses **PostgreSQL** as its relational database.

The data model represents common e-commerce relationships between entities such as:

```text
Customer
   │
   ├── Cart
   │    └── Cart Items ── Product
   │
   └── Orders
        └── Order Items ── Product

Collection ── Products

Product ── Reviews
Product ── Promotions
```

## Docker

The project includes Docker configuration for running the application and supporting services.

Services can be managed with Docker Compose.

Start the environment with:

```bash
docker compose up --build
```

Stop the environment with:

```bash
docker compose down
```

## Local Development

### 1. Clone the repository

```bash
git clone https://github.com/musbahughassan/storefront.git
cd storefront
```

### 2. Install dependencies

The project uses Pipenv.

```bash
pipenv install
```

Activate the environment:

```bash
pipenv shell
```

### 3. Configure environment variables

Create a `.env` file for local configuration.

Do not commit secrets, passwords, API keys, or other sensitive configuration to Git.

Example:

```env
SECRET_KEY=your-development-secret-key
```

Configure database and other service variables according to your local environment.

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Testing

The project uses **Pytest** for automated testing.

Run the test suite with:

```bash
pytest
```

For Django's built-in test runner:

```bash
python manage.py test
```

## Load Testing

Locust is included for load testing.

Load-testing scenarios are located in:

```text
locustfiles/
```

Locust can be used to evaluate API behavior under concurrent requests and identify potential performance bottlenecks.

## Deployment

The project includes configuration for deployment with:

* Gunicorn
* PostgreSQL
* Redis
* Heroku

The repository also contains a `Procfile` for process configuration.

The application was previously deployed to Heroku during development.

## Engineering Concepts Demonstrated

This project provided practical experience with:

* REST API design
* Django application architecture
* Database modeling and relationships
* PostgreSQL
* Authentication and authorization
* API filtering and pagination
* Caching
* Asynchronous task processing
* Redis
* Celery
* Containerization
* Automated testing
* Load testing
* Environment-based configuration
* Application deployment
* Version control

## Future Improvements

Potential future improvements include:

* API documentation with OpenAPI/Swagger
* CI/CD pipeline
* Improved observability and centralized logging
* More comprehensive integration tests
* Production-grade configuration management
* API rate limiting
* Improved caching strategy
* Payment gateway integration
* Inventory management
* Order-status workflow
* More extensive performance testing

## Author

**Musbahu Hassan**

Backend Software Engineer focused on Python, Django, REST APIs, databases, and distributed backend systems.

GitHub:
https://github.com/musbahughassan
