from data_logging import *
import os
import shutil


def test_folder_creater():
    """
    This test  check folder create step successfully run or not
    There is a 2 step of this test.

    First step is check create a folder without the set a folder_path parameter
    later that check create a folder with folder_path

    :return:
    """

    test_folder_name = "unit_test_folder"
    test_custom_folder_path = os.path.join(os.getcwd(), test_folder_name)
    test_folder_name_custom = "unit_test_custom_folder_name"

    base_create_successfully = 0
    custom_create_successfully = 0

    # first step
    folder_creater(folder_name= test_folder_name)

    # is it the first step done
    if os.path.isdir(test_folder_name):
        base_create_successfully = 1

    # second step
    folder_creater(folder_name= test_folder_name_custom, folder_path=test_custom_folder_path)
    # is it the second step done
    if os.path.isdir(os.path.join(test_custom_folder_path, test_folder_name_custom)):
        custom_create_successfully = 1

    # delete all test related folder.
    shutil.rmtree(test_folder_name)


    assert base_create_successfully == 1 and custom_create_successfully == 1