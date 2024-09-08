import unittest
import Module_12_1

caseMyTests = unittest.TestSuite()
caseMyTests.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_1.RunnerTest))
# caseMyTests.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.TournamentTest))
unittest.TextTestRunner(verbosity=2).run(caseMyTests)
