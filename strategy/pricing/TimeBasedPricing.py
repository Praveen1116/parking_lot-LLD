"""
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;

public class TimeBasedPricing implements PricingStrategy {
    // Peak period hours (e.g., 8:00 to 17:00)
    private static final LocalTime PEAK_START = LocalTime.of(8, 0);
    private static final LocalTime PEAK_END = LocalTime.of(17, 0);

    private boolean isPeak(LocalTime time) {
        return !time.isBefore(PEAK_START) && !time.isAfter(PEAK_END);
    }

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        if (exitTime.isBefore(entryTime)) throw new IllegalArgumentException("Exit time before entry time");

        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long totalHours = (long) Math.ceil(durationMinutes / 60.0);

        // Count peak hours and non-peak hours by iterating hour by hour
        int peakHours = 0;
        int nonPeakHours = 0;

        LocalDateTime cursor = entryTime.truncatedTo(ChronoUnit.HOURS);
        // If entry time has minutes, consider first hour partially occupied, count as 1 hour anyway (already rounded)
        for (int i = 0; i < totalHours; i++) {
            LocalTime hourStart = cursor.toLocalTime();
            if (isPeak(hourStart)) peakHours++;
            else nonPeakHours++;
            cursor = cursor.plusHours(1);
        }

        double peakRate = switch (type) {
            case CAR -> 30.0;
            case BIKE -> 15.0;
            case TRUCK -> 50.0;
        };

        double nonPeakRate = switch (type) {
            case CAR -> 20.0;
            case BIKE -> 10.0;
            case TRUCK -> 30.0;
        };

        return peakHours * peakRate + nonPeakHours * nonPeakRate;
    }
}
"""

import math
from datetime import datetime, time, timedelta
from enums.VehicleType import VehicleType
from strategy.pricing.PricingStrategy import PricingStrategy

class TimeBasedPricing(PricingStrategy):
    PEAK_START = time(8, 0)
    PEAK_END = time(17, 0)

    def _isPeak(self, current_time: time) -> bool:
        return self.PEAK_START <= current_time <= self.PEAK_END

    def calculateFee(self, type: VehicleType, entryTime: datetime, exitTime: datetime) -> float:
        if exitTime < entryTime:
            raise ValueError("Exit time before entry time")

        duration_seconds = (exitTime - entryTime).total_seconds()
        duration_minutes = duration_seconds / 60.0
        total_hours = math.ceil(duration_minutes / 60.0)

        peak_hours = 0
        non_peak_hours = 0

        cursor = entryTime.replace(minute=0, second=0, microsecond=0)
        for _ in range(int(total_hours)):
            hour_start = cursor.time()
            if self._isPeak(hour_start):
                peak_hours += 1
            else:
                non_peak_hours += 1
            cursor += timedelta(hours=1)

        match type:
            case VehicleType.CAR:
                peak_rate = 30.0
                non_peak_rate = 20.0
            case VehicleType.BIKE:
                peak_rate = 15.0
                non_peak_rate = 10.0
            case VehicleType.TRUCK:
                peak_rate = 50.0
                non_peak_rate = 30.0
            case _:
                raise ValueError(f"Invalid vehicle type: {type}")

        return float(peak_hours * peak_rate + non_peak_hours * non_peak_rate)
