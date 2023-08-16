import Utility
import Database
import MainWindow
import pandas as pd

def mainLogic(values, skill_to_test):

    success_df = pd.read_csv('success.csv')
    values = Utility.RemoveInnerList(values)
    skill_to_test_value = values[-1]
    has_succeded = True
    roll_differences, rolls = Utility.CompareStats(values[:-1])
    terrible_roll = False
    great_roll = False

    for value in roll_differences:
        if value < 0:
            if (skill_to_test_value + value) > 0:
                skill_to_test_value = skill_to_test_value + value
            else:
                has_succeded = False
    
    for value in rolls:
        if value == 20:
            terrible_roll = True
            has_succeded = False
        elif value == 1:
            great_roll = True
            has_succeded = True



    quality = 0
    if has_succeded == True:
        index = success_df[success_df['Key'] == 'success'].index
        success_df.loc[index, 'Value'] += 1
        success_df.to_csv('success.csv', index=False)
        j = 0
        for i in range(7):
            j = j + 3
            if j >= 16:
                quality = 6
                break
            elif skill_to_test_value >= j :
                quality = quality + 1
            else:
                break
    else:
        index = success_df[success_df['Key'] == 'failed'].index
        success_df.loc[index, 'Value'] += 1
        success_df.to_csv('success.csv', index=False)
        
    
    

    MainWindow.mainWindow(skill_to_test, True, quality, has_succeded, terrible_roll, great_roll, items= [])
    


    
    
    


        


            
            
            

            








