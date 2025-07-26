from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        # Create groups and permissions
        editors_group, _ = Group.objects.get_or_create(name='Editors')
        content_type = ContentType.objects.get_for_model(Book)

        permissions = [
            ("can_create_book", "Can create book"),
            ("can_edit_book", "Can edit book"),
        ]

        for perm in permissions:
            permission, _ = Permission.objects.get_or_create(
                codename=perm[0],
                name=perm[1],
                content_type=content_type,
            )
            editors_group.permissions.add(permission)
        editors_group.save()

        viewers_group, _ = Group.objects.get_or_create(name='Viewers')
        content_type = ContentType.objects.get_for_model(Book)

        permissions = [
            ("can_view_book", "Can view book"),
        ]

        for perm in permissions:
            permission, _ = Permission.objects.get_or_create(
                codename=perm[0],
                name=perm[1],
                content_type=content_type,
            )
            viewers_group.permissions.add(permission)
        viewers_group.save()

        admins_group, _ = Group.objects.get_or_create(name='Admins')
        content_type = ContentType.objects.get_for_model(Book)

        permissions = [
            ("can_view_book", "Can view book"),
            ("can_create_book", "Can create book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

        for perm in permissions:
            permission, _ = Permission.objects.get_or_create(
                codename=perm[0],
                name=perm[1],
                content_type=content_type,
            )
            admins_group.permissions.add(permission)
        admins_group.save()