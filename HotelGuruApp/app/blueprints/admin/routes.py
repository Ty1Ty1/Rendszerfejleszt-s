from app.blueprints.admin import bp
from app.blueprints.admin.schemas import (
    RoomCreateUpdateSchema, RoomAdminResponseSchema, RoomStatusUpdateSchema
)
from app.blueprints.admin.service import AdminService
from apiflask import HTTPError, input, output, abort
from apiflask.fields import Integer

@bp.get('/rooms')
@output(RoomAdminResponseSchema(many=True))
def admin_list_rooms():
    success, response = AdminService.list_all_rooms()
    if success:
        return response, 200
    abort(400, message=response)

@bp.post('/rooms')
@input(RoomCreateUpdateSchema)
@output(RoomAdminResponseSchema, status_code=201)
def admin_create_room(data):
    success, response = AdminService.create_room(data)
    if success:
        return response, 201
    abort(400, message=response) 

@bp.get('/rooms/<int:room_id>')
@output(RoomAdminResponseSchema)
def admin_get_room(room_id):
    success, response = AdminService.get_room_details(room_id)
    if success:
        return response, 200
    abort(404, message=response) 

@bp.put('/rooms/<int:room_id>')
@input(RoomCreateUpdateSchema)
@output(RoomAdminResponseSchema)
def admin_update_room(room_id, data):
    success, response = AdminService.update_room(room_id, data)
    if success:
        return response, 200
    abort(400, message=response) 

@bp.delete('/rooms/<int:room_id>')
@output({}, status_code=200)
def admin_delete_room(room_id):
    success, response = AdminService.delete_room(room_id)
    if success:
        return response, 200
    abort(400, message=response) 

@bp.put('/rooms/<int:room_id>/status')
@input(RoomStatusUpdateSchema)
@output(RoomAdminResponseSchema) 
def admin_update_room_status(room_id, data):
    success, response = AdminService.update_room_status(room_id, data['status'])
    if success:
        return response, 200
    abort(400, message=response) 