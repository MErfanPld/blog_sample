from django.contrib import admin
from .models import Cost, Income, Debtor, Creditor


class CostAdmin(admin.ModelAdmin):
    list_display = ('cost_title', 'cost_type', 'cost_amount', 'cost_date',)
    list_filter = ('cost_type', 'cost_date',)
    search_fields = ('cost_title', 'cost_type', 'cost_amount', 'cost_revenue', 'cost_date',)
    ordering = ['-cost_date']


admin.site.register(Cost, CostAdmin)


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_date', 'income_amount',)
    list_filter = ('income_date', 'income_amount',)
    search_fields = ('income_date', 'income_amount',)
    ordering = ['-income_date']


admin.site.register(Income, IncomeAdmin)


class DebtorAdmin(admin.ModelAdmin):
    list_display = ('debtor_received', 'debtor_to_borrow',)
    list_filter = ('debtor_received', 'debtor_to_borrow',)
    search_fields = ('debtor_received', 'debtor_to_borrow',)


admin.site.register(Debtor, DebtorAdmin)


class CreditorAdmin(admin.ModelAdmin):
    list_display = ('creditor_payment', 'creditor_to_lend',)
    list_filter = ('creditor_payment', 'creditor_to_lend',)
    search_fields = ('creditor_payment', 'creditor_to_lend',)


admin.site.register(Creditor, CreditorAdmin)
