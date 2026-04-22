from aiogram import Router
from aiogram.types import CallbackQuery

from database import save_order
from handlers.menu import items_keyboard


router = Router()


@router.callback_query(lambda c: c.data and c.data.startswith("order:"))
async def order_item(callback: CallbackQuery) -> None:
    _, category, item_name = callback.data.split(":", 2)
    user = callback.from_user

    save_order(
        user_id=user.id,
        username=user.username,
        category=category,
        item_name=item_name,
    )

    await callback.answer("Added to your order!", show_alert=False)
    await callback.message.edit_text(
        f"Added: {item_name}\n"
        f"Category: {category}\n\n"
        "You can add more items:",
        reply_markup=items_keyboard(category),
    )
