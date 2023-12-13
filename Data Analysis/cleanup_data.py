import pandas as pd

def categorize_and_clean_csv(input_file_path, cleaned_output_file_path, fnf_output_file_path, response_bins, response_labels):
    try:
        df = pd.read_csv(input_file_path)
        label_mapping = {
            "Never": 0,
            "Occasionally": 1,
            "Frequently": 2,
            "Always": 3,
        }

        # Categorize all columns with numeric data
        numeric_columns = df.select_dtypes(include=['number']).columns
        for column_to_categorize in numeric_columns:
            df[column_to_categorize] = pd.cut(df[column_to_categorize], bins=response_bins, labels=response_labels, right=False)

        # Replace "yes" with 1 and "no" with 0 in all columns
        df.replace({'Yes': 1, 'No': 0}, inplace=True)
        df.replace(label_mapping, inplace=True)

        # Drop specified columns
        columns_to_exclude = ["Started Time", "Submitted Time", "CompletionStatus", "IP Address", "Location",
                              "DMS (Lat, Long)", "Channel Type", "Channel Name", "Device ID", "Device Name",
                              "Browser", "OS", "Contact Name", "Contact Email", "Contact Mobile", "Contact Phone",
                              "Contact Job Title", "Submission Id", "Time Zone", "Device Type", "Browser Language",
                              "Tags", "Language Name", "Contact Created Date", "Contact Department", "Contact Team",
                              "Contact Division", "Contact Union", "Contact Local Field", "Contact Reporting Manager"]
        df_cleaned = df.drop(columns=columns_to_exclude, errors='ignore')

        # Write the cleaned DataFrame to the cleaned_output_file_path
        df_cleaned.to_csv(cleaned_output_file_path, index=False)

        question_column_start = 147
        # Create a new DataFrame with only values from column 151 and onwards
        fnf_df = df_cleaned.iloc[:, question_column_start:]  # Assuming 0-based indexing

        # Add the 'Question' labels to the top row
        question_labels = [f"Question {i}" for i in range(1, len(fnf_df.columns) + 1)]
        fnf_df.columns = question_labels

        # Write the fnf_df to the fnf_output_file_path
        fnf_df.to_csv(fnf_output_file_path, index=False)

        print(f"Cleaned and categorized data exported to {cleaned_output_file_path}")
        print(f"FnF questions data exported to {fnf_output_file_path}")
    except FileNotFoundError:
        print(f"Error: File not found - {input_file_path}")
    except pd.errors.EmptyDataError:
        print(f"Error: Empty CSV file - {input_file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    CSV_FILE_PATH = "Data/Responses - SEC Function & Facility.csv"
    CLEANED_OUTPUT_PATH = "Data/cleaned_responses.csv"
    FnF_OUTPUT_PATH = "Data/cleaned_questions.csv"

    # Clean and categorize CSV data for all columns
    response_bins = [0, 1, 2, 3, 4]  # Adjust the bin edges as needed
    response_labels = ["Never", "Occasionally", "Frequently", "Always"]
    categorize_and_clean_csv(CSV_FILE_PATH, CLEANED_OUTPUT_PATH, FnF_OUTPUT_PATH, response_bins, response_labels)
