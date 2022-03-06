from model.group import Group


def test_edit_group_name(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    app.group.edit_first_group(Group(name="test edit"))


def test_edit_group_header(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    app.group.edit_first_group(Group(header="test edit"))


def test_edit_group_footer(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    app.group.edit_first_group(Group(footer="test edit"))
