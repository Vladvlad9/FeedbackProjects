from sqladmin import ModelView

from models import User, Admin, Dialogue, TelegramMessage


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.user_id, User.phone]

    name = "Пользователи"
    name_plural = "Пользователя"
    icon = "fa-solid fa-user"

    column_labels = {
        User.id: "id",
        User.user_id: "id Телеграм",
        User.phone: "№ телефона",
        User.created_at: "Зарегистрировался в боте",
        User.updated_at: "Был в боте",
        User.is_block: "Заблокирован",
    }

    can_export = False
    can_view_details = True
    # list_template = "list.html"
    # details_template = "details.html"
    # edit_template = "edit.html"
    # create_template = "create.html"
    # column_details_list = [User.id, User.user_id, User.phone]


class AdminAdmin(ModelView, model=Admin):
    column_list = [Admin.id, Admin.admin_id]

    name = "Администратора"
    name_plural = "Администраторы"

    # list_template = "list.html"
    # details_template = "details.html"
    # edit_template = "edit.html"
    # create_template = "create.html"

    column_labels = {
        Admin.id: "id",
        Admin.admin_id: "id Телеграм"
    }


class DialogAdmin(ModelView, model=Dialogue):
    column_list = [Dialogue.id, Dialogue.user_id, Dialogue.admin_id, Dialogue.is_active, Dialogue.who_closed]

    name = "Диалог"

    # list_template = "list.html"
    # details_template = "details.html"
    # edit_template = "edit.html"
    # create_template = "create.html"

    column_labels = {
        Dialogue.id: "id",
        Dialogue.user_id: "id Пользователя",
        Dialogue.admin_id: "id Администратора",
        Dialogue.is_active: "Активный",
        Dialogue.created_at: "Создан",
        Dialogue.updated_at: "Обновлен",
        Dialogue.who_closed: "Кто закрыл",
    }
    can_create = False
    can_edit = False
    can_delete = False


class TelegramMessageAdmin(ModelView, model=TelegramMessage):
    pass
    name = "Рассылка"
    list_template = "test.html"
