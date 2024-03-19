from aiogram.filters import Command
from aiogram import F, types, Router , Bot
from database import user as db
from keyboards.inline import  earn_button ,subs_button , report_button  , confirm_button ,reports_button ,withdrawl_button

from keyboards.regular import regular_button
from aiogram.enums import ParseMode


other_router = Router()



@other_router.message(F.text.contains(' Earn'))
async def inline_keyboard(message: types.Message ) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        await message.answer("Choose a way to make money." , reply_markup=earn_button())
    else:
        await message.reply("You are not a registered user.\nPress /start to register.")


@other_router.callback_query(F.data == "invite_friend")
async def invite_friend(call: types.CallbackQuery, bot: Bot):
    user = await db.select_user(call.from_user.id)
    # Get bot information
    me = await bot.get_me()

    # Prepare the invitation message
    message = f"""💁‍♂️ Invite friends to the bot and earn rewards!

Send this link to your friends:
https://t.me/{me.username}?start={call.from_user.id}

<b>Get 200 ₹ for each friend you invite!</b>
(Referral rewards are credited only after your friend activates the bot)

◽️ Users Invited: {user.invited_count}
◽️ Earnings: {user.balance} ₹"""

    # Edit the message with the updated information
    await call.message.edit_text(message, parse_mode=ParseMode.HTML)



@other_router.callback_query(F.data == "join_channel")
async def invite_friend(call: types.CallbackQuery, bot: Bot):
    user = await db.select_user(call.from_user.id)
    msg = "Join to the channel and get 100 ₹ \nhttps://t.me/tgsponser"
    await call.message.edit_text(msg, reply_markup=subs_button())



  
@other_router.callback_query(F.data=="subs")
async def invite_friend(call: types.CallbackQuery, bot: Bot):
    user = await db.select_user(call.from_user.id)
    if not user.joined:
        result = await bot.get_chat_member("@tgsponser", user.user_id)
        if result.status not in ["member", "creator", "administrator"]:
            await call.answer("❌ Check failed! Subscribe to the channel" , show_alert=True)
        else:
            await db.user_joined_channel(user.user_id)
            await call.message.edit_text("✅ Verification passed! You have credited 300 ₹\n\nStay active and do not unsubscribe from the channel for 5 days. If you unsubscribe, the money will be returned.")
    else:
        await call.message.edit_text("You have already done this. Try another option to earn.")
    


@other_router.callback_query(F.data=="view_post")
async def invite_friend(call: types.CallbackQuery, bot: Bot):
    user = await db.select_user(call.from_user.id)
    if not user.viewed:
        await call.message.edit_text("Watching started")
        
        # Simulate watching 10 posts
        for i in range(1, 11):
            await call.message.edit_text(f"{i} post(s) watched.")
      
        await call.message.edit_text("<b>View of posts completed! You have been credited with 100 ₹!</b>", parse_mode=ParseMode.HTML)
        await db.user_viewed(call.from_user.id)

    else:
        await call.message.edit_text("Viewing posts will be available through next day.")
   





@other_router.message(F.text.contains('Partners'))
async def inline_keyboard(message: types.Message , bot: Bot) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        me = await bot.get_me()
        msg= f"""💁‍♂️Invite partners to the bot and get paid for them!

Send this link to a friend:
https://t.me/{me.username}?start={user.user_id}

<b>Get 200 ₹ for each friend you invite!</b>
(Referral rewards are credited only after your friend activates the bot)

◽️ Users Invited: {user.invited_count}
◽️ Earnings: {user.balance} ₹"""

       # Edit the message with the updated information
        await message.answer(msg, parse_mode=ParseMode.HTML)


    else:
        await message.reply("You are not a registered user.\nPress /start to register.")
   

   
@other_router.message(F.text.contains('Balance'))
async def inline_keyboard(message: types.Message ) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        msg = f"""
Balance: {user.balance} ₹
Hold balance: 0 ₹
Minimum withdrawal amount 7000 ₹"""
        await message.answer(msg , parse_mode=ParseMode.HTML,reply_markup=withdrawl_button())
    else:
        await message.reply("You are not a registered user.\nPress /start to register." )



@other_router.callback_query(F.data=="withdrawl")
async def invite_friend(call: types.CallbackQuery , bot:Bot):
    user = await db.select_user(call.from_user.id)
    if user:
        if user.balance   > 7000:
            msg = "You are eligible to withdrawl money.\nSend qr at @XoronMan to get money."
            await bot.send_message(call.from_user.id , msg)

        
        else:
            await bot.send_message(call.from_user.id ,"❌ Minimum withdrawal amount 7.000 ₹" )
 

       
    else:
        await call.message.edit_text("You are not a registered user.\nPress /start to register." )

        
        




   

@other_router.message(F.text.contains('❓ Help'))
async def inline_keyboard(message: types.Message ) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        msg ="""This bot has a very simple system: sponsor channels pay the bot for advertising, and the bot pays you for subscribing to these channels!

<b>🔑You can withdraw money from the bot to: PayTM, UPI, Mobikwik Visa/Mastercard, etc.</b>"""
        await message.answer(msg , parse_mode=ParseMode.HTML ,reply_markup=report_button())
    else:
        await message.reply("You are not a registered user.\nPress /start to register.")
 



@other_router.callback_query(F.data=="report")
async def invite_friend(call: types.CallbackQuery):
    await call.message.edit_text("Select Report type:" , reply_markup=reports_button())


@other_router.callback_query(F.data=="confirm")
async def invite_friend(call: types.CallbackQuery):
    await call.message.edit_text("Do you really want to send a report?" , reply_markup=confirm_button())



@other_router.callback_query(F.data=="yes")
async def invite_friend(call: types.CallbackQuery):
    await call.message.edit_text("✅ The report has been sent and will be reviewed shortly.")


@other_router.callback_query(F.data=="no")
async def invite_friend(call: types.CallbackQuery):
    await call.message.edit_text("❌ Action canceled")

