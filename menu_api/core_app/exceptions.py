from rest_framework.exceptions import APIException


class VotingIsEndedException(APIException):
    status_code = 400
    default_detail = 'Voting has ended.'
    default_code = 'voting_ended'
    