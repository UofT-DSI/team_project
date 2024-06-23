# main.py

# Import necessary modules
from DataPreProcess import data_loader
import logging

# Define main function
def main():
    logging.basicConfig(filename='../log/app.log', format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Credit risk sampling project!")

    # Call function to execute data extraction, transformation and loading (ETL)
    dataLoader = data_loader.DataLoader()
    creditData = dataLoader.preProcessData()

    print(f"Result from data pre processing: {creditData.head}")


# Entry point of the script
if __name__ == "__main__":
    main()