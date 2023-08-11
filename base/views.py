# your_app_name/views.py

from django.shortcuts import render
import tensorflow as tf
from PIL import Image
import numpy as np
from sklearn.metrics import f1_score

# Register custom metric function
def F1_score(y_true, y_pred):
    # Implement your custom F1 score function here
    # Make sure to follow the format: F1 = ...

    return "hop s"

class_names = ['air hockey',
 'ampute football',
 'archery',
 'arm wrestling',
 'axe throwing',
 'balance beam',
 'barell racing',
 'baseball',
 'basketball',
 'baton twirling',
 'bike polo',
 'billiards',
 'bmx',
 'bobsled',
 'bowling',
 'boxing',
 'bull riding',
 'bungee jumping',
 'canoe slamon',
 'cheerleading',
 'chuckwagon racing',
 'cricket',
 'croquet',
 'curling',
 'disc golf',
 'fencing',
 'field hockey',
 'figure skating men',
 'figure skating pairs',
 'figure skating women',
 'fly fishing',
 'football',
 'formula 1 racing',
 'frisbee',
 'gaga',
 'giant slalom',
 'golf',
 'hammer throw',
 'hang gliding',
 'harness racing',
 'high jump',
 'hockey',
 'horse jumping',
 'horse racing',
 'horseshoe pitching',
 'hurdles',
 'hydroplane racing',
 'ice climbing',
 'ice yachting',
 'jai alai',
 'javelin',
 'jousting',
 'judo',
 'lacrosse',
 'log rolling',
 'luge',
 'motorcycle racing',
 'mushing',
 'nascar racing',
 'olympic wrestling',
 'parallel bar',
 'pole climbing',
 'pole dancing',
 'pole vault',
 'polo',
 'pommel horse',
 'rings',
 'rock climbing',
 'roller derby',
 'rollerblade racing',
 'rowing',
 'rugby',
 'sailboat racing',
 'shot put',
 'shuffleboard',
 'sidecar racing',
 'ski jumping',
 'sky surfing',
 'skydiving',
 'snow boarding',
 'snowmobile racing',
 'speed skating',
 'steer wrestling',
 'sumo wrestling',
 'surfing',
 'swimming',
 'table tennis',
 'tennis',
 'track bicycle',
 'trapeze',
 'tug of war',
 'ultimate',
 'uneven bars',
 'volleyball',
 'water cycling',
 'water polo',
 'weightlifting',
 'wheelchair basketball',
 'wheelchair racing',
 'wingsuit flying']


def predict_image(request):
    # Load the saved model
    model_path = "/home/nortln/sports/saved_model/EfficientNetB0-100-(224 X 224)- 98.40.h5"

    # Register the custom metric function before loading the model
    model = tf.keras.models.load_model(
    "/home/nortln/sports/saved_model/EfficientNetB0-100-(224 X 224)- 98.40.h5",
    custom_objects={'F1_score': F1_score})

    context = {'prediction': None}


    if request.method == 'POST' and request.FILES['image']:

        uploaded_image = request.FILES['image']


        img = Image.open(uploaded_image)
        height = 224
        width = 224

        img = img.resize((width, height))
        img_array = np.array(img)

        prediction = model.predict(tf.expand_dims(img_array, axis=0))


        f1 = "hello"


        prediction = np.argmax(prediction)
        print(prediction)
        prediction = class_names[prediction]
        print(prediction)




        # Pass the prediction result and F1 score to the template context
        context = {'prediction': prediction}



    return render(request, 'home.html', context)
