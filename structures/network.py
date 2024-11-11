import numpy as np

import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import layers

from PyQt5.QtCore import QObject, pyqtSignal

import os

LOCAL = os.path.dirname(os.path.abspath(__file__))

TRAINING_DATA = "/../data/training"
TESTING_DATA = "/../data/testing"

class Network(QObject):

  log = pyqtSignal(str)
  training = pyqtSignal()

  def __init__(self):
    super(QObject, self).__init__()

  def train(self):
    if not os.path.isdir(os.path.join(LOCAL, TRAINING_DATA)):
      self.log("No training directory was found in 'data/'. Unable to initiate training.")
      #!Pop up alert here too
      return


  def predict(self):
    if not os.path.isdir(os.path.join(LOCAL, TESTING_DATA)):
      self.log("No testing directory was found in 'data/'. Unable to initiate training.")
      #!Pop up alert here too
      return