import pickle

# Loading from a .pkl file


def test_load_model():
    file_loaded = False
    try:
        with open("ml/salary/model.pkl", "rb") as f:
            model = pickle.load(f)
        file_loaded = True
    except:
        pass
    assert file_loaded == True


def test_load_processor():
    file_loaded = False
    try:
        with open("ml/salary/processing.pkl", "rb") as f:
            model = pickle.load(f)
        file_loaded = True
    except:
        pass
    assert file_loaded == True
