
class Group:

    def __init__(self, name, header, footer):
        # for group creation
        self.name = name
        self.header = header
        self.footer = footer

    def __init__(self, new_name, new_header, new_footer):
        # for modify_first_group
        self.newName = new_name
        self.newHeader = new_header
        self.newFooter = new_footer