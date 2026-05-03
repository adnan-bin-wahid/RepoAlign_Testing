def update_project(request):
    return project_service.update(request)


def delete_project(request):
    return project_service.delete(request)

def archive_project(project_id, user_id, force, notify):
    return project_service.archive(project_id)
