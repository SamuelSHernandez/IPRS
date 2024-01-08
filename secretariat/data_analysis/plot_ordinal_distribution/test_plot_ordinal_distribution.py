import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import matplotlib.pyplot as plt
from plot_ordinal_distribution import plot_ordinal_distribution

class TestPlotOrdinalDistribution(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'question_id': [1, 2, 3, 4],
            'question': ['Q1', 'Q2', 'Q3', 'Q4'],
            'answer': ['Never', 'Occasionally', 'Frequently', 'Always'],
            'category': ['Test', 'Test', 'Test', 'Test']
        }
        self.filtered_df = pd.DataFrame(data)

    @patch('builtins.print')
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.core.series.Series.plot')
    def test_plot_ordinal_distribution(self, mock_plot, mock_subplots, mock_show, mock_print):
        # Mock Axes object returned by subplots
        mock_axes = MagicMock()
        mock_subplots.return_value = (mock_axes,)

        filtered_category = "Test"
        plot_ordinal_distribution(filtered_category, self.filtered_df)

        # Check if the correct title is set
        mock_plot.assert_called_once_with(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
        mock_plot_args, mock_plot_kwargs = mock_plot.call_args
        self.assertNotIn('ax', mock_plot_kwargs)  # Check that 'ax' parameter is not present


        # Ensure show() is called
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
