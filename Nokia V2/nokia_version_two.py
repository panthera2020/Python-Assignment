
while True:
    nokia_main_menu = """

        Nokia Menu

        1 PhoneBook
        2 Message
        3 Chat
        4 Call Register
        5 Tones
        6 Settings
        7 Call Divert
        8 Games
        9 Calculator
        10 Reminder
        11 Clock
        12 Profiles
        13 SIM services

        Enter 0 to Exit.
                    """

    nokia_main_menu_choice = int(input(nokia_main_menu))

    match nokia_main_menu_choice:
        case 1:
            while True:
                print("PhoneBook")
                print()
                phonebook = """
                1 Search
                2 Service Nos
                3 Add name
                4 Erase
                5 Edit
                6 Assign tone
                7 Send b'card
                8 Option
                9 Speed dial
                10 Voice tags

                Enter 0 for Previous Menu
                    """
                phonebook_choice = int(input(phonebook))

                match phonebook_choice:
                    case 1:
                        print("Search")
                    case 2:
                        print("Service Nos")
                    case 3:
                        print("Add name")
                    case 4:
                        print("Erase")
                    case 5:
                        print("Edit")
                    case 6:
                        print("Assign tone")
                    case 7:
                        print("Send b'card")
                    case 8:
                        while True:
                            print("Option")
                            print()
                            option_menu = """
                            1 Type of view
                            2 Memory status

                            Enter 0 for Previous Menu
                            """
                            option_menu_choice = int(input(option_menu))
                            match option_menu_choice:
                                case 1:
                                    print("Type of view")
                                case 2:
                                    print("Memory status")
                                case 0: break
                                case _:
                                    print("Invalid Input")
                            

                    case 9:
                        print("Speed dial")
                    case 10:
                        print("Voice tags")
                    case 0: break
                    case _:
                        print("Invalid Input")

            
        case 2:
            while True:
                print("Message")
                print()
                message = """
                1 Write messages
                2 Inbox
                3 Outbox
                4 Picture messages
                5 Templates
                6 Smileys
                7 Message settings
                8 Info service
                9 Voice mailbox number
                10 Service command editor

                Enter 0 for Previous Menu
                """
                message_choice = int(input(message))

                match message_choice:
                    case 1:
                        print("Write messages")
                    case 2:
                        print("Inbox")
                    case 3:
                        print("Outbox")
                    case 4:
                        print("Picture messages")
                    case 5:
                        print("Templates")
                    case 6:
                        print("Smileys")
                    case 7:
                        while True:
                            print("Message settings")
                            message_settings = """
                            1 Set 1
                            2 Common

                            Enter 0 for Previous Menu
                            """
                            message_settings_choice = int(input(message_settings))

                            match message_settings_choice:
                                case 1:
                                    while True:
                                        print("Set 1")
                                        set_one = """
                                        1 Message centre number
                                        2 Message sent as
                                        3 Message validity

                                        Enter 0 for Previous Menu
                                        """
                                        set_one_choice = int(input(set_one))

                                        match set_one_choice:
                                            case 1:
                                                print("Message center number")
                                            case 2:
                                                print("Message sent as")
                                            case 3:
                                                print("Message validity")
                                            case 0: break
                                            case _:
                                                print("Invalid Input")
                                                
                                case 2:
                                    while True:
                                        print("Common")
                                        common = """
                                        1 Delivery reports
                                        2 Reply via same centre
                                        3 Character support

                                        Enter 0 for Previous Menu
                                        """
                                        common_choice = int(input(common))

                                        match common_choice:
                                            case 1:
                                                print("Delivery reports")
                                            case 2:
                                                print("Reply via same centre")
                                            case 3:
                                                print("Character support")
                                            case 0: break
                                            case _:
                                                print("Invalid Input")
                                                

                                case 0: break
                                case _:
                                    print("Invalid Input")
                                    
                    case 8:
                        print("Info services")
                    case 9:
                        print("Voice mailbox number")
                    case 10:
                        print("Service command editor")
                    case 0: break
                    case _:
                        print("Invalid Input")


        case 3:
            print("Chat")

        case 4:
            while True:
                print("Call Register")
                call_register = """
                1 Missed calls
                2 Recieved calls
                3 Dialed number
                4 Erase recent call list
                5 Show call duration
                6 Show call cost
                7 Call cost settings
                8 Prepaid credit

                Enter 0 for Previous Menu 
                """
                call_register_choice = int(input(call_register))

                match call_register_choice:
                    case 1:
                        print("Missed Calls")
                    case 2:
                        print("Recieved Calls")
                    case 3:
                        print("Dialed Calls")
                    case 4:
                        print("Erase recent call list")
                    case 5:
                        while True:
                            print("Show call duration")
                            print()
                            show_call_duration = """
                            1 Last call duration
                            2 All calls' duration
                            3 Recieved calls' duration
                            4 Dialed calls' duration
                            5 Clear timers

                            Enter 0 for Previous Menu
                            """
                            show_call_duration_choice = int(input(show_call_duration))

                            match show_call_duration_choice:
                                case 1:
                                    print("Last call duration")
                                case 2:
                                    print("All calls' duration")
                                case 3:
                                    print("Recieved call's duration")
                                case 4:
                                    print("Dialed calls' duration")
                                case 5:
                                    print("Clear timers")
                                case 0: break
                                case _:
                                    print("Invalid Input")

                    case 6:
                        while True:
                            print("Show call cost")
                            print()
                            show_call_cost = """
                            1 Last call cost
                            2 All calls' cost
                            3 Clear counters

                            Enter 0 for Previous Menu
                            """
                            show_call_cost_choice = int(input(show_call_cost))

                            match show_call_cost_choice:
                                case 1:
                                    print("Last call cost")
                                case 2:
                                    print("All calls' cost")
                                case 3:
                                    print("Clear counters")
                                case 0: break
                                case _:
                                    print("Invalid Input")
                                
                    case 7:
                        while True:
                            print("Call cost settings")
                            print()
                            call_cost_settings = """
                            1 Call cost limit
                            2 Show cost in

                            Enter 0 for Previous Menu
                            """
                            call_cost_settings_choice = int(input(call_cost_settings))

                            match call_cost_settings_choice:
                                case 1:
                                    print("Call cost limit")
                                case 2:
                                    print("Show cost in")
                                case 0: break
                                case _:
                                    print("Invalid Input")
                                    
                    case 8:
                        print("Prepaid credit")
                    case 0: break
                    case _:
                        print("Invalid Input")


        case 5:
            while True:
                print("Tones")
                print()
                tones = """
                1 Ringing tone
                2 Ringing volume
                3 Incoming call alert
                4 Composer
                5 Message alert tone
                6 Keypad tone
                7 Warning and game tone
                8 Vibrating alert
                9 Screen saver

                Enter 0 for Previous Menu
                """
                tone_choice = int(input(tones))

                match tone_choice:
                    case 1:
                        print("Ringing tone")
                    case 2:
                        print("Ringing volume")
                    case 3:
                        print("Incoming call alert")
                    case 4:
                        print("Composer")
                    case 5:
                        print("Message alert tone")
                    case 6:
                        print("Keypad tone")
                    case 7:
                        print("Warning and game tone")
                    case 8:
                        print("Vibrating alert")
                    case 9:
                        print("Screen saver")
                    case 0: break
                    case _:
                        print("Invalid input")

        case 6:
            while True:
                print("Settings")
                settings = """
                1 Call settings
                2 Phone settings
                3 Security settings
                4 Restore factory settings

                Enter 0 for Previous Menu
                """
                settings_choice = int(input(settings))

                match settings_choice:
                    case 1:
                        while True:
                            print("Call settings")
                            call_settings = """
                            1 Automatic redial
                            2 Speed dialing
                            3 Call waiting options
                            4 Own number sending
                            5 Phone line in use
                            6 Automatic answer

                            Enter 0 for Previous menu
                            """
                            call_settings_choice = int(input(call_settings))

                            match call_settings_choice:
                                case 1:
                                    print("Automatic redial")
                                case 2:
                                    print("Speed dialing")
                                case 3:
                                    print("Call waiting options")
                                case 4:
                                    print("Own number sending")
                                case 5:
                                    print("Phone line in use")
                                case 6:
                                    print("Automatic answer")
                                case 0: break
                                case _:
                                    print("Invalid Input")

                    case 2:
                        while True:
                            print("Phone settings")
                            phone_settings = """
                            1 Language
                            2 Cell info display
                            3 Welcome note
                            4 Network selection
                            5 Lights
                            6 Confirm SIM service actions

                            Enter 0 for Previous Menu
                            """
                            phone_settings_choice = int(input(phone_settings))

                            match phone_settings_choice:
                                case 1:
                                    print("Language")
                                case 2:
                                    print("Cell info display")
                                case 3:
                                    print("Welcome note")
                                case 4:
                                    print("Network Selection")
                                case 5:
                                    print("Lights")
                                case 6:
                                    print("Confirm SIM service actions")
                                case 0: break
                                case _:
                                    print("Invalid Input")
                                    
                    case 3:
                        while True:
                            print("Security settings")
                            security_settings = """
                            1 PIN code request
                            2 Call barring service
                            3 Fixed dialing
                            4 Closed user group
                            5 Phone security
                            6 Change access codes

                            Enter 0 for Previous Menu
                            """
                            security_settings_choice = int(input(security_settings))

                            match security_settings_choice:
                                case 1:
                                    print("PIN code request")
                                case 2:
                                    print("Call barring services")
                                case 3:
                                    print("Fixed dialing")
                                case 4:
                                    print("Closed user group")
                                case 5:
                                    print("Phone security")
                                case 6:
                                    print("Change access codes")
                                case 0: break
                                case _:
                                    print("Invalid Input")
                                    
                    case 4:
                        print("Restore factory settings")
                    case 0: break
                    case _:
                        print("Invalid Input")

            
        case 7:
            print("Call Divert")

        case 8:
            print("Games")

        case 9:
            print("Calculator")

        case 10:
            print("Reminder")

        case 11:
            while True:
                print("Clock")
                clock = """
                1 Alarm clock
                2 Clock settings
                3 Date settings
                4 Stopwatch
                5 Countdown timer
                6 Auto update of date and time

                Enter 0 to Previous Menu
                """
                clock_choice = int(input(clock))

                match clock_choice:
                    case 1:
                        print("Alarm clock")
                    case 2:
                        print("Clock settings")
                    case 3:
                        print("Date settings")
                    case 4:
                        print("Stopwatch")
                    case 5:
                        print("Countdown timer")
                    case 6:
                        print("Auto update of date and time")
                    case 0: break 
                    case _:
                        print("Invalid Input")

        case 12:
            print("Profiles")

        case 13:
            print("SIM services")
        case 0: break

        case _:
            print("Invalid Input")