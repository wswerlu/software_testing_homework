from model.group import Group


def test_edit_group_name(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="test edit"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="test edit"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_footer(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="test edit"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
