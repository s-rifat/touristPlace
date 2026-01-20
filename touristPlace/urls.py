# Tourist Place API

A simple Django REST Framework API to manage tourist places.

---

## Features
- User login required to create/update/delete places
- View all places with pagination & ordering
- CRUD operations: Create, Read, Update, Delete
- Image upload with removal functionality
- Swagger API documentation

---

## Requirements / Versions
- Python: 3.12.10
- Django: 6.0.1
- Django REST Framework: 3.16.1
- drf-yasg (for Swagger)

---

## Setup

```bash
git clone https://github.com/s-rifat/touristPlace.git
cd touristPlace
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


