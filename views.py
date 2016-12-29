from pyramid.view import view_config


@view_config(route_name='home', renderer='')
def my_view(request):
    return {'project': 'scaffolds'}
@view_config(route_name='home', renderer='templates/login.pt')
def my_view(request):
    return {}


