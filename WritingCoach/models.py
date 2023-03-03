from django.db import models

class WritingCoach(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

import tensorflow
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("anujraymajhi/t5-GEC-128len-9e")
model = AutoModelForSeq2SeqLM.from_pretrained("anujraymajhi/t5-GEC-128len-9e")

def predict_error(sentence):
    input_ids = tokenizer.encode(sentence, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=False)
    output = tokenizer.decode(outputs[0])
    return output