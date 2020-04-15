from django.conf import settings
from django.db import models
from django.utils import timezone

# models.ModelはDjango　Modelだという宣言
class Post(models.Model):
    # CharField : 文字数が制限されたテキストを定義するフィールド
    # TextField : 文字数の制限がないテキストを定義するフィールド
    # DataTimeField : 日付と時間のフィールド
    # ForeignKey : 他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
