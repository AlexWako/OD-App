import requests
import shopify
import pandas as pd
from ShopifyApp import *
from paginate import *
from EditMeasureScript import *

non_jeans = []

for row in df.itertuples(index = False):

    data_list1 = []
    data_list2 = []

    id = eval(row.id) if pd.notna(row.id) else []
    type1 = eval(row._2) if pd.notna(row._2) else []
    type2 = eval(row._3) if pd.notna(row._3) else []

    for measure in type1:
        if len(measure) == 8:
            data_list1.append({'Size': measure[0],'Waist': measure[1], 'Front Rise': measure[2], 'Back Rise': measure[3], 'Upper Thigh': measure[4], 'Knee': measure[5], 'Leg Opening': measure[6], 'Inseam': measure[7]})
        elif len(measure) == 7:
            data_list1.append({'Size': measure[0],'Waist': measure[1], 'Front Rise': measure[2], 'Back Rise': measure[3], 'Upper Thigh': measure[4], 'Leg Opening': measure[5], 'Inseam': measure[6]})
        elif len(measure) == 6:
            data_list1.append({'Size': measure[0],'Waist': measure[1], 'Front Rise': measure[2], 'Upper Thigh': measure[3], 'Leg Opening': measure[4], 'Inseam': measure[5]})
        else:
            non_jeans.append(id[0])
    if type2 != []:
        for measure in type2:
            if len(measure) == 8:
                data_list2.append({'Size': measure[0],'Waist': measure[1], 'Front Rise': measure[2], 'Back Rise': measure[3], 'Upper Thigh': measure[4], 'Knee': measure[5], 'Leg Opening': measure[6], 'Inseam': measure[7]})
            elif len(measure) == 7:
                data_list2.append({'Size': measure[0],'Waist': measure[1], 'Front Rise': measure[2], 'Back Rise': measure[3], 'Upper Thigh': measure[4], 'Leg Opening': measure[5], 'Inseam': measure[6]})
            elif len(measure) == 6:
                data_list2.append({'Size': measure[0],'Waist': measure[1], 'Front Rise': measure[2], 'Upper Thigh': measure[3], 'Leg Opening': measure[4], 'Inseam': measure[5]})
        new_df1 = pd.DataFrame(data_list1)
        new_df2 = pd.DataFrame(data_list2)
        new_df1.to_csv(f'jean_measurements/{id[0]}_1.csv')
        new_df2.to_csv(f'jean_measurements/{id[0]}_2.csv')
    else:
        new_df1 = pd.DataFrame(data_list1)
        new_df1.to_csv(f'jean_measurements/{id[0]}_1.csv')