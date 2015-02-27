from django.contrib.auth.models import Permission, User, Group, ContentType

article_type = ContentType.objects.get(app_label="auth", model="user")
assignment_perm = Permission(name="assignment",content_type=article_type,codename="assignment")
assignment_perm.save()

post_type = ContentType.objects.get(app_label="auth", model="user")
post_perm = Permission(name="post",content_type=post_type,codename="post")
post_perm.save()

edit_type = ContentType.objects.get(app_label="auth", model="user")
edit_perm = Permission(name="edit",content_type=edit_type,codename="edit")
edit_perm.save()

manage_type = ContentType.objects.get(app_label="auth", model="user")
manage_perm = Permission(name="manage",content_type=edit_type,codename="manage")
manage_perm.save()

bronze = Group(name="bronze")
bronze.save();
bronze.permissions.add(assignment_perm, post_perm)

silver = Group(name="silver")
silver.save();
silver.permissions.add(assignment_perm, post_perm, edit_perm)

gold = Group(name="gold")
gold.save();
gold.permissions.add(assignment_perm, post_perm, edit_perm, manage_perm);

kent = User(username="kshikama")
kent.save()
kent.groups.add(gold)

zq = User(username="zxiong")
zq.save()
zq.groups.add(gold)

latina = User(username="vlatina")
latina.save()
latina.groups.add(gold)