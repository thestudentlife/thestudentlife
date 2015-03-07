from django.contrib.auth.models import Permission, User, Group, ContentType

plastic = Group(name="plastic")
plastic.save()

bronze = Group(name="bronze")
bronze.save()

silver = Group(name="silver")
silver.save()

gold = Group(name="gold")
gold.save()

kent = User(username="kshikama")
kent.set_password("tsl")
kent.save()
kent.groups.add(gold, silver, bronze, plastic)

zq = User(username="zxiong")
zq.set_password("tsl")
zq.save()
zq.groups.add(gold, silver, bronze, plastic)

latina = User(username="vlatina")
latina.set_password("tsl")
latina.save()
latina.groups.add(gold, silver, bronze, plastic)