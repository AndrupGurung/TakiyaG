{
    'name': 'Doppler_HMS',
    'version': '16.0.0.0.0',
    'category': 'Extra Tools',
    'website': 'www.hmsdoppler.com',
    'sequence': '1',
    'summary': 'Module for managing the hotels',
    'author': 'Doppler Netcare',
    'depends': [
        'mail', 'board'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/billing.xml',
        'views/currentDate.xml',
        'views/currentTime.xml',
        'views/dashboard.xml',
        'views/endOfDay.xml',
        'views/fo_status.xml',
        'views/frontOffice.xml',
        'views/hk_status.xml',
        'views/logOut.xml',
        'views/menu.xml',
        'views/notifications.xml',
        'views/reports.xml',
        'views/reservation.xml',
        'views/roomFeatures.xml',
        'views/roomTypes.xml',
        'views/roomStatus.xml'
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'Doppler_HMS/static/src/xml/box.html',
    ],
    'assets': {
        'web.assets_backend': [
            'Doppler_HMS/static/src/css/box.css',
            'Doppler_HMS/Static/src/css/banner.css',
        ]},
    'auto_install': False,
}
