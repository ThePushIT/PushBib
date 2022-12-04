from flask import Blueprint
from services.reference_service import reference_service
from services.user_service import user_service

test_controller = Blueprint("test", __name__)


@test_controller.route("/tests/reset/", methods=["POST"])
def reset():
    print('ollaan test reset routessa')
    reference_service.delete_all_references()
    user_service.delete_all_users()

    return "ok"
