from django.db import models


class BotMessage(models.Model):
    user_id = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.user_id} at {self.timestamp}"
