from enum import Enum

from pydantic import Field, BaseModel, StrictInt, StrictStr


class PollValue(BaseModel):
    """Класс значения опроса"""
    text: StrictStr
    value: StrictInt


class PollField(Enum):
    """Базовый класс для перечислений значений опроса"""

    def __getattr__(self, item):
        return getattr(Enum, item)

    @staticmethod
    def get_value_by_text(poll, text: str) -> int | None:
        """Получение значения по тексту"""
        for field in poll:
            if field.value.text == text:
                return field.value.value

        return None

    def __list__(self):
        return [field for field in self.__dict__.keys()]


class AuditPoll(BaseModel):
    """Класс опроса AUDIT

    https://mosgorzdrav.ru/ru-Ru/test/default/card/5.html
    """

    class Field1Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Раз в месяц или реже", value=1)
        value_3 = PollValue(text="2-4 раза в месяц", value=2)
        value_4 = PollValue(text="2-3 раза в неделю", value=3)
        value_5 = PollValue(text="4 раза в неделю и чаще", value=4)

    field1: Field1Enum = Field(title="Как часто Вы употребляете алкогольные напитки?")

    class Field2Enum(PollField):
        value_1 = PollValue(text="1 или 2 стандартных порции", value=0)
        value_2 = PollValue(text="3 или 4 стандартных порции", value=1)
        value_3 = PollValue(text="5 или 6 стандартных порций", value=2)
        value_4 = PollValue(text="7 или 9 стандартных порций", value=3)
        value_5 = PollValue(text="10 или более стандартных порций", value=4)

    field2: Field2Enum = Field(
        title="Сколько алкогольных напитков (стандартных порций) Вы употребляете в типичный день, когда выпиваете?"
    )

    class Field3Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Реже одного раза в месяц", value=1)
        value_3 = PollValue(text="Ежемесячно", value=2)
        value_4 = PollValue(text="Еженедельно", value=3)
        value_5 = PollValue(text="Ежедневно или почти ежедневно", value=4)

    field3: Field3Enum = Field(
        title="Как часто Вы употребляете как минимум 1,5 л пива, или как минимум 180 мл крепкого алкоголя, или как "
              "минимум бутылку вина или шампанского (750 мл) в течение 24 часов?"
    )

    class Field4Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Менее, чем 1 раз в месяц", value=1)
        value_3 = PollValue(text="1 раз в месяц (ежемесячно)", value=2)
        value_4 = PollValue(text="1 раз в неделю (еженедельно)", value=3)
        value_5 = PollValue(text="Ежедневно или почти ежедневно", value=4)

    field4: Field4Enum = Field(
        title="Как часто за последние 12 месяцев Вы не смогли остановиться, начав употреблять алкогольные напитки?"
    )

    class Field5Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Менее, чем 1 раз в месяц", value=1)
        value_3 = PollValue(text="1 раз в месяц (ежемесячно)", value=2)
        value_4 = PollValue(text="1 раз в неделю (еженедельно)", value=3)
        value_5 = PollValue(text="Ежедневно или почти ежедневно", value=4)

    field5: Field5Enum = Field(
        title="Как часто за последние 12 месяцев из-за выпивки Вы не сделали то, что от Вас обычно ожидалось?"
    )

    class Field6Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Менее, чем 1 раз в месяц", value=1)
        value_3 = PollValue(text="1 раз в месяц (ежемесячно)", value=2)
        value_4 = PollValue(text="1 раз в неделю (еженедельно)", value=3)
        value_5 = PollValue(text="Ежедневно или почти ежедневно", value=4)

    field6: Field6Enum = Field(
        title="Как часто за последние 12 месяцев Вам необходимо было выпить утром, чтобы прийти в себя после выпивки "
              "(опохмелиться)"
    )

    class Field7Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Менее, чем 1 раз в месяц", value=1)
        value_3 = PollValue(text="1 раз в месяц (ежемесячно)", value=2)
        value_4 = PollValue(text="1 раз в неделю (еженедельно)", value=3)
        value_5 = PollValue(text="Ежедневно или почти ежедневно", value=4)

    field7: Field7Enum = Field(
        title="Как часто за последние 12 месяцев Вы испытывали чувство вины или сожаления после выпивки?"
    )

    class Field8Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Менее, чем 1 раз в месяц", value=1)
        value_3 = PollValue(text="1 раз в месяц (ежемесячно)", value=2)
        value_4 = PollValue(text="1 раз в неделю (еженедельно)", value=3)
        value_5 = PollValue(text="Ежедневно или почти ежедневно", value=4)

    field8: Field8Enum = Field(
        title="Как часто за последние 12 месяцев Вы были неспособны вспомнить, что было накануне, из-за того, что Вы "
              "выпивали?"
    )

    class Field9Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Да, но это было более, чем год назад", value=2)
        value_3 = PollValue(text="Да, в течение этого года", value=4)

    field9: Field9Enum = Field(
        title="Являлось ли Ваше употребление алкогольных напитков причиной травмы у Вас или других людей?"
    )

    class Field10Enum(PollField):
        value_1 = PollValue(text="Никогда", value=0)
        value_2 = PollValue(text="Да, но это было более, чем год назад", value=2)
        value_3 = PollValue(text="Да, в течение этого года", value=4)

    field10: Field10Enum = Field(
        title="Случалось ли, что Ваш близкий человек или родственник, друг или врач беспокоился насчет употребления "
              "Вами алкоголя или советовал выпивать меньше?"
    )

    @staticmethod
    def get_fields():
        return AuditPoll.__fields__

    @staticmethod
    def get_result() -> dict:
        return {
            "1": {
                "name": "Зона 1",
                "value_for": {
                    "woman": {
                        "between": {
                            "from": 0,
                            "to": 4
                        },
                    },
                    "man": {
                        "between": {
                            "from": 0,
                            "to": 8
                        },
                    }
                },
                "level": "Относительно низкий риск возникновения проблем, связанных с употреблением алкоголя",
            }
        }
