import wezel


def dev(parent): 

    # Core wezel menus
    wezel.menu.folder.all(parent.menu('File'))
    wezel.menu.edit.all(parent.menu('Edit'))
    wezel.menu.view.all(parent.menu('View'))

    # Image processing methods included in wezel
    # Requirements: dipy, SimpleITK, itk-elastix
    wezel.menu.filter.all(parent.menu('Filter'))
    wezel.menu.segment.all(parent.menu('Segment'))
    wezel.menu.transform.all(parent.menu('Transform'))

    # My menus
    mymenu = parent.menu('Myproj')
    mymenu.action(HelloWorld, text='Hello World!')
    mymenu.action(HelloSheffield, text="Hello Sheffield!")


# Your custom made menu buttons

class HelloWorld(wezel.Action):
    def run(self, app):
        app.dialog.information("Hello World!", title = 'My first button!')


class HelloSheffield(wezel.Action):
    def run(self, app):
        app.dialog.information("Hello Sheffield!", title = 'My second button!')