import numpy as np
import ollama
from numpy import array
test=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(test)

response = ollama.chat(model='gemma4:31b-cloud', messages=[
    {
        'role': 'user',
        'content': 'Write a Python function to calculate fibonacci numbers.',
    },
])

print(response['message']['content'])