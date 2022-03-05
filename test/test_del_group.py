from model.group import Group


def test_delete_first_group(app):
    app.group.is_group_present(Group(name="test delete"))
    app.group.delete_first_group()
