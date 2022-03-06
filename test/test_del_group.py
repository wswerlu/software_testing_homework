from model.group import Group


def test_delete_first_group(app):
    app.group.create_group_if_it_not_exist(Group(name="test delete"))
    app.group.delete_first_group()
