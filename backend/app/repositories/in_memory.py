from typing import Dict, List, Optional
from copy import deepcopy

class InMemoryRepository:
    def __init__(self):
        self.users: List[Dict] = []
        self.products: List[Dict] = []
        self.categories: List[Dict] = []
        self.stock_movements: List[Dict] = []
        self.customers: List[Dict] = []
        self.purchases: List[Dict] = []
        self.sales: List[Dict] = []
        self.financial_transactions: List[Dict] = []
        self.employees: List[Dict] = []
        self.alerts: List[Dict] = []
        self._seed_data()

    def _seed_data(self):
        self.users = [
            {"id": "usr-1", "username": "admin", "email": "admin@msme360.com", "password_hash": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", "role": "ADMIN", "is_active": True, "name": "System Admin"},
            {"id": "usr-2", "username": "owner", "email": "owner@msme360.com", "password_hash": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", "role": "OWNER", "is_active": True, "name": "Business Owner"},
            {"id": "usr-3", "username": "manager", "email": "manager@msme360.com", "password_hash": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", "role": "MANAGER", "is_active": True, "name": "Store Manager"},
            {"id": "usr-4", "username": "staff", "email": "staff@msme360.com", "password_hash": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", "role": "STAFF", "is_active": True, "name": "Sales Staff"},
        ]

        self.categories = [
            {"id": "cat-1", "name": "Electronics", "description": "Gadgets and tech accessories"},
            {"id": "cat-2", "name": "Office Supplies", "description": "Stationery and paper items"}
        ]

        self.products = [
            {"id": "prod-1", "name": "Wireless Mouse", "sku": "ELE-001", "category_id": "cat-1", "cost_price": 15.0, "selling_price": 25.0, "stock_quantity": 40, "min_stock_level": 10, "is_active": True},
            {"id": "prod-2", "name": "Mechanical Keyboard", "sku": "ELE-002", "category_id": "cat-1", "cost_price": 45.0, "selling_price": 75.0, "stock_quantity": 5, "min_stock_level": 8, "is_active": True},
            {"id": "prod-3", "name": "A4 Paper Ream", "sku": "OFF-001", "category_id": "cat-2", "cost_price": 3.0, "selling_price": 6.0, "stock_quantity": 100, "min_stock_level": 20, "is_active": True},
        ]

        self.customers = [
            {"id": "cust-1", "name": "Acme Corp", "email": "contact@acme.com", "phone": "555-0192", "total_spent": 450.0, "is_active": True},
            {"id": "cust-2", "name": "Jane Doe", "email": "jane@example.com", "phone": "555-0144", "total_spent": 120.0, "is_active": True}
        ]

        self.employees = [
            {"id": "emp-1", "user_id": "usr-3", "name": "Store Manager", "role": "MANAGER", "department": "Operations", "salary": 4500.0, "is_active": True},
            {"id": "emp-2", "user_id": "usr-4", "name": "Sales Staff", "role": "STAFF", "department": "Sales", "salary": 2800.0, "is_active": True}
        ]

db = InMemoryRepository()
