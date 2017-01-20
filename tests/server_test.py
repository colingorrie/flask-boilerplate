from . import BoilerplateTestCase


class AppTemplateTest(BoilerplateTestCase):
    render_templates = False

    def test_root_template_used(self):
        self.client.get("/")

        self.assert_template_used("blueprint/root.html")
