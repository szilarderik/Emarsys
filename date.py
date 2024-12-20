class Date:
    """Date osztály, amely tartalmazza az év, hónap, nap, óra és perc mezőket."""

    def __init__(self, year, month, day, hour=0, minute=0):
        """Inicializálja a dátumot a megadott év, hónap, nap, óra és perc értékekkel."""
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def __str__(self):
        """Visszaadja a dátum szöveges formátumát 'YYYY-MM-DD HH:MM' formában."""
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d} {self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        """Meghatározza, hogy két Date objektum egyenlő-e az év, hónap, nap, óra és perc alapján."""
        if not isinstance(other, Date):
            return False
        return (self.year == other.year and
                self.month == other.month and
                self.day == other.day and
                self.hour == other.hour and
                self.minute == other.minute)

    def is_weekend(self):
        """Ellenőrzi, hogy a dátum szombatra vagy vasárnapra esik-e."""
        day_of_week = self.get_day_of_week()
        return day_of_week in [5, 6]

    def get_day_of_week(self):
        """Meghatározza a hét napját a dátum alapján (0 = hétfő, 6 = vasárnap)."""
        y = self.year
        m = self.month
        if m == 1 or m == 2:
            m += 12
            y -= 1
        q = self.day
        K = y % 100
        J = y // 100
        h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
        return (h + 5) % 7

    def increment_day(self):
        """Növeli az aktuális dátumot egy nappal, és frissíti a hónapot és az évet, ha szükséges."""
        r_date = Date(self.year, self.month, self.day, self.hour, self.minute)
        r_date.day += 1
        if r_date.day > r_date.get_days_in_month():
            r_date.day = 1
            r_date.month += 1
            if r_date.month > 12:
                r_date.month = 1
                r_date.year += 1
        return r_date

    def get_days_in_month(self):
        """Visszaadja az aktuális hónap napjainak számát, figyelembe véve a szökőéveket is."""
        if self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        else:
            return 31

    def is_leap_year(self):
        """Eldönti, hogy az adott év szökőév-e."""
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def adjust_to_working_hours(self):
        """Igazítja a dátumot munkaidőhöz. Ha az idő 9:00 előtt vagy 17:00 után van, akkor a megfelelő következő időpontra állítja"""
        r_date = Date(self.year, self.month, self.day, self.hour, self.minute)
        if r_date.is_weekend():
            r_date.hour = 9
            r_date.minute = 0
        while r_date.is_weekend():
            r_date = r_date.increment_day()
        if r_date.hour < 9:
            r_date.hour = 9
            r_date.minute = 0
        elif r_date.hour >= 17:
            r_date = r_date.increment_day()
            while r_date.is_weekend():
                r_date = r_date.increment_day()
            r_date.hour = 9
            r_date.minute = 0
        return r_date

    def add_working_days(self, workdays_to_add):
        """Hozzáad egy adott számú munkanapot a dátumhoz, figyelembe véve a hétvégéket."""
        r_date = Date(self.year, self.month, self.day, self.hour, self.minute)
        day_of_week = r_date.get_day_of_week()
        if day_of_week == 5:
            r_date.day += 2
        elif day_of_week == 6:
            r_date.day += 1
        while workdays_to_add > 0:
            r_date.day += 1
            day_of_week = (day_of_week + 1) % 7
            if day_of_week < 5:
                workdays_to_add -= 1
            if r_date.day > r_date.get_days_in_month():
                r_date.day = 1
                r_date.month += 1
                if r_date.month > 12:
                    r_date.month = 1
                    r_date.year += 1
        return r_date

    def calculate_date(self, time):
        """Kiszámítja, hogy mennyi idővel később (órákban) esedékes a bejelentés teljesítése, figyelembe véve a munkaidőt és a hétvégéket."""
        r_date = Date(self.year, self.month, self.day, self.hour, self.minute)
        r_date = r_date.adjust_to_working_hours()
        plus_hours_minus_one = 0
        if r_date.hour == 16 and r_date.minute != 0:
            time += 1
            plus_hours_minus_one = -1
        if r_date.hour + time <= 17 and not (r_date.hour == 16 and r_date.minute != 0):
            r_date.hour += time
        else:
            today_hours = 17 - r_date.hour
            time -= today_hours
            workdays = time // 8
            extra_hours = time % 8
            r_date = r_date.add_working_days(workdays + 1)
            r_date.hour = 9 + extra_hours + plus_hours_minus_one
        return r_date
