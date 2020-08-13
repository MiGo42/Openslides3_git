# Generated by Finn Stutzenstein on 2020-08-25 10:22

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import migrations

from openslides.users.models import Group


def add_permission_to_delegates(apps, schema_editor):
    """
    Adds the permissions `can_see_autopilot` to the delegate group.
    """
    Projector = apps.get_model("core", "Projector")

    try:
        delegate = Group.objects.get(name="Delegates")
    except Group.DoesNotExist:
        return

    content_type = ContentType.objects.get_for_model(Projector)
    try:
        perm = Permission.objects.get(
            content_type=content_type, codename="can_see_autopilot"
        )
    except Permission.DoesNotExist:
        perm = Permission.objects.create(
            codename="can_see_autopilot",
            name="Can see the autopilot",
            content_type=content_type,
        )

    delegate.permissions.add(perm)
    delegate.save()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0034_amendment_projection_defaults"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projector",
            options={
                "default_permissions": (),
                "permissions": (
                    ("can_see_projector", "Can see the projector"),
                    ("can_manage_projector", "Can manage the projector"),
                    ("can_see_frontpage", "Can see the front page"),
                    ("can_see_livestream", "Can see the live stream"),
                    ("can_see_autopilot", "Can see the autopilot"),
                ),
            },
        ),
        migrations.RunPython(add_permission_to_delegates),
    ]
