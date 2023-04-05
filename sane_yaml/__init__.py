import yaml

__all__ = [
    'to_yaml',
    'read_yaml',
    'inline_list',
]

class inline_list(list):
    pass

def inline_list_repr(dumper, data):
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True)

yaml.SafeDumper.add_representer(inline_list, inline_list_repr)

class IndentDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

def to_yaml(obj, filename):
    with open(filename, 'w') as fout:
        yaml.dump(obj, fout, sort_keys=False, Dumper=IndentDumper, allow_unicode=True)

def read_yaml(filename):
    with open(filename, 'r') as fin:
        return yaml.safe_load(fin)
