from model.group import Group
import random


def test_edit_some_group(app, db, data_groups, check_ui):
    group = data_groups
    app.group.create_group_if_it_not_exist(Group(name="test"))
    old_groups = db.get_group_list()
    some_group = random.choice(old_groups)
    index = old_groups.index(some_group)
    group.id = some_group.id
    app.group.edit_group_by_id(group, some_group.id)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
