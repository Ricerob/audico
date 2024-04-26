from clips import Clips

class Dataset:
    def __init__(self, classifiers: list[str] , clips: list[Clips] = []):
        self.classifiers = classifiers
        if not classifiers:
            raise ValueError("Classifiers list must not be empty")
        if len(classifiers) == 1:
            self.classification_type = "binary"
        else:
            self.classification_type = "multi"

        self.test = []
        self.train = []
        self.validate = []
        self.clips = clips

    def _check_split_arr(self, split_arr):
        if len(split != 3):
            raise Exception("Split array must contain 3 int values.")
        if sum(split != 100):
            raise Exception("Split array must add to 100.")

    def load_clips_from_dir(self, path: str, split: list[int]) -> None:
        self._check_split_arr(split)

        # TODO

    def split(self, split: list[int]) -> list[list[Clips]]:
        self._check_split_arr(split)

        # TODO

    def set_train_clips(self, clips: list[Clips]) -> list[Clips]:
        if len(clips) < 1:
            raise Exception("Clips length must be greater than 0.")

        # TODO

    def set_test_clips(self, clips: list[Clips]) -> list[Clips]:
        if len(clips) < 1:
            raise Exception("Clips length must be greater than 0.")

        # TODO

    def set_validate_clips(self, clips: list[Clips]) -> list[Clips]:
        if len(clips) < 1:
            raise Exception("Clips length must be greater than 0.")

        # TODO


    def get_all_clips(self) -> list[Clips]:
        return self.clips

    def get_train_clips(self) -> list[Clips]:
        return self.train

    def get_test_clips(self) -> list[Clips]:
        return self.test

    def get_validate_clips(self) -> list[Clips]:
        return self.validate