from abc import ABC, abstractmethod


class Middle(ABC):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes  # пользовательские оценки
        self.expert_votes = expert_votes  # оценки критиков

    def get_correct_user_votes(self, to_sort=False):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.user_votes if 10 < vote < 90]
        return sorted(votes) if to_sort else votes

    def get_correct_expert_votes(self, to_sort=False):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.expert_votes if 5 < vote < 95]
        return sorted(votes) if to_sort else votes

    @abstractmethod
    def get_average(self, users=True, to_sort=False):
        if users:
            votes = self.get_correct_user_votes(to_sort)
        else:
            votes = self.get_correct_expert_votes(to_sort)
        return votes


class Average(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users)
        return sum(votes) / len(votes)


class Median(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users, to_sort=True)
        return votes[len(votes) // 2]


class Harmonic(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users)
        return len(votes) / sum(map(lambda vote: 1 / vote, votes))


user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
average = Average(user_votes, expert_votes)

print(average.get_correct_user_votes())
print(average.get_correct_expert_votes())
print(average.get_average())
print(average.get_average(False))
