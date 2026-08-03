"""One-shot database seeding script."""
from app import auth
from app.database import Base, _Engine, init_db
from app.models import User

ADMIN_USERNAME = "admin"
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin1234"


def main():
    init_db()
    db = _Engine.SessionLocal()
    try:
        if db.query(User).filter(User.username == ADMIN_USERNAME).first():
            print("Admin already exists; nothing to seed.")
            return
        db.add(
            User(
                username=ADMIN_USERNAME,
                email=ADMIN_EMAIL,
                hashed_password=auth.hash_password(ADMIN_PASSWORD),
            )
        )
        db.commit()
        print(f"Seeded admin user: {ADMIN_USERNAME} / {ADMIN_PASSWORD}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
