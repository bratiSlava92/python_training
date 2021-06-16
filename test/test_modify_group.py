from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(new_name="new_group", new_header="new_header", new_footer="new_footer"))
    app.session.logout()