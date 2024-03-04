import pickle
import numpy as np
import config
import json



def get_predicted_emission(Plant,Type,Treatment,conc,uptake):

    print('Plant,Type,Treatment,conc,uptake',Plant,Type,Treatment,conc,uptake)
    model_file_path = config.MODEL_FILE_PATH

    with open(model_file_path, 'rb') as f:
        model = pickle.load(f)

    with open(config.COLUMN_DATA_JSON, 'r') as f:
        col_data = json.load(f)

    col_names = model.feature_names_in_


    #region_index = np.where(col_names == 'region_'+ region)[0][0]
    # print("region_index",region_index)

    #gender = col_data['gender'][gender]
    #smoker = col_data['smoker'][smoker]

   # test_array = np.zeros((1,model.n_features_in_))
    #test_array[0,0] = age
    #test_array[0,1] = gender
    #test_array[0,2] = bmi
    #test_array[0,3] = children
   # test_array[0,4] = smoker
    #test_array[0,region_index] = 1

   # predicted_price = model.predict(test_array)
    #print("predicted_price :",predicted_price)

    #return predicted_price
   col_data = pd.DataFrame({
    'Plant': ['Qn1']*5 + ['Mc3']*5,
    'Type': ['Quebec']*5 + ['Mississippi']*5,
    'Treatment': ['nonchilled']*5 + ['chilled']*5,
    'conc': [95, 175, 250, 350, 500]*2,
    'uptake': [16.0, 30.4, 34.8, 37.2, 35.3, 17.9, 17.9, 17.9, 17.9, 17.9]
})

Type = 'Quebec'
Treatment = 'nonchilled'
conc = 95

# Filter the DataFrame based on conditions
subset = col_data[(col_data['Type'] == Type) & (col_data['Treatment'] == Treatment) & (col_data['conc'] == conc)]

# Check if any rows match the conditions
if not subset.empty:
    # Assuming you want the first row, you can access the 'uptake' value
    uptake_value = subset['uptake'].values[0]
    print('Predicted Emission:', uptake_value)
else:
    print('No matching data found for the given conditions.')