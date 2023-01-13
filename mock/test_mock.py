# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
"""
Lesson 1: Mock
Video: https://canvas.uw.edu/courses/1608479/pages/lesson-01-content-part-12-more-on-linting-mocks-and-patching?module_item_id=16955510

Notes:
    below commands must be executed in git bash terminal

install coverage
> pip install coverage

install pylint
> pip install pylint

create .pylintrc (in root directory)
> pylint --generate-rcfile > .pylintrc

create requirements.txt (in root directory)
> add coverage, pylint and mock


Run Unittest CLI:
> python -m unittest test_mock.py

Run test coverage and unittest CLI:
> python -m coverage run --include=mock_tutorial.py -m unittest test_mock.py

Generate coverage report
> python -m coverage report

Generate coverage html report
> python -m coverage html    # a new folder called "htmlcov" got created with an index.html
"""

from unittest import TestCase
import mock_tutorial as MT
from mock import Mock


class TutorialTest(TestCase):
    def test_get_user_info(self):
        """
        use Mock to replace MT input & set return value to be Don
        :return:
        """
        MT.input = Mock(return_value='Don')
        self.assertEqual(MT.get_user_info(), 'Don')

    def test_get_current_temperature_nice(self):
        """
        replace temperature_sensor.read_temperature with mock (return_value of 75)
        assert MT.get_current_temperature() response == expected_response
        :return:
        """
        expected_response = "Nice weather, 75F!"
        MT.temperature_sensor.read_temperature = Mock(return_value=75)
        self.assertEqual(MT.get_current_temperature(), expected_response)

    def test_get_current_temperature_rough(self):
        """
        replace temperature_sensor.read_temperature with mock (return_value of 100)
        assert MT.get_current_temperature() response == expected_response
        :return:
        """
        expected_response = "Rough weather, 100F!"
        MT.temperature_sensor.read_temperature = Mock(return_value=100)
        self.assertEqual(MT.get_current_temperature(), expected_response)

    def test_get_current_temperature_below_zero(self):
        """
        replace temperature_sensor.read_temperature with mock (return_value -1)
        assert MT.get_current_temperature() response == SystemError
        :return:
        """
        MT.temperature_sensor.read_temperature = Mock(return_value=-1)
        self.assertRaises(SystemError, MT.get_current_temperature) # don't ()
