from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message


router = Router()


MENU_DATA: dict[str, list[str]] = {
    "Shawarma": [
        "Classic Shawarma",
        "Cheese Shawarma",
        "Spicy Shawarma",
    ],
    "Mangal": [
        "Lula Kebab",
        "Chicken Wings",
        "Beef Skewers",
    ],
    "Fastfood": [
        "Burger",
        "French Fries",
        "Nuggets",
    ],
    "Coffee": [
        "Espresso",
        "Americano",
        "Latte",
    ],
}


def categories_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=category, callback_data=f"category:{category}")]
        for category in MENU_DATA.keys()
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def items_keyboard(category: str) -> InlineKeyboardMarkup:
    items = MENU_DATA.get(category, [])
    buttons = [
        [InlineKeyboardButton(text=item, callback_data=f"order:{category}:{item}")]
        for item in items
    ]
    buttons.append([InlineKeyboardButton(text="Back to categories", callback_data="menu:back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(
        "Welcome to *Shawarma good*!\n"
        "Choose a category from the menu:",
        parse_mode="Markdown",
        reply_markup=categories_keyboard(),
    )


@router.message(Command("menu"))
async def menu_handler(message: Message) -> None:
    await message.answer("Menu categories:", reply_markup=categories_keyboard())


@router.callback_query(lambda c: c.data and c.data.startswith("category:"))
async def show_category(callback: CallbackQuery) -> None:
    category = callback.data.split(":", 1)[1]
    await callback.message.edit_text(
        f"{category} menu. Select an item:",
        reply_markup=items_keyboard(category),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "menu:back")
async def back_to_categories(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        "Menu categories:",
        reply_markup=categories_keyboard(),
    )
    await callback.answer()
