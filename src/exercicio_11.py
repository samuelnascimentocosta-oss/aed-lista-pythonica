def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
    if unavailable in guests:
        guests[guests.index(unavailable)] = new_guest
        return guests