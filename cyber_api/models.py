from django.db import models
import random 


class Person(models.Model):
    full_name = models.CharField(verbose_name = 'tulliq ismi', max_length=65, blank=True, null=False)
    phone_number = models.CharField(verbose_name = 'tellfon raqam', max_length=20, blank=True, null=True)
    telegram_id = models.CharField(max_length=20)
    district = models.CharField(verbose_name = 'tuman', max_length = 20)
    city = models.CharField(verbose_name='viloyat', max_length=20)
    level = models.IntegerField(verbose_name = 'daraja', default=0)
    # username = models.CharField(max_length=200, null=True, blank=True)

    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    
    class Meta:
        def __str__(self):
            return self.full_name
        

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.TextField()
    img = models.ImageField(upload_to='img/', blank=True, null=True)
    option_type = models.CharField(max_length=200, blank=True, null=True)

    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class QuestionText(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    text = models.TextField()

    def save(self, *args, **kwargs):
        questions = self.text.split('+++++')

        for question_data in questions:
            if question_data.strip():
                parts = question_data.split('=====')
                question_text = parts[0].strip()  # Savol matni
                options = parts[1:]  # Variantlar

                option_data = []
                for option in options:
                    option_text = option.strip()
                    is_correct = option_text.startswith('#')  
                    if is_correct:
                        option_text = option_text[1:]  

                    option_data.append((option_text, is_correct))

                random.shuffle(option_data)

                # Create the question
                question = Question.objects.create(
                    quiz=self.quiz,
                    title=question_text,
                )

                for option_text, is_correct in option_data:
                    Option.objects.create(
                        question=question,
                        text=option_text,
                        is_correct=is_correct
                    )

        super().save(*args, **kwargs)  

    def __str__(self):
        return self.quiz.title


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text



