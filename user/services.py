from common.runnable import Runnable
from user.models import Mentor, Mentee


class MatchMentorAndMenteeService(Runnable):

    @classmethod
    def run(cls, mentor: Mentor, mentee: Mentee) -> None:
        pass