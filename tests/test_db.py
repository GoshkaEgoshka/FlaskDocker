from unittest import TestCase
from flask.cli import with_appcontext

import pytest

from aiounittest import AsyncTestCase

from web.app import app
from web.models import db, Users
from web.database import add_user_to_db, remove_user, get_user_by_id, update_user


class TestDB(AsyncTestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.drop_all()
            db.create_all()
        self.test_app = app.test_client()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    @pytest.mark.asyncio
    async def test_add_user_to_db(self):
        user = {
            'user_id': 1,
            'username': 'testuser',
            'email': 'testemail@gmail.com'
        }
        with app.app_context():
            await add_user_to_db(**user)
            added_user = Users.query.filter_by(
                username='testuser'
            ).first()
            all_u = [u for u in Users.query.all()]
        self.assertEqual(added_user.email, 'testemail@gmail.com')
        self.assertEqual(len(all_u), 1)

    @pytest.mark.asycio
    async def test_get_user_by_id(self):
        user = {
            'user_id': 12345,
            'username': 'supertest',
            'email': 'supertest@gmail.com'
        }
        with app.app_context():
            await add_user_to_db(**user)
            user = await get_user_by_id(id=12345)
        self.assertEqual(user['id'], 12345)
        self.assertEqual(user['username'], 'supertest')
        self.assertEqual(user['email'], 'supertest@gmail.com')

    @pytest.mark.asycio
    async def test_get_user_by_id_user_not_exists(self):
        with app.app_context():
            result = await get_user_by_id(id=555555)
            self.assertEqual(result, 'User does not exist!')

    @pytest.mark.asyncio
    async def test_remove_user(self):
        user = {
            'user_id': 1,
            'username': 'testuser',
            'email': 'testemail@gmail.com'
        }
        with app.app_context():
            await add_user_to_db(**user)
            await remove_user(id=1)
            all_u = [u for u in Users.query.all()]
            removed_user = Users.query.filter_by(
                id=1
            ).first()
        self.assertEqual(len(all_u), 0)
        self.assertEqual(removed_user, None)

    @pytest.mark.asyncio
    async def test_remove_user_not_exists(self):
        with app.app_context():
            result = await remove_user(id=888888)
            self.assertEqual(result, 'User does not exist!')

    @pytest.mark.asyncio
    async def test_update_user(self):
        user = {
            'user_id': 1,
            'username': 'testuser',
            'email': 'testemail@gmail.com'
        }
        with app.app_context():
            await add_user_to_db(**user)
            result = await update_user(id=1, username='updateduser', email='updatedemail@gmail.com')
            user = await get_user_by_id(id=1)
            all_u = [u for u in Users.query.all()]
        self.assertEqual(len(all_u), 1)
        self.assertEqual(result, 'Updated')
        self.assertEqual(user['id'], 1)
        self.assertEqual(user['username'], 'updateduser')
        self.assertEqual(user['email'], 'updatedemail@gmail.com')

    @pytest.mark.asyncio
    async def test_update_user_not_exists(self):
        with app.app_context():
            result = await update_user(id=288882, username='updateduser', email='updatedemail@gmail.com')
        self.assertEqual(result, 'User does not exist!')
