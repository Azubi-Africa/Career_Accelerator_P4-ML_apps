import pickle
import os


DIRPATH = os.path.dirname(os.path.realpath(__file__))


ML_SALARY_DIR = os.path.join(
    DIRPATH,
    "..",
    "..",
    "ml",
    "salary",
)
# Loading from a .pkl file


def test_load_model():
    file_loaded = False
    try:
        with open(os.path.join(ML_SALARY_DIR, "model.pkl"), "rb") as f:
            model = pickle.load(f)
        file_loaded = True
    except:
        pass
    assert file_loaded == True


def test_load_processor():
    file_loaded = False
    try:
        with open(os.path.join(ML_SALARY_DIR, "processing.pkl"), "rb") as f:
            processor = pickle.load(f)
        file_loaded = True
    except:
        pass
    assert file_loaded == True
