def test_open_mainpage(app):
    app.open_main_page()
    assert app.is_valid()
    app.destroy()
