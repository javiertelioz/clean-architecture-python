import abc


class TransactionClient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_transactions(self, date):
        """
        Get the transactional data for the specified date.

        Args:
            date (str): The date to retrieve the transactional data.

        Returns:
            dict: The transactional data.
        """
        pass
