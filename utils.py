import pickle
import numpy as np

with open(r"static/model_file/linear_regression.pkl","rb") as f:
    model = pickle.load(f)

def get_concrete_strength(cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age):
    test_array = np.zeros([1,model.n_features_in_])
    test_array[0,0] = cement
    test_array[0,1] = blast_furnace_slag
    test_array[0,2] = fly_ash
    test_array[0,3] = water
    test_array[0,4] = superplasticizer
    test_array[0,5] = coarse_aggregate
    test_array[0,6] = fine_aggregate
    test_array[0,7] = age

    predict_concrete_strength = np.around(model.predict(test_array)[0],7)
    return predict_concrete_strength