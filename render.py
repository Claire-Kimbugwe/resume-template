from jinja2 import Template
from config import config

if __name__ == "__main__":
    with open('template.jinja') as f:
        template = Template(f.read())
    with open('out.html', 'w') as f:
        for l in template.generate(**config):
            f.write(l)

