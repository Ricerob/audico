from numpy import (
    ndarray
)
from tensorflow.io import (
    read_file
)
# from tensorflow.audio import (
#     decode_mp3,
#     decode_wav
# )

import os

class Clip:
    '''
        Clip instance. Represents one audio file.
    '''

    def __init__(self, path: str, labels: list = None, skip_preprocessing: bool = False):
        self.path = path
        self.state = 'unprocessed'
        self.sr = 0
        self.duration = 0.0
        self.spectrogram = None
        self.labels = labels
        self.skip_preprocessing = skip_preprocessing
        # TODO: Load in data, given format is accepted.
        self.raw_data = self._load_audio_data(path)

        # TODO: If skip_preprocessing not True, preprocess using load_bytes_to_16k_mono

    def _load_audio_data(self, path: str) -> bytes:
        '''
            Loads data from path. Assumes format is in accepted format list. MP3 or WAV.

            Args:
                path: String representation of path to clip from root_path environment variable

            Returns:
                bytes: Bytes object representing the loaded-in audio object.

            Throws:
                FileNotFoundError: If the file is not found at the given path.
                Exception: If an error occurs while loading the data.
        '''

        full_path = os.path.join(os.getenv("ROOT_PATH"), path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found at path: {full_path}")
        
        try:
            data = read_file(full_path)
        except Exception as e:
            raise Exception(e)

        # If can't load, throw error
        return data

    def load_bytes_to_16k_mono(self, data: bytes) -> None:
        print('placeholder')

    def return_bytes(self) -> bytes:
        return self.raw_data