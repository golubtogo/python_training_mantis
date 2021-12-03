from selenium.webdriver.support.select import Select
from model.project import Project
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and
                len(wd.find_elements_by_xpath("//button[@type='submit']")) > 0):
            wd.find_element_by_xpath("//span[contains(text(),'Manage')]").click()
            wd.find_element_by_xpath("//a[contains(text(),'Manage Projects')]").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        before_project_list = self.get_project_list()
        self.init_project_creation()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@type='submit']").click()
        self.project_cache = None
        after_project_list = self.get_project_list()
        list_difference = []
        for item in after_project_list:
            if item not in before_project_list:
                list_difference.append(item)
        return list_difference.pop()

    def init_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[@type='submit']").click()

    def fill_project_form(self, project):
        self.change_field_value(project)

    def change_field_value(self, project):
        wd = self.app.wd
        if project.status:
            wd.find_element_by_name("status").click()
            Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)

        if project.view_state:
            wd.find_element_by_name("view_state").click()
            Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)

        project_data = project.__dict__

        for label in project_data:
            value = project_data[label]
            if value is not None and \
               not any(ext in label for ext in ["status", "inherit_global", "view_state"]) and \
               label != 'id':
                wd.find_element_by_name(label).click()
                wd.find_element_by_name(label).clear()
                wd.find_element_by_name(label).send_keys(value)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("div.col-md-12>div.widget-box div.table-responsive tbody tr"):
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                view_state = cells[3].text
                description = cells[4].text
                id = element.find_element_by_tag_name("td a").get_attribute('href').split("=")[1]
                self.project_cache.append(Project(id=id, name=name, status=status,
                                                  view_state=view_state, description=description))
        return list(self.project_cache)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(name).click()
        self.delete_project()
        self.delete_project()
        self.project_cache = None

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        list = wd.find_elements_by_css_selector("div.col-md-12>div.widget-box div.table-responsive tbody tr")
        return len(list)

    user_cache = None



