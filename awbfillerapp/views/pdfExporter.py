from django.http import FileResponse
from django.views import View
from fillpdf import fillpdfs

from awbfillerapp.models import airwayBill

class pdfExport(View):
    def exporter(request, id):
        file_path = 'Air Waybill Form _ Printable Template (4).pdf'
        form_fields = list(fillpdfs.get_form_fields(file_path))
        # print(form_fields)
        ShippingInfo = airwayBill.objects.get(pk=id)

        form_fields_mapping = {
    'Text-shipper-name': ShippingInfo.shipper_name,
    'Text-shipper-address': ShippingInfo.shipper_address,
    'Text-awb-no': ShippingInfo.awb_no,
    'Text-issued-by': ShippingInfo.issued_by,
    'Text-consignee-name': ShippingInfo.consignee_name,
    'Text-consignee-address': ShippingInfo.consignee_address,
    'Text-issuing-agent-name': ShippingInfo.issuing_agent_name,
    'Text-issuing-agent-city': ShippingInfo.issuing_agent_city,
    'Text-accounting-information': ShippingInfo.accounting_information,
    'Text-agent-aita-code': ShippingInfo.agent_aita_code,
    'Text-agent-account-no': ShippingInfo.agent_account_no,
    'Text-airport-departure': ShippingInfo.airport_departure,
    'Text-referenceno': ShippingInfo.reference_no,
    'Text-optionalshippinginfo1': ShippingInfo.optional_shipping_info1,
    'Text-optionalshippinginfo2': ShippingInfo.optional_shipping_info2,
    'Text-to': ShippingInfo.to,
    'Text-by_first_carrier': ShippingInfo.by_first_carrier,
    'Text-to_after_byfirstcarrier': ShippingInfo.to_after_by_first_carrier,
    'Text-by_afterCarrier': ShippingInfo.by_after_carrier,
    'Text-to_aftertoafterCarrier': ShippingInfo.to_after_to_after_carrier,
    'Text-by_afterbyafterCarrier': ShippingInfo.by_after_by_after_carrier,
    'Text-currency': ShippingInfo.currency,
    'Text-chgscode': ShippingInfo.chgs_code,
    'Text-wt_ppd': ShippingInfo.wt_ppd,
    'Text-wt_col': ShippingInfo.wt_col,
    'Text-other_ppd': ShippingInfo.other_ppd,
    'Text-other_coll': ShippingInfo.other_col,
    'Text-declaredvalcarriage': ShippingInfo.declared_val_carriage,
    'Text-declaredvalcustomse': ShippingInfo.declared_val_customse,
    'Text-destination': ShippingInfo.destination,
    'Text-flightdate': ShippingInfo.flight_date,
    'Text-NFKcBalxE_': ShippingInfo.flight_date_carrier,
    'Text-amount_insurance': ShippingInfo.amount_insurance,
    'Paragraph-handling_information': ShippingInfo.handling_information,
    'Paragraph-no_of_pieces': ShippingInfo.no_of_pieces,
    'Paragraph-gross_weight': ShippingInfo.gross_weight,
    'Paragraph-kg_lb': ShippingInfo.kg_lb,
    'Paragraph-rateclass_commodityitemno': ShippingInfo.rate_class_commodity_item_no,
    'Paragraph-chargeable_weight': ShippingInfo.chargeable_weight,
    'Paragraph-rate_charge': ShippingInfo.rate_charge,
    'Paragraph-total': ShippingInfo.total,
    'Paragraph-nature_of_goods': ShippingInfo.nature_of_goods,
    'Text-prepaid': ShippingInfo.prepaid,
    'Text-collect': ShippingInfo.collect,
    'Text-val_change1': ShippingInfo.val_change1,
    'Text-val_change2': ShippingInfo.val_change2,
    'Text-tax1': ShippingInfo.tax1,
    'Text-totchgdueagent1': ShippingInfo.tot_chg_due_agent1,
    'Text-totchgdueagent2': ShippingInfo.tot_chg_due_agent2,
    'Text-totchgduecarrier': ShippingInfo.tot_chg_due_carrier,
    'Text-totchgduecarrier2': ShippingInfo.tot_chg_due_carrier2,
    'Text-total_prepaid_bottom': ShippingInfo.total_prepaid_bottom,
    'Text-total_collect_bottom': ShippingInfo.total_collect_bottom,
    'Text-currconversionrate': ShippingInfo.curr_conversion_rate,
    'Text-ccchanges': ShippingInfo.cc_changes,
    'Text-carrieratdestination': ShippingInfo.carrier_at_destination,
    'Text-chargesatdestination': ShippingInfo.charges_at_destination,
    'Paragraph-othercharges': ShippingInfo.other_charges,
    'Text-totalcollectcharges': ShippingInfo.total_collect_charges,
    'text-total-no_of_pieces': ShippingInfo.total_no_of_pieces,
    'Text-total-gross_weight': ShippingInfo.total_gross_weight,
    'Text-total-total': ShippingInfo.total_total
}


        export_pdf = fillpdfs.write_fillable_pdf(file_path, 'awb.pdf', form_fields_mapping,flatten=True)

        response = FileResponse(open('awb.pdf', "rb"), as_attachment=True)
        return response
    