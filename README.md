# Product Catalog - Django Take-Home Assignment

A Django project that models products, categories, and tags with search and filter functionality. Built for the Remarcable Full Stack Developer Co-op take-home assignment.

## Overview

This project implements a simple product catalog themed around soccer gear. Users can:
- Search products by name or description
- Filter products by category (dropdown)
- Filter products by tags (multi-select checkboxes)
- Combine any of the above

The database was populated through the Django admin interface with 5 categories, 10 tags, and 20 products.

## Tech Stack

- Python 3.14
- Django 6.0.3
- SQLite (default Django database)
- Django Templates (no front-end framework)

## Setup Instructions

### 1. Clone the repository
```bash
git clone 
cd remarcable_django_project
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```

### 3. Install Django
```bash
pip install django
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000/` to view the product catalog.
Visit `http://localhost:8000/admin/` to access the admin panel.

### Note on sample data

The repository includes a populated `db.sqlite3` file with 5 categories, 10 tags, and 20 soccer-themed products already added. If you want to start fresh:

1. Delete `db.sqlite3`
2. Run `python manage.py migrate`
3. Run `python manage.py createsuperuser`
4. Log into the admin panel and populate manually

## Project Structure
<img width="519" height="391" alt="Screenshot 2026-04-04 at 11 44 40 PM" src="https://github.com/user-attachments/assets/844efc22-6680-4ac8-a5a3-d8427d959cf2" />


## AI Attribution

Per the Remarcable AI policy, I am documenting AI tool usage transparently.

**What I wrote and understand fully:**
- All models in `models.py` (Category, Tag, Product) including field choices and relationships
- All view logic in `views.py` (queryset filtering, Q objects, GET parameter handling)
- URL routing in both `product_catalog/urls.py` and `products/urls.py`
- Admin registration in `admin.py`
- Template structure (Django template tags `{% for %}`, `{% if %}`, `{{ variable }}`, form inputs, context variable usage)

**Where AI assistance was used:**
- CSS styling in `product_list.html` was scaffolded with AI assistance, since the assignment noted styling is not the focus. I reviewed all CSS, understand the layout (sidebar + grid), and can explain the template logic and how context data flows from view to template.
- Code comments and README formatting were refined with AI assistance.

## Running Tests / Verification

To verify functionality:
1. Visit `localhost:8000/` — should show all 20 products
2. Type "nike" in the search box → should filter to Nike products
3. Select a category from the dropdown → should filter
4. Check multiple tags → should show products with any of the selected tags
5. Combine all three → should progressively narrow results
6. Click "Reset" → returns to full catalog
