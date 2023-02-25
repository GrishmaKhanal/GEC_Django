from django.db import models

class WritingCoach(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# import for ml
import tensorflow as tf
import pickle, re
import numpy as np

def load_model():
    model_path = 'ml_models/model.h5'
    tokenizer_path = 'ml_models/tokenizer.pkl'

    with open(tokenizer_path, 'rb') as handle:
        tokenizer = pickle.load(handle)
    model = tf.keras.models.load_model(model_path)
    return model, tokenizer

def predict_error(text):
    MAX_SEQUENCE_LENGTH = 32
    model, tokenizer = load_model()
    sequence = tokenizer.texts_to_sequences([text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post', truncating='post')
    
    # generate prediction and convert it to text
    prediction = model.predict(padded)
    output = tokenizer.sequences_to_texts([prediction])[0]
    return output

# def correct_sentence(sentence):
#     sequence = tkn_all.texts_to_sequences([start_token + " " + sentence + " " + stop_token])
#     padded = pad_sequences(sequence, maxlen=inc_train_seq.shape[1], padding = 'post', truncating = 'post')
#     encoded = model.predict(padded)
#     y = np.argmax(encoded, axis = 2)
#     y = np.reshape(y, (1,32))
#     decoded = []
#     decoded_np = np.ndarray(32)
#     for i in range(encoded.shape[1]):
#         word_index = np.argmax(encoded[0, i, :])
#         decoded_np = np.append(decoded_np,word_index)
#         if word_index > 0:
#             decoded.append(tkn_all.index_word[word_index])
#             if word_index == tkn_all.word_index[stop_token]:
#                 break
#         else:
#             decoded.append('<OOV>')
#     return ' '.join(decoded)