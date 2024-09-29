from pweb import Blueprint
from pweb_form_rest import ssr_ui_render

url_prefix = "/social"
social_controller = Blueprint(
    "social_controller",
    __name__,
    url_prefix=url_prefix
)


@social_controller.route("/", methods=['GET'])
def index():
    return ssr_ui_render(view_name="social/home")

@social_controller.route("/profile", methods=['GET'])
def profile():
    return ssr_ui_render(view_name="social/profile")