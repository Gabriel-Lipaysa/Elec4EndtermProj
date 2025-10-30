from app import bcrypt, db, app
from app.models.user import User
from datetime import datetime

def seed():
    with app.app_context():
        existing = User.query.filter_by(email='admin@example.com').first()
        
        if existing:
            print('Admin already seeded')
            return
        
        user = User(
            name = 'Admin',
            username = 'admin',
            email = 'admin@example.com',
            password = bcrypt.generate_password_hash('admin123').decode('utf-8'),
            role = 'admin',
            created_at = datetime.now(),
            updated_at = datetime.now()
            )
        
        db.session.add(user)
        db.session.commit()

        print('Admin user seeded successfully!')

if __name__ == '__main__':
    seed()