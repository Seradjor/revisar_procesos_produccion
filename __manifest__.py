# -*- coding: utf-8 -*-
{
    'name': "revisar_procesos_produccion",

    'summary': """
        Revisión del correcto funcionamiento de los procesos de la línea de producción.""",

    'description': """
        El objetivo de este módulo es la revisión y control de los distintos procesos realizados en la línea de producción para validar su correcto funcionamiento.

        Para ello, se han definido una serie de comprobaciones para cada uno de dichos procesos para que, el usuario que acceda al módulo, las valide.

        En caso de que alguna de dichas comprobaciones no sean correctas, el usuario deberá indicarlo, abriéndose automáticamente una petición de mantenimiento a rellenar indicando la corrección o reparación a realizar.

        En todo caso, el usuario podrá dejar cualquier tipo de comentario en cada una de las comprobaciones para su futura revisión por parte del responsable de producción.

        El módulo se ejecutará el primer día laboral de la semana, previo a empezar la producción semanal.
    """,

    'author': "Sergio Adell",
    'website': "https://seradjor.github.io/revisar_procesos_produccion/",

    # Indicamos que es una aplicación
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # Seguridad
        'security/ir.model.access.csv',
        # Vistas
        'views/views.xml',
        'views/templates.xml',
        # Datos de modelos
        'data/process.xml',
        'data/verifications.xml',
        'data/errors.xml',
        'data/revisions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
