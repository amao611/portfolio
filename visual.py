import json
from watson_developer_cloud import VisualRecognitionV3

# Create an instance of your Watson Visual Recognition service
instance = VisualRecognitionV3(version='2016-05-20', api_key='08123ad43281dc729ecae62287a2582c2e37494f')

# Classify the image using Watson Visual Recognition
img = instance.classify(images_url='https://gm1.ggpht.com/5rrJuVvsrCfbImo5Hs7013xGOhILqrIKFeNIDbvOfqOQhFUuM-TodJV4b1AD4sdGZ7foz8tIZzf0khbM_QVAL2UD1A5SqRxtNiv1nOb8hNjLv_tGgT-uRZ4zuqKWS3OCX9OYJfXJb9zNQ46tAIaB46s5phUBc95B2vpvwZaa8UyBtOh_dBRs7C8xeYAHWKcI4LQ3FfZR8xxDI47joby8Lk6g_0vrtvDiAdjRogQPWqEYZmNX0OdeDpdqmKdCLgh9A2syILSC6l-2yxs7xQeHhW_Cwt8m7bGcBN531Y0YHPVQj4IgSlsboswjlZ5QoHOUGGrK4q1Im5qndkIxXAqSGcxtW3EW65uZnFpVuspmXBrpxwgpCYhNEafUcyCv5L_9d3HQMaIfx7NlkPLFh5h-RsPRCqx5IFjQxwrvt5Jn3adRWz0SbePHYdno8NxESAMYVfwEDg7h278-OIgdvzxu_DpPe3kwFW0atFDbus8hAcowztQ1xVQOkBM2SrveFMoWEC9dGXO_CBcLS6hEYLaeofvvhTNoHwZu0KoU_UHEXe6IyGAj2H5HC91zJTkXKXw0wc03McosITEWccNnfYr42jUnwT1Ql1ZlB_LZx5KLnH54kpdoe6Az14zBhpmPzXHCgRzSyivckvqSEoFh2LMwYy6QzHIP33xxaRFdICWIcvFS99HWOkN1GI7tlHv9A6vEYZ5XKymHQhxIAzMadDGWquEo=s0-l75-ft-l75-ft')

# Print the JSON results
#print(json.dumps(img, indent=2))

# Format the results to be more readable
for results in img['images'][0]['classifiers'][0]['classes']:
    print('\n There is a ' + str(round((results['score']*100),1)) + ' percent chance the image contains: '+ results['class'])
