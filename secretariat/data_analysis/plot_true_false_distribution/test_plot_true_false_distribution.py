import unittest
from unittest.mock import patch, MagicMock, call
import pandas as pd
from plot_true_false_distribution import plot_true_false_distribution

class TestPlotTrueFalseDistribution(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'question_id': [1, 2, 3, 4],
            'question': ['Q1', 'Q2', 'Q3', 'Q4'],
            'answer': ['True', 'False', 'True', 'True'],
            'category': ['Test', 'Test', 'Test', 'Test']
        }
        self.filtered_df = pd.DataFrame(data)

    @patch('builtins.print')
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.core.series.Series.plot')
    def test_plot_true_false_distribution(self, mock_plot, mock_subplots, mock_show, mock_print):
        # Mock Axes object returned by subplots
        mock_axes = MagicMock()
        mock_subplots.return_value = (mock_axes,)

        filtered_category = "Test"
        plot_true_false_distribution(filtered_category, self.filtered_df)

        # Check if the correct title is set
        expected_calls = [call(kind='bar', color=['green', 'red'])]
        actual_calls = mock_plot.call_args_list
        self.assertEqual(actual_calls, expected_calls)

        # Ensure show() is called
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
