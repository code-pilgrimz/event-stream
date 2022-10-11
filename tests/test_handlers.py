from app.events.user import UserEvent


def test_user_event():
    e = UserEvent(id=1, email="a@b.c", full_name="a", is_active=True, hashed_password="x")
    assert e.id == 1
# left a note for myself
