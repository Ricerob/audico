from .clip import Clip
import os

class Dataset:
    def __init__(self, labels: list[str] , clips: list[Clip] = []):
        self.labels = labels
        if not labels:
            raise ValueError("labels list must not be empty.")

        # TODO: Check for string "correctness" AKA no empty strings

        self.test = []
        self.train = []
        self.validate = []
        self.clips = clips

    def _check_split_arr(self, split_arr):
        if len(split != 3):
            raise Exception("Split array must contain 3 int values.")
        if sum(split != 100):
            raise Exception("Split array must add to 100.")

    def load_clips_from_dir(self, path: str, label: str) -> list[Clip]:
        '''
            Loads all clips from a directory. Automatically normalizes clips and appends to clips.

            Args:
                path: String representation of path to directory comtaining clips.
                label: Label for dir.

            Returns:
                clips: List of normalized Clips.

            Throws:
                Exception: Path contains no files or given label not a part of dataset labels.
                FileNotFoundError: Path doesn't exist.
        '''

        if not os.path.exists(path):
            raise FileNotFoundError(f"Path {path} doesn't exist.")
        
        contents = os.listdir(path)

        if len(contents) < 1:
            raise Exception(f"Path {path} contains no files.")

        if label not in self.labels:
            raise Exception(f"Given label {label} not a part of defined labels {', '.join(self.labels)}")

        clips = []
        for clip in contents:
            if os.path.isfile(os.path.join(path, clip)):
                try:
                    clips.append(Clip(path=os.path.join(path, clip), label=label))
                except Exception as e:
                    print(f"Could not add clip at {os.path.join(path, clip)}:\n{e}")
                    continue

        if len(clips) < 1:
            raise Exception(f"Not enough clips to create dataset from source {path}.")

        self.clips.append(clips)

        return clips

    def split(self, split: list[int]) -> list[list[Clip]]:
        '''
            Splits loaded-in Clips into a given train/ test/ validate split, represented by 3 integers. Must add to 100.

            Args:
                split: List of 3 integers representing percentages of training splits.

            Returns:
                clip_splits: List of train/ test/ validate Clip lists. Self.clips is maintained.

            Throws:
                Exception: No clips are loaded in, or split isn't formatted correctly.
        '''

        self._check_split_arr(split)

        # TODO


    def reset_splits(self) -> list[Clip]:
        '''
            Resets clips from splits and empties internal splits.

            Returns:
                clips: List of all clips.

            Throws:
                Exception: At least one validation step is empty, or no clips are loaded in.
        '''

        # TODO

    def set_train_clips(self, clips: list[Clip]) -> list[Clip]:
        if len(clips) < 1:
            raise Exception("Clips length must be greater than 0.")

        # TODO

    def set_test_clips(self, clips: list[Clip]) -> list[Clip]:
        if len(clips) < 1:
            raise Exception("Clips length must be greater than 0.")

        # TODO

    def set_validate_clips(self, clips: list[Clip]) -> list[Clip]:
        if len(clips) < 1:
            raise Exception("Clips length must be greater than 0.")

        # TODO


    def get_all_clips(self) -> list[Clip]:
        return self.clips

    def get_train_clips(self) -> list[Clip]:
        return self.train

    def get_test_clips(self) -> list[Clip]:
        return self.test

    def get_validate_clips(self) -> list[Clip]:
        return self.validate