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
            'type': tuple,
            'incl_only': str
        }
    ],
    "get_account_info": [
        {
            'name': 'account_id',
            'value': None,
            'type': tuple,
            'incl_only': int
        },
        {
            'name': 'extra',
            'value': None,
            'type': tuple,
            'incl_only': str
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple,
            'incl_only': str
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
            'type': tuple,
            'incl_only': str
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
            'type': tuple,
            'incl_only': str
        }
    ],
    "get_clan_info_by_name": [
        {
            'name': 'clan_name',
            'value': None,
            'type': str,
            'min_len': 2
        },
        {
            'name': 'limit',
            'value': None,
            'type': int,
            'min_num': 1,
            'max_num': 100
        },
        {
            'name': 'page_no',
            'value': None,
            'type': int,
            'min_num': 1,
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple,
            'incl_only': str
        }

    ],
    "get_clan_member_details": [
        {
            'name': 'account_id',
            'value': None,
            'type': tuple,
            'incl_only': int
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple,
            'incl_only': str
        }
    ],
    "get_clan_glossary": [
        {
            'name': 'fields',
            'value': None,
            'type': tuple,
            'incl_only': str
        }
    ],
    "get_clan_messageboard": [
        {
            'name': 'access_token',
            'value': None,
            'type': str,
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple,
            'incl_only': str
        }
    ],
    "get_players_clan_history": [
        {
            'name': 'account_id',
            'value': None,
            'type': tuple,
            'incl_only': int
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple,
            'incl_only': str
        }
    ],
    "get_dates_with_available_clan_ratings": [
        {
            'name': 'limit',
            'value': None,
            'type': int
        }
    ],
    "get_clan_ratings": [
        {
            'name': 'clan_id',
            'value': None,
            'type': tuple,
            'incl_only': int
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple,
            'incl_only': str
        }
    ],
    "get_clan_adjacent_position_in_rating": [
        {
            'name': 'clan_id',
            'value': None,
            'type': int,
        },
        {
            'name': 'rank_field',
            'value': None,
            'type': str
        },
        {
            'name': 'date',
            'value': None,
            'type': int
        },
        {
            'name': 'limit',
            'value': None,
            'type': int
        },
        {
            'name': 'fields',
            'value': None,
            'type': tuple,
            'incl_only': str
        }
    ]


}

sheffield = '''
     
                                 _   √L~` ╕__,
                               g▄√╖_ª¬╖▀╓  ╓    ÷~.
                             √▀  ^ªΣ+▄ δ>▄___,,,_¿ '
                           ε▀   _▄╔╩▀▀~       ,~~▀?÷╣▄
                           ╣▄*▀~ ;          __,   `   ~π_
                          √▀ τ'  ,    ▄*▀"~``  ~~î╥.╔'√_ ` _  ┤
                       _/` ┤ _π, τ╓¢~             ,▐▌   ~▄,~«q╥╥╗_
                  .'   ~▀o,  ΣL_▄f                  ▐Fτª   ª╗½\▄`_`
                 ε   ██╕╖_▐█_φ▄F                  ▄▄▄█▀▄▌_    ▀▄
                τ ª┤▐███▄████╝                  _╝Φ  ▀▓_  ≈,    π,
                 #~Σ▓Ñ▓█▌▀W█~ ,▀               ╓ ª÷   ▀╨ç, ~╕  ^_~▄_
                Σ     ██ ÷▄` K'               π   :    δ ";_ ▄  ~╕~~
                ╓   τ██F  ╛▄█"                ' τ j    _~w_ ~Θ,  ▐ ╣,
                    ███  ╞æ▀▒        ▌       ╞  , ╛           █  τ╕⌡
                  ╡π███ .█╢ █        ╣       ²               τ█╕  █
                   ▒██▌  █▌ε▒   τ    ▐.      ,ε'             ▐█▌ φ'
                   ███▌ _▒█▀▐p  ╣    ~╣     τ╣      ΘM█████▀▒█Q▌τ╝
                  ▐███   ~@  ▐╓_▌, ,  ⌠g   τ,▐        ▀▀▐▌▐'τ█π_/
                  ████    ╚,'ª▀▐ Ω/>π⌐╖▐M_.▐ δ⌡       ╚▄ `~ Θ ▀'
                 ⌠█▌██     ~¬╖_ _ ~╚zj+>▀É≈2,  `        `   π'
                 ▒█╛██          ▀≈_    ▐█@▄╥,             _÷
                 ██ ██             ~"-┤_▒████,╥╥;._   _┤ ~
                τ██ ██                 ▄█████▀╣╣V*▐██
                ▐█▌ ██               ▄███████▀▀ª▀▀▒███▄
                ▒█╛ ██            ╔██████████ ╚  ╟ ▒▓W██_
                ▒█  ▒█         _¢█████ÑÑ████████@███▌   ▀M,
                ▒█  ▐█╕      æ██▓`      @████████████╕    ~╗
                ▀ª  ╞█▌  ╓▄@██▌▀⌐     τ█████▒█████████     ▀~╕
                     ~  æ█▐█▐███▄_  -æ████████████████▌_▄@███████_
                         ~███████▄_▌██████████████████████████████╕
                           ~▀███████g█████████████████▓▀ ╔█████████
                            ╓██████████` ▀▀▀▀▀▀▀ÑP▀" ¬▄████████████╕
                           τ█████▓▀████     ████▌    τ██████████████
                           ▒████    ▀▀▒_,  Σ    ╨    Σ▀███████▀▀~
                            ▐██▌      ▐█▒▒▒╣     █@█▓█  ~   ▐▌
                             ~▀       Σ█▒▒▒╛     Σ█▒▒▒
                                       ~╝╝▀        ~▀
'''