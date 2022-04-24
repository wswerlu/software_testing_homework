from model.group import Group
import random
import allure


def test_edit_some_group(app, db, data_groups, check_ui):
    group = data_groups
    with allure.step("Given a non-empty group list"):
        app.group.create_group_if_it_not_exist(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        some_group = random.choice(old_groups)
    with allure.step(f"When I make changes {group} in the group {some_group} from the list"):
        index = old_groups.index(some_group)
        group.id = some_group.id
        app.group.edit_group_by_id(group, some_group.id)
    with allure.step("Then the new group list is equal to the old group list with the edited group"):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
