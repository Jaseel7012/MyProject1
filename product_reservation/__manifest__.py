{
    'name': 'Product Reservation',
    'depends': [
               'base_setup','contacts'],
    'data' : [

        'security/ir.model.access.csv',
        'view/sequence.xml',
        'view/product_reservation_form_view.xml',
        'view/product_reservation_details_menu.xml',
        'view/product_reservation_menu.xml',
        'view/product_reservation_list_view.xml',
       # 'data/smart_button_in_contact.xml',
    ],



    'application': True


}