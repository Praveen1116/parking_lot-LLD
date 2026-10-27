"""
package org.nailyourinterview.lld.parking_lot.utils;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class DateTimeParser {
    private static final DateTimeFormatter FORMATTER =
        DateTimeFormatter.ofPattern("d MMM h:mm a yyyy", Locale.ENGLISH);

    public static LocalDateTime parse(String dateStr) {
        return LocalDateTime.parse(dateStr, FORMATTER);
    }
}
"""

from datetime import datetime

class DateTimeParser:
    DEFAULT_FORMAT = "%d %b %I:%M %p %Y"

    @staticmethod
    def parse(date_str: str, fmt: str = DEFAULT_FORMAT) -> datetime:
        return datetime.strptime(date_str, fmt)

