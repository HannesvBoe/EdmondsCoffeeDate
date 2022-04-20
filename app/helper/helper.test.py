from helper import convert_string_to_nested_list, convert_matchings_to_string


def test_convert_string_to_nested_list():
    test_string = "Jasper Anders\nHannes von Boetticher\n\nPert Gubbi\nBob Senrie"
    assert convert_string_to_nested_list(test_string) == [
        [
            "Jasper Anders",
            "Hannes von Boetticher",
        ],
        ["Pert Gubbi", "Bob Senrie"],
    ]


def test_convert_matchings_to_string():
    matching = [
        {"Jasper Anders": "Pert", "Bob": "Hannes von Boetticher"},
        {"Jasper Anders": "Bob", "Pert": "Hannes von Boetticher"},
    ]

    assert (
        convert_matchings_to_string(matching)
        == "1.\n@Jasper Anders & @Pert\n@Bob & @Hannes von Boetticher\n\n2.\n@Jasper Anders & @Bob\n@Pert & @Hannes von Boetticher\n\n"
    )
