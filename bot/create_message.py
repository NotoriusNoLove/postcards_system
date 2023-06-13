


def create_message(name, group, date, compliment, stage, *args,**kwargs):
    match stage:

        case "basic":
            return (f""" 
<b>👨‍🎓 Имя:</b> <code>{name}</code>
<b>📅 Дата рождения:</b> <code>{date} </code>
<b>🗽 Группа:</b> <code>{group} </code>

<b>🎂 Поздравление:</b> <code>{compliment}</code>
    """)

        case "cancel":
            return (f"""
<b>❌ Отменено </b> <s>

<b>👨‍🎓 Имя:</b> {name}
<b>📅 Дата рождения:</b> {date} 
<b>🗽 Группа:</b> {group} 

<b>🎂 Поздравление: </b> С днем рождения, Данил! В этот день в 1948 году родился комикс "Супермен" - пусть и ты раскроешь свою суперсилу! </s>
    """)

        case "custom":

            return (f""" 
<b>👨‍🎓 Имя:</b> <code>{name}</code>
<b>📅 Дата рождения:</b> <code>{date} </code>
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