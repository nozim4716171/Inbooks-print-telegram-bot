from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu_keyboard(i18n) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=i18n("order")),
                KeyboardButton(text=i18n("prices")),
            ],
            [
                KeyboardButton(text=i18n("calculate_price")),
                KeyboardButton(text=i18n("my_orders")),
            ],
            [
                KeyboardButton(text=i18n("cart")),
                KeyboardButton(text=i18n("branches")),
            ],
            [
                KeyboardButton(text=i18n("contact_us")),
                KeyboardButton(text=i18n("settings")),
            ],
            [
                KeyboardButton(text=i18n("feedbacks")),
            ],
        ],
        resize_keyboard=True,
    )


def phone_request_keyboard(i18n) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text=i18n("send_phone_number"),
                    request_contact=True,
                )
            ]
        ],
        resize_keyboard=True,
    )
