from django.db import models

class airwayBill(models.Model):
    shipper_name = models.CharField(max_length=255, null=True, blank=True, default = '')
    shipper_address = models.TextField(blank=True, default = '')
    awb_no = models.CharField(max_length=100, null=True, blank=True, default = '')
    issued_by = models.CharField(max_length=100, blank=True, default = '')
    consignee_name = models.CharField(max_length=255, blank=True, default = '') 
    consignee_address = models.TextField(blank=True, default = '')
    issuing_agent_name = models.CharField(max_length=255, blank=True, default = '')
    issuing_agent_city = models.CharField(max_length=2055, blank=True, default = '')
    accounting_information = models.CharField(max_length=2055, blank=True, default = '')
    agent_aita_code = models.CharField(max_length=50, blank=True)
    agent_account_no = models.CharField(max_length=100, blank=True, default = '')
    airport_departure = models.CharField(max_length=100, blank=True, default = '')
    reference_no = models.CharField(max_length=100, blank=True, default = '')
    optional_shipping_info1 = models.CharField(max_length=255, blank=True, default = '')
    optional_shipping_info2 = models.CharField(max_length=255, blank=True, default = '')
    to = models.CharField(max_length=100, blank=True, default = '')
    by_first_carrier = models.CharField(max_length=100, blank=True, default = '')
    to_after_by_first_carrier = models.CharField(max_length=100, blank=True, default = '')
    by_after_carrier = models.CharField(max_length=100, blank=True, default = '')
    to_after_to_after_carrier = models.CharField(max_length=100, blank=True, default = '')
    by_after_by_after_carrier = models.CharField(max_length=100, blank=True, default = '')
    currency = models.CharField(max_length=10, blank=True, default = '')
    chgs_code = models.CharField(max_length=10, blank=True, default = '')
    wt_ppd = models.CharField( max_length=10,blank=True, default = '')
    wt_col = models.CharField(  max_length=10,blank=True, default = '')
    other_ppd = models.CharField(  max_length=10,blank=True, default = '')
    other_col = models.CharField(  max_length=10,blank=True, default = '')
    declared_val_carriage = models.CharField(max_length=10,blank=True, default = '')
    declared_val_customse = models.CharField(max_length=10,blank=True, default = '')
    destination = models.CharField(max_length=100, blank=True, default = '')
    flight_date = models.DateField(blank=True, null=True)
    flight_date_carrier = models.CharField(max_length=100, blank=True, default = '')
    amount_insurance = models.CharField(max_length=255,  blank=True, default = '')
    handling_information = models.TextField(blank=True, default = '')
    no_of_pieces = models.CharField(blank=True,default = '',max_length=255 )
    gross_weight = models.CharField(max_length=255,  blank=True, default = '')
    kg_lb = models.CharField(max_length=10, blank=True, default = '')
    rate_class_commodity_item_no = models.CharField(max_length=100, blank=True, default = '')
    chargeable_weight = models.CharField(max_length=255,  blank=True, default = '')
    rate_charge = models.CharField(max_length=255,  blank=True, default = '')
    total = models.CharField(max_length=255,  blank=True,default = '' )
    nature_of_goods = models.TextField(blank=True, default = '')
    prepaid = models.CharField(max_length=255,  blank=True, default = '')
    collect = models.CharField(max_length=255,  blank=True, default = '')
    val_change1 = models.CharField(max_length=255,  blank=True, default = '')
    val_change2 = models.CharField(max_length=255,  blank=True, default = '')
    tax1 = models.CharField(max_length=255,  blank=True, default = '')
    tot_chg_due_agent1 = models.CharField(max_length=255,  blank=True, default = '')
    tot_chg_due_agent2 = models.CharField(max_length=255,  blank=True, default = '')
    tot_chg_due_carrier = models.CharField(max_length=255,  blank=True,default = '')
    tot_chg_due_carrier2 = models.CharField(max_length=255,  blank=True, default = '')
    total_prepaid_bottom = models.CharField(max_length=255,  blank=True, default = '')
    total_collect_bottom = models.CharField(max_length=255,  blank=True, default = '')
    curr_conversion_rate = models.CharField(max_length=255,  blank=True, default = '')
    cc_changes = models.CharField(max_length=255,  blank=True,default = '')
    carrier_at_destination = models.CharField(max_length=255, blank=True, default = '')
    charges_at_destination = models.CharField(max_length=255,  blank=True,default = '')
    other_charges = models.CharField(max_length=2055, blank=True, )
    total_collect_charges = models.CharField(max_length=255,  blank=True,default = '' )
    total_no_of_pieces = models.CharField(blank=True,max_length=255,default = '' )
    total_gross_weight = models.CharField(max_length=255,  blank=True,default = '')
    total_total = models.CharField(max_length=255,  blank=True, default = '')



    def __str__(self):
        return f'AWB No: {self.awb_no} - Shipper: {self.shipper_name}'
  