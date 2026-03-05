from quick_calc.gui import QuickCalcApp

def test_full_user_interaction_addition():
    app = QuickCalcApp()
    for token in ["5", "+", "3", "="]:
        app.press(token)
    assert app.calcresult.cget("text") == "8"

def test_clear_resets_display_to_zero():
    app = QuickCalcApp()
    for token in ["9", "*", "9", "="]:
        app.press(token)
    app.press("C")
    assert app.calcresult.cget("text") == "0"