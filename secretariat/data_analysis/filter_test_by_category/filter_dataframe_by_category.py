import logging as log

# Configure the logging module
log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def filter_dataframe_by_category(dataframe, category):
    """
    Filter the DataFrame based on the desired question category.

    Parameters:
    - dataframe (pd.DataFrame): The input DataFrame containing question and answer data.
    - category (str): The desired category to filter the DataFrame.

    Returns:
    - pd.DataFrame: A new DataFrame containing only rows with the specified category.
    """
    # Use the pandas DataFrame query method to filter rows based on the specified category
    filtered_df = dataframe.query("category == @category").copy()
    # Display all answers for the specified category
    log.debug(f"All answers for questions in the category '{category}':")
    log.debug(filtered_df[['question_id', 'question', 'answer']])
    return filtered_df
