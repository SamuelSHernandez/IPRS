import logging as log
import matplotlib.pyplot as plt

# Configure the logging module
log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_ordinal_distribution(filtered_category, filtered_df):
    """
    Plot the distribution of ordinal data for the specified category.

    Parameters:
    - filtered_category (str): The category for which the distribution will be plotted.
    - filtered_df (pd.DataFrame): The filtered DataFrame containing question and answer data.

    Returns:
    - None
    """
    # Ordinal data labels
    LABEL_MAPPING = {
        "Never": "0",
        "Occasionally": "1",
        "Frequently": "2",
        "Always": "3",
    }

    # Filter DataFrame for ordinal values
    filtered_df_ordinal = filtered_df[filtered_df['answer'].isin(LABEL_MAPPING.values())].copy()

    # Map ordinal values to more readable labels
    filtered_df_ordinal['answer_label'] = filtered_df_ordinal['answer'].map({v: k for k, v in LABEL_MAPPING.items()})

    # Choose visually appealing colors
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    # Plot the distribution
    plt.figure(figsize=(8, 6))
    filtered_df_ordinal['answer_label'].value_counts().sort_index().plot(kind='bar', color=colors)
    plt.title(f'Distribution of Ordinal data for questions in the category "{filtered_category}"')
    plt.xlabel('Answer')
    plt.ylabel('Count')
    plt.show()
