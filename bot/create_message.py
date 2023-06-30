import random
choice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


def create_message(name, group, date, compliment, stage, other=None,*args,**kwargs):
    choice_ = random.choice(choice)
    match stage:

        case "basic":
            return (f""" 
<b>👨‍🎓 Имя:</b> <code>{name}</code>
<b>📅 Дата рождения:</b> <code>{date.strftime("%d.%m")} </code>
<b>🗽 Группа:</b> <code>{group} </code>

<b>🎂 Поздравление:</b> <code>{compliment}</code>
    """)

        case "cancel":
            return (f"""
<b>❌ Отменено </b> <s>

<b>👨‍🎓 Имя:</b> {name}
<b>📅 Дата рождения:</b> {date.strftime("%d.%m")} 
<b>🗽 Группа:</b> {group} 

<b>🎂 Поздравление: </b> С днем рождения, Данил! В этот день в 1948 году родился комикс "Супермен" - пусть и ты раскроешь свою суперсилу! </s>
    """)

        case "custom":

            return (f""" 
<b>👨‍🎓 Имя:</b> <code>{name}</code>
<b>📅 Дата рождения:</b> <code>{date.strftime("%d.%m")} </code>
<b>🗽 Группа:</b> <code>{group} </code>

<b>📝 Введите текст:</b>
    """)
        case "show":
            return (f""" 
<b>👨‍🎓 Имя:</b> <code>Данила Гинда Александрович</code>
<b>📅 Дата рождения:</b> <code>2005-04-07 </code>
<b>🗽 Группа:</b> <code>ШАД-112 </code>

<b>🎂 Поздравление: С днем рождения, Данил! В этот день в 1948 году родился комикс "Супермен" - пусть и ты раскроешь свою суперсилу!</b>
    """)
        case "regenerate":
            return (f""" 
<b>👨‍🎓 Имя:</b> <code>{name}</code>
<b>📅 Дата рождения:</b> <code>{date.strftime("%d.%m")} </code>
<b>🗽 Группа:</b> <code>{group} </code>

<b>🎂 Поздравление:</b> <code>{compliment} + {choice_}</code> 
    """)

