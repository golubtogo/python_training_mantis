import random
import pytest
from data.project_data import testdata


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_delete_project(app, project):
    app.project.open_projects_page()
    if app.project.count() == 0:
        app.project.create_project(project)
    before_project_list = app.soap.get_project_list()
    project = random.choice(before_project_list)
    app.project.delete_project_by_name(project.name)
    before_project_list.remove(project)
    after_project_list = app.soap.get_project_list()
    assert sorted(before_project_list, key=lambda p: p.name) == sorted(after_project_list, key=lambda p: p.name)
