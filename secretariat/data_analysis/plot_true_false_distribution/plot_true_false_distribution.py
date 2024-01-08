import logging as log
import matplotlib.pyplot as plt

# Configure the logging module
log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_true_false_distribution(filtered_category, filtered_df):
    """
    Plot the distribution of true and false answers for the specified category.

    Parameters:
    - filtered_category (str): The category for which the distribution will be plotted.
    - filtered_df (pd.DataFrame): The filtered DataFrame containing question and answer data.

    Returns:
    - None
    """
    log.debug("\"plot_true_false_distribution\" function ran")
    # Filter DataFrame for 'True' and 'False' answers
    filtered_df_bool = filtered_df[filtered_df['answer'].isin(["True", "False"])].copy()
    # Plot the distribution
    plt.figure(figsize=(8, 6))
    filtered_df_bool['answer'].value_counts().plot(kind='bar', color=['green', 'red'])
    plt.title(f'Distribution of True/False for questions in the category "{filtered_category}"')
    plt.xlabel('Answer')
    plt.ylabel('Count')
    plt.show()
