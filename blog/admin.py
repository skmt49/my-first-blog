from django.contrib import admin
# models.pyで定義したクラス
from .models import Post

# Register your models here.
# モデルを管理画面で見えるようにする
admin.site.register(Post)
