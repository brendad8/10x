
#------------------------------------------------------------------------
import N10X

#------------------------------------------------------------------------
# Vim Commands

def w():
    N10X.Editor.ExecuteCommand("SaveFile")
    result = "Saved " + N10X.Editor.GetCurrentFilename()
    print(result)

def wa():
    N10X.Editor.ExecuteCommand("SaveAll")
    result = "Saved file(s)"
    print(result)

def noh():
    N10X.Editor.SetFindText("")

#------------------------------------------------------------------------
# Custom Commands

def OpenAllCode():
    workspace_files = N10X.Editor.GetWorkspaceFiles()
    open_files = N10X.Editor.GetOpenFiles()
    for file in workspace_files:
        if file not in open_files:
            N10X.Editor.OpenFile(file)

# TODO(bcall):
#    - some kind of find file where i can specify rough name/pattern
#      and it opens best candidate if any