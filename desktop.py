import eel, os
from jinja2 import Environment, FileSystemLoader
from bottle import route, run, response

join_path = os.path.join

project_root_folder = os.getcwd()

html_server_folder = join_path(project_root_folder, "web")
template_folder = join_path(html_server_folder, "templates")

static_files = join_path(project_root_folder, "static")

template_context = {
    "sep":os.sep,
    "static_custom_path" : join_path(static_files, "custom") + os.sep,
    "fontawesome_path" : join_path(static_files, "fontawesome") + os.sep,
}

env = Environment(loader=FileSystemLoader(template_folder))

@route("/index.html", "/")
def serve_index():
    template = env.get_template("index.html")
    html = template.render(**template_context)
    return html

def _stop():
    os._exit(0)

eel.init('web')
eel.start('index.html',
          jinja_templates="templates",
          mode=None,
          close_callback=_stop,
          block=True
        )

