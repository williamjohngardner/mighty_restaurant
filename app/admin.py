from django.contrib import admin
from app.models import MenuItem, Category, Position, Profile, Order

admin.site.register(MenuItem),
admin.site.register(Category),
admin.site.register(Position),
admin.site.register(Profile),
admin.site.register(Order)
