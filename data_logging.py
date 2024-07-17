import os



def folder_creater(folder_name: str, folder_path: str = None):
    """
    This func create a folder. You can customize the folder path.

    :param folder_name: name of the you want the create
    :param folder_path: if the customize need it then you need the use the custom folder path.
    :return:
    """

    # if user customize the path we will use that path, but if not we have use cwd.
    if folder_path == None:
        folder_path = os.getcwd()
    # assign the final path
    folder_create_path = os.path.join(folder_path, folder_name)


    # check the folder already exist?
    if not os.path.isdir(folder_create_path):
        os.makedirs(folder_create_path)


