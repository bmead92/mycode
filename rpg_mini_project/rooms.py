rooms = {
        'Entrance' : {
            'south' : 'Hall',
            'item' : 'flashlight'
            },

        'Hall' : {
            'north' : 'Entrance',
            'south' : 'Kitchen',
            'east' : 'Dining Room',
            'item': 'key'
            },

        'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster',
                },

        'Dining Room' : {
            'west' : 'Hall',
            'south' : 'Garden',
            'item' : 'potion'
            },

        'Garden' : {
            'north' : 'Dining Room',
            }
        }
