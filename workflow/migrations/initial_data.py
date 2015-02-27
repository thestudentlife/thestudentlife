from django.contrib.auth.models import Permission, User, Group, ContentType

article_type = ContentType.objects.get(app_label="auth", model="user")
assignment_perm=Permission(name="assignment",content_type=article_type,codename="assignment")
assignment_perm.save()

post_type = ContentType.objects.get(app_label="auth", model="user")
post_perm=Permission(name="post",content_type=post_type,codename="post")
post_perm.save()

edit_type = ContentType.objects.get(app_label="auth", model="user")
edit_perm=Permission(name="edit",content_type=edit_type,codename="edit")
edit_perm.save()



