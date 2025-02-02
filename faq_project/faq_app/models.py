from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()
    question_hi = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer_bn = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            translator = Translator()
            try:
                # Hindi translations
                self.question_hi = translator.translate(self.question_en, dest='hi').text
                self.answer_hi = translator.translate(self.answer_en, dest='hi').text
            except:
                self.question_hi = self.question_en
                self.answer_hi = self.answer_en
            
            try:
                # Bengali translations
                self.question_bn = translator.translate(self.question_en, dest='bn').text
                self.answer_bn = translator.translate(self.answer_en, dest='bn').text
            except:
                self.question_bn = self.question_en
                self.answer_bn = self.answer_en
        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question_en)

    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer_en)