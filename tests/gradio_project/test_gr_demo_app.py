# importation of the solution function to test
from gradio_project.demo_app import greet


def test_solution_valid_inputs():
    """This is the test for the implemented solution passing
    valid inputs"""
    valid_inputs = ["Emmanuel", "Alain"]
    expected_outputs = ["Hello Emmanuel!!", "Hello Alain!!"]
    outputs = []

    for input in valid_inputs:
        outputs.append(greet(input))

    assert outputs == expected_outputs
