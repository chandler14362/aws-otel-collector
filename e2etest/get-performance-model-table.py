import os
import json
import sys
from pathlib import Path
import jinja2
import string


if __name__ == "__main__":
    from jinja2 import Environment, PackageLoader, select_autoescape
    templateLoader = jinja2.FileSystemLoader(searchpath="e2etest/templates/")
    env = Environment(loader=templateLoader)

    # get performance models from artifacts
    performance_models = []
    artifacts_path = "artifacts/"
    for filename in os.listdir(artifacts_path):
        with open(artifacts_path + filename) as f:
            performance_models.append(json.load(f))

    # render performance models into markdown
    template = env.get_template('performance_model.tpl')
    rendered_result = template.render({"performance_models": performance_models})
    print(rendered_result)

    # write rendered result to docs/performance_model.md
    with open("docs/performance_model.md", "w") as f:
        f.write(rendered_result)