from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def earn_button():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💼 Invite a friend (₹200)", callback_data="invite_friend")],
            [InlineKeyboardButton(text="📢 Join a channel (₹300)", callback_data="join_channel")],
            [InlineKeyboardButton(text="👀 View a post (₹100)", callback_data="view_post")],
        ]
    )
    return kb


def subs_button():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Check subscription", callback_data="subs")],
           
        ]
    )
    return kb



def report_button():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⚠️ Report", callback_data="report")],
           
        ]
    )
    return kb


def withdrawl_button():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Withdrawal 💸", callback_data="withdrawl")],
        ]
    )
    return kb


def confirm_button():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Yes", callback_data="yes")],
            [InlineKeyboardButton(text="❌ No", callback_data="no")],
        ]
    )
    return kb




def reports_button():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Scam", callback_data="confirm")],
            [InlineKeyboardButton(text="Pornography", callback_data="confirm")],
            [InlineKeyboardButton(text="Fake", callback_data="confirm")],
            [InlineKeyboardButton(text="Not working", callback_data="confirm")],
            [InlineKeyboardButton(text="Other", callback_data="confirm")],

        ]
    )
    return kb