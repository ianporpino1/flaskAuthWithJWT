from flaskapp import create_app
from app.models import db, User

app = create_app()

with app.app_context():
    db.create_all()
    # Crie um usuário de exemplo
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', email='admin@example.com')
        admin.set_password('password')
        db.session.add(admin)
        db.session.commit()