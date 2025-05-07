# Inventory Management System

A Django-based inventory management system with REST API support.

## Features

- Inventory item management with supplier relationships
- REST API endpoints with search functionality
- Web interface for viewing inventory items
- Admin interface for managing data
- Unit tests for all major functionality

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Inventory-Management-Django
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

On Windows:
```bash
.\venv\Scripts\activate
```

On Unix or MacOS:
```bash
source venv/bin/activate
```

4. Install required packages:
```bash
pip install django djangorestframework django-filter
```

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

## Running the Project

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the following URLs:
- Admin Interface: http://127.0.0.1:8000/admin/
- Inventory List: http://127.0.0.1:8000/inventory/
- Inventory Detail: http://127.0.0.1:8000/inventory/<id>/
- API Endpoints:
  - List/Search: http://127.0.0.1:8000/api/inventory/
  - Detail: http://127.0.0.1:8000/api/inventory/<id>/

## API Usage

### List all inventory items:
```
GET /api/inventory/
```

### Search inventory items by name:
```
GET /api/inventory/?search=<search-term>
```

### Get specific inventory item:
```
GET /api/inventory/<id>/
```

## Running Tests

To run the test suite:
```bash
python manage.py test inventory
```

## Project Structure

- `inventory/` - Main application directory
  - `models.py` - Database models (Supplier, Inventory)
  - `views.py` - Web views and API endpoints
  - `serializers.py` - API serializers
  - `tests.py` - Unit tests
  - `templates/` - HTML templates
  - `static/` - Static files (images, CSS)

### Supplier
- name: CharField

### Inventory
- name: CharField
- description: CharField
- note: TextField
- stock: IntegerField
- availability: BooleanField
- supplier: ForeignKey to Supplier

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request