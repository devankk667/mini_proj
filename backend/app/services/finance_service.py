from typing import List, Dict
from backend.app.repositories.in_memory import db
from backend.app.schemas.finance_and_mgmt import FinancialTransactionCreate, FinancialSummaryResponse
from backend.app.schemas.enums import TransactionType

class FinanceService:
    @classmethod
    def get_summary(cls) -> FinancialSummaryResponse:
        income = sum(t["amount"] for t in db.financial_transactions if t["type"] == TransactionType.INCOME.value)
        expenses = sum(t["amount"] for t in db.financial_transactions if t["type"] == TransactionType.EXPENSE.value)

        sales_income = sum(s["total"] for s in db.sales if s["status"] == "COMPLETED")
        total_rev = income + sales_income

        purchases_expense = sum(p["total"] for p in db.purchases if p["status"] == "COMPLETED")
        total_exp = expenses + purchases_expense

        gross_profit = total_rev - purchases_expense
        net_profit = total_rev - total_exp
        margin = (net_profit / total_rev * 100.0) if total_rev > 0 else 0.0

        return FinancialSummaryResponse(
            total_revenue=round(total_rev, 2),
            total_expenses=round(total_exp, 2),
            gross_profit=round(gross_profit, 2),
            net_profit=round(net_profit, 2),
            profit_margin_percent=round(margin, 2),
            total_receivables=150.0,
            total_payables=300.0
        )

    @classmethod
    def list_transactions(cls) -> List[dict]:
        return db.financial_transactions
