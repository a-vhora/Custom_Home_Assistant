"""Constants for the Islamic Prayer component."""
from prayer_times_calculator import PrayerTimesCalculator

DOMAIN = "islamic_prayer_times_custom"
NAME = "Prayer Times"
PRAYER_TIMES_ICON = "mdi:calendar-clock"

SENSOR_TYPES = {
    "Fajr": "prayer",
    "Sunrise": "time",
    "Dhuhr": "prayer",
    "Asr": "prayer",
    "Maghrib": "prayer",
    "Isha": "prayer",
    "Midnight": "time",
    "Updated": "time",    
}

CONF_CALC_METHOD = "calculation_method"

CALC_METHODS: list[str] = list(PrayerTimesCalculator.CALCULATION_METHODS)
DEFAULT_CALC_METHOD = "isna"

CONF_SCHOOL = "school"

SCHOOLS: list[str] = list(PrayerTimesCalculator.SCHOOLS)
DEFAULT_SCHOOL = "shafi"

DATA_UPDATED = "Islamic_prayer_data_updated"
