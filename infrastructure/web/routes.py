# pyrefly: ignore [missing-import]
from infrastructure.web.controllers.display_controller import create_display_blueprint
# pyrefly: ignore [missing-import]
from flask import Flask

from infrastructure.web.controllers.cpu_brand_controller import (
    create_cpu_brand_blueprint,
)
from infrastructure.web.controllers.processor_controller import (
    create_processor_blueprint,
)
from infrastructure.web.controllers.vga_brand_controller import (
    create_vga_brand_blueprint,
)
from infrastructure.web.controllers.vga_brand_controller import (
    create_vga_brand_blueprint,
)

API_V1_PREFIX = "/api/v1"


def register_api_v1_routes(app: Flask, session_factory) -> None:
    app.register_blueprint(
        create_cpu_brand_blueprint(session_factory),
        url_prefix=API_V1_PREFIX,
    )
    app.register_blueprint(
        create_processor_blueprint(session_factory),
        url_prefix=API_V1_PREFIX,
    )
    app.register_blueprint(
        create_vga_brand_blueprint(session_factory),
        url_prefix=API_V1_PREFIX
    )
    app.register_blueprint(
        create_display_blueprint(session_factory),
        url_prefix=API_V1_PREFIX,
    )
