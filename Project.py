import os

# Class Project collaborates with GUI and LUA script
# Displays project name and its specific protocol.
# Projects can be imported and exported from the workspace
# @param (name, path, protocol, layout)


class Project:
    def __init__(self, name, path, protocol, layout, description):
        self.name = name
        self.path = path
        self.protocol = protocol
        self.layout = layout
        self.description = description

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_path(self):
        return self.path

    def set_path(self, value):
        self.path = value

    def get_protocol(self):
        return self.protocol

    def set_protocol(self, value):
        self.protocol = value

    def get_layout(self):
        return self.layout

    def set_layout(self, value):
        self.layout = value

    def get_description(self):
        return self.description

    def set_description(self, value):
        self.description = value


# creates new project directory with description
# @\requires (name != null or contain illegal characters) && (save_path exists)
# @\ensures project exists at save_path with description text file
def new_project(name, save_path, description):
    # Check if path exists
    if verify_path(save_path):
        # Set directory at save_path
        os.chdir(save_path)
        try:
            # If project name doesn't exists create new project
            os.makedirs(name, 1) #
            created_project = Project(name, save_path, "protocol", "layout")  # change to xml
            c_project = created_project.get_name()

            # Create protocol file.xml
            os.chdir(save_path + "/" + c_project)
            filename1 = name + "_proto.xml"
            proto_file = open(filename1, "w")
            proto_file.write("Write Protocol here")

            # Create text file that holds description (in SRS)
            filename2 = name + "_description.txt"
            desc_file = open(filename2, "w")
            desc_file.write(description)
        except OSError as e:
            print('Directory name already exists: Directory not created.')


# Opens existing project onto gui
# @\requires project != null
# @\ensures saved project is open on gui
def open_project(project):  # untested
    try:
        with open(project, 'r') as f:
            contents = f.read()
            # print(contents)
    except IOError as e:
        print "Unable to open file"


# save current project layout and protocol
# @\REQUIRES collaboration with layout & protocol to continue
# @\ensures (new)project state is saved
def save_project(project):  # untested
    layout = "current layout"  # requires layout
    protocol = "current proto"  # requires protocol
    project.set_layout(layout)
    project.set_protocol(protocol)


# export dissector in LUA script format
# REQUIRES collab with lua script
# @\ensure file == lua format
def export_lua_dissector(project, save_path):  # not working / take in project or xml file???
    xml_file = project.get_path()
    os.chdir(xml_file)
    xml_file = xml_file + "\\" + project.get_name()
    try:
        print "db:3"
        filename = project.get_name() + ".lua"
        fd = os.open(filename, os.O_CREAT | os.O_EXCL)
        os.fdopen(fd, 'w')

    except OSError:
        print('LUA dissector already exists: Dissector not created.')


# adds self to workspace
def add_to_workspace(project, workspace):  # not complete
    print "not started"


# verify directory path
def verify_path(path):
    if os.path.exists(path):
        return 1


def main():
    # testing
    path1 = r"C:\Users\luui9\Desktop\test"  # annoying path requires char 'r' before string
    dis = r"C:\Users\luui9\Desktop\test\new_project555"
    # new_project("new_project555", path1, "description")
    new_project = Project("test_project", path1, "protocool", "layout")  # works

    export_lua_dissector(new_project, path1)
    # open_project("test.txt") # untested with projec
    # ts on gui


if __name__ == "__main__":
    main()
