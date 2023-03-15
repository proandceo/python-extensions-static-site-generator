from ssg import hooks, parsers

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: isinstance(p, parsers.ResourceParser)
