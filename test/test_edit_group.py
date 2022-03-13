from model.group import Group


def test_edit_group_name(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="test edit")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_header(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(header="test edit")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_footer(app):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(footer="test edit")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
