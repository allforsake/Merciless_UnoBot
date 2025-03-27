#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Colors
RED = 'r'
BLUE = 'b'
GREEN = 'g'
YELLOW = 'y'
BLACK = 'x'

COLORS = (RED, BLUE, GREEN, YELLOW)

COLOR_ICONS = {
    RED: '❤️',
    BLUE: '💙',
    GREEN: '💚',
    YELLOW: '💛',
    BLACK: '⬛️'
}

# Values
ZERO = '0'
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
DRAW_TWO = 'draw'
REVERSE = 'reverse'
SKIP = 'skip'

VALUES = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, DRAW_TWO,
          REVERSE, SKIP)
WILD_VALUES = (ONE, TWO, THREE, FOUR, FIVE, DRAW_TWO, REVERSE, SKIP)

# Special cards
CHOOSE = 'colorchooser'
DRAW_FOUR = 'draw_four'

SPECIALS = (CHOOSE, DRAW_FOUR)

CARDS_CLASSIC = {
    "normal": {
        "b_0": "CAACAgIAAxkBAAFA0uVn5CqdJK2uBVB--spJwIXpBLIJpQAC320AAnSoGEum_5ZWd8-gsDYE",
        "b_1": "CAACAgIAAxkBAAFA0vFn5CqhdLqM2-bjb91aLnArSjrUDgAC8noAAtq2GUtcJY1qj6kHuzYE",
        "b_2": "CAACAgIAAxkBAAFA0vdn5CqlRFIqRDcmr32Gfnn7RZ9ZVQACd2kAAlRVGUvuaSAJdNJLtzYE",
        "b_3": "CAACAgIAAxkBAAFA0v1n5Cqo8eqWZ_P26pZwnk1Dyc6XnQACknsAAuizGUvv2Chb-Wgl7DYE",
        "b_4": "CAACAgIAAxkBAAFA0wdn5Cqr9D-yk-fcqQFeopQ2DmwUqwACRHIAAlgSGEs_GfdctJ_5wjYE",
        "b_5": "CAACAgIAAxkBAAFA0w1n5CquF1nx_MHjNCmsUs3I1ORhXwACFW4AAnn0GUvT52h1lgzvvTYE",
        "b_6": "CAACAgIAAxkBAAFA0w9n5Cqx7tcIKPxd0x5tTiSQZGBVMgACzHsAAhZ6GUuZevqaKLZFsDYE",
        "b_7": "CAACAgIAAxkBAAFA0xNn5Cq0Y3FFrKFu8n8m8TJ-cyL2tAACrnAAAioBGEu7Jl4F922h2DYE",
        "b_8": "CAACAgIAAxkBAAFA0yFn5Cq339DGGaulJAhGy2YRES_GuAACRHIAAklbGUuklN_F09npbDYE",
        "b_9": "CAACAgIAAxkBAAFA0ydn5Cq5OthPaJpkgteRZx_iRKQvtQACAnwAAra1GEud22PaqcxUmTYE",
        "b_draw": "CAACAgIAAxkBAAFA0zFn5Cq9lsnPwPz8gRcSfu9wQCNgWQAC23YAAnzLGEvePnUvtDdOGDYE",
        "b_skip": "CAACAgIAAxkBAAFA0z9n5CrEap9I7VbLcPNlvFYJ3d39mgACWnUAAoIJGUswx3bFVH6rAzYE",
        "b_reverse": "CAACAgIAAxkBAAFA001n5CrH2omCLpfBIGK8WaoxMNgonwACj3MAAkHxGEuMoBlQjoixRTYE",
        "g_0": "CAACAgIAAxkBAAFA059n5CrZAmP8mDYKRFThi23sDP_wOAACN3wAAswHGUtNKXKosc6b-TYE",
        "g_1": "CAACAgIAAxkBAAFA069n5CrgI6XFK8CNLZDPxcKbHVxBCwACsG8AAl7GGUtduxGAes5tFDYE",
        "g_2": "CAACAgIAAxkBAAFA071n5CrkqMPcaje9Zb3g07SvwVQukQACe2gAAkkuGEuhW9mNwAzajTYE",
        "g_3": "CAACAgIAAxkBAAFA08tn5CrndI8-KjQO30sCK11GDJXRiwACyGgAAmK6GUsfNiPfHHi7QTYE",
        "g_4": "CAACAgIAAxkBAAFA09Nn5CrrHHMIB1mCRdInjlS5ct7dYQACgmgAAsFQGEvokZwFGHSgIzYE",
        "g_5": "CAACAgIAAxkBAAFA09ln5Cruj-_LR8YoBrZiBBP3orVFUAAC8Y8AAmgsGUurytL0kknrSDYE",
        "g_6": "CAACAgIAAxkBAAFA099n5CrylXhPxqSrX_zEC2_eupOLBAAC4HoAAqGxGEtIZKZSAxwndTYE",
        "g_7": "CAACAgIAAxkBAAFA0-ln5Cr1bn8Sf5XMRj7sKD--Q93INgACGncAAt65GUuqoZWFA7nzHzYE",
        "g_8": "CAACAgIAAxkBAAFA0-9n5Cr64U2ReQzbm7fRAAEmLk7T6agAAgx3AAIN2xhLYk8SeDUzXuw2BA",
        "g_9": "CAACAgIAAxkBAAFA0_Zn5Cr9ccowNmEWW6xyvOEgHt1sugACgmUAAminGUvNSdKbwNB8BTYE",
        "g_draw": "CAACAgIAAxkBAAFA0_pn5CsBi5iAA_uxWRLufSU6p0oiIQAC2W4AAvyIGUtlRr3MDFJrkjYE",
        "g_skip": "CAACAgIAAxkBAAFA1AVn5CsIcOjlCA1EnD4F9Z6GrbRMAwACZWcAAt2JGEt2AAEkkUJ_Wdo2BA",
        "g_reverse": "CAACAgIAAxkBAAFA1BRn5CsLD0P1OvKBr29jgGmxSF3OuwACInsAAtFZGUsd9kL6IcaA9jYE",
        "r_0": "CAACAgIAAxkBAAFA1DNn5CsY3Y3bvRpYwfySirNKTG_09AACOXQAAnnqGUviFyCbwbJNyDYE",
        "r_1": "CAACAgIAAxkBAAFA1Dxn5Cscp7KeRmVbgHdIaj9UauM9gQACKm8AAnnSGEuDLwvo3qhfbjYE",
        "r_2": "CAACAgIAAxkBAAFA1Ehn5CskMf9Bg5VKooc1QpIIr4Hh2QAChHQAAl_0GEv_j78-jhRHCjYE",
        "r_3": "CAACAgIAAxkBAAFA1Exn5Csn3lkvhPfBBCC5BzqJEpKKqwAC3XYAAjLvGEtUsntPSnysNTYE",
        "r_4": "CAACAgIAAxkBAAFA1FBn5Csqx4MpBdu_Dx6zKKw3wsAHuQACE3MAAjm_GEuY_VwfBJL6GTYE",
        "r_5": "CAACAgIAAxkBAAFA1FRn5Csv3NJAieVv_S3c5f3fXizXNQAC72QAAmyIGUuX2AtxmAv4vDYE",
        "r_6": "CAACAgIAAxkBAAFA1Fhn5CszwrYVIxECwwABmTplcV-ZgToAArhiAAIYsxlLwOTkEl3ifwI2BA",
        "r_7": "CAACAgIAAxkBAAFA1GRn5Cs3mb2ktjpcT9wVYLeLsJj3AgACgm0AAmd7GEuFRErLrJKS4DYE",
        "r_8": "CAACAgIAAxkBAAFA1HBn5Cs7UAm-gTso9KUGrS127yrWaAACV3UAAhgAARhLwvRW_JXpsSs2BA",
        "r_9": "CAACAgIAAxkBAAFA1IRn5CtCtFIGwUes1w5gkIoNjiUlyQACXnMAAg3xGEuFBO3ToZ0c1TYE",
        "r_draw": "CAACAgIAAxkBAAFA1Ixn5CtG1wXotS2XYfg5BOGqSgpQEgACaXQAAqN4GEsOmbA03hdGszYE",
        "r_skip": "CAACAgIAAxkBAAFA1KJn5CtQEuB1YxjxvD1Q0QYcCCXkqgACDGwAAlhZGEvxXqvZhRCm4TYE",
        "r_reverse": "CAACAgIAAxkBAAFA1LRn5CtZyrsBN_vuHmS3RH1j2hSeigACTW4AAuQeGUtcAAEtEdZlTf82BA",
        "y_0": "CAACAgIAAxkBAAFA1OBn5CtnDZ0k0OKnWSZuXKTStA0tBAACjWoAAlB-GEt2k7rUq8AnujYE",
        "y_1": "CAACAgIAAxkBAAFA1PJn5CtrVXO7SwLsm2g6kAABzv2eoIUAAh1rAAJsyxhL3lWr8-f8T4A2BA",
        "y_2": "CAACAgIAAxkBAAFA1Qhn5Ctv1YkzEj1bIb4eiL7iqR4CAwACS20AAoTwGEu4v5DbEnwnRjYE",
        "y_3": "CAACAgIAAxkBAAFA1Q5n5Ctz-5FQ9w9nAoD6UzcwA6nKnAAC0HAAAqJUGUtRUXTlxnireTYE",
        "y_4": "CAACAgIAAxkBAAFA1R9n5Ct44EEvLJ5JNiHzr-xdlrkt0gACymwAAh4SGEud7QF_07Z9ITYE",
        "y_5": "CAACAgIAAxkBAAFA1S9n5Ct8hEEV9yx3FL9db8SBDIhCNwACvmQAApfcGUvVTep1cELNpjYE",
        "y_6": "CAACAgIAAxkBAAFA1Ttn5CuAalxL5UATwlLpPH_ol410HwACvnMAApDYGEtgiLUG0nJ0IjYE",
        "y_7": "CAACAgIAAxkBAAFA1UNn5CuE7kkYuUudBr8493Z-yWZmLwACzXcAAqsCGEvoGyxIOoRGBTYE",
        "y_8": "CAACAgIAAxkBAAFA1VFn5CuIOJ4FTE6Ip1NpK67xvYYWvAACOoAAAiQnGUvTAAGREM09u0g2BA",
        "y_9": "CAACAgIAAxkBAAFA1Vtn5CuMTa6NITk3xScYglHfiifzdgACw20AAkaZGUvZlqwPqQYYSjYE",
        "y_draw": "CAACAgIAAxkBAAFA1Wln5CuQdGXJ3BYOgBxnbFkP4LH68QACo3YAAhUXGEuWDFVvE_527zYE",
        "y_skip": "CAACAgIAAxkBAAFA1Xdn5CuZA3KZstZVqhU7355fMsh34gACV3IAAurBIUuYLUwfuVn9rTYE",
        "y_reverse": "CAACAgIAAxkBAAFA1Zln5CuiKsPVDX6GBkFHp4fxurn7MQACkGEAAjHSGUv4ZoaOPRBwNjYE",
        "draw_four": "CAACAgIAAxkBAAFA0sVn5CqAmTXi0agfDzkdDCU4xKP7XAACiXYAAgrMGUusZtA4sBwQFzYE",
        "colorchooser": "CAACAgIAAxkBAAFAmlpn46jO8Jv5Z5Nqlt-YaClEPMpJIwACsnYAAus0GUvesMCWW01hLzYE",
    },
    "not_playable": {
        "b_0": "BQADBAADRQIAAl9XmQAB1IfkQ5xAiK4C",
        "b_1": "BQADBAADRwIAAl9XmQABbWvhTeKBii4C",
        "b_2": "BQADBAADSQIAAl9XmQABS1djHgyQokMC",
        "b_3": "BQADBAADSwIAAl9XmQABwQ6VTbgY-MIC",
        "b_4": "BQADBAADTQIAAl9XmQABAlKUYha8YccC",
        "b_5": "BQADBAADTwIAAl9XmQABMvx8xVDnhUEC",
        "b_6": "BQADBAADUQIAAl9XmQABDEbhP1Zd31kC",
        "b_7": "BQADBAADUwIAAl9XmQABXb5XQBBaAnIC",
        "b_8": "BQADBAADVQIAAl9XmQABgL5HRDLvrjgC",
        "b_9": "BQADBAADVwIAAl9XmQABtO3XDQWZLtYC",
        "b_draw": "BQADBAADWQIAAl9XmQAB2kk__6_2IhMC",
        "b_skip": "BQADBAADXQIAAl9XmQABEGJI6CaH3vcC",
        "b_reverse": "BQADBAADWwIAAl9XmQAB_kZA6UdHXU8C",
        "g_0": "BQADBAADYwIAAl9XmQABGD5a9oG7Yg4C",
        "g_1": "BQADBAADZQIAAl9XmQABqwABZHAXZIg0Ag",
        "g_2": "BQADBAADZwIAAl9XmQABTI3mrEhojRkC",
        "g_3": "BQADBAADaQIAAl9XmQABVi3rUyzWS3YC",
        "g_4": "BQADBAADawIAAl9XmQABZIf5ThaXnpUC",
        "g_5": "BQADBAADbQIAAl9XmQABNndVJSQCenIC",
        "g_6": "BQADBAADbwIAAl9XmQABpoy1c4ZkrvwC",
        "g_7": "BQADBAADcQIAAl9XmQABDeaT5fzxwREC",
        "g_8": "BQADBAADcwIAAl9XmQABLIQ06ZM5NnAC",
        "g_9": "BQADBAADdQIAAl9XmQABel-mC7eXGsMC",
        "g_draw": "BQADBAADdwIAAl9XmQABOHEpxSztCf8C",
        "g_skip": "BQADBAADewIAAl9XmQABDaQdMxjjPsoC",
        "g_reverse": "BQADBAADeQIAAl9XmQABek1lGz7SJNAC",
        "r_0": "BQADBAADfQIAAl9XmQABWrxoiXcsg0EC",
        "r_1": "BQADBAADfwIAAl9XmQABlav-bkgSgRcC",
        "r_2": "BQADBAADgQIAAl9XmQABDjZkqfJ4AdAC",
        "r_3": "BQADBAADgwIAAl9XmQABT7lH7VVcy3MC",
        "r_4": "BQADBAADhQIAAl9XmQAB1arPC5x0LrwC",
        "r_5": "BQADBAADhwIAAl9XmQABWvs7xkCDldkC",
        "r_6": "BQADBAADiQIAAl9XmQABjwABH5ZonWn8Ag",
        "r_7": "BQADBAADiwIAAl9XmQABjekJfm4fBDIC",
        "r_8": "BQADBAADjQIAAl9XmQABqFjchpsJeEkC",
        "r_9": "BQADBAADjwIAAl9XmQAB-sKdcgABdNKDAg",
        "r_draw": "BQADBAADkQIAAl9XmQABtw9RPVDHZOQC",
        "r_skip": "BQADBAADlQIAAl9XmQABtG2GixCxtX4C",
        "r_reverse": "BQADBAADkwIAAl9XmQABz2qyEbabnVsC",
        "y_0": "BQADBAADlwIAAl9XmQABAb3ZwTGS1lMC",
        "y_1": "BQADBAADmQIAAl9XmQAB9v5qJk9R0x8C",
        "y_2": "BQADBAADmwIAAl9XmQABCsgpRHC2g-cC",
        "y_3": "BQADBAADnQIAAl9XmQAB3kLLXCv-qY0C",
        "y_4": "BQADBAADnwIAAl9XmQAB7R_y-NexNLIC",
        "y_5": "BQADBAADoQIAAl9XmQABl-7mwsjD-cMC",
        "y_6": "BQADBAADowIAAl9XmQABwbVsyv2MfPkC",
        "y_7": "BQADBAADpQIAAl9XmQABoBqC0JsemVwC",
        "y_8": "BQADBAADpwIAAl9XmQABpkwAAeh9ldlHAg",
        "y_9": "BQADBAADqQIAAl9XmQABpSBEUfd4IM8C",
        "y_draw": "BQADBAADqwIAAl9XmQABMt-2zW0VYb4C",
        "y_skip": "BQADBAADrwIAAl9XmQABIDf-_TuuxtEC",
        "y_reverse": "BQADBAADrQIAAl9XmQABm9M0Zh-_UwkC",
        "draw_four": "BQADBAADYQIAAl9XmQAB_HWlvZIscDEC",
        "colorchooser": "BQADBAADXwIAAl9XmQABY_ksDdMex-wC",
    },
}

CARDS_CLASSIC_COLORBLIND = {
    "normal": {
        "colorchooser": "CAADBAADrg4AAvX2mVEpx_BiDIE5nQI",
        "draw_four": "CAADBAADYRAAArnkmVGmqXHhjWEBxAI",
        "r_0": "CAADBAAD6A8AAn_ckVHPWHqiBR_3jAI",
        "r_1": "CAADBAAD5Q0AAg-ImVEx-blQI88RrQI",
        "r_2": "CAADBAAD1g0AAuMjmVEkQsVhN49DMAI",
        "r_3": "CAADBAADlhAAAqy4mVHWovoaWfQG_gI",
        "r_4": "CAADBAADCRoAAqf_kVFnl8ACL1rjpwI",
        "r_5": "CAADBAADVw8AAjmamVEEv2TVeL9cpQI",
        "r_6": "CAADBAADHQ4AAuuUkVH2I-yn6nRBVAI",
        "r_7": "CAADBAADNQ8AArP1kVF5rqHtk0pQ-AI",
        "r_8": "CAADBAAD1BAAAuQDkVEPiIodUi6WvwI",
        "r_9": "CAADBAAD2Q4AAq1nkFHM6z5C0Kff2QI",
        "r_draw": "CAADBAADvQ8AAqZukFGEmkRSoSZQEwI",
        "r_reverse": "CAADBAAD5RAAAg89mVE8-EY_2DifcAI",
        "r_skip": "CAADBAADRg4AAp8bmVFOC6xdEZZRwwI",
        "g_0": "CAADBAADTg4AAoQxmFF07jR_vfB4xgI",
        "g_1": "CAADBAADQg4AAhkgmFGlsif9nNtXwgI",
        "g_2": "CAADBAAD2BUAAue_mFGENiPSjZxbiQI",
        "g_3": "CAADBAADpw4AAjO9mFHAOz8KD2n7BwI",
        "g_4": "CAADBAADRhAAAqF7kFEcwLalLfDfaAI",
        "g_5": "CAADBAADAg8AAqXLmFHJyg2F_ybbvwI",
        "g_6": "CAADBAADVhYAAtK7mVGigRq_EkCuVgI",
        "g_7": "CAADBAAD2RIAArccmFEj-8LIVNAbsgI",
        "g_8": "CAADBAAD6AwAAuvmmFHBRarMimOWawI",
        "g_9": "CAADBAADExEAAsNkmVFr8DaHGOwsggI",
        "g_draw": "CAADBAADhA8AArxYmVH9ch5Jp00AAboC",
        "g_reverse": "CAADBAADMhAAAvVOmFGH284LIY7cegI",
        "g_skip": "CAADBAADbBcAAqinkVEOwkJtDRfk2gI",
        "b_0": "CAADBAAD-BAAAkj8kFG61GJdw29QOAI",
        "b_1": "CAADBAADcRMAAu-EmFFT1i4LcqO4OQI",
        "b_2": "CAADBAAD0xQAAqVhmVHyrFSAbxtfjwI",
        "b_3": "CAADBAADNg0AAn-xmFHev8IdF_ie0wI",
        "b_4": "CAADBAADlQ4AAjZamVFcIL_pVB5cFwI",
        "b_5": "CAADBAADrgwAAuL5mVHvEBZ8CG5p5QI",
        "b_6": "CAADBAADDhUAAuGRmVGQYvmEOxczBAI",
        "b_7": "CAADBAADIxEAAv_dmFEuVt39kkgZgwI",
        "b_8": "CAADBAAD2w0AAoE6kVHG7WscV4F2hwI",
        "b_9": "CAADBAADvQ0AArRMmVErWaSRP_giKQI",
        "b_draw": "CAADBAADlw4AAjF_kFHPWSoYKBwtwQI",
        "b_reverse": "CAADBAADog8AAqDJmVEJQp5WocnUnQI",
        "b_skip": "CAADBAAD-QwAAgbZmFGltUlnslDNUQI",
        "y_0": "CAADBAADrQ4AAr5WmVHNf69eBn2YOAI",
        "y_1": "CAADBAADcg8AAmqKmVHfVeUI3u_i7AI",
        "y_2": "CAADBAADkA4AAuDImFEQ8qjFlcKplQI",
        "y_3": "CAADBAAD-QwAAmromFGAqVn-Y8N72wI",
        "y_4": "CAADBAADjQ4AAmNLmFG80k7kfgx1NAI",
        "y_5": "CAADBAADqQ8AAmgYmFH1_ey_bMQNYwI",
        "y_6": "CAADBAADdQ0AAuWcmFEbG_gm1wGYCQI",
        "y_7": "CAADBAAD6QwAApQAAZhRI8OfRvLX3vkC",
        "y_8": "CAADBAADARAAAi-2kVEifJ-O9WVilgI",
        "y_9": "CAADBAADxA0AAhQ8mFHjnl9tUCHSLAI",
        "y_draw": "CAADBAADzw4AAncZmVEhLhX17eqX8AI",
        "y_reverse": "CAADBAADTxAAAqgFmVEJRBw4eWgnDwI",
        "y_skip": "CAADBAADPhYAAiGbkFG9hptFPLgj7wI",
    },
    "not_playable": {
        "colorchooser": "CAADBAADpQ4AAlfDmFFHGkwyGFeCFQI",
        "draw_four": "CAADBAADMRMAAv7amFHvKGLoNyFbNQI",
        "r_0": "CAADBAADsBMAAuGdkFHTZ-jl4eNn-gI",
        "r_1": "CAADBAADVA4AAhpfkFEKt19qveGSPgI",
        "r_2": "CAADBAADrw0AAoWsmVHguULNoYJwUwI",
        "r_3": "CAADBAADzxMAAjvkkFFdtKJu5WGwUgI",
        "r_4": "CAADBAAD1Q8AAoHZkFFvyQnFHzfwiQI",
        "r_5": "CAADBAADWxEAAvkHkFGUo86qxKV0kwI",
        "r_6": "CAADBAAD_hIAAjx0mVGmlm-b_FHQBAI",
        "r_7": "CAADBAADmhEAAslomFHOv7bqcDJkDAI",
        "r_8": "CAADBAADtw0AAgqVmVG2HdSbcJYxZgI",
        "r_9": "CAADBAADNxEAAuF6mVE3WzTMJkSVAgI",
        "r_draw": "CAADBAADVxAAAiNukFE1K2xORNnfMwI",
        "r_reverse": "CAADBAADQxMAAvH0mVHKznpt-uu9ngI",
        "r_skip": "CAADBAADZA4AApbPkFFB9E2Px-HFpgI",
        "g_0": "CAADBAAD8w4AAjDEmFG7DwKggUEj9QI",
        "g_1": "CAADBAAD2g0AAo_DmVHIPG84WdIo1wI",
        "g_2": "CAADBAADEhEAAoRXmVGIG2nuN45P6AI",
        "g_3": "CAADBAADug8AAsSRmFFzk0TcRuG8VAI",
        "g_4": "CAADBAADrQ8AAvgmkFESfo9BjF7-3gI",
        "g_5": "CAADBAADVhAAAnPqkFFtxtFX9HlT-AI",
        "g_6": "CAADBAADMg8AAiSBmFHIQw1jFjv6UwI",
        "g_7": "CAADBAADvREAAv0BkVGDq3H1DCq_DQI",
        "g_8": "CAADBAADWQ4AAhOEkVG96JDgCtFrEwI",
        "g_9": "CAADBAAD2xYAAruDmFFAUMFryEwjoAI",
        "g_draw": "CAADBAADLA4AAu9tkVGTzBbeeYydIQI",
        "g_reverse": "CAADBAADVAwAAhYYmFExJS0ozE8-rAI",
        "g_skip": "CAADBAADYg4AAulsmFHxOkaz9OsTiwI",
        "b_0": "CAADBAADVxUAAtnOkFEIAAGw5CZEIxgC",
        "b_1": "CAADBAAD1RAAAnQqkFF9kDqD0wp3ngI",
        "b_2": "CAADBAADZg4AAvcUmVHTXwldirf1hAI",
        "b_3": "CAADBAADfBAAAkX1mVHw0CWX0h31iQI",
        "b_4": "CAADBAADPBAAAuTCmFFDpvXzes4qjwI",
        "b_5": "CAADBAADTQ4AAsWQmVHcrxDQUWOB4AI",
        "b_6": "CAADBAAD_hAAAoUhmVG8kjd65J8EngI",
        "b_7": "CAADBAADlRAAArtjkFGko5TuFNnncwI",
        "b_8": "CAADBAADZQ8AAltEmFE_fDYIXBrV3QI",
        "b_9": "CAADBAADrhAAAtM-mVGwhrWTD9IaYgI",
        "b_draw": "CAADBAADtQ0AAnVbmFGC1hI60JaOQQI",
        "b_reverse": "CAADBAADShEAAlcOmFHStPeFzfVIEwI",
        "b_skip": "CAADBAAD_xEAAgZFmVFMRA1J8Y1gxAI",
        "y_0": "CAADBAAD7xAAAqjjmFHnCu7eKJvSBgI",
        "y_1": "CAADBAADJQwAAp6tmFE2zDPVMieQ2QI",
        "y_2": "CAADBAADNA4AAl2mmVFpQOxJ41gk_gI",
        "y_3": "CAADBAAD3A4AAsxPmFGyZFv42UlxAQI",
        "y_4": "CAADBAADwg8AAm88kVEc9HZpl2gmzQI",
        "y_5": "CAADBAAD5hIAAkQ6mFHS-aGVuYZAnAI",
        "y_6": "CAADBAADvQ8AAs3RmVHVkVBfEF7eIwI",
        "y_7": "CAADBAAD1gwAAjlbmFGGH6rBdqP8QQI",
        "y_8": "CAADBAADbg8AAqvXkVH1ESeZFcGVrgI",
        "y_9": "CAADBAADOQ8AAnjokVG96pmCP7aZ3AI",
        "y_draw": "CAADBAAD6w4AAgsJmVETUteFwqTVJgI",
        "y_reverse": "CAADBAADtg8AAqiFmFFwothyN9TrXwI",
        "y_skip": "CAADBAADSxEAAhcSmFGu_F5LffmsZgI",
    },
}

STICKERS_OPTIONS = {
    "option_draw": "BQADBAAD-AIAAl9XmQABxEjEcFM-VHIC",
    "option_pass": "BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg",
    "option_bluff": "BQADBAADygIAAl9XmQABJoLfB9ntI2UC",
    "option_info": "BQADBAADxAIAAl9XmQABC5v3Z77VLfEC",
}

# TODO: Support multiple card packs
# For now, just use classic colorblind
STICKERS = {
    **CARDS_CLASSIC_COLORBLIND["normal"],
    **STICKERS_OPTIONS,
}

STICKERS_GREY = {
    **CARDS_CLASSIC_COLORBLIND["not_playable"],
}


class Card(object):
    """This class represents an UNO card"""

    def __init__(self, color, value, special=None):
        self.color = color
        self.value = value
        self.special = special

    def __str__(self):
        if self.special:
            return self.special
        else:
            return '%s_%s' % (self.color, self.value)

    def __repr__(self):
        if self.special:
            return '%s%s%s' % (COLOR_ICONS.get(self.color, ''),
                               COLOR_ICONS[BLACK],
                               ' '.join([s.capitalize()
                                         for s in self.special.split('_')]))
        else:
            return '%s%s' % (COLOR_ICONS[self.color], self.value.capitalize())

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)


def from_str(string):
    """Decodes a Card object from a string"""
    if string not in SPECIALS:
        color, value = string.split('_')
        return Card(color, value)
    else:
        return Card(None, None, string)
