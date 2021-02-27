import unittest
from TestAlerts import alert
from TestInputElement_1 import InputElement
from TestCheckBox import CheckBox
from TestDropDoemList import dropDown
from TestRadioBtn import radioButton

alertTest= unittest.TestLoader().loadTestsFromTestCase(alert)
inputTest=unittest.TestLoader().loadTestsFromTestCase(InputElement)
checkBoxTest=unittest.TestLoader().loadTestsFromTestCase(CheckBox)
dropDownTest=unittest.TestLoader().loadTestsFromTestCase(dropDown)
radioButtonTest=unittest.TestLoader().loadTestsFromTestCase(radioButton)





test_suite = unittest.TestSuite([alertTest,inputTest,checkBoxTest,dropDownTest,radioButtonTest])


unittest.TextTestRunner(verbosity=1).run(test_suite)