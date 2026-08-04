from quantium_forage_internship.app import app, update_line_chart

def test_title():
    assert app.layout.children[0].children == "Pink Morsels Sales Dashboard"    


def test_checklist():
    assert any(hasattr(child, "id") and child.id == "checklist" for child in app.layout.children)


def test_visualisation():
    fig = update_line_chart(["north", "south", "east", "west"])
    assert fig is not None

