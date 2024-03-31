#jaimesg


def add_inventory(widgets, widget_name, quantity):
    widgets[widget_name] = quantity
  

def delete_inventory(widgets, widget_name):
    if widget_name in widgets:
        del widgets[widget_name]
        return 'record has been removed'
    else:
        return 'item not found'




