import random
from model.group import Group
import allure


def test_delete_some_group(app, db, check_ui):
    with allure.step("Given a non-empty group list"):
        app.group.create_group_if_it_not_exist(Group(name="test delete"))
        old_groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        group = random.choice(old_groups)
    with allure.step(f"When I delete the group {group} from the list"):
        app.group.delete_group_by_id(group.id)
    with allure.step("Then the new group list is equal to the old group list with the deleted group"):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
