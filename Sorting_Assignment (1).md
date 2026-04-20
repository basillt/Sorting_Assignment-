# Sorting_Assignment

**שמות הסטודנטים:**
* DEMA MOHAMED - 212931380
* BASIL TAHA - 214656852

## האלגוריתמים שבחרתי

למטלה הזו, בחרתי להתמקד בשלושה אלגוריתמי מיון שונים, כדי להראות מגוון בביצועים ובגישות:

*   **מיון בועות (Bubble Sort):** בחרתי בו כי הוא אחד האלגוריתמים הפשוטים והבסיסיים ביותר להבנה. הוא לא יעיל במיוחד, אבל הוא מצוין כדי להדגים איך אלגוריתמים איטיים יותר מתנהגים כשכמות הנתונים גדלה. הוא כמו ה"נקודת ייחוס" שלנו לאלגוריתם פחות אופטימלי.

*   **מיון מיזוג (Merge Sort):** זהו אלגוריתם "חלוק וכבוש" (Divide and Conquer) יעיל ויציב. הוא תמיד עובד בזמן של O(n log n), מה שהופך אותו לבחירה טובה כשאנחנו רוצים ביצועים עקביים ויעילים, בלי קשר לסדר ההתחלתי של הנתונים. הוא מייצג את הקבוצה של האלגוריתמים היעילים יותר.

*   **מיון מהיר (Quick Sort):** גם הוא אלגוריתם "חלוק וכבוש", והוא נחשב לאחד מאלגוריתמי המיון המהירים ביותר בפועל עבור רוב המקרים. בחרתי בו כדי להראות את הפוטנציאל למהירות גבוהה, למרות שבמקרים מסוימים (כמו מערכים ממוינים כמעט לגמרי) הוא יכול להיות פחות יעיל ממיון מיזוג. הוא מייצג את האלגוריתמים המהירים והמורכבים יותר.

## תוצאות הניסויים

### result1.png: השוואת אלגוריתמי מיון (מערכים אקראיים)

![השוואת אלגוריתמי מיון (מערכים אקראיים)](https://private-us-east-1.manuscdn.com/sessionFile/dJMRjijqXD6DqkC3sy2c7Q/sandbox/L0REniuHKkHQNJr4sn6XyK-images_1776690569604_na1fn_L2hvbWUvdWJ1bnR1L3Jlc3VsdDE.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZEpNUmppanFYRDZEcWtDM3N5MmM3US9zYW5kYm94L0wwUkVuaXVIS2tIUU5KcjRzbjZYeUstaW1hZ2VzXzE3NzY2OTA1Njk2MDRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxjM1ZzZERFLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=ngpM5Ua9zUJ4l0-IqFuphW40nea749GOZDU8yFZUyJIIoWGzgIQzpKMgNTcITkr8qHMAh5U7SESh7cSi-bi1DpcM5tRz~ycXK~GsK7A3aG0KE5t63NrlwxycFbdEaWISyLTcOpDV4mB6RBlXOKYKdlY~EV1hkCxEQfkW2E-4q9X6bJ-8LxwIBwpA848fzC9YituaoXkEORpgMxWShZJmhl5KnpydqnLSGFW2IxiFHkdZ~wHrZ5ofm37BIv4T54BxveTOROetyvddpoCuksevLYrgPlT5UDpnMwSLC5WRUxSeSsHBCpxRjOmKE2HyvTBWrWP9xyp0WbuBp84XXKrXAg__)

בגרף הזה אנחנו רואים איך שלושת האלגוריתמים שבחרתי מתמודדים עם מערכים שמלאים במספרים אקראיים. אפשר לראות בבירור שמיון בועות (Bubble Sort) הוא האיטי ביותר – ככל שהמערך גדול יותר, כך זמן הריצה שלו קופץ בצורה דרמטית. זה בדיוק מה שציפינו מאלגוריתם עם סיבוכיות של O(n^2). לעומתו, מיון מיזוג (Merge Sort) ומיון מהיר (Quick Sort) הרבה יותר מהירים ויעילים. זמן הריצה שלהם עולה בצורה מתונה יותר, וזה תואם את הסיבוכיות שלהם של O(n log n). הגרף הזה מראה לנו כמה חשוב לבחור את האלגוריתם הנכון כשעובדים עם כמויות גדולות של נתונים.

### result2.png: השוואת אלגוריתמי מיון (מערכים ממוינים כמעט לגמרי, עם 5% רעש)

![השוואת אלגוריתמי מיון (מערכים ממוינים כמעט לגמרי, עם 5% רעש)](https://private-us-east-1.manuscdn.com/sessionFile/dJMRjijqXD6DqkC3sy2c7Q/sandbox/L0REniuHKkHQNJr4sn6XyK-images_1776690569604_na1fn_L2hvbWUvdWJ1bnR1L3Jlc3VsdDI.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZEpNUmppanFYRDZEcWtDM3N5MmM3US9zYW5kYm94L0wwUkVuaXVIS2tIUU5KcjRzbjZYeUstaW1hZ2VzXzE3NzY2OTA1Njk2MDRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxjM1ZzZERJLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=ssFBF3Tk057xPxf5CZSZP8IcAvu4bNOnKnDLrh7Upmenkv6a3avgQ8N7HCfS36558JY63jybHkAh5iMwmgA4EFUQ4VUd6p6cCIWAi1ibKCE1lL28aoPmou~ZiDEPfPlxa6DztYFGMFPjMKhrrImeFxEi5jMQ5zA~bnBtDMzLfLsoO9B64PVGZQwCLpIyQzuEuPtuCoNM7kLW~zOK6uy8yrG4K6l8Xlc~-5FnBbibCULg~QhrwPQm9MQNIlDb~ghfglleEXd-Iuu3K2LOgAN19qoddDQjQ2CnpN95vM8loXtFuoHP6j3du7uvCO~2wXmTMpxNrITPMKNDLyypUf7UvA__)

הגרף השני מציג מצב קצת שונה: מה קורה כשהמערך כבר כמעט ממוין, ויש בו רק "רעש" קטן (במקרה הזה, 5% מהאיברים הוחלפו באופן אקראי)? כאן אנחנו רואים שמיון בועות עדיין איטי, אבל אולי קצת פחות גרוע מאשר במערך אקראי לגמרי. מיון מיזוג ומיון מהיר ממשיכים להיות מהירים ויעילים, כמעט באותה מידה כמו במערכים אקראיים. זה מראה שהם לא מושפעים יותר מדי מהסדר ההתחלתי של הנתונים, כל עוד הרעש קטן. זה מדגיש את החוזק שלהם כאלגוריתמים כלליים וטובים לרוב המצבים.

לסיכום, הניסויים האלה עוזרים לנו להבין לא רק איך כל אלגוריתם עובד, אלא גם מתי כדאי להשתמש בו, ואיך סוג הנתונים יכול להשפיע על הביצועים שלו בפועל.
