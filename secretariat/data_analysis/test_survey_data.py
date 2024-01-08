from data_analysis import filter_dataframe_by_category, fil

import unittest
import pandas as pd


class TestFilterDataFrameByCategory(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        
        data = {
            'question_id': [1, 2, 3, 4],
            'question': ['Q1', 'Q2', 'Q3', 'Q4'],
            'answer': ['A1', 'A2', 'A3', 'A4'],
            'category': ['Yearbook', 'Math', 'Yearbook', 'Science']
        }
        self.df = pd.DataFrame(data)

    def test_filter_dataframe_by_category(self):
        # Test filtering by an existing category
        filtered_df = filter_dataframe_by_category(self.df, 'Yearbook')
        expected_df = pd.DataFrame({
            'question_id': [1, 3],
            'question': ['Q1', 'Q3'],
            'answer': ['A1', 'A3'],
            'category': ['Yearbook', 'Yearbook']
        })

        pd.testing.assert_frame_equal(filtered_df, expected_df)

        # Test filtering by a non-existing category
        filtered_df_empty = filter_dataframe_by_category(self.df, 'NonExistingCategory')
        expected_df_empty = pd.DataFrame(columns=['question_id', 'question', 'answer', 'category'])

        pd.testing.assert_frame_equal(filtered_df_empty, expected_df_empty)

if __name__ == '__main__':
    unittest.main()