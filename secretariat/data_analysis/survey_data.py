import pandas as pd

LABEL_MAPPING = {
    "Never": 0,
    "Occasionally": 1,
    "Frequently": 2,
    "Always": 3,
}

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"CSV file '{file_path}' successfully loaded into DataFrame.")
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        print(f"Error: {str(e)}")

# Specify the paths to the CSV files
survey_responses = "survey_responses.csv"
survey_questions = "../Data/survey_questions.csv"
survey_questions_category = "../Data/survey_questions_category.csv"

# Load CSV files with error handling
df_survey_responses = load_csv(survey_responses)
df_survey_questions = load_csv(survey_questions)
df_survey_questions_category = load_csv(survey_questions_category)

# Convert 'question_id' to the same data type in both DataFrames
df_survey_responses['question_id'] = df_survey_responses['question_id'].astype(str)
df_survey_questions['question_id'] = df_survey_questions['question_id'].astype(str)

# Merge the DataFrames based on common keys
df_merged = pd.merge(df_survey_responses, df_survey_questions, on='question_id')
df_merged = pd.merge(df_merged, df_survey_questions_category, left_on='category_id', right_on='id')

# Filter the DataFrame based on the desired question category
filtered_category = "Mission and Dicipleship"
filtered_df = df_merged[df_merged['category'] == filtered_category]

# Convert labels to numerical values using LABEL_MAPPING
filtered_df['answer'] = filtered_df['answer'].map(LABEL_MAPPING)

# Display all answers for the specified category
print(f"All answers for questions in the category '{filtered_category}':")
print(filtered_df[['question_id', 'question', 'answer']])
