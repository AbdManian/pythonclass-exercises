def list_to_table(data: list, right_justify=True):
    """
    Convert list to the list of strings as two column table.
    First column should be row number and second one 
    contains content of the list.
    Example:
    list_to_table(["polecat", "rat", "seal"])  ->
        ["1 polecat", "2     rat", "3    seal"]
    """

    pass

if __name__ == "__main__":
    # test list_to_table
    test_data = ["A", "D", "ABCD"]
    ret_data = list_to_table(test_data)
    exp_data = ["1    A", "2    D", "3 ABCD"]
    assert ret_data == exp_data
