from django.utils import timezone
from datetime import datetime

from menu_api.settings import VOTE_DEADLINE


def is_voting_ended() -> bool:
        """
            This function checks if the time has passed when users can vote for dishes from the menu. 
            Returns True if the time has passed, otherwise returns False.
        """
        time_now = timezone.now()
        deadline = datetime.combine(time_now.date(), VOTE_DEADLINE)        

        if time_now > deadline:
            return True
        
        return False
