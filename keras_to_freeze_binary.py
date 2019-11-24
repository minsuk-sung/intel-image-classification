#
#     Copywrite 2017 Alan Steremberg and Arthur Conner
#revised hoesungryu

import argparse
from keras import backend as K
from keras.models import load_model
#from tensorflow_serving.session_bundle import exporter
from keras.models import model_from_config
from keras.models import Sequential,Model
import tensorflow as tf
import os   
from tensorflow.python.framework import graph_io

def convert(prevmodel,export_path):#,freeze_graph_binary):

   # open up a Tensorflow session
   sess = tf.Session()
   # tell Keras to use the session
   K.set_session(sess)

   # From this document: https://blog.keras.io/keras-as-a-simplified-interface-to-tensorflow-tutorial.html
   
   # let's convert the model for inference
   K.set_learning_phase(0)  # all new operations will be in test mode from now on
   # serialize the model and get its weights, for quick re-building
   previous_model = tf.keras.models.load_model(prevmodel)
   previous_model.summary()

   config = previous_model.get_config()
   weights = previous_model.get_weights()

   # re-build a model where the learning phase is now hard-coded to 0
   try:
     model = tf.keras.models.Sequential.from_config(config)
     #model = Sequential.from_config(config)
   except:
     model= Model.from_config(config) 
   #model= model_from_config(config)
   model.set_weights(weights)

   print("Input name:")
   print(model.input.name)
   print("Output name:")
   print(model.output.name)
   output_name=model.output.name.split(':')[0]
   frozen = tf.compat.v1.graph_util.convert_variables_to_constants(sess, sess.graph_def, [output_name])
   #frozen = tf.graph_util.convert_variables_to_constants(sess, sess.graph_def, [output_name])
   graph_io.write_graph(frozen, './', export_path + '.pb', as_text=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Keras Tensorflow Converter')
    parser.add_argument(
        'model',
        type=str,
        help='Path to the keras model'
    )
    parser.add_argument(
        'frozen',
        type=str,
        help='Path to the frozen output'
    )    
    args = parser.parse_args()    
    convert(args.model,args.frozen)
    print('COMPLETE CONVERTING h5 to pb FILE')
