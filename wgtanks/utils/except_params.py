params = {
    "get_account_id_by_name": [
        {
            'name': 'account_name',
            'value': None,
            'type': str,
            'min_len': 3,
            'max_len': 24
        },
        {
            'name': 'limit',
            'value': None,
            'type': int,
            'min_num': 1,
            'max_num': 100
        },
        {
            'name': 'exact',
            'value': None,
            'type': bool
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple
        }
    ],
    "get_account_info_by_id": [
        {
            'name': 'account_id',
            'value': None,
            'type': tuple,
            'incl_only': int
        },
        {
            'name': 'extra',
            'value': None,
            'type': str
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple
        }
    ],
    "get_players_vehicles": [
        {
            'name': 'account_id',
            'value': None,
            'type': tuple,
            'incl_only': int
        },
        {
            'name': 'tank_id',
            'value': None,
            'type': tuple,
            'min_len': 0,
            'max_len': 100
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple
        }
    ],
    "get_players_achievements": [
        {
            'name': 'account_id',
            'value': None,
            'type': tuple,
            'incl_only': int
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple
        }
    ]

}