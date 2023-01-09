from django.core.management.base import BaseCommand

from loans.models import Loan
from loans.scraper import Scraper


class Command(BaseCommand):
    help = (
        "Get all loans from https://www.eib.org/en/projects/loans/index.htm"
        "and register them in the database."
    )

    def handle(self, *args, **kwargs):
        scraper = Scraper()
        scraped_loans = scraper.get_loans()

        queryset = Loan.objects.all()
        if not queryset.exists():

            loans = [
                Loan(
                    title=param["title"],
                    loan_url=param["loan_url"],
                    signature_date=param["signature_date"],
                    signed_amount=param["signed_amount"],
                    country=param["country"],
                    country_url=param["country_url"],
                    sector=param["sector"],
                )
                for param in scraped_loans
            ]
            Loan.objects.bulk_create(loans, ignore_conflicts=True)
