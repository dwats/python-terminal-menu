from ..src.terminalmenu import TerminalMenu
from nose.tools import with_setup

def opt_func():
    return True


TestDisplay = "TestDisplay"
TestOption = [{"text": "test option", "func": opt_func}]
menu = None


def setup():
    global menu
    print("Setup")
    menu = TerminalMenu(TestDisplay)
    menu.option = TestOption


def teardown():
    global menu
    print("Teardown")
    menu = None


@with_setup(setup, teardown)
def test_init():
    print("test_init")
    assert type(menu) == TerminalMenu


@with_setup(setup, teardown)
def test_display():
    print("test_display")
    assert menu.display == TestDisplay


@with_setup(setup, teardown)
def test_option():
    print("test_option")
    assert menu.option == TestOption


@with_setup(setup, teardown)
def test_back_action():
    print("test_back_action")

    def back_stub():
        return True

    menu.back = back_stub
    assert menu.back_action()
