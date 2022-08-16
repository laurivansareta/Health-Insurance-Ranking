import pickle
import numpy as np
import pandas as pd

class HealthInsurance(object):
    def __init__( self ):
        print('__init__')
        self.home_path = ''

        # Standardization
        self.annual_premium_scaler = pickle.load(open(self.home_path + 'features/annual_premium_scaler.pkl', 'rb'))
        # Rescaling
        self.age_scaler = pickle.load(open(self.home_path + 'features/age_scaler.pkl', 'rb'))
        self.vintage_scaler = pickle.load(open(self.home_path + 'features/vintage_scaler.pkl', 'rb'))
        # Encoder
        self.target_encode_gender_scaler = pickle.load(open(self.home_path + 'features/target_encode_gender_scaler.pkl', 'rb'))
        self.target_encode_region_code_scaler = pickle.load(open(self.home_path + 'features/target_encode_region_code_scaler.pkl', 'rb'))
        self.te_policy_sales_chanel_scaler = pickle.load(open(self.home_path + 'features/te_policy_sales_chanel_scaler.pkl', 'rb'))
        
    def data_cleaning( self, df1 ):
        cols_new = ['id', 'gender', 'age', 'driving_license', 'region_code',
                    'previously_insured', 'vehicle_age', 'vehicle_damage', 'annual_premium',
                    'policy_sales_channel', 'vintage', 'response']
        df1.columns = cols_new
        
        return df1
        
    def feature_engineering( self, df2):
        # Vehicle age
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'over_2_years' if x=='> 2 Years' else 'between_1_2_year' 
                                                        if x=='1-2 Year' else 'below_1_year')

        # vehicle damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 1 if x=='Yes' else 0)

        return df2
        
    def data_preparation( self, df5 ):
        print('data_preparation')

        # annual_premium
        df5['annual_premium'] = self.annual_premium_scaler.transform(df5[['annual_premium']].values)

        # Age
        df5['age'] = self.age_scaler.transform(df5[['age']].values)

        # vintage
        df5['vintage'] = self.vintage_scaler.transform(df5[['vintage']].values)

        # gender -> One Hot Encoding / Frequency Encoding        
        df5.loc[:, 'gender'] = df5['gender'].map(self.target_encode_gender_scaler)

        # region_code -> Target Encoding / Frequency Encoding / Weighted Target Encoding        
        df5.loc[:, 'region_code'] = df5['region_code'].map(self.target_encode_region_code_scaler)

        # vehicle_age -> One Hot Encoding / Order Encoding / Frequency Encoding 
        df5 = pd.get_dummies(df5, prefix='vehicle_age', columns=['vehicle_age'])

        # policy_sales_channel - > Frequency Encoding / Target Encoding
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map(self.te_policy_sales_chanel_scaler)

        cols_selected = ['annual_premium', 'vintage', 'age', 'region_code', 'vehicle_damage', 'previously_insured',
                 'policy_sales_channel']

        return df5[cols_selected]
        
    def get_prediction(self, model, original_data, test_data):
        # print('get_prediction')
        # print('original_data:\n', original_data)
        # print('test_data:\n', test_data)
        # Model
        pred = model.predict_proba(test_data)

        # Une a predição com dados originais
        original_data['score'] = pred[:, 1].tolist()

        return original_data.to_json(orient='records', date_format='iso')