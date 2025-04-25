
{
    'name': "Real Estate",
    'summary': "Manage real estate agences works ",
    'description': "Manage real estate listings and client offers.",    

    'author': "Diego Vega",
    'category': 'Management',
    'version': '16.0',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    "application":True,
    "installable":True,
    "auto_install":False,
}