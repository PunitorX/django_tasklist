from django.db import models

# Representing a database model
class Todo(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False) # Completion status of the item
  created_at = models.DateTimeField(auto_now=True) # Timestamp auto set to the current date and time

  # Returns a string representation of the Todo object, to display meaningful info
  def __str__(self):
    return self.title