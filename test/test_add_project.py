import pytest
from data.project_data import testdata


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    app.project.open_projects_page()
    before_project_list = app.project.get_project_list()
    project = app.project.create_project(project)
    before_project_list.append(project)
    after_project_list = app.project.get_project_list()
    assert sorted(before_project_list) == sorted(after_project_list)
