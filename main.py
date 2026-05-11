# pyrefly: ignore [missing-import]
from flask import Flask, jsonify
# pyrefly: ignore [missing-import]
from sqlalchemy import text
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from infrastructure.database.session import SessionLocal


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(
            {
                "app": "spk-dss",
                "message": "SPK DSS API is running",
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/db-check")
    def db_check():
        session = SessionLocal()

        try:
            session.execute(text("SELECT 1"))
            return jsonify(
                {
                    "database": "connected",
                    "status": "ok",
                }
            )
        except SQLAlchemyError as exc:
            return (
                jsonify(
                    {
                        "database": "disconnected",
                        "status": "error",
                        "detail": str(exc),
                    }
                ),
                500,
            )
        finally:
            session.close()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
