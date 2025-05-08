from app.blueprints.admin import bp
from app.blueprints.admin.schemas import (
    RoomCreateUpdateSchema, RoomAdminResponseSchema, RoomStatusUpdateSchema
)
from app.blueprints.admin.service import AdminService
from apiflask import HTTPError
from apiflask.fields import Integer

@bp.route('/')
def index():
    return 'This is The Admin Blueprint'

@bp.get('/rooms')
@bp.output(RoomAdminResponseSchema(many=True))
def admin_list_rooms():
    success, response = AdminService.list_all_rooms()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.post('/rooms')
@bp.input(RoomCreateUpdateSchema)
@bp.output(RoomAdminResponseSchema, status_code=201)
def admin_create_room(data):
    success, response = AdminService.create_room(data)
    if success:
        return response, 201
    raise HTTPError(message=response, status_code=400)

@bp.get('/rooms/<int:room_id>')
@bp.output(RoomAdminResponseSchema)
def admin_get_room(room_id):
    success, response = AdminService.get_room_details(room_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400) 

@bp.put('/rooms/<int:room_id>')
@bp.input(RoomCreateUpdateSchema)
@bp.output(RoomAdminResponseSchema)
def admin_update_room(room_id, data):
    success, response = AdminService.update_room(room_id, data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.delete('/rooms/<int:room_id>')
@bp.output({}, status_code=200)
def admin_delete_room(room_id):
    success, response = AdminService.delete_room(room_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400) 

@bp.put('/rooms/<int:room_id>/status')
@bp.input(RoomStatusUpdateSchema)
@bp.output(RoomAdminResponseSchema) 
def admin_update_room_status(room_id, data):
    success, response = AdminService.update_room_status(room_id, data['status'])
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400) 
