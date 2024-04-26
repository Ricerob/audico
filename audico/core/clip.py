from numpy import (
    ndarray
)
import librosa
import tensorflow as tf
import numpy as np
# from tensorflow import (
#     # squeeze,
#     # cast,
#     # int64,
#     # Tensor,
#     convert_to_tensor
# )

import os

accepted_formats = ["wav", "mp3"]

class Clip:
    '''
        Clip instance. Represents one audio file.
    '''

    def __init__(self, path: str, label: list = None, skip_preprocessing: bool = False):
        self.path = path                                # String representation of path
        self.state = 'unprocessed'                      # For future multithreading applications.
        self.sr = 0                                     # Sample rate of clip.
        self.duration = 0.0                             # Float of duration for clip.
        self.spectrogram = None                         # Spectrogram representation of clip. Optional.
        self.labels = labels                            # Included labels for this clip.
        self.skip_preprocessing = skip_preprocessing    # Optionally skip preprocessing used for ML applications.

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found at path: {path}")

        file_extension = path.split(".")[-1].lower()
        
        if file_extension not in accepted_formats:
            raise Exception(f"File at {path} not in accepted formats: {', '.join(accepted_formats)}.")

        # TODO: If skip_preprocessing not True, preprocess using load_bytes_to_16k_mono
        if skip_preprocessing == False:
            self.state = 'processing'
            self.tensor, self.sr = self._load_audio_data(path)
            self.duration = len(self.tensor) / self.sr
            self.normalize_16k_mono(self.tensor, self.sr)
            self.state = 'processed'

    def _load_audio_data(self, path: str) -> (tf.Tensor, int):
        '''
            Loads data from path. Assumes format is in accepted format list. MP3 or WAV.

            Args:
                path: String representation of path to clip from root_path environment variable

            Returns:
                audio_tensor: tf.Tensor object representing the tensor.
                sample_rate: int of sample rate.

            Throws:
                Exception: If an error occurs while loading the data.
        '''
        
        try:
            data, sample_rate = librosa.load(path, sr=None)
            audio_tensor = tf.convert_to_tensor(data, dtype=tf.float32)
        except Exception as e:
            raise Exception(e)

        return (audio_tensor, sample_rate)

    def normalize_16k_mono(self, tensor: tf.Tensor, sr: int) -> None:
        '''
            Normalizes data to mono channel, 16k amplitude. Needed for machine learning applications.
            Sets self.tensor to normalized Tensor.
            Note: Because we're using Librosa to load in data, mono is default. It averages multichannel audio to mono.

            Args:
                tensor: tf.Tensor representation of data.
                sr: Original sample rate.

            Throws:
                Exception: If an error occurs while formatting the data.
        '''

        try:
            # Convert to nparray
            nparr = tensor.numpy()

            normalized_tensor = librosa.resample(nparr, orig_sr=sr, target_sr=16000)

            # Convert back to Tensor
            normalized_tensor = tf.convert_to_tensor(normalized_tensor)

            self.tensor = normalized_tensor

        except Exception as e:
            raise Exception(f"Exception while preprocessing data: {e}")


    def get_tensor(self):
        return self.tensor