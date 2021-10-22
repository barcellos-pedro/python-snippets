

class Tests():

    def __init__(self) -> None:
        self.success_tests = 0
        self.failed_tests = 0

    def result(self) -> str:
        """
        Print the amount of succeed and failed tests
        """
        print("- - - - - - - - - - - -")
        print(f"Success tests {self.success_tests}")
        print(f"Failed tests {self.failed_tests}")
        print("- - - - - - - - - - - -")

    def run_tests(self) -> None:
        """
        Runs all tests
        """
        self.test_is_equal()

    def test_is_equal(self) -> str:
        """
        Tests if one string equals the other one
        """
        name1 = 'a'
        name2 = 'b'
        try:
            assert name1 == name2, f"[TEST FAILED] Nome {name1} !== {name2}"
        except AssertionError as error:
            self.failed_tests += 1
            print(error)
        else:
            self.success_tests += 1
        finally:
            self.result()


Tests().run_tests()
