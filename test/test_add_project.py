import pytest
from data.project_data import testdata


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    before_project_list = app.soap.get_project_list()
    app.project.open_projects_page()
    project = app.project.create_project(project)
    before_project_list.append(project)
    after_project_list = app.soap.get_project_list()
    assert sorted(before_project_list, key=lambda p: p.name) == sorted(after_project_list, key=lambda p: p.name)
