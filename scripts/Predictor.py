import tensorflow as tf
import os

"""
This script uses the model in the "model" folder and makes predictions
with a certain accuracy
"""

def get_current_path(path_to_stop=""):
    full_path = ""
    before_path = __file__.split('\\')
    for path in before_path:
        if path != path_to_stop:
            if path != os.path.splitext(os.path.basename(__file__))[0] + ".py":
                full_path += path
                full_path += "\\"
        else:
            break
    return full_path


def load_model(path = ""):
    """
    Loads any .SavedModel file from the given path
    :param path: Path in which the function will search for models
    :return: The model as a tensorflow object?
    """
    if(len(os.listdir(path)) <= 1):
        print("Loading Model")
        return tf.keras.models.load_model(path)
    else:
        raise Exception("The model folder has more than 1 file")

def predictor(model, data_path):
    for file in os.listdir(data_path):
        return file ,model.predict(get_current_path("scripts") + "dataset/" + file)

test_data_path = get_current_path("scripts") + "dataset/test"

if __name__ == '__main__':
    main_model = load_model(path = get_current_path("scripts") + "model")
    name, result = predictor(main_model,test_data_path)
    print("The file is", name, "With result ", result)