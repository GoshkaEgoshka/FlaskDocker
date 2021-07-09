from web.app import app, db

def create_app():
    """
        Creates app
    """
    if app.config['INIT_DB']:
        with app.app_context():
            db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=1, host='0.0.0.0', port=5000)
