# 📝 Blog Post Feature – Django CRUD

This module provides full CRUD functionality for blog posts using Django's class-based views and Django REST Framework (DRF). It supports both HTML-rendered views and RESTful API endpoints.

---

## 🚀 Features

### Web Views (HTML)
- **List Posts**: `/posts/` – View all blog posts.
- **Create Post**: `/posts/new/` – Authenticated users can create a post.
- **View Post**: `/posts/<int:pk>/` – View details of a single post.
- **Edit Post**: `/posts/<int:pk>/edit/` – Only the post author can edit.
- **Delete Post**: `/posts/<int:pk>/delete/` – Only the post author can delete.

### API Endpoints (JSON)
- **List & Create**: `GET/POST /api/posts/`
- **Retrieve, Update, Delete**: `GET/PUT/DELETE /api/posts/<int:pk>/`

---

## 🔐 Permissions

- **Create**: Only authenticated users can create posts.
- **Edit/Delete**: Only the author of a post can edit or delete it.
- **View/List**: Accessible to all users, including unauthenticated visitors.

---

## 🧩 Data Handling

- `author` field is automatically set to the logged-in user during creation.
- `created_at` is auto-generated on post creation.
- API responses include `author_username` for clarity.

---

## 🛠 Setup Instructions

1. Add `'blog'` and `'rest_framework'` to `INSTALLED_APPS`.
2. Include `blog.urls` in your `project/urls.py`.
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`.
4. Create templates in `templates/blog/`.
5. Use Django admin or API to manage posts.

---

## 📄 Notes

- Uses `LoginRequiredMixin` and `UserPassesTestMixin` for access control.
- API views use DRF’s `GenericAPIView` with custom `perform_create`, `perform_update`, and `perform_destroy` methods.
- Form validation includes minimum title length check.

---

## ✅ To Do / Extensions

- Add pagination to list views.
- Integrate rich text editor (e.g., CKEditor).
- Add tags or categories.
- Implement search and filtering.
