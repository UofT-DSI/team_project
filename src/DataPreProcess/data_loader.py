import pandas as pd
import os
import logging

class DataLoader:

    rawData_filepath = "../data/raw/"
    processedData_filepath = "../data/processed/"

    def __init__(self, filename = 'credit_risk_dataset', extension = '.csv'):
        logging.basicConfig(filename='../log/app.log', format='%(asctime)s - %(levelname)s - %(message)s')
        self.filename = filename
        self.extension = extension
        
    def preProcessData(self):
        ''' Performs data extraction, transformation and loading process '''
        logging.info(f"Starting data ETL process...") 

        # Extract data
        df = self.extract_dataset()

        # Transform data
        df = self.transform_dataset(df)

        # Load processed data
        df = self.load_dataset(df)

        logging.info(f"Data ETL process completed.") 
        return df

    def extract_dataset(self):
        ''' Performs data extraction process '''
        logging.info(f"Starting data extraction process...") 

        # Specify the path to load the CSV file
        file_path = self.rawData_filepath + self.filename + self.extension
        print(file_path)

        # check if file path exists
        if (self.checkIfFilePathExists(file_path) == False):
            return

        # Read the file into a DataFrame
        if (self.extension == '.csv'):
            df = pd.read_csv(file_path)
        elif (self.extension == '.xlsx'):
            df = pd.read_excel(file_path)
        elif (self.extension == '.json'):
            df = pd.read_json(file_path)
        
        # return the dataset as dataframe
        logging.info(f"The file has been extracted to a Data frame.\\n")
        print(df.head)
        return df
    
    def transform_dataset(self, df):
        ''' Performs data transformation process '''
        logging.info(f"Starting data cleaning and transformation process...")
        try:
            # If data frame is empty return
            if df.empty:
                logging.error("DataFrame is empty")
                return

            # Remove rows with any missing values
            df.dropna(inplace=True)
            logging.info(f"dropping rows with nan or null")

            # Remove Duplicates
            df.drop_duplicates(inplace=True)
            logging.info(f"dropping duplicate rows")

            # Remove outliers based on condition (e.g., values greater than a threshold)
            df = df[df['person_emp_length'] > 50]  # person with employment length in years over 50
            logging.info(f"removing outliers")

            # Rename Columns
            df.rename(columns={'cb_person_cred_hist_length': 'person_credit_history'}, inplace=True)
            df.rename(columns={'cb_person_default_on_file': 'person_credit_default'}, inplace=True)
            logging.info(f"renaming columns")

            # Convert column values to specific type (e.g., 'int', 'float', 'str')
            df['person_credit_default'] = df['person_credit_default'].map({'Y': 1, 'N': 0}) # person credit default value from Y/N to 0 or 1
            logging.info(f"mapping data values")

        except Exception as ex:
            print('Data cleaning failed')
            logging.exception(ex)

        print('The Dataset cleaning and transforming completed\\n')
        return df
    
    def load_dataset(self, df):
        ''' Performs data loading process '''
        logging.info(f"Starting data loading process...") 
        processed_file_path = self.processedData_filepath + self.filename + "_processed" + self.extension

        # check if file path exists
        if (self.checkIfFilePathExists(processed_file_path)):
          
            # Save the cleaned DataFrame to a new CSV file in processed folder
            df.to_csv(processed_file_path, index=False)
            print('The processed Dataset has been loaded\\n')
        return df

    def checkIfFilePathExists(self, file_path):
        ''' Checks if a file path exists in the system '''
        if os.path.exists(file_path):
            logging.info(f"The file path '{file_path}' exists.")
            return True
        else:
            logging.error(f"The file path '{file_path}' does not exist or is inaccessible.")
            return False